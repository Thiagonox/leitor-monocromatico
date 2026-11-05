import path from 'path';
import { fileURLToPath } from 'url';
import 'dotenv/config';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export const CONFIG = {
  PORT: process.env.API_PORT ? parseInt(process.env.API_PORT, 10) : 3001,
  DATA_DIR: process.env.DATA_DIR || path.resolve(__dirname, '../../../data'),
  AUDIO_CACHE_DIR: process.env.AUDIO_CACHE_DIR || path.resolve(__dirname, '../../../data/audio-cache'),
  // Configurações do Bucket S3 nativo do Railway
  BUCKET_ENDPOINT: process.env.BUCKET_ENDPOINT || "https://t3.storageapi.dev",
  BUCKET_NAME: process.env.BUCKET_NAME || "audio-cache-ydiiexjbawkub",
  BUCKET_ACCESS_KEY_ID: process.env.BUCKET_ACCESS_KEY_ID || "tid_sJbZL_uwATkXhVPjVeeCHUqkAXuciLemdvdLffWXfxZHzQGTgD",
  BUCKET_SECRET_ACCESS_KEY: process.env.BUCKET_SECRET_ACCESS_KEY || "tsec_2yKBtzFBUjcoSxMLeWecJDIQejA7Gx-WO3DCwQIL5MNdK2gYRzgHJTV1goO40+QYFCQuAX",
  BUCKET_REGION: process.env.BUCKET_REGION || "auto",
  DEFAULT_NVIDIA_API_KEY: process.env.NVIDIA_API_KEY || "",
  DEFAULT_MODEL: process.env.AI_MODEL || "z-ai/glm-5.3-flash",
  DEFAULT_BASE_URL: process.env.AI_BASE_URL || "https://integrate.api.nvidia.com/v1",
  DEFAULT_HEYGEN_API_KEY: process.env.HEYGEN_API_KEY || process.env.OPENROUTER_API_KEY || "",
  DEFAULT_HEYGEN_MODEL: process.env.HEYGEN_MODEL || "heygen/heygen-voice-1-turbo:free",
  OPENROUTER_TEXT_MODELS: [
    "nvidia/nemotron-3.5-lightning:free",
    "nvidia/nemotron-3.5-super-vl:free",
    "recursive/flint-v1.0:free"
  ]
};
