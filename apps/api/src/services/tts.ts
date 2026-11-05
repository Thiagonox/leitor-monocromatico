import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import https from 'https';
import { CONFIG } from '../config.js';
import { callNvidiaLlm } from './llm.js';

// Garante que o diretório de cache persistente exista
export function ensureCacheDir(): string {
  const cacheDir = process.env.AUDIO_CACHE_DIR || CONFIG.AUDIO_CACHE_DIR;
  if (!fs.existsSync(cacheDir)) {
    fs.mkdirSync(cacheDir, { recursive: true });
  }
  return cacheDir;
}

// Gera hash único para cache com base no conteúdo e modo
export function getAudioCacheKey(text: string, mode: string = 'audiodescricao', chapterId?: string): string {
  const content = `${mode}:${chapterId || ''}:${text.trim()}`;
  return crypto.createHash('sha256').update(content).digest('hex').slice(0, 24);
}

// Verifica se o áudio já está no bucket/cache
export function isAudioCached(cacheKey: string): boolean {
  const cacheDir = ensureCacheDir();
  const filePath = path.join(cacheDir, `${cacheKey}.mp3`);
  return fs.existsSync(filePath) && fs.statSync(filePath).size > 0;
}

// Caminho do arquivo no cache
export function getAudioFilePath(cacheKey: string): string {
  const cacheDir = ensureCacheDir();
  return path.join(cacheDir, `${cacheKey}.mp3`);
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
        content: 'Você é um narrador pedagógico especializado em audiodescrição clara, humana e didática.'
      },
      {
        role: 'user',
        content: prompt
      }
    ]);

    if (res.text && res.text.trim().length > 50) {
      // Remove resíduos de formatação markdown para a voz ficar limpa
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

// Divide texto em sentenças pequenas (máx ~160 caracteres) para síntese perfeita sem cortes abruptos
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
      // Divide por vírgulas ou palavras se a frase for longa
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

// Sintetiza texto completo em MP3 e persiste no volume/bucket do Railway
export async function synthesizeAndCacheAudio(
  text: string,
  cacheKey: string
): Promise<{ filePath: string; durationEstimateSec: number }> {
  const cacheDir = ensureCacheDir();
  const targetPath = path.join(cacheDir, `${cacheKey}.mp3`);

  // Se já existir, retorna imediatamente do bucket
  if (fs.existsSync(targetPath) && fs.statSync(targetPath).size > 0) {
    return {
      filePath: targetPath,
      durationEstimateSec: Math.round(text.split(' ').length / 2.5),
    };
  }

  const sentences = splitTextIntoSentences(text.slice(0, 3500));
  const audioBuffers: Buffer[] = [];

  // Baixa os chunks em série para respeitar rate limits e garantir ordenação perfeita
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

  const finalMp3 = Buffer.concat(audioBuffers);
  fs.writeFileSync(targetPath, finalMp3);

  console.log(`[TTS Cache] Áudio salvo no bucket Railway: ${targetPath} (${finalMp3.length} bytes)`);

  return {
    filePath: targetPath,
    durationEstimateSec: Math.round(text.split(' ').length / 2.5),
  };
}
