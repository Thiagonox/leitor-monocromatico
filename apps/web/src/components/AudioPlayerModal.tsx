'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Volume2, Play, Pause, Square, X, Sparkles, Database, FileText, ChevronDown, ChevronUp } from 'lucide-react';
import { requestTTS, TTSResponse } from '../lib/api';

interface AudioPlayerModalProps {
  isOpen: boolean;
  onClose: () => void;
  textToRead: string;
  chapterTitle?: string;
  chapterId?: string;
}

export function AudioPlayerModal({
  isOpen,
  onClose,
  textToRead,
  chapterTitle,
  chapterId,
}: AudioPlayerModalProps) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [rate, setRate] = useState(1);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [isCached, setIsCached] = useState<boolean | null>(null);
  const [aiScript, setAiScript] = useState<string | null>(null);
  const [showScript, setShowScript] = useState(false);
  const [mode, setMode] = useState<'audiodescricao' | 'direct'>('audiodescricao');
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const audioRef = useRef<HTMLAudioElement | null>(null);

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

  // Carrega ou busca no bucket cache quando o modal abre ou o modo muda
  useEffect(() => {
    if (!isOpen || !textToRead) return;

    let active = true;

    async function loadAudio() {
      setIsLoading(true);
      setErrorMessage(null);
      if (audioRef.current) {
        audioRef.current.pause();
      }
      setIsPlaying(false);

      try {
        const res = await requestTTS({
          text: textToRead,
          chapterTitle,
          chapterId,
          mode,
        });

        if (!active) return;

        if (res.status === 'ok' && res.audioUrl) {
          setAudioUrl(res.audioUrl);
          setIsCached(Boolean(res.cached));
          setAiScript(res.script || null);
        } else {
          setErrorMessage(res.message || 'Falha ao carregar áudio');
        }
      } catch (err: any) {
        if (!active) return;
        setErrorMessage(err?.message || 'Erro de conexão com o serviço de áudio');
      } finally {
        if (active) setIsLoading(false);
      }
    }

    loadAudio();

    return () => {
      active = false;
    };
  }, [isOpen, chapterId, mode, chapterTitle]);

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
      {/* Elemento de Áudio HTML5 Nativo */}
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
            Audiodescrição com IA
          </span>
          {isCached && (
            <span
              className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-[10px] font-mono border border-[var(--border-strong)] bg-[var(--bg-secondary)] text-[var(--text-primary)]"
              title="Áudio salvo no bucket Railway — carregamento instantâneo sem reprocessamento"
            >
              <Database className="w-2.5 h-2.5" />
              Cache
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

      {chapterTitle && (
        <p className="font-serif text-xs italic text-[var(--text-secondary)] mb-2 line-clamp-1">
          {chapterTitle}
        </p>
      )}

      {/* Seletor de Modo: Audiodescrição com IA vs Narração Direta */}
      <div className="flex items-center gap-1.5 mb-3 bg-[var(--bg-surface)] p-1 rounded border border-[var(--border-color)] text-[11px] font-mono">
        <button
          onClick={() => setMode('audiodescricao')}
          disabled={isLoading}
          className={`flex-1 py-1 px-2 rounded flex items-center justify-center gap-1 transition-colors ${
            mode === 'audiodescricao'
              ? 'bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
              : 'text-[var(--text-secondary)] hover:text-[var(--text-primary)]'
          }`}
        >
          <Sparkles className="w-3 h-3" />
          Audiodescrição Didática (IA)
        </button>
        <button
          onClick={() => setMode('direct')}
          disabled={isLoading}
          className={`flex-1 py-1 px-2 rounded flex items-center justify-center gap-1 transition-colors ${
            mode === 'direct'
              ? 'bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
              : 'text-[var(--text-secondary)] hover:text-[var(--text-primary)]'
          }`}
        >
          Leitura Integral
        </button>
      </div>

      {/* Estado de Carregamento ou Erro */}
      {isLoading && (
        <div className="py-4 text-center">
          <div className="inline-block animate-spin rounded-full h-4 w-4 border-2 border-current border-t-transparent mb-2"></div>
          <p className="font-mono text-xs text-[var(--text-muted)]">
            {mode === 'audiodescricao'
              ? 'IA elaborando roteiro e sintetizando voz...'
              : 'Sintetizando áudio no bucket cache...'}
          </p>
        </div>
      )}

      {errorMessage && (
        <div className="py-2 px-3 mb-3 bg-red-900/10 border border-red-500/30 rounded text-xs text-red-400 font-mono">
          {errorMessage}
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

          {/* Visualizar Roteiro da IA (Progressive Disclosure) */}
          {aiScript && (
            <div className="mt-3 pt-2 border-t border-[var(--border-color)]">
              <button
                onClick={() => setShowScript(!showScript)}
                className="flex items-center justify-between w-full text-[11px] font-mono text-[var(--text-muted)] hover:text-[var(--text-primary)]"
              >
                <span className="flex items-center gap-1">
                  <FileText className="w-3 h-3" />
                  Roteiro de Audiodescrição (IA)
                </span>
                {showScript ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
              </button>

              {showScript && (
                <div className="mt-2 p-2.5 rounded bg-[var(--bg-surface)] border border-[var(--border-color)] text-xs font-serif leading-relaxed text-[var(--text-secondary)] max-h-36 overflow-y-auto">
                  {aiScript}
                </div>
              )}
            </div>
          )}
        </>
      )}
    </div>
  );
}
