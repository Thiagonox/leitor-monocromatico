'use client';

import React, { useState, useEffect, useRef, useCallback } from 'react';
import {
  Volume2,
  Play,
  Pause,
  Square,
  X,
  Database,
  AlertCircle,
  SkipBack,
  SkipForward,
  Layers,
} from 'lucide-react';
import { requestTTS, resolveAudioUrl } from '../lib/api';
import { audioSyncBus, analyzeAudioEnvelope, AcousticProfile } from '../lib/audioSync';

export interface AudioBlockItem {
  index: number;
  id: string;
  text: string;
  label?: string;
}

export interface AudioPlaybackState {
  isPlaying: boolean;
  currentTime: number;
  duration: number;
  isLoading: boolean;
  activeBlockIndex: number;
  totalBlocks: number;
  playbackRate?: number;
}

interface AudioPlayerModalProps {
  isOpen: boolean;
  onClose: () => void;
  blocks: AudioBlockItem[];
  activeBlockIndex: number;
  onActiveBlockChange: (index: number) => void;
  bookTitle?: string;
  onPlaybackUpdate?: (state: AudioPlaybackState) => void;
  onNearEnd?: () => void;
}

const VOICES = [
  { id: 'nadine', name: 'Nadine', desc: 'Feminina' },
  { id: 'marcus', name: 'Marcus', desc: 'Masculina' },
];

const PREFETCH_WINDOW = 4; // Pré-carrega e decodifica 4 blocos à frente em background
const CROSSFADE_SEC = 0.016; // 16ms de micro-crossfade acústico imperceptível entre blocos

// Remove silêncio residual no float32 AudioBuffer e aplica envelope cosseno suave nas bordas
function trimAudioBuffer(ctx: AudioContext, buffer: AudioBuffer): AudioBuffer {
  const sampleRate = buffer.sampleRate;
  const length = buffer.length;
  if (length < sampleRate * 0.08) return buffer;

  const ch0 = buffer.getChannelData(0);
  const threshold = 0.0035;
  let firstSample = 0;
  let lastSample = length - 1;

  for (let i = 0; i < length; i++) {
    if (Math.abs(ch0[i]) > threshold) {
      firstSample = i;
      break;
    }
  }

  for (let i = length - 1; i >= firstSample; i--) {
    if (Math.abs(ch0[i]) > threshold) {
      lastSample = i;
      break;
    }
  }

  const leadPad = Math.floor(sampleRate * 0.015);
  const tailPad = Math.floor(sampleRate * 0.035);
  const start = Math.max(0, firstSample - leadPad);
  const end = Math.min(length, lastSample + tailPad);
  const newLen = end - start;

  if (newLen <= 0 || newLen >= length) return buffer;

  const trimmed = ctx.createBuffer(buffer.numberOfChannels, newLen, sampleRate);
  const fadeSamples = Math.min(Math.floor(sampleRate * 0.006), Math.floor(newLen / 4));

  for (let c = 0; c < buffer.numberOfChannels; c++) {
    const src = buffer.getChannelData(c);
    const dst = trimmed.getChannelData(c);
    for (let i = 0; i < newLen; i++) {
      dst[i] = src[start + i];
    }
    for (let i = 0; i < fadeSamples; i++) {
      const gain = 0.5 * (1 - Math.cos((Math.PI * i) / fadeSamples));
      dst[i] *= gain;
      dst[newLen - 1 - i] *= gain;
    }
  }

  return trimmed;
}

interface ScheduledSlot {
  blockIndex: number;
  source: AudioBufferSourceNode;
  gain: GainNode;
  buffer: AudioBuffer;
  acousticProfile?: AcousticProfile;
  startCtxTime: number;
  startOffset: number;
  endCtxTime: number;
  stitchCtxTime: number;
  cached: boolean;
}

export function AudioPlayerModal({
  isOpen,
  onClose,
  blocks,
  activeBlockIndex,
  onActiveBlockChange,
  bookTitle,
  onPlaybackUpdate,
  onNearEnd,
}: AudioPlayerModalProps) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [rate, setRate] = useState(1);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [isCached, setIsCached] = useState<boolean | null>(null);
  const [voice, setVoice] = useState('nadine');
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [prefetchedCount, setPrefetchedCount] = useState(0);

  const audioCtxRef = useRef<AudioContext | null>(null);
  const decodedCacheRef = useRef<Map<string, { buffer: AudioBuffer; cached: boolean; acousticProfile?: AcousticProfile }>>(new Map());
  const inflightRef = useRef<Map<string, Promise<{ buffer: AudioBuffer; cached: boolean; acousticProfile?: AcousticProfile } | null>>>(new Map());

  const currentSlotRef = useRef<ScheduledSlot | null>(null);
  const nextSlotRef = useRef<ScheduledSlot | null>(null);

  const isPlayingRef = useRef(false);
  const rateRef = useRef(1);
  const voiceRef = useRef('nadine');
  const blocksRef = useRef<AudioBlockItem[]>(blocks);
  const activeIdxRef = useRef(activeBlockIndex);
  const rafRef = useRef<number | null>(null);

  blocksRef.current = blocks;
  activeIdxRef.current = activeBlockIndex;
  rateRef.current = rate;
  voiceRef.current = voice;

  const getAudioCtx = useCallback((): AudioContext => {
    if (!audioCtxRef.current || audioCtxRef.current.state === 'closed') {
      const Ctx = window.AudioContext || (window as any).webkitAudioContext;
      audioCtxRef.current = new Ctx();
    }
    return audioCtxRef.current;
  }, []);

  const getBlockCacheKey = useCallback((block: AudioBlockItem, v: string) => {
    return `${v}:${block.id}:${block.text.slice(0, 80)}`;
  }, []);

  // Notifica o leitor principal com baixa frequência (apenas transições de estado macro)
  useEffect(() => {
    onPlaybackUpdate?.({
      isPlaying,
      currentTime,
      duration,
      isLoading,
      activeBlockIndex,
      totalBlocks: blocks.length,
      playbackRate: rate,
    });
  }, [isPlaying, isLoading, activeBlockIndex, blocks.length, rate, onPlaybackUpdate]);

  // Busca o áudio do bloco no Bucket S3 (ou gera via HeyGen) e decodifica em AudioBuffer
  const fetchAndDecodeBlock = useCallback(
    async (blockIndex: number, targetVoice: string): Promise<{ buffer: AudioBuffer; cached: boolean; acousticProfile?: AcousticProfile } | null> => {
      const list = blocksRef.current;
      if (blockIndex < 0 || blockIndex >= list.length) return null;
      const block = list[blockIndex];
      if (!block || !block.text.trim()) return null;

      const key = getBlockCacheKey(block, targetVoice);
      const existing = decodedCacheRef.current.get(key);
      if (existing) return existing;

      const inflight = inflightRef.current.get(key);
      if (inflight) return inflight;

      const promise = (async () => {
        try {
          const res = await requestTTS({
            text: block.text,
            voice: targetVoice,
            chapterId: block.id,
          });

          if (res.status !== 'ok' || !res.audioUrl) {
            throw new Error(res.message || 'Falha ao sintetizar bloco via HeyGen Turbo');
          }

          const directUrl = resolveAudioUrl(res.audioUrl);
          const audioResp = await fetch(directUrl);
          if (!audioResp.ok) {
            throw new Error(`HTTP ${audioResp.status} ao baixar áudio do Bucket S3`);
          }

          const arrayBuf = await audioResp.arrayBuffer();
          const ctx = getAudioCtx();
          const rawAudioBuf = await ctx.decodeAudioData(arrayBuf.slice(0));
          const cleanAudioBuf = trimAudioBuffer(ctx, rawAudioBuf);
          const acousticProfile = analyzeAudioEnvelope(cleanAudioBuf);

          const entry = {
            buffer: cleanAudioBuf,
            cached: Boolean(res.cached),
            acousticProfile,
          };
          decodedCacheRef.current.set(key, entry);

          // Atualiza contador de blocos prontos na janela
          let readyInWindow = 0;
          for (let i = activeIdxRef.current; i <= Math.min(list.length - 1, activeIdxRef.current + PREFETCH_WINDOW); i++) {
            if (decodedCacheRef.current.has(getBlockCacheKey(list[i], targetVoice))) {
              readyInWindow++;
            }
          }
          setPrefetchedCount(readyInWindow);

          return entry;
        } catch (err: any) {
          if (blockIndex === activeIdxRef.current) {
            setErrorMessage(err?.message || 'Erro ao gerar áudio do bloco');
          }
          return null;
        } finally {
          inflightRef.current.delete(key);
        }
      })();

      inflightRef.current.set(key, promise);
      return promise;
    },
    [getAudioCtx, getBlockCacheKey]
  );

  // Agenda o próximo bloco com precisão de amostra (sample-accurate) no relógio de hardware do Web Audio API
  const scheduleNextSlotIfReady = useCallback(() => {
    const cur = currentSlotRef.current;
    if (!cur || !isPlayingRef.current) return;
    if (nextSlotRef.current && nextSlotRef.current.blockIndex === cur.blockIndex + 1) {
      return; // Já agendado no hardware
    }

    const nextIdx = cur.blockIndex + 1;
    const list = blocksRef.current;
    if (nextIdx >= list.length) return;

    const nextBlock = list[nextIdx];
    const key = getBlockCacheKey(nextBlock, voiceRef.current);
    const decoded = decodedCacheRef.current.get(key);
    if (!decoded) return;

    const ctx = getAudioCtx();
    const curRate = rateRef.current;
    const stitchTime = Math.max(ctx.currentTime + 0.004, cur.endCtxTime - CROSSFADE_SEC);

    const source = ctx.createBufferSource();
    source.buffer = decoded.buffer;
    source.playbackRate.value = curRate;

    const gain = ctx.createGain();
    gain.gain.setValueAtTime(0.0001, stitchTime);
    gain.gain.linearRampToValueAtTime(1.0, stitchTime + CROSSFADE_SEC);

    // Suaviza a saída do bloco atual exatamente no ponto de costura
    try {
      cur.gain.gain.setValueAtTime(1.0, stitchTime);
      cur.gain.gain.linearRampToValueAtTime(0.0001, stitchTime + CROSSFADE_SEC);
    } catch (e) {}

    source.connect(gain);
    gain.connect(ctx.destination);
    source.start(stitchTime, 0);

    const nextDurationScaled = decoded.buffer.duration / curRate;
    const nextEndCtxTime = stitchTime + nextDurationScaled;

    nextSlotRef.current = {
      blockIndex: nextIdx,
      source,
      gain,
      buffer: decoded.buffer,
      acousticProfile: decoded.acousticProfile,
      startCtxTime: stitchTime,
      startOffset: 0,
      endCtxTime: nextEndCtxTime,
      stitchCtxTime: nextEndCtxTime - CROSSFADE_SEC,
      cached: decoded.cached,
    };
  }, [getAudioCtx, getBlockCacheKey]);

  // Dispara o pipeline de pré-carregamento para os próximos N blocos em background
  const triggerLookaheadPrefetch = useCallback(
    async (fromIndex: number, targetVoice: string) => {
      const list = blocksRef.current;
      if (fromIndex >= list.length - 3) {
        onNearEnd?.();
      }

      for (let offset = 1; offset <= PREFETCH_WINDOW; offset++) {
        const idx = fromIndex + offset;
        if (idx >= list.length) break;
        fetchAndDecodeBlock(idx, targetVoice).then((res) => {
          if (res && isPlayingRef.current) {
            scheduleNextSlotIfReady();
          }
        });
      }
    },
    [fetchAndDecodeBlock, onNearEnd, scheduleNextSlotIfReady]
  );

  const stopAllNodes = useCallback(() => {
    if (rafRef.current) {
      cancelAnimationFrame(rafRef.current);
      rafRef.current = null;
    }
    audioSyncBus.emit({ isPlaying: false });
    if (currentSlotRef.current) {
      try {
        currentSlotRef.current.source.onended = null;
        currentSlotRef.current.source.stop();
        currentSlotRef.current.source.disconnect();
      } catch (e) {}
      currentSlotRef.current = null;
    }
    if (nextSlotRef.current) {
      try {
        nextSlotRef.current.source.onended = null;
        nextSlotRef.current.source.stop();
        nextSlotRef.current.source.disconnect();
      } catch (e) {}
      nextSlotRef.current = null;
    }
  }, []);

  // Inicia a reprodução de um bloco específico a partir de um offset em segundos
  const playBlockAt = useCallback(
    async (blockIndex: number, offsetSeconds: number = 0) => {
      const list = blocksRef.current;
      if (blockIndex < 0 || blockIndex >= list.length) {
        setIsPlaying(false);
        isPlayingRef.current = false;
        return;
      }

      stopAllNodes();
      setErrorMessage(null);

      const ctx = getAudioCtx();
      if (ctx.state === 'suspended') {
        await ctx.resume();
      }

      // Dispara prefetch imediato dos blocos seguintes em paralelo
      triggerLookaheadPrefetch(blockIndex, voiceRef.current);

      const key = getBlockCacheKey(list[blockIndex], voiceRef.current);
      let decoded = decodedCacheRef.current.get(key) || null;

      if (!decoded) {
        setIsLoading(true);
        decoded = await fetchAndDecodeBlock(blockIndex, voiceRef.current);
        setIsLoading(false);
      }

      if (!decoded) return;

      const curRate = rateRef.current;
      const safeOffset = Math.max(0, Math.min(offsetSeconds, decoded.buffer.duration - 0.05));
      const remainingDuration = (decoded.buffer.duration - safeOffset) / curRate;

      const source = ctx.createBufferSource();
      source.buffer = decoded.buffer;
      source.playbackRate.value = curRate;

      const gain = ctx.createGain();
      gain.gain.setValueAtTime(1.0, ctx.currentTime);

      source.connect(gain);
      gain.connect(ctx.destination);

      const startAt = ctx.currentTime + 0.005;
      const endAt = startAt + remainingDuration;

      source.start(startAt, safeOffset);

      currentSlotRef.current = {
        blockIndex,
        source,
        gain,
        buffer: decoded.buffer,
        acousticProfile: decoded.acousticProfile,
        startCtxTime: startAt,
        startOffset: safeOffset,
        endCtxTime: endAt,
        stitchCtxTime: endAt - CROSSFADE_SEC,
        cached: decoded.cached,
      };

      isPlayingRef.current = true;
      setIsPlaying(true);
      setIsCached(decoded.cached);
      setDuration(decoded.buffer.duration);
      setCurrentTime(safeOffset);

      if (activeIdxRef.current !== blockIndex) {
        activeIdxRef.current = blockIndex;
        onActiveBlockChange(blockIndex);
      }

      audioSyncBus.emit({
        blockIndex,
        blockId: `reader-block-${blockIndex}`,
        currentTime: safeOffset,
        duration: decoded.buffer.duration,
        isPlaying: true,
        isLoading: false,
        playbackRate: curRate,
        acousticProfile: decoded.acousticProfile,
      });

      // Tenta pré-agendar o próximo bloco no relógio de hardware imediatamente
      scheduleNextSlotIfReady();

      // Fallback caso o próximo bloco ainda esteja baixando quando o bloco atual terminar
      source.onended = () => {
        if (!isPlayingRef.current) return;
        if (currentSlotRef.current && currentSlotRef.current.blockIndex === blockIndex && !nextSlotRef.current) {
          const nextIdx = blockIndex + 1;
          if (nextIdx < blocksRef.current.length) {
            playBlockAt(nextIdx, 0);
          } else {
            isPlayingRef.current = false;
            setIsPlaying(false);
          }
        }
      };

      // Loop de sincronização de relógio de hardware (60fps)
      const tick = () => {
        if (!isPlayingRef.current || !audioCtxRef.current) return;
        const now = audioCtxRef.current.currentTime;
        const cur = currentSlotRef.current;

        if (cur) {
          // Verifica se cruzamos o ponto exato de costura para promover o próximo bloco sem qualquer corte!
          if (nextSlotRef.current && now >= nextSlotRef.current.startCtxTime) {
            const promoted = nextSlotRef.current;
            nextSlotRef.current = null;
            currentSlotRef.current = promoted;

            activeIdxRef.current = promoted.blockIndex;
            onActiveBlockChange(promoted.blockIndex);
            setIsCached(promoted.cached);
            setDuration(promoted.buffer.duration);
            setCurrentTime(0);

            audioSyncBus.emit({
              blockIndex: promoted.blockIndex,
              blockId: `reader-block-${promoted.blockIndex}`,
              currentTime: 0,
              duration: promoted.buffer.duration,
              isPlaying: true,
              isLoading: false,
              playbackRate: rateRef.current,
              acousticProfile: promoted.acousticProfile,
            });

            // Configura fallback onended para o bloco recém-promovido
            promoted.source.onended = () => {
              if (!isPlayingRef.current) return;
              if (
                currentSlotRef.current &&
                currentSlotRef.current.blockIndex === promoted.blockIndex &&
                !nextSlotRef.current
              ) {
                const afterIdx = promoted.blockIndex + 1;
                if (afterIdx < blocksRef.current.length) {
                  playBlockAt(afterIdx, 0);
                } else {
                  isPlayingRef.current = false;
                  setIsPlaying(false);
                  audioSyncBus.emit({ isPlaying: false });
                }
              }
            };

            // Avança a janela de prefetch e agenda o bloco seguinte
            triggerLookaheadPrefetch(promoted.blockIndex, voiceRef.current);
            scheduleNextSlotIfReady();
          } else {
            const elapsed = Math.max(0, (now - cur.startCtxTime) * rateRef.current + cur.startOffset);
            const clampedCurrent = Math.min(cur.buffer.duration, elapsed);
            setCurrentTime(clampedCurrent);
            setDuration(cur.buffer.duration);

            audioSyncBus.emit({
              blockIndex: cur.blockIndex,
              blockId: `reader-block-${cur.blockIndex}`,
              currentTime: clampedCurrent,
              duration: cur.buffer.duration,
              isPlaying: true,
              playbackRate: rateRef.current,
              acousticProfile: cur.acousticProfile,
            });

            scheduleNextSlotIfReady();
          }
        }

        rafRef.current = requestAnimationFrame(tick);
      };

      rafRef.current = requestAnimationFrame(tick);
    },
    [
      fetchAndDecodeBlock,
      getAudioCtx,
      getBlockCacheKey,
      onActiveBlockChange,
      scheduleNextSlotIfReady,
      stopAllNodes,
      triggerLookaheadPrefetch,
    ]
  );

  // Ao abrir o player, pré-carrega o bloco atual e os próximos imediatamente
  useEffect(() => {
    if (!isOpen) {
      stopAllNodes();
      isPlayingRef.current = false;
      setIsPlaying(false);
      return;
    }

    let cancelled = false;
    async function warmup() {
      const idx = activeIdxRef.current;
      if (blocksRef.current.length === 0) return;
      setIsLoading(true);
      const first = await fetchAndDecodeBlock(idx, voiceRef.current);
      if (cancelled) return;
      setIsLoading(false);
      if (first) {
        setDuration(first.buffer.duration);
        setIsCached(first.cached);
      }
      triggerLookaheadPrefetch(idx, voiceRef.current);
    }

    warmup();

    return () => {
      cancelled = true;
    };
  }, [isOpen, voice, fetchAndDecodeBlock, stopAllNodes, triggerLookaheadPrefetch]);

  // Se o usuário clicou em outro bloco diretamente no texto enquanto o player estava aberto
  const prevExternalIdxRef = useRef(activeBlockIndex);
  useEffect(() => {
    if (prevExternalIdxRef.current !== activeBlockIndex) {
      const currentPlayingIdx = currentSlotRef.current?.blockIndex;
      prevExternalIdxRef.current = activeBlockIndex;
      if (isOpen && currentPlayingIdx !== activeBlockIndex) {
        if (isPlayingRef.current) {
          playBlockAt(activeBlockIndex, 0);
        } else {
          setCurrentTime(0);
          fetchAndDecodeBlock(activeBlockIndex, voiceRef.current).then((res) => {
            if (res) {
              setDuration(res.buffer.duration);
              setIsCached(res.cached);
            }
          });
          triggerLookaheadPrefetch(activeBlockIndex, voiceRef.current);
        }
      }
    }
  }, [activeBlockIndex, isOpen, playBlockAt, fetchAndDecodeBlock, triggerLookaheadPrefetch]);

  if (!isOpen) return null;

  const handlePlay = () => {
    playBlockAt(activeBlockIndex, currentTime >= duration - 0.1 ? 0 : currentTime);
  };

  const handlePause = () => {
    stopAllNodes();
    isPlayingRef.current = false;
    setIsPlaying(false);
  };

  const handleStop = () => {
    stopAllNodes();
    isPlayingRef.current = false;
    setIsPlaying(false);
    setCurrentTime(0);
  };

  const handleSeek = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newTime = parseFloat(e.target.value);
    setCurrentTime(newTime);
    if (isPlayingRef.current) {
      playBlockAt(activeBlockIndex, newTime);
    }
  };

  const handleRateChange = (newRate: number) => {
    setRate(newRate);
    rateRef.current = newRate;
    if (isPlayingRef.current && currentSlotRef.current) {
      playBlockAt(activeBlockIndex, currentTime);
    }
  };

  const handlePrevBlock = () => {
    if (activeBlockIndex > 0) {
      const prev = activeBlockIndex - 1;
      onActiveBlockChange(prev);
      if (isPlayingRef.current) {
        playBlockAt(prev, 0);
      } else {
        setCurrentTime(0);
      }
    }
  };

  const handleNextBlock = () => {
    if (activeBlockIndex < blocks.length - 1) {
      const next = activeBlockIndex + 1;
      onActiveBlockChange(next);
      if (isPlayingRef.current) {
        playBlockAt(next, 0);
      } else {
        setCurrentTime(0);
      }
    }
  };

  const formatTime = (seconds: number) => {
    if (isNaN(seconds) || seconds < 0) return '00:00';
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const currentBlock = blocks[activeBlockIndex];

  return (
    <div className="fixed bottom-0 left-0 right-0 sm:bottom-6 sm:right-6 sm:left-auto z-[600] w-full sm:max-w-md bg-[var(--bg-surface)] border-t-2 sm:border border-[var(--border-strong)] sm:rounded-xl shadow-2xl p-3.5 pb-6 sm:pb-4 font-sans text-[var(--text-primary)] transition-all max-h-[90vh] overflow-y-auto box-border">
      {/* Cabeçalho do Player Gapless */}
      <div className="flex items-center justify-between pb-2 border-b border-[var(--border-color)] mb-2.5">
        <div className="flex items-center gap-1.5 sm:gap-2 min-w-0">
          <Volume2 className="w-4 h-4 text-[var(--text-primary)] shrink-0" />
          <span className="font-mono text-xs font-bold uppercase tracking-wider truncate">
            HeyGen Gapless Stream
          </span>
          {isCached && (
            <span
              className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-[10px] font-mono border border-[var(--border-strong)] bg-[var(--bg-secondary)] text-[var(--text-primary)] shrink-0"
              title="Bloco servido do Bucket S3 + Agendamento Gapless Web Audio"
            >
              <Database className="w-2.5 h-2.5" />
              S3 · Bloco {activeBlockIndex + 1}/{blocks.length}
            </span>
          )}
        </div>
        <button
          onClick={() => {
            handleStop();
            onClose();
          }}
          className="p-1.5 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-muted)] hover:text-[var(--text-primary)] transition-colors shrink-0 ml-2"
          aria-label="Fechar player de áudio"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      {/* Indicador do Bloco Atual e Buffer Gapless */}
      <div className="flex items-center justify-between text-xs font-mono text-[var(--text-secondary)] mb-2 gap-2">
        <span className="text-[11px] truncate flex-1 min-w-0 font-medium" title={currentBlock?.text}>
          {currentBlock?.label || `Bloco ${activeBlockIndex + 1}: ${currentBlock?.text?.slice(0, 48) || ''}...`}
        </span>
        <span className="text-[9px] sm:text-[10px] text-[var(--text-muted)] shrink-0 inline-flex items-center gap-1 font-mono opacity-85">
          <Layers className="w-2.5 h-2.5" />
          Buffer: {prefetchedCount}/{PREFETCH_WINDOW}
        </span>
      </div>

      {/* Seletor de Voz */}
      <div className="flex items-center gap-2 mb-2.5 text-xs font-mono">
        <span className="text-[var(--text-muted)] text-[11px] shrink-0">Voz:</span>
        <div className="flex items-center gap-1.5 flex-wrap">
          {VOICES.map((v) => (
            <button
              key={v.id}
              onClick={() => {
                stopAllNodes();
                isPlayingRef.current = false;
                setIsPlaying(false);
                setVoice(v.id);
              }}
              disabled={isLoading}
              className={`px-2.5 py-1 rounded text-[10px] sm:text-[11px] border transition-colors ${
                voice === v.id
                  ? 'border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
                  : 'border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-secondary)] hover:bg-[var(--bg-secondary)]'
              }`}
            >
              {v.name} <span className="text-[9px] opacity-75">({v.desc})</span>
            </button>
          ))}
        </div>
      </div>

      {/* Estado de Carregamento do Bloco Inicial */}
      {isLoading && (
        <div className="py-3 text-center">
          <div className="inline-block animate-spin rounded-full h-4 w-4 border-2 border-current border-t-transparent mb-1.5"></div>
          <p className="font-mono text-xs text-[var(--text-muted)]">
            Sintetizando Bloco {activeBlockIndex + 1} e pré-alocando fila gapless...
          </p>
        </div>
      )}

      {/* Erro do Provedor HeyGen */}
      {errorMessage && (
        <div className="py-2.5 px-3 mb-3 bg-red-950/20 border border-red-500/40 rounded text-xs font-mono text-red-400 flex items-start gap-2">
          <AlertCircle className="w-4 h-4 mt-0.5 flex-shrink-0" />
          <div className="overflow-hidden">
            <p className="font-bold mb-0.5">Erro no HeyGen Turbo:</p>
            <p className="text-[11px] opacity-90 break-words">{errorMessage}</p>
          </div>
        </div>
      )}

      {!isLoading && !errorMessage && (
        <>
          {/* Barra de Progresso do Bloco Atual */}
          <div className="space-y-1 mb-2.5">
            <input
              type="range"
              min={0}
              max={duration || 10}
              step="0.05"
              value={currentTime}
              onChange={handleSeek}
              className="w-full h-1.5 bg-[var(--border-color)] rounded-lg appearance-none cursor-pointer accent-[var(--text-primary)]"
            />
            <div className="flex justify-between text-[10px] font-mono text-[var(--text-muted)]">
              <span>{formatTime(currentTime)}</span>
              <span>
                Bloco {activeBlockIndex + 1}/{blocks.length} · {formatTime(duration)}
              </span>
            </div>
          </div>

          {/* Controles Principais */}
          <div className="flex items-center justify-between gap-2 pt-0.5">
            <div className="flex items-center gap-1.5 sm:gap-2">
              <button
                onClick={handlePrevBlock}
                disabled={activeBlockIndex <= 0}
                className="p-1.5 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-muted)] hover:text-[var(--text-primary)] disabled:opacity-30 transition-colors"
                title="Bloco Anterior"
              >
                <SkipBack className="w-3.5 h-3.5" />
              </button>

              {isPlaying ? (
                <button
                  onClick={handlePause}
                  className="p-2 sm:p-2.5 rounded-full bg-[var(--text-primary)] text-[var(--bg-primary)] hover:opacity-90 transition-opacity shadow-sm"
                  title="Pausar"
                >
                  <Pause className="w-4 h-4" />
                </button>
              ) : (
                <button
                  onClick={handlePlay}
                  className="p-2 sm:p-2.5 rounded-full bg-[var(--text-primary)] text-[var(--bg-primary)] hover:opacity-90 transition-opacity shadow-sm"
                  title="Reproduzir Sequência Contínua Sem Cortes"
                >
                  <Play className="w-4 h-4 ml-0.5" />
                </button>
              )}

              <button
                onClick={handleNextBlock}
                disabled={activeBlockIndex >= blocks.length - 1}
                className="p-1.5 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-muted)] hover:text-[var(--text-primary)] disabled:opacity-30 transition-colors"
                title="Próximo Bloco"
              >
                <SkipForward className="w-3.5 h-3.5" />
              </button>

              <button
                onClick={handleStop}
                className="p-1.5 sm:p-2 rounded border border-[var(--border-color)] text-[var(--text-muted)] hover:text-[var(--text-primary)] hover:bg-[var(--bg-secondary)] transition-colors"
                title="Parar"
              >
                <Square className="w-3 h-3 sm:w-3.5 sm:h-3.5" />
              </button>
            </div>

            {/* Velocidade de Reprodução Compacta */}
            <div className="flex items-center gap-0.5 sm:gap-1 text-xs font-mono shrink-0">
              <span className="text-[var(--text-muted)] text-[10px] hidden sm:inline">Vel:</span>
              {[0.8, 1, 1.25, 1.5, 2].map((r) => (
                <button
                  key={r}
                  onClick={() => handleRateChange(r)}
                  className={`px-1.5 py-0.5 rounded text-[10px] ${
                    rate === r
                      ? 'bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
                      : 'text-[var(--text-secondary)] hover:bg-[var(--bg-secondary)]'
                  }`}
                >
                  {r}x
                </button>
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  );
}