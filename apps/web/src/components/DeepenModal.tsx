'use client';

import React, { useState } from 'react';
import { X, Sparkles, Loader2 } from 'lucide-react';
import { deepenTopic } from '@/lib/api';

interface DeepenModalProps {
  isOpen: boolean;
  onClose: () => void;
  initialTopic?: string;
  contextText?: string;
}

export function DeepenModal({ isOpen, onClose, initialTopic = '', contextText = '' }: DeepenModalProps) {
  const [topic, setTopic] = useState(initialTopic);
  const [loading, setLoading] = useState(false);
  const [content, setContent] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  if (!isOpen) return null;

  const handleDeepen = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!topic.trim() || loading) return;

    setLoading(true);
    setError(null);
    setContent(null);

    try {
      const data = await deepenTopic({
        topic: topic.trim(),
        contextText,
        style: 'didatico',
        level: 1
      });
      setContent(data.content);
    } catch (err: any) {
      setError(err.message || 'Erro ao aprofundar conceito.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="fixed inset-0 bg-black/60 backdrop-blur-sm" onClick={onClose} />

      <div className="relative w-full max-w-2xl bg-[var(--bg-primary)] border border-[var(--border-strong)] rounded-lg shadow-2xl p-6 z-10 max-h-[85vh] flex flex-col">
        <div className="flex items-center justify-between pb-4 border-b border-[var(--border-color)] mb-4">
          <div className="flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-[var(--text-primary)]" />
            <h3 className="font-serif text-lg font-bold text-[var(--text-primary)]">
              Aprofundamento Didático por IA
            </h3>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-muted)] hover:text-[var(--text-primary)]"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <form onSubmit={handleDeepen} className="mb-4">
          <div className="flex gap-2">
            <input
              type="text"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              placeholder="Digite o conceito ou termo a aprofundar..."
              className="flex-1 p-2.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-primary)] text-sm font-sans focus:outline-none focus:border-[var(--border-strong)]"
            />
            <button
              type="submit"
              disabled={loading || !topic.trim()}
              className="px-4 py-2.5 rounded bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90 disabled:opacity-50 flex items-center gap-1.5"
            >
              {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : 'Aprofundar'}
            </button>
          </div>
        </form>

        <div className="flex-1 overflow-y-auto pr-2">
          {loading && (
            <div className="flex flex-col items-center justify-center py-12 text-center text-xs font-mono text-[var(--text-muted)]">
              <Loader2 className="w-6 h-6 animate-spin mb-3 text-[var(--text-primary)]" />
              <span>Consultando referências e estruturando explicação didática...</span>
            </div>
          )}

          {error && (
            <div className="p-4 rounded border border-red-500 bg-red-50 dark:bg-red-950/40 text-red-600 dark:text-red-300 text-xs font-mono">
              {error}
            </div>
          )}

          {content && (
            <div className="space-y-4 font-serif text-sm leading-relaxed text-[var(--text-primary)] whitespace-pre-line">
              {content}
            </div>
          )}

          {!loading && !content && !error && (
            <p className="text-center py-8 text-xs text-[var(--text-muted)] font-mono">
              Clique em &quot;Aprofundar&quot; para gerar uma análise detalhada deste conceito com analogias, mecanismos e aplicações práticas.
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
