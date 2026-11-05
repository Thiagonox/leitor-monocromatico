'use client';

import React from 'react';
import Link from 'next/link';
import { Book, Layers, Clock, Bookmark, Sparkles } from 'lucide-react';
import { CatalogItem } from '@mono-reader/shared';

interface BookCardProps {
  book: CatalogItem;
}

export function BookCard({ book }: BookCardProps) {
  const isPriority = book.isPriority || book.id === 'redacao-enem';

  return (
    <div className={`flex flex-col justify-between p-6 rounded border bg-[var(--bg-card)] transition-all duration-200 hover:border-[var(--border-strong)] relative ${
      isPriority ? 'border-[var(--border-strong)] shadow-sm' : 'border-[var(--border-color)]'
    }`}>
      {isPriority && (
        <div className="absolute -top-3 left-5 bg-[var(--text-primary)] text-[var(--bg-primary)] px-2.5 py-0.5 text-[10px] font-mono uppercase tracking-wider font-bold rounded">
          Obra Oficial em Destaque
        </div>
      )}

      <div>
        <div className="flex items-center justify-between text-xs text-[var(--text-muted)] font-mono mb-2">
          <span className="uppercase tracking-wider">{book.category || 'Estudo Editorial'}</span>
          {book.isGeneratedByAI && (
            <span className="flex items-center gap-1 text-[11px]">
              <Sparkles className="w-3 h-3" /> IA Editorial
            </span>
          )}
        </div>

        <h3 className="font-serif text-xl font-bold leading-snug mb-2 text-[var(--text-primary)]">
          {book.title}
        </h3>

        {book.subtitle && (
          <p className="font-serif text-sm text-[var(--text-secondary)] italic mb-3 line-clamp-2">
            {book.subtitle}
          </p>
        )}

        <p className="text-xs text-[var(--text-secondary)] line-clamp-3 mb-4 leading-relaxed font-sans">
          {book.description}
        </p>
      </div>

      <div>
        <div className="flex items-center justify-between pt-3 border-t border-[var(--border-color)] text-xs text-[var(--text-muted)] font-mono mb-4">
          <div className="flex items-center gap-1.5">
            <Book className="w-3.5 h-3.5" />
            <span>{book.chaptersCount} {book.chaptersCount === 1 ? 'capítulo' : 'capítulos'}</span>
          </div>
          {book.estimatedTime && (
            <div className="flex items-center gap-1.5">
              <Clock className="w-3.5 h-3.5" />
              <span>{book.estimatedTime}</span>
            </div>
          )}
        </div>

        <div className="grid grid-cols-2 gap-2">
          <Link
            href={`/reader/${book.id}`}
            className="flex items-center justify-center gap-1.5 py-2 px-3 text-xs font-mono font-medium border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] hover:opacity-90 rounded transition-opacity"
          >
            <Book className="w-3.5 h-3.5" />
            <span>Leitor Padrão</span>
          </Link>

          <Link
            href={`/reader/${book.id}/camadas`}
            className="flex items-center justify-center gap-1.5 py-2 px-3 text-xs font-mono font-medium border border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] rounded transition-colors"
          >
            <Layers className="w-3.5 h-3.5" />
            <span>Modo Camadas</span>
          </Link>
        </div>
      </div>
    </div>
  );
}
