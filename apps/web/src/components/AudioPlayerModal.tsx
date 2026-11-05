'use client';

import React, { useState, useEffect } from 'react';
import { Volume2, Play, Pause, Square, X, RotateCcw } from 'lucide-react';

interface AudioPlayerModalProps {
  isOpen: boolean;
  onClose: () => void;
  textToRead: string;
  chapterTitle?: string;
}

export function AudioPlayerModal({ isOpen, onClose, textToRead, chapterTitle }: AudioPlayerModalProps) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [rate, setRate] = useState(1);
  const [synth, setSynth] = useState<SpeechSynthesis | null>(null);

  useEffect(() => {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      setSynth(window.speechSynthesis);
    }
  }, []);

  useEffect(() => {
    return () => {
      if (synth) {
        synth.cancel();
      }
    };
  }, [synth]);

  if (!isOpen) return null;

  const handlePlay = () => {
    if (!synth) return;

    if (synth.paused) {
      synth.resume();
      setIsPlaying(true);
      return;
    }

    synth.cancel();
    const utterance = new SpeechSynthesisUtterance(textToRead.slice(0, 3000));
    utterance.lang = 'pt-BR';
    utterance.rate = rate;

    utterance.onend = () => {
      setIsPlaying(false);
    };

    utterance.onerror = () => {
      setIsPlaying(false);
    };

    synth.speak(utterance);
    setIsPlaying(true);
  };

  const handlePause = () => {
    if (!synth) return;
    synth.pause();
    setIsPlaying(false);
  };

  const handleStop = () => {
    if (!synth) return;
    synth.cancel();
    setIsPlaying(false);
  };

  const handleRateChange = (newRate: number) => {
    setRate(newRate);
    if (isPlaying) {
      handleStop();
      setTimeout(handlePlay, 100);
    }
  };

  return (
    <div className="fixed bottom-6 right-6 z-50 w-full max-w-sm bg-[var(--bg-primary)] border border-[var(--border-strong)] rounded-lg shadow-2xl p-4">
      <div className="flex items-center justify-between pb-3 border-b border-[var(--border-color)] mb-3">
        <div className="flex items-center gap-2">
          <Volume2 className="w-4 h-4 text-[var(--text-primary)]" />
          <span className="font-mono text-xs font-bold uppercase tracking-wider text-[var(--text-primary)]">
            Audiodescrição & Leitura
          </span>
        </div>
        <button
          onClick={() => {
            handleStop();
            onClose();
          }}
          className="p-1 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-muted)] hover:text-[var(--text-primary)]"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      {chapterTitle && (
        <p className="font-serif text-xs italic text-[var(--text-secondary)] mb-3 line-clamp-1">
          {chapterTitle}
        </p>
      )}

      <div className="flex items-center justify-between gap-3">
        <div className="flex items-center gap-2">
          {isPlaying ? (
            <button
              onClick={handlePause}
              className="p-2.5 rounded-full bg-[var(--text-primary)] text-[var(--bg-primary)] hover:opacity-90 transition-opacity"
            >
              <Pause className="w-4 h-4" />
            </button>
          ) : (
            <button
              onClick={handlePlay}
              className="p-2.5 rounded-full bg-[var(--text-primary)] text-[var(--bg-primary)] hover:opacity-90 transition-opacity"
            >
              <Play className="w-4 h-4 ml-0.5" />
            </button>
          )}

          <button
            onClick={handleStop}
            className="p-2 rounded border border-[var(--border-color)] text-[var(--text-muted)] hover:text-[var(--text-primary)]"
          >
            <Square className="w-3.5 h-3.5" />
          </button>
        </div>

        <div className="flex items-center gap-1.5 text-xs font-mono">
          <span className="text-[var(--text-muted)]">Vel:</span>
          {[0.8, 1, 1.25, 1.5].map((r) => (
            <button
              key={r}
              onClick={() => handleRateChange(r)}
              className={`px-1.5 py-0.5 rounded text-[11px] ${
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
    </div>
  );
}
