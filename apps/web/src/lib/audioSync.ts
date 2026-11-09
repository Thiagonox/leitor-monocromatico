'use client';

export interface AcousticProfile {
  voiceIntervals: { start: number; end: number }[];
  silenceIntervals: { start: number; end: number }[];
  totalDuration: number;
}

export interface AudioSyncData {
  blockIndex: number;
  blockId: string;
  currentTime: number;
  duration: number;
  isPlaying: boolean;
  isLoading: boolean;
  playbackRate: number;
  acousticProfile?: AcousticProfile | null;
}

type AudioSyncListener = (data: AudioSyncData) => void;

class AudioSyncBus {
  private currentData: AudioSyncData = {
    blockIndex: 0,
    blockId: '',
    currentTime: 0,
    duration: 0,
    isPlaying: false,
    isLoading: false,
    playbackRate: 1,
    acousticProfile: null,
  };

  private listeners: Set<AudioSyncListener> = new Set();

  public getCurrent(): AudioSyncData {
    return this.currentData;
  }

  public emit(data: Partial<AudioSyncData>) {
    this.currentData = { ...this.currentData, ...data };
    this.listeners.forEach((listener) => {
      try {
        listener(this.currentData);
      } catch (err) {
        console.error('Erro no listener do AudioSyncBus:', err);
      }
    });
  }

  public subscribe(listener: AudioSyncListener): () => void {
    this.listeners.add(listener);
    listener(this.currentData);
    return () => {
      this.listeners.delete(listener);
    };
  }
}

export const audioSyncBus = new AudioSyncBus();

/**
 * Analisa o buffer PCM float32 para extrair os intervalos exatos de fala (voice intervals)
 * e pausas respiratórias (silêncios acústicos entre pontuações), garantindo precisão milimétrica.
 */
export function analyzeAudioEnvelope(buffer: AudioBuffer): AcousticProfile {
  const sampleRate = buffer.sampleRate;
  const length = buffer.length;
  const totalDuration = buffer.duration;

  if (length === 0 || totalDuration === 0) {
    return { voiceIntervals: [], silenceIntervals: [], totalDuration: 0 };
  }

  const channelData = buffer.getChannelData(0);
  const windowMs = 25; // Janela temporal de 25ms
  const windowSize = Math.max(1, Math.floor(sampleRate * (windowMs / 1000)));
  const numWindows = Math.floor(length / windowSize);

  if (numWindows === 0) {
    return {
      voiceIntervals: [{ start: 0, end: totalDuration }],
      silenceIntervals: [],
      totalDuration,
    };
  }

  const rmsValues = new Float32Array(numWindows);
  let maxRms = 0;

  for (let w = 0; w < numWindows; w++) {
    let sum = 0;
    const start = w * windowSize;
    for (let i = 0; i < windowSize; i++) {
      const s = channelData[start + i];
      sum += s * s;
    }
    const rms = Math.sqrt(sum / windowSize);
    rmsValues[w] = rms;
    if (rms > maxRms) maxRms = rms;
  }

  // Piso adaptativo de silêncio: no mínimo 0.004 ou 8% do pico
  const silenceThreshold = Math.max(0.004, maxRms * 0.08);
  const minPauseWindows = Math.max(3, Math.floor(0.16 / (windowMs / 1000))); // Pausas >= 160ms

  const voiceIntervals: { start: number; end: number }[] = [];
  const silenceIntervals: { start: number; end: number }[] = [];

  let inVoice = false;
  let voiceStartSec = 0;
  let silenceRun = 0;

  for (let w = 0; w < numWindows; w++) {
    const isVoice = rmsValues[w] > silenceThreshold;
    const t = w * (windowMs / 1000);

    if (isVoice) {
      if (!inVoice) {
        inVoice = true;
        voiceStartSec = t;
        if (silenceIntervals.length > 0) {
          const lastSilence = silenceIntervals[silenceIntervals.length - 1];
          lastSilence.end = t;
        }
      }
      silenceRun = 0;
    } else {
      if (inVoice) {
        silenceRun++;
        if (silenceRun >= minPauseWindows || w === numWindows - 1) {
          const voiceEndSec = (w - silenceRun + 1) * (windowMs / 1000);
          if (voiceEndSec - voiceStartSec >= 0.1) {
            voiceIntervals.push({
              start: Math.max(0, voiceStartSec - 0.03),
              end: Math.min(totalDuration, voiceEndSec + 0.03),
            });
            silenceIntervals.push({
              start: voiceEndSec,
              end: totalDuration,
            });
          }
          inVoice = false;
          silenceRun = 0;
        }
      }
    }
  }

  if (inVoice) {
    voiceIntervals.push({
      start: voiceStartSec,
      end: totalDuration,
    });
  }

  // Fallback caso todo o áudio seja muito suave ou contínuo
  if (voiceIntervals.length === 0) {
    voiceIntervals.push({ start: 0, end: totalDuration });
  }

  return {
    voiceIntervals,
    silenceIntervals,
    totalDuration,
  };
}
