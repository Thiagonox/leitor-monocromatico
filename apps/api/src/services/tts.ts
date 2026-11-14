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

// Remove silêncio excessivo no início e fim do buffer PCM 16-bit mono e aplica micro-fade suave (gapless)
export function trimPcmSilence(
  pcmBuffer: Buffer,
  sampleRate: number = 44100,
  threshold: number = 140
): Buffer {
  const totalSamples = Math.floor(pcmBuffer.length / 2);
  if (totalSamples < sampleRate * 0.1) return pcmBuffer;

  let firstActive = 0;
  let lastActive = totalSamples - 1;

  for (let i = 0; i < totalSamples; i++) {
    const sample = Math.abs(pcmBuffer.readInt16LE(i * 2));
    if (sample > threshold) {
      firstActive = i;
      break;
    }
  }

  for (let i = totalSamples - 1; i >= firstActive; i--) {
    const sample = Math.abs(pcmBuffer.readInt16LE(i * 2));
    if (sample > threshold) {
      lastActive = i;
      break;
    }
  }

  // Margem natural de 20ms no início e 45ms no final para respiração contínua sem corte perceptível
  const leadSamples = Math.floor(sampleRate * 0.02);
  const tailSamples = Math.floor(sampleRate * 0.045);
  const startSample = Math.max(0, firstActive - leadSamples);
  const endSample = Math.min(totalSamples, lastActive + tailSamples);

  if (endSample <= startSample) return pcmBuffer;

  const trimmed = Buffer.from(pcmBuffer.subarray(startSample * 2, endSample * 2));
  const trimmedSamples = Math.floor(trimmed.length / 2);
  const fadeSamples = Math.min(Math.floor(sampleRate * 0.006), Math.floor(trimmedSamples / 4));

  // Aplica micro-fade de 6ms nas bordas para eliminar qualquer estalo (click/pop) na junção gapless
  for (let i = 0; i < fadeSamples; i++) {
    const gain = i / fadeSamples;
    const inVal = Math.round(trimmed.readInt16LE(i * 2) * gain);
    trimmed.writeInt16LE(Math.max(-32768, Math.min(32767, inVal)), i * 2);

    const outIdx = trimmedSamples - 1 - i;
    const outVal = Math.round(trimmed.readInt16LE(outIdx * 2) * gain);
    trimmed.writeInt16LE(Math.max(-32768, Math.min(32767, outVal)), outIdx * 2);
  }

  return trimmed;
}

// Converte PCM linear 16-bit 44.1kHz mono em arquivo WAV RIFF universal com trim gapless
export function pcmToWav(
  pcmBuffer: Buffer,
  sampleRate: number = 44100,
  numChannels: number = 1,
  bitsPerSample: number = 16
): Buffer {
  const bytesPerSample = Math.max(1, Math.floor(bitsPerSample / 8));
  const blockAlign = numChannels * bytesPerSample;
  const validLength = pcmBuffer.length - (pcmBuffer.length % blockAlign);
  const alignedPcm = validLength === pcmBuffer.length ? pcmBuffer : pcmBuffer.subarray(0, validLength);
  const cleanPcm = (numChannels === 1 && bitsPerSample === 16)
    ? trimPcmSilence(alignedPcm, sampleRate)
    : alignedPcm;

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

// Hash determinístico por bloco de texto para cache compartilhado no Bucket Railway S3
export function getAudioCacheKey(text: string, voice: string = 'nadine', _chapterId?: string): string {
  const cleanVoice = (voice || 'nadine').trim().toLowerCase();

  // Normaliza o texto do bloco para garantir que o mesmo parágrafo compartilhe o mesmo áudio no S3
  const normalized = (text || '')
    .replace(/[*#_`~>\[\]\r]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 2500);

  const content = `heygen-voice-1-turbo:block-v2:${cleanVoice}:${normalized}`;
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

  const maxAttempts = 2;
  let lastError: Error | null = null;
  let rawBuf: Buffer = Buffer.alloc(0);

  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      const resp = await fetch(endpoint, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${apiKey}`,
          'Content-Type': 'application/json',
          'HTTP-Referer': 'https://mono-readerweb-production.up.railway.app',
          'X-Title': 'Leitor Monocromatico HeyGen Audio',
        },
        body: JSON.stringify(payload),
        signal: AbortSignal.timeout(22000),
      });

      if (!resp.ok) {
        const errorText = await resp.text();
        console.error(`[HeyGen TTS Error] Tentativa ${attempt}/${maxAttempts} HTTP ${resp.status}:`, errorText);
        const err = new Error(`Erro do provedor HeyGen (${resp.status}): ${errorText}`);
        if ((resp.status === 429 || resp.status >= 500) && attempt < maxAttempts) {
          lastError = err;
          await new Promise((r) => setTimeout(r, 700 * attempt));
          continue;
        }
        throw err;
      }

      const arrayBuf = await resp.arrayBuffer();
      rawBuf = Buffer.from(arrayBuf);
      if (rawBuf.length === 0) {
        throw new Error('O provedor HeyGen retornou um áudio vazio.');
      }
      lastError = null;
      break;
    } catch (err: any) {
      lastError = err instanceof Error ? err : new Error(String(err));
      if (attempt < maxAttempts) {
        console.warn(`[HeyGen TTS Retry] Tentativa ${attempt} falhou (${lastError.message}), tentando novamente...`);
        await new Promise((r) => setTimeout(r, 700 * attempt));
        continue;
      }
      throw lastError;
    }
  }

  if (lastError || rawBuf.length === 0) {
    throw lastError || new Error('Falha ao sintetizar áudio via HeyGen.');
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
