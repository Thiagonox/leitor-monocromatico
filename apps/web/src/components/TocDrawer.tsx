'use client';

import React from 'react';
import { X, Check } from 'lucide-react';
import { Chapter } from '@mono-reader/shared';

interface TocDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  chapters: Chapter[];
  currentChapterIndex: number;
  onSelectChapter: (index: number) => void;
  bookTitle: string;
}

export function TocDrawer({
  isOpen,
  onClose,
  chapters,
  currentChapterIndex,
  onSelectChapter,
  bookTitle
}: TocDrawerProps) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex">
      {/* Overlay */}
      <div
        className="fixed inset-0 bg-black/50 transition-opacity"
        onClick={onClose}
      />

      {/* Drawer */}
      <div className="relative w-full max-w-md bg-[var(--bg-primary)] border-r border-[var(--border-strong)] h-full overflow-y-auto p-6 z-10 flex flex-col justify-between shadow-2xl">
        <div>
          <div className="flex items-center justify-between pb-4 border-b border-[var(--border-color)] mb-6">
            <div>
              <span className="text-[10px] font-mono uppercase tracking-wider text-[var(--text-muted)]">Sumário da Obra</span>
              <h2 className="font-serif text-lg font-bold text-[var(--text-primary)] line-clamp-1">
                {bookTitle}
              </h2>
            </div>
            <button
              onClick={onClose}
              className="p-1.5 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          <div className="space-y-1">
            {chapters.map((chap, idx) => {
              const isActive = idx === currentChapterIndex;
              return (
                <button
                  key={chap.id || idx}
                  onClick={() => {
                    onSelectChapter(idx);
                    onClose();
                  }}
                  className={`w-full text-left p-3 rounded flex items-start gap-3 transition-colors ${
                    isActive
                      ? 'bg-[var(--text-primary)] text-[var(--bg-primary)] font-medium'
                      : 'hover:bg-[var(--bg-secondary)] text-[var(--text-primary)]'
                  }`}
                >
                  <span className={`font-mono text-xs pt-0.5 ${isActive ? 'text-[var(--bg-primary)]' : 'text-[var(--text-muted)]'}`}>
                    {chap.number}.
                  </span>
                  <div className="flex-1">
                    <div className="font-serif text-sm leading-snug">
                      {chap.title}
                    </div>
                  </div>
                  {isActive && <Check className="w-4 h-4 shrink-0 text-[var(--bg-primary)]" />}
                </button>
              );
            })}
          </div>
        </div>

        <div className="pt-6 border-t border-[var(--border-color)] mt-6 text-xs text-[var(--text-muted)] font-mono text-center">
          Total de {chapters.length} capítulos
        </div>
      </div>
    </div>
  );
}
