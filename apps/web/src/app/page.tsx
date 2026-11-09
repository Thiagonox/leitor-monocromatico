'use client';

import React, { useEffect, useState } from 'react';
import { Search, Book, Layers, Sparkles } from 'lucide-react';
import { fetchCatalog } from '@/lib/api';
import { getCustomCatalog, purgeLegacyRedacaoBooks } from '@/lib/storage';
import { CatalogItem } from '@mono-reader/shared';
import { ThemeToggle } from '@/components/ThemeToggle';
import { BookCard } from '@/components/BookCard';
import { AiStudio } from '@/components/AiStudio';
import { EnemEssayCorrector } from '@/components/EnemEssayCorrector';

export default function HomePage() {
  const [catalog, setCatalog] = useState<CatalogItem[]>([]);
  const [search, setSearch] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('todos');
  const [loading, setLoading] = useState(true);

  const loadAllBooks = async () => {
    purgeLegacyRedacaoBooks();
    setLoading(true);
    try {
      const baseCatalog = await fetchCatalog();
      const custom = getCustomCatalog();

      // Mescla removendo duplicatas
      const map = new Map<string, CatalogItem>();
      [...custom, ...baseCatalog].forEach(b => {
        if (!map.has(b.id)) map.set(b.id, b);
      });

      setCatalog(Array.from(map.values()));
    } catch (err) {
      console.error('Erro ao carregar catálogo:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadAllBooks();
  }, []);

  const categories = ['todos', ...Array.from(new Set(catalog.map(b => b.category).filter(Boolean)))];

  const filteredBooks = catalog.filter(book => {
    const matchesSearch =
      book.title.toLowerCase().includes(search.toLowerCase()) ||
      (book.subtitle && book.subtitle.toLowerCase().includes(search.toLowerCase())) ||
      (book.description && book.description.toLowerCase().includes(search.toLowerCase()));

    const matchesCategory =
      selectedCategory === 'todos' || book.category === selectedCategory;

    return matchesSearch && matchesCategory;
  });

  return (
    <div className="min-h-screen bg-[var(--bg-primary)] text-[var(--text-primary)]">
      {/* Top Header Minimalista */}
      <header className="border-b border-[var(--border-color)] bg-[var(--bg-surface)] sticky top-0 z-40">
        <div className="max-w-5xl mx-auto px-6 h-14 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <span className="font-mono text-sm font-bold tracking-widest px-2 py-0.5 rounded border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)]">
              墨 / INK
            </span>
            <span className="font-serif text-lg font-bold tracking-tight">
              Biblioteca de Estudos
            </span>
          </div>

          <div className="flex items-center gap-3">
            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Conteúdo Principal */}
      <main className="max-w-5xl mx-auto px-6 py-8">
        {/* Banner Editorial */}
        <div className="mb-8 pb-6 border-b border-[var(--border-color)]">
          <h1 className="font-serif text-3xl sm:text-4xl font-bold tracking-tight mb-2 text-[var(--text-primary)]">
            Acervo Editorial Monocromático
          </h1>
          <p className="font-serif text-sm sm:text-base text-[var(--text-secondary)] italic max-w-2xl leading-relaxed">
            Experiência imersiva em alto contraste inspirada no papel e-ink. Sem distrações, com tipografia refinada e leitura profunda em camadas.
          </p>
        </div>

        {/* Estúdio de Criação por IA */}
        <AiStudio onBookGenerated={loadAllBooks} />

        {/* Agente Examinador de Redação ENEM */}
        <EnemEssayCorrector />

        {/* Barra de Filtros e Busca */}
        <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4 mb-6">
          <div className="relative flex-1 max-w-md">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-[var(--text-muted)]" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Buscar por tema, tese, repertório ou autor..."
              className="w-full pl-9 pr-4 py-2 text-xs font-sans rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-primary)] focus:outline-none focus:border-[var(--border-strong)]"
            />
          </div>

          {/* Categorias */}
          <div className="flex flex-wrap items-center gap-1.5 overflow-x-auto pb-1 sm:pb-0">
            {categories.map((cat) => (
              <button
                key={cat}
                onClick={() => setSelectedCategory(cat)}
                className={`px-3 py-1 rounded text-xs font-mono capitalize transition-colors ${
                  selectedCategory === cat
                    ? 'border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
                    : 'border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-secondary)] hover:border-[var(--border-strong)]'
                }`}
              >
                {cat}
              </button>
            ))}
          </div>
        </div>

        {/* Grid de Obras */}
        {loading ? (
          <div className="py-20 text-center font-mono text-xs text-[var(--text-muted)]">
            Carregando catálogo de obras...
          </div>
        ) : filteredBooks.length === 0 ? (
          <div className="py-16 text-center border border-dashed border-[var(--border-color)] rounded p-8">
            <Book className="w-8 h-8 mx-auto mb-3 text-[var(--text-muted)]" />
            <h3 className="font-serif text-lg font-bold mb-1">Nenhuma obra encontrada</h3>
            <p className="text-xs text-[var(--text-secondary)] font-sans">
              Tente buscar por outros termos ou utilize o estúdio acima para gerar uma obra nova sob demanda.
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredBooks.map((book) => (
              <BookCard key={book.id} book={book} />
            ))}
          </div>
        )}
      </main>

      {/* Footer Minimalista */}
      <footer className="mt-20 border-t border-[var(--border-color)] py-8 text-center text-xs font-mono text-[var(--text-muted)]">
        <p>墨 / INK — Leitor Monocromático de Alto Foco • Next.js Monorepo</p>
      </footer>
    </div>
  );
}
