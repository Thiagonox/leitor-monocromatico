import crypto from 'crypto';
import path from 'path';
import { Readable } from 'stream';
import {
  S3Client,
  PutObjectCommand,
  HeadObjectCommand,
  GetObjectCommand,
} from '@aws-sdk/client-s3';
import { CONFIG } from '../config.js';

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

// Converte PCM linear 16-bit 44.1kHz mono em arquivo WAV RIFF universal
export function pcmToWav(
  pcmBuffer: Buffer,
  sampleRate: number = 44100,
  numChannels: number = 1,
  bitsPerSample: number = 16
): Buffer {
  const bytesPerSample = Math.max(1, Math.floor(bitsPerSample / 8));
  const blockAlign = numChannels * bytesPerSample;
  const validLength = pcmBuffer.length - (pcmBuffer.length % blockAlign);
  const cleanPcm = validLength === pcmBuffer.length ? pcmBuffer : pcmBuffer.subarray(0, validLength);

  const byteRate = sampleRate * blockAlign;
  const dataSize = cleanPcm.length;
  const header = Buffer.alloc(44);

  header.write('RIFF', 0);
  header.writeUInt32LE(36 + dataSize, 4);
  header.write('WAVE', 8);
  header.write('fmt ', 12);
  header.writeUInt32LE(16, 16);
  header.writeUInt16LE(1, 20); // PCM format (1)
  header.writeUInt16LE(numChannels, 22);
  header.writeUInt32LE(sampleRate, 24);
  header.writeUInt32LE(byteRate, 28);
  header.writeUInt16LE(blockAlign, 32);
  header.writeUInt16LE(bitsPerSample, 34);
  header.write('data', 36);
  header.writeUInt32LE(dataSize, 40);

  return Buffer.concat([header, cleanPcm]);
}

// Hash determinístico para cache no Bucket Railway
export function getAudioCacheKey(text: string, voice: string = 'nadine', chapterId?: string): string {
  const content = `heygen-voice-1-turbo:${voice}:${chapterId || ''}:${text.trim()}`;
  return crypto.createHash('sha256').update(content).digest('hex').slice(0, 24);
}

// Verifica se o áudio do HeyGen já existe no Bucket S3 do Railway
export async function isAudioInBucket(cacheKey: string): Promise<boolean> {
  const client = getS3Client();
  const s3Key = `${cacheKey}.wav`;

  try {
    const head = await client.send(
      new HeadObjectCommand({
        Bucket: CONFIG.BUCKET_NAME,
        Key: s3Key,
      })
    );
    return Boolean(head.ContentLength && head.ContentLength > 0);
  } catch (err: any) {
    if (err.name === 'NotFound' || err.$metadata?.httpStatusCode === 404) {
      return false;
    }
    console.warn(`[Bucket Head Error] key ${s3Key}:`, err.message);
    return false;
  }
}

// Salva áudio WAV no Bucket S3
export async function saveAudioToBucket(cacheKey: string, audioBuffer: Buffer): Promise<void> {
  const client = getS3Client();
  const s3Key = `${cacheKey}.wav`;

  await client.send(
    new PutObjectCommand({
      Bucket: CONFIG.BUCKET_NAME,
      Key: s3Key,
      Body: audioBuffer,
      ContentType: 'audio/wav',
      Metadata: {
        model: 'heygen/heygen-voice-1-turbo:free',
        cacheKey,
        createdAt: new Date().toISOString(),
      },
    })
  );

  console.log(`[Bucket Upload OK] Áudio HeyGen salvo no Bucket Railway: s3://${CONFIG.BUCKET_NAME}/${s3Key} (${audioBuffer.length} bytes)`);
}

// Obtém stream de áudio do Bucket S3
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
      contentType: resp.ContentType || 'audio/wav',
      status: range ? 206 : 200,
    };
  } catch (err: any) {
    console.warn(`[Bucket Get Error] ${sanitized}:`, err.message);
    return null;
  }
}

// Geração EXCLUSIVA via heygen/heygen-voice-1-turbo:free (SEM QUALQUER FALLBACK)
export async function synthesizeHeyGenAudio(
  text: string,
  voice: string = 'nadine',
  userApiKey?: string
): Promise<{ audioBuffer: Buffer; model: string; voice: string }> {
  const cleanText = text
    .replace(/[*#_`~>\[\]]/g, '')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 4000);

  if (!cleanText) {
    throw new Error('Texto vazio para audiodescrição HeyGen.');
  }

  const model = 'heygen/heygen-voice-1-turbo:free';
  const apiKey = userApiKey || CONFIG.DEFAULT_HEYGEN_API_KEY;

  if (!apiKey) {
    throw new Error('Chave de API do HeyGen/OpenRouter não configurada. Configure HEYGEN_API_KEY no Railway.');
  }

  const endpoint = 'https://openrouter.ai/api/v1/audio/speech';
  const payload = {
    model,
    input: cleanText,
    voice: voice || 'nadine',
    response_format: 'pcm',
  };

  console.log(`[HeyGen TTS] Chamando exclusivamente ${model} (voz: ${voice}, chars: ${cleanText.length})...`);

  const resp = await fetch(endpoint, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
      'HTTP-Referer': 'https://mono-readerweb-production.up.railway.app',
      'X-Title': 'Leitor Monocromatico HeyGen Audio',
    },
    body: JSON.stringify(payload),
  });

  if (!resp.ok) {
    const errorText = await resp.text();
    console.error(`[HeyGen TTS Error] HTTP ${resp.status}:`, errorText);
    throw new Error(`Erro do provedor HeyGen (${resp.status}): ${errorText}`);
  }

  const arrayBuf = await resp.arrayBuffer();
  const rawBuf = Buffer.from(arrayBuf);

  if (rawBuf.length === 0) {
    throw new Error('O provedor HeyGen retornou um áudio vazio.');
  }

  // Se o OpenRouter retornar PCM puro, converte para WAV universal 16-bit 44.1kHz mono
  const isAlreadyWav = rawBuf.length > 4 && rawBuf.subarray(0, 4).toString() === 'RIFF';
  const finalWavBuffer = isAlreadyWav ? rawBuf : pcmToWav(rawBuf, 44100, 1, 16);

  return {
    audioBuffer: finalWavBuffer,
    model,
    voice,
  };
}
