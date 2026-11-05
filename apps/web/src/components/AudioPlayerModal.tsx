'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Volume2, Play, Pause, Square, X, Database, AlertCircle } from 'lucide-react';
import { requestTTS } from '../lib/api';

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
}

const VOICES = [
  { id: 'nadine', label: 'Nadine (Feminina)' },
  { id: 'marcus', label: 'Marcus (Masculina)' },
];

export function AudioPlayerModal({
  isOpen,
  onClose,
  textToRead,
  chapterTitle,
  chapterId,
  onPlaybackUpdate,
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
    }
  }, [isOpen]);

  // Carrega ou busca no bucket cache quando o modal abre ou a voz muda
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
      setIsPlaying(false);

      try {
        const res = await requestTTS({
          text: textToRead,
          voice,
          chapterId,
        });

        if (!active) return;

        if (res.status === 'ok' && res.audioUrl) {
          setAudioUrl(res.audioUrl);
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
      await audioRef.current.play();
      setIsPlaying(true);
    } catch (e) {
      console.error('Falha ao reproduzir áudio:', e);
    }
  };

  const handlePause = () => {
    if (!audioRef.current) return;
    audioRef.current.pause();
    setIsPlaying(false);
  };

  const handleStop = () => {
    if (!audioRef.current) return;
    audioRef.current.pause();
    audioRef.current.currentTime = 0;
    setIsPlaying(false);
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
    <div className="fixed bottom-6 right-6 z-50 w-full max-w-md bg-[var(--bg-primary)] border border-[var(--border-strong)] rounded-lg shadow-2xl p-4 font-sans text-[var(--text-primary)]">
      {/* Elemento de Áudio HTML5 Nativo (Sem Fallbacks) */}
      {audioUrl && (
        <audio
          ref={audioRef}
          src={audioUrl}
          preload="metadata"
          onTimeUpdate={() => {
            if (audioRef.current) setCurrentTime(audioRef.current.currentTime);
          }}
          onLoadedMetadata={() => {
            if (audioRef.current) setDuration(audioRef.current.duration);
          }}
          onEnded={() => setIsPlaying(false)}
        />
      )}

      {/* Cabeçalho do Player */}
      <div className="flex items-center justify-between pb-3 border-b border-[var(--border-color)] mb-3">
        <div className="flex items-center gap-2">
          <Volume2 className="w-4 h-4 text-[var(--text-primary)]" />
          <span className="font-mono text-xs font-bold uppercase tracking-wider">
            HeyGen Voice Turbo
          </span>
          {isCached && (
            <span
              className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-[10px] font-mono border border-[var(--border-strong)] bg-[var(--bg-secondary)] text-[var(--text-primary)]"
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
          className="p-1 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-muted)] hover:text-[var(--text-primary)] transition-colors"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      <div className="flex items-center justify-between text-xs font-mono text-[var(--text-secondary)] mb-2">
        <span className="text-[11px] truncate max-w-[200px]">
          {chapterTitle || 'Capítulo'}
        </span>
        <span className="text-[10px] text-[var(--text-muted)]">
          heygen/heygen-voice-1-turbo:free
        </span>
      </div>

      {/* Seletor de Voz */}
      <div className="flex items-center gap-2 mb-3 text-xs font-mono">
        <span className="text-[var(--text-muted)] text-[11px]">Voz:</span>
        {VOICES.map((v) => (
          <button
            key={v.id}
            onClick={() => setVoice(v.id)}
            disabled={isLoading}
            className={`px-2 py-0.5 rounded text-[11px] border transition-colors ${
              voice === v.id
                ? 'border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
                : 'border-[var(--border-color)] text-[var(--text-secondary)] hover:bg-[var(--bg-secondary)]'
            }`}
          >
            {v.label}
          </button>
        ))}
      </div>

      {/* Estado de Carregamento */}
      {isLoading && (
        <div className="py-4 text-center">
          <div className="inline-block animate-spin rounded-full h-4 w-4 border-2 border-current border-t-transparent mb-2"></div>
          <p className="font-mono text-xs text-[var(--text-muted)]">
            Gerando áudio via heygen/heygen-voice-1-turbo:free...
          </p>
        </div>
      )}

      {/* Erro do Provedor HeyGen (Sem Máscara ou Fallback) */}
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
          <div className="space-y-1 mb-3">
            <input
              type="range"
              min={0}
              max={duration || 100}
              value={currentTime}
              onChange={handleSeek}
              className="w-full h-1 bg-[var(--border-color)] rounded-lg appearance-none cursor-pointer accent-[var(--text-primary)]"
            />
            <div className="flex justify-between text-[10px] font-mono text-[var(--text-muted)]">
              <span>{formatTime(currentTime)}</span>
              <span>{formatTime(duration)}</span>
            </div>
          </div>

          {/* Controles Principais */}
          <div className="flex items-center justify-between gap-3 pt-1">
            <div className="flex items-center gap-2">
              {isPlaying ? (
                <button
                  onClick={handlePause}
                  className="p-2.5 rounded-full bg-[var(--text-primary)] text-[var(--bg-primary)] hover:opacity-90 transition-opacity"
                  title="Pausar"
                >
                  <Pause className="w-4 h-4" />
                </button>
              ) : (
                <button
                  onClick={handlePlay}
                  className="p-2.5 rounded-full bg-[var(--text-primary)] text-[var(--bg-primary)] hover:opacity-90 transition-opacity"
                  title="Reproduzir"
                >
                  <Play className="w-4 h-4 ml-0.5" />
                </button>
              )}

              <button
                onClick={handleStop}
                className="p-2 rounded border border-[var(--border-color)] text-[var(--text-muted)] hover:text-[var(--text-primary)] hover:bg-[var(--bg-secondary)] transition-colors"
                title="Parar e voltar ao início"
              >
                <Square className="w-3.5 h-3.5" />
              </button>
            </div>

            {/* Velocidade de Reprodução */}
            <div className="flex items-center gap-1 text-xs font-mono">
              <span className="text-[var(--text-muted)] text-[10px]">Vel:</span>
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
