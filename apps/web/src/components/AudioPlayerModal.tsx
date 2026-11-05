'use client';

import React, { useState, useEffect, useRef } from 'react';
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
} from 'lucide-react';
import { requestTTS, resolveAudioUrl } from '../lib/api';

export interface AudioPlaybackState {
  isPlaying: boolean;
  currentTime: number;
  duration: number;
  isLoading: boolean;
}

interface AudioPlayerModalProps {
  isOpen: boolean;
  onClose: () => void;
  textToRead: string;
  chapterTitle?: string;
  chapterId?: string;
  onPlaybackUpdate?: (state: AudioPlaybackState) => void;
  onNextChapter?: () => void;
  onPreviousChapter?: () => void;
  hasNextChapter?: boolean;
  hasPreviousChapter?: boolean;
}

const VOICES = [
  { id: 'nadine', name: 'Nadine', desc: 'Feminina' },
  { id: 'marcus', name: 'Marcus', desc: 'Masculina' },
];

export function AudioPlayerModal({
  isOpen,
  onClose,
  textToRead,
  chapterTitle,
  chapterId,
  onPlaybackUpdate,
  onNextChapter,
  onPreviousChapter,
  hasNextChapter = false,
  hasPreviousChapter = false,
}: AudioPlayerModalProps) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [rate, setRate] = useState(1);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [isCached, setIsCached] = useState<boolean | null>(null);
  const [voice, setVoice] = useState('nadine');
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const audioRef = useRef<HTMLAudioElement | null>(null);
  const wasPlayingRef = useRef(false);

  // Notifica o estado de reprodução para o Lápis de Leitura e componentes externos
  useEffect(() => {
    onPlaybackUpdate?.({
      isPlaying,
      currentTime,
      duration,
      isLoading,
    });
  }, [isPlaying, currentTime, duration, isLoading, onPlaybackUpdate]);

  // Limpa o áudio ao fechar
  useEffect(() => {
    if (!isOpen) {
      if (audioRef.current) {
        audioRef.current.pause();
        audioRef.current.currentTime = 0;
      }
      setIsPlaying(false);
      wasPlayingRef.current = false;
    }
  }, [isOpen]);

  // Carrega ou busca no bucket cache quando o modal abre ou a voz/capítulo muda
  useEffect(() => {
    if (!isOpen || !textToRead) return;

    let active = true;

    async function loadAudio() {
      setIsLoading(true);
      setErrorMessage(null);
      setCurrentTime(0);
      setDuration(0);

      if (audioRef.current) {
        audioRef.current.pause();
        audioRef.current.currentTime = 0;
      }

      try {
        const res = await requestTTS({
          text: textToRead,
          voice,
          chapterId,
        });

        if (!active) return;

        if (res.status === 'ok' && res.audioUrl) {
          const directUrl = resolveAudioUrl(res.audioUrl);
          setAudioUrl(directUrl);
          setIsCached(Boolean(res.cached));
        } else {
          setErrorMessage(res.message || 'Falha ao gerar áudio com heygen/heygen-voice-1-turbo:free');
        }
      } catch (err: any) {
        if (!active) return;
        setErrorMessage(err?.message || 'Erro ao conectar ao serviço HeyGen TTS');
      } finally {
        if (active) setIsLoading(false);
      }
    }

    loadAudio();

    return () => {
      active = false;
    };
  }, [isOpen, chapterId, voice, textToRead]);

  if (!isOpen) return null;

  const handlePlay = async () => {
    if (!audioRef.current) return;
    try {
      audioRef.current.playbackRate = rate;
      const playPromise = audioRef.current.play();
      if (playPromise !== undefined) {
        await playPromise;
        setIsPlaying(true);
        wasPlayingRef.current = true;
      }
    } catch (e: any) {
      // Ignora AbortError que ocorre quando o carregamento é interrompido ou pausado
      if (e?.name === 'AbortError') {
        return;
      }
      console.warn('Interrupção ou aviso ao reproduzir áudio:', e?.message || e);
    }
  };

  const handlePause = () => {
    if (!audioRef.current) return;
    audioRef.current.pause();
    setIsPlaying(false);
    wasPlayingRef.current = false;
  };

  const handleStop = () => {
    if (!audioRef.current) return;
    audioRef.current.pause();
    audioRef.current.currentTime = 0;
    setIsPlaying(false);
    wasPlayingRef.current = false;
  };

  const handleSeek = (e: React.ChangeEvent<HTMLInputElement>) => {
    const time = parseFloat(e.target.value);
    setCurrentTime(time);
    if (audioRef.current) {
      audioRef.current.currentTime = time;
    }
  };

  const handleRateChange = (newRate: number) => {
    setRate(newRate);
    if (audioRef.current) {
      audioRef.current.playbackRate = newRate;
    }
  };

  const formatTime = (seconds: number) => {
    if (isNaN(seconds)) return '00:00';
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <div className="fixed bottom-0 left-0 right-0 sm:bottom-6 sm:right-6 sm:left-auto z-50 w-full sm:max-w-md bg-[var(--bg-surface)] border-t-2 sm:border border-[var(--border-strong)] sm:rounded-xl shadow-2xl p-3.5 pb-6 sm:pb-4 font-sans text-[var(--text-primary)] transition-all max-h-[90vh] overflow-y-auto box-border">
      {/* Elemento de Áudio HTML5 Nativo com URL direta e streaming HTTP Range */}
      {audioUrl && (
        <audio
          ref={audioRef}
          src={audioUrl}
          preload="metadata"
          onTimeUpdate={() => {
            if (audioRef.current) setCurrentTime(audioRef.current.currentTime);
          }}
          onLoadedMetadata={() => {
            if (audioRef.current) {
              setDuration(audioRef.current.duration);
              if (wasPlayingRef.current) {
                audioRef.current.playbackRate = rate;
                audioRef.current.play().then(() => setIsPlaying(true)).catch((err) => {
                  if (err?.name !== 'AbortError') console.warn('Aviso play onLoadedMetadata:', err);
                });
              }
            }
          }}
          onEnded={() => {
            setIsPlaying(false);
            if (onNextChapter && hasNextChapter) {
              wasPlayingRef.current = true;
              onNextChapter();
            } else {
              wasPlayingRef.current = false;
            }
          }}
        />
      )}

      {/* Cabeçalho do Player */}
      <div className="flex items-center justify-between pb-2 border-b border-[var(--border-color)] mb-2.5">
        <div className="flex items-center gap-1.5 sm:gap-2 min-w-0">
          <Volume2 className="w-4 h-4 text-[var(--text-primary)] shrink-0" />
          <span className="font-mono text-xs font-bold uppercase tracking-wider truncate">
            HeyGen Voice Turbo
          </span>
          {isCached && (
            <span
              className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-[10px] font-mono border border-[var(--border-strong)] bg-[var(--bg-secondary)] text-[var(--text-primary)] shrink-0"
              title="Áudio salvo no Bucket Railway S3 — carregamento instantâneo"
            >
              <Database className="w-2.5 h-2.5" />
              Bucket S3
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

      {/* Título do Capítulo e Provedor */}
      <div className="flex items-center justify-between text-xs font-mono text-[var(--text-secondary)] mb-2 gap-2">
        <span className="text-[11px] truncate flex-1 min-w-0 font-medium" title={chapterTitle}>
          {chapterTitle || 'Capítulo'}
        </span>
        <span className="text-[9px] sm:text-[10px] text-[var(--text-muted)] shrink-0 hidden xs:inline font-mono opacity-80">
          heygen-voice-1-turbo
        </span>
      </div>

      {/* Seletor de Voz */}
      <div className="flex items-center gap-2 mb-2.5 text-xs font-mono">
        <span className="text-[var(--text-muted)] text-[11px] shrink-0">Voz:</span>
        <div className="flex items-center gap-1.5 flex-wrap">
          {VOICES.map((v) => (
            <button
              key={v.id}
              onClick={() => setVoice(v.id)}
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

      {/* Estado de Carregamento */}
      {isLoading && (
        <div className="py-3 text-center">
          <div className="inline-block animate-spin rounded-full h-4 w-4 border-2 border-current border-t-transparent mb-1.5"></div>
          <p className="font-mono text-xs text-[var(--text-muted)]">
            Gerando audiodescrição via heygen/heygen-voice-1-turbo:free...
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
          {/* Barra de Progresso / Scrubber */}
          <div className="space-y-1 mb-2.5">
            <input
              type="range"
              min={0}
              max={duration || 100}
              step="0.1"
              value={currentTime}
              onChange={handleSeek}
              className="w-full h-1.5 bg-[var(--border-color)] rounded-lg appearance-none cursor-pointer accent-[var(--text-primary)]"
            />
            <div className="flex justify-between text-[10px] font-mono text-[var(--text-muted)]">
              <span>{formatTime(currentTime)}</span>
              <span>{formatTime(duration)}</span>
            </div>
          </div>

          {/* Controles Principais */}
          <div className="flex items-center justify-between gap-2 pt-0.5">
            <div className="flex items-center gap-1.5 sm:gap-2">
              {hasPreviousChapter && onPreviousChapter && (
                <button
                  onClick={() => {
                    wasPlayingRef.current = isPlaying;
                    onPreviousChapter();
                  }}
                  className="p-1.5 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-muted)] hover:text-[var(--text-primary)] transition-colors"
                  title="Capítulo Anterior"
                >
                  <SkipBack className="w-3.5 h-3.5" />
                </button>
              )}

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
                  title="Reproduzir"
                >
                  <Play className="w-4 h-4 ml-0.5" />
                </button>
              )}

              {hasNextChapter && onNextChapter && (
                <button
                  onClick={() => {
                    wasPlayingRef.current = isPlaying;
                    onNextChapter();
                  }}
                  className="p-1.5 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-muted)] hover:text-[var(--text-primary)] transition-colors"
                  title="Próximo Capítulo"
                >
                  <SkipForward className="w-3.5 h-3.5" />
                </button>
              )}

              <button
                onClick={handleStop}
                className="p-1.5 sm:p-2 rounded border border-[var(--border-color)] text-[var(--text-muted)] hover:text-[var(--text-primary)] hover:bg-[var(--bg-secondary)] transition-colors"
                title="Parar e voltar ao início"
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