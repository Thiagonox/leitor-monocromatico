import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import https from 'https';
import { Readable } from 'stream';
import {
  S3Client,
  PutObjectCommand,
  HeadObjectCommand,
  GetObjectCommand,
} from '@aws-sdk/client-s3';
import { CONFIG } from '../config.js';
import { callNvidiaLlm } from './llm.js';

// Inicializa o cliente S3 para o Bucket nativo do Railway
let s3ClientInstance: S3Client | null = null;

export function getS3Client(): S3Client {
  if (!s3ClientInstance) {
    s3ClientInstance = new S3Client({
      endpoint: CONFIG.BUCKET_ENDPOINT,
      region: CONFIG.BUCKET_REGION,
      credentials: {
        accessKeyId: CONFIG.BUCKET_ACCESS_KEY_ID,
        secretAccessKey: CONFIG.BUCKET_SECRET_ACCESS_KEY,
      },
    });
  }
  return s3ClientInstance;
}

// Gera hash único para cache com base no conteúdo e modo
export function getAudioCacheKey(text: string, mode: string = 'audiodescricao', chapterId?: string): string {
  const content = `${mode}:${chapterId || ''}:${text.trim()}`;
  return crypto.createHash('sha256').update(content).digest('hex').slice(0, 24);
}

// Verifica se o áudio já existe no Bucket S3 do Railway
export async function isAudioInBucket(cacheKey: string): Promise<boolean> {
  const client = getS3Client();
  const s3Key = `${cacheKey}.mp3`;

  try {
    const head = await client.send(
      new HeadObjectCommand({
        Bucket: CONFIG.BUCKET_NAME,
        Key: s3Key,
      })
    );
    return Boolean(head.ContentLength && head.ContentLength > 0);
  } catch (err: any) {
    // 404 / NotFound significa que ainda não foi gerado
    if (err.name === 'NotFound' || err.$metadata?.httpStatusCode === 404) {
      return false;
    }
    console.warn(`[Bucket Head Error] key ${s3Key}:`, err.message);
    return false;
  }
}

// Salva o buffer MP3 diretamente no Bucket S3 do Railway
export async function saveAudioToBucket(cacheKey: string, mp3Buffer: Buffer): Promise<void> {
  const client = getS3Client();
  const s3Key = `${cacheKey}.mp3`;

  await client.send(
    new PutObjectCommand({
      Bucket: CONFIG.BUCKET_NAME,
      Key: s3Key,
      Body: mp3Buffer,
      ContentType: 'audio/mpeg',
      Metadata: {
        cacheKey,
        createdAt: new Date().toISOString(),
      },
    })
  );

  console.log(`[Bucket Upload OK] Áudio salvo no Bucket Railway: s3://${CONFIG.BUCKET_NAME}/${s3Key} (${mp3Buffer.length} bytes)`);
}

// Obtém stream de áudio do Bucket S3 com suporte a HTTP Range (seeking)
export async function getAudioFromBucket(
  filename: string,
  range?: string
): Promise<{
  stream: Readable;
  contentLength?: number;
  contentRange?: string;
  contentType: string;
  status: number;
} | null> {
  const client = getS3Client();
  const sanitized = path.basename(filename);

  try {
    const resp = await client.send(
      new GetObjectCommand({
        Bucket: CONFIG.BUCKET_NAME,
        Key: sanitized,
        Range: range,
      })
    );

    return {
      stream: resp.Body as Readable,
      contentLength: resp.ContentLength,
      contentRange: resp.ContentRange,
      contentType: resp.ContentType || 'audio/mpeg',
      status: range ? 206 : 200,
    };
  } catch (err: any) {
    console.warn(`[Bucket Get Error] ${sanitized}:`, err.message);
    return null;
  }
}

// Gera um roteiro didático de audiodescrição usando IA (LLM)
export async function generateAiAudioDescriptionScript(
  chapterTitle: string,
  rawText: string
): Promise<string> {
  const prompt = `Você é um professor e especialista em audiodescrição didática e acessibilidade pedagógica para o Leitor Monocromático.
Sua missão é transformar o conteúdo escrito deste capítulo em uma narrativa falada, fluida e envolvente para audiodescrição.

Diretrizes obrigatórias:
1. Apresente o capítulo com voz acolhedora e pedagógica.
2. Explique os conceitos centrais, exemplos e aplicações de forma clara, como se estivesse conversando diretamente com o estudante.
3. Não leia códigos de formatação ou caracteres estranhos (nada de asteriscos, hashtags ou colchetes).
4. Use frases com bom ritmo de fala, com pausas naturais para compreensão.
5. Seja conciso e direto: sintetize o essencial entre 2 e 4 minutos de fala (máximo de 2500 caracteres de roteiro).

Capítulo: "${chapterTitle}"
Conteúdo base:
${rawText.slice(0, 4500)}

Retorne APENAS o roteiro de fala corrido em português:`;

  try {
    const res = await callNvidiaLlm([
      {
        role: 'system',
        content: 'Você é um narrador pedagógico especializado em audiodescrição clara, humana e didática.',
      },
      {
        role: 'user',
        content: prompt,
      },
    ]);

    if (res.text && res.text.trim().length > 50) {
      return res.text
        .replace(/[*#_`~>\[\]]/g, '')
        .replace(/\n+/g, ' ')
        .trim();
    }
  } catch (err) {
    console.warn('[TTS] Falha ao gerar roteiro via LLM, usando síntese direta:', err);
  }

  // Fallback de roteiro se o LLM falhar
  return `Audiodescrição do capítulo: ${chapterTitle}. ${rawText.slice(0, 1500).replace(/[*#_`~>\[\]]/g, '').replace(/\n+/g, ' ')}`;
}

// Faz download de um trecho curto de áudio MP3 (Google TTS Engine)
function fetchMp3Chunk(textChunk: string): Promise<Buffer> {
  return new Promise((resolve, reject) => {
    const encoded = encodeURIComponent(textChunk.trim());
    const url = `https://translate.google.com/translate_tts?ie=UTF-8&tl=pt-BR&client=tw-ob&q=${encoded}`;

    const req = https.get(
      url,
      {
        headers: {
          'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
          Referer: 'https://translate.google.com/',
        },
      },
      (res) => {
        if (res.statusCode !== 200) {
          return reject(new Error(`TTS chunk status code ${res.statusCode}`));
        }
        const chunks: Buffer[] = [];
        res.on('data', (d) => chunks.push(d));
        res.on('end', () => resolve(Buffer.concat(chunks)));
        res.on('error', reject);
      }
    );

    req.on('error', reject);
    req.setTimeout(12000, () => {
      req.destroy();
      reject(new Error('TTS chunk timeout'));
    });
  });
}

// Divide texto em sentenças pequenas (máx ~160 caracteres)
function splitTextIntoSentences(text: string, maxLen: number = 160): string[] {
  const cleaned = text.replace(/[*#_`~>\[\]]/g, '').replace(/\s+/g, ' ').trim();
  const rawParts = cleaned.match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [cleaned];
  const chunks: string[] = [];

  for (const part of rawParts) {
    const trimmed = part.trim();
    if (!trimmed) continue;

    if (trimmed.length <= maxLen) {
      chunks.push(trimmed);
    } else {
      const words = trimmed.split(' ');
      let current = '';
      for (const word of words) {
        if ((current + ' ' + word).trim().length <= maxLen) {
          current = (current + ' ' + word).trim();
        } else {
          if (current) chunks.push(current);
          current = word;
        }
      }
      if (current) chunks.push(current);
    }
  }

  return chunks;
}

// Sintetiza texto completo em MP3 Buffer
export async function synthesizeMp3Buffer(text: string): Promise<Buffer> {
  const sentences = splitTextIntoSentences(text.slice(0, 3500));
  const audioBuffers: Buffer[] = [];

  for (const sentence of sentences) {
    if (!sentence || sentence.length < 2) continue;
    try {
      const buf = await fetchMp3Chunk(sentence);
      audioBuffers.push(buf);
    } catch (err) {
      console.warn(`[TTS] Erro no trecho: "${sentence.slice(0, 30)}..."`, err);
    }
  }

  if (audioBuffers.length === 0) {
    throw new Error('Nenhum áudio pôde ser gerado a partir do texto.');
  }

  return Buffer.concat(audioBuffers);
}
