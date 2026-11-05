'use client';

import React, { useEffect, useState, use } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import {
  ArrowLeft,
  List,
  Layers,
  Volume2,
  Sparkles,
  ChevronLeft,
  ChevronRight,
  Bookmark,
  Type
} from 'lucide-react';
import { fetchBook } from '@/lib/api';
import { BookDoc, Chapter, Section } from '@mono-reader/shared';
import {
  getStoredTheme,
  setStoredTheme,
  getStoredFont,
  setStoredFont,
  getStoredFontSize,
  setStoredFontSize,
  getBookProgress,
  setBookProgress,
  ThemeMode,
  FontMode
} from '@/lib/storage';
import { ThemeToggle } from '@/components/ThemeToggle';
import { TocDrawer } from '@/components/TocDrawer';
import { QuizBlock } from '@/components/QuizBlock';
import { DeepenModal } from '@/components/DeepenModal';
import { AudioPlayerModal } from '@/components/AudioPlayerModal';

export default function ReaderPage({ params }: { params: Promise<{ id: string }> }) {
  const resolvedParams = use(params);
  const router = useRouter();

  const [book, setBook] = useState<BookDoc | null>(null);
  const [currentChapterIndex, setCurrentChapterIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [tocOpen, setTocOpen] = useState(false);
  const [deepenOpen, setDeepenOpen] = useState(false);
  const [audioOpen, setAudioOpen] = useState(false);
  const [fontSize, setFontSizeState] = useState(20);
  const [fontMode, setFontModeState] = useState<FontMode>('serif');
  const [selectedTextForDeepen, setSelectedTextForDeepen] = useState('');

  // Carrega Livro
  useEffect(() => {
    let active = true;
    async function load() {
      setLoading(true);
      const doc = await fetchBook(resolvedParams.id);
      if (active) {
        if (doc) {
          setBook(doc);
          const progress = getBookProgress(doc.meta.id);
          if (progress.chapterIndex < doc.chapters.length) {
            setCurrentChapterIndex(progress.chapterIndex);
          }
        }
        setLoading(false);
      }
    }
    load();
    return () => { active = false; };
  }, [resolvedParams.id]);

  // Carrega Preferências
  useEffect(() => {
    const sSize = getStoredFontSize();
    setFontSizeState(sSize);
    const sFont = getStoredFont();
    setFontModeState(sFont);
  }, []);

  // Salva Progresso ao trocar de capítulo
  useEffect(() => {
    if (book) {
      setBookProgress(book.meta.id, currentChapterIndex, 0);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }, [currentChapterIndex, book]);

  const changeFontSize = (delta: number) => {
    const next = Math.min(32, Math.max(14, fontSize + delta));
    setFontSizeState(next);
    setStoredFontSize(next);
  };

  const toggleFont = () => {
    const next: FontMode = fontMode === 'serif' ? 'sans' : fontMode === 'sans' ? 'mono' : 'serif';
    setFontModeState(next);
    setStoredFont(next);
  };

  const currentChapter: Chapter | undefined = book?.chapters[currentChapterIndex];

  // Captura seleção de texto para aprofundar
  const handleOpenDeepen = () => {
    const sel = window.getSelection()?.toString().trim();
    if (sel && sel.length > 2) {
      setSelectedTextForDeepen(sel);
    } else {
      setSelectedTextForDeepen(currentChapter?.title || '');
    }
    setDeepenOpen(true);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-[var(--bg-primary)] flex items-center justify-center font-mono text-xs text-[var(--text-muted)]">
        Carregando obra no leitor monocromático...
      </div>
    );
  }

  if (!book || !currentChapter) {
    return (
      <div className="min-h-screen bg-[var(--bg-primary)] flex flex-col items-center justify-center p-6 text-center">
        <h2 className="font-serif text-2xl font-bold mb-3">Obra não encontrada</h2>
        <p className="text-xs text-[var(--text-secondary)] font-sans mb-6">
          Não foi possível localizar o conteúdo desta obra.
        </p>
        <Link
          href="/"
          className="px-4 py-2 border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs rounded"
        >
          Voltar para a Biblioteca
        </Link>
      </div>
    );
  }

  const allChapterText = currentChapter.sections.map(s => s.content || '').join('\n\n');

  return (
    <div className="min-h-screen bg-[var(--bg-primary)] text-[var(--text-primary)]">
      {/* Barra de Ferramentas Superior Fixa */}
      <header className="sticky top-0 z-40 bg-[var(--bg-primary)]/95 backdrop-blur-sm border-b border-[var(--border-color)]">
        <div className="max-w-4xl mx-auto px-4 h-14 flex items-center justify-between gap-2">
          {/* Voltar & Sumário */}
          <div className="flex items-center gap-2">
            <Link
              href="/"
              className="p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono"
              title="Voltar à Biblioteca"
            >
              <ArrowLeft className="w-4 h-4" />
              <span className="hidden sm:inline">Biblioteca</span>
            </Link>

            <button
              onClick={() => setTocOpen(true)}
              className="p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono"
              title="Abrir Sumário"
            >
              <List className="w-4 h-4" />
              <span className="hidden md:inline">Sumário</span>
            </button>
          </div>

          {/* Título Central Truncado */}
          <div className="hidden lg:block text-center flex-1 mx-4">
            <span className="font-serif text-xs italic text-[var(--text-secondary)] line-clamp-1">
              {book.meta.title} — Cap. {currentChapter.number}
            </span>
          </div>

          {/* Controles de Leitura */}
          <div className="flex items-center gap-1.5 sm:gap-2">
            {/* Modo Camadas */}
            <Link
              href={`/reader/${book.meta.id}/camadas`}
              className="px-2.5 py-1.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] text-xs font-mono flex items-center gap-1"
              title="Alternar para Modo de Leitura em Camadas"
            >
              <Layers className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Camadas</span>
            </Link>

            {/* Aprofundar */}
            <button
              onClick={handleOpenDeepen}
              className="p-1.5 sm:px-2 sm:py-1.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] text-xs font-mono flex items-center gap-1"
              title="Aprofundar conceito selecionado com IA"
            >
              <Sparkles className="w-3.5 h-3.5" />
              <span className="hidden md:inline">Aprofundar</span>
            </button>

            {/* Ouvir */}
            <button
              onClick={() => setAudioOpen(true)}
              className="p-1.5 sm:px-2 sm:py-1.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] text-xs font-mono flex items-center gap-1"
              title="Audiodescrição / Ouvir Capítulo"
            >
              <Volume2 className="w-3.5 h-3.5" />
              <span className="hidden md:inline">Ouvir</span>
            </button>

            {/* Alternar Fonte */}
            <button
              onClick={toggleFont}
              className="p-1.5 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-xs"
              title={`Alternar Fonte (Atual: ${fontMode})`}
            >
              <Type className="w-4 h-4" />
            </button>

            {/* Tamanho de Fonte */}
            <div className="flex items-center border border-[var(--border-color)] rounded bg-[var(--bg-surface)] text-xs font-mono">
              <button
                onClick={() => changeFontSize(-2)}
                className="px-2 py-1 hover:bg-[var(--bg-secondary)] border-r border-[var(--border-color)]"
                title="Diminuir Fonte"
              >
                A-
              </button>
              <button
                onClick={() => changeFontSize(2)}
                className="px-2 py-1 hover:bg-[var(--bg-secondary)]"
                title="Aumentar Fonte"
              >
                A+
              </button>
            </div>

            {/* Alternar Tema */}
            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Sumário Drawer */}
      <TocDrawer
        isOpen={tocOpen}
        onClose={() => setTocOpen(false)}
        chapters={book.chapters}
        currentChapterIndex={currentChapterIndex}
        onSelectChapter={setCurrentChapterIndex}
        bookTitle={book.meta.title}
      />

      {/* Coluna Central de Leitura */}
      <main className="reader-container py-12 md:py-16">
        {/* Cabeçalho do Capítulo */}
        <header className="mb-10 text-center">
          <div className="font-mono text-xs uppercase tracking-widest text-[var(--text-muted)] mb-3">
            Capítulo {currentChapter.number} de {book.chapters.length}
          </div>
          <h1 className="reader-heading-1 font-serif text-3xl sm:text-4xl leading-tight">
            {currentChapter.title}
          </h1>

          {/* Epígrafe */}
          {currentChapter.epigraph && (
            <div className="reader-epigraph font-serif text-sm">
              <p className="italic">&ldquo;{currentChapter.epigraph.text}&rdquo;</p>
              {currentChapter.epigraph.author && (
                <span className="reader-epigraph-author">
                  — {currentChapter.epigraph.author}
                </span>
              )}
            </div>
          )}
        </header>

        {/* Seções do Capítulo */}
        <article className="space-y-6">
          {currentChapter.sections.map((sec: Section, sIdx: number) => {
            if (sec.type === 'heading') {
              if (sec.level === 2) {
                return (
                  <h2 key={sIdx} className="reader-heading-2">
                    {sec.content}
                  </h2>
                );
              }
              return (
                <h3 key={sIdx} className="reader-heading-3">
                  {sec.content}
                </h3>
              );
            }

            if (sec.type === 'callout') {
              return (
                <div key={sIdx} className="reader-callout font-sans text-sm">
                  {sec.title && (
                    <div className="font-mono text-xs uppercase tracking-wider font-bold mb-2 text-[var(--text-primary)]">
                      {sec.title}
                    </div>
                  )}
                  <p className="whitespace-pre-line leading-relaxed text-[var(--text-secondary)]">
                    {sec.content}
                  </p>
                </div>
              );
            }

            if (sec.type === 'quote') {
              return (
                <blockquote key={sIdx} className="reader-blockquote font-serif text-base">
                  <p className="italic">&ldquo;{sec.content}&rdquo;</p>
                  {sec.author && (
                    <cite className="block text-xs font-mono not-italic mt-2 text-[var(--text-muted)]">
                      — {sec.author}
                    </cite>
                  )}
                </blockquote>
              );
            }

            // Paragraph padrão
            return (
              <p key={sIdx} className="reader-paragraph">
                {sec.content}
              </p>
            );
          })}
        </article>

        {/* Quizzes do Capítulo */}
        {currentChapter.quiz && currentChapter.quiz.length > 0 && (
          <div className="mt-12 pt-8 border-t border-[var(--border-strong)]">
            <h3 className="font-serif text-xl font-bold mb-4">
              Recuperação Ativa & Fixação
            </h3>
            {currentChapter.quiz.map((q, qIdx) => (
              <QuizBlock key={qIdx} quiz={q} index={qIdx + 1} />
            ))}
          </div>
        )}

        {/* Quizzes Globais da Obra no último capítulo */}
        {currentChapterIndex === book.chapters.length - 1 && book.quiz && book.quiz.length > 0 && (
          <div className="mt-12 pt-8 border-t-2 border-[var(--border-strong)]">
            <h3 className="font-serif text-2xl font-bold mb-2">
              Desafio Geral da Obra
            </h3>
            <p className="text-xs text-[var(--text-secondary)] font-sans mb-6">
              Teste sua fixação final com as questões fundamentais do manual.
            </p>
            {book.quiz.map((q, qIdx) => (
              <QuizBlock key={`global-${qIdx}`} quiz={q} index={qIdx + 1} />
            ))}
          </div>
        )}

        {/* Navegação Inferior entre Capítulos */}
        <nav className="mt-16 pt-8 border-t border-[var(--border-color)] flex items-center justify-between gap-4 font-mono text-xs">
          <button
            onClick={() => setCurrentChapterIndex(prev => Math.max(0, prev - 1))}
            disabled={currentChapterIndex === 0}
            className="flex items-center gap-1.5 p-2 rounded border border-[var(--border-color)] hover:bg-[var(--bg-secondary)] disabled:opacity-30 disabled:hover:bg-transparent"
          >
            <ChevronLeft className="w-4 h-4" />
            <span>Anterior</span>
          </button>

          <span className="text-[var(--text-muted)] text-center">
            {currentChapterIndex + 1} / {book.chapters.length}
          </span>

          <button
            onClick={() => setCurrentChapterIndex(prev => Math.min(book.chapters.length - 1, prev + 1))}
            disabled={currentChapterIndex === book.chapters.length - 1}
            className="flex items-center gap-1.5 p-2 rounded border border-[var(--border-color)] hover:bg-[var(--bg-secondary)] disabled:opacity-30 disabled:hover:bg-transparent"
          >
            <span>Próximo</span>
            <ChevronRight className="w-4 h-4" />
          </button>
        </nav>
      </main>

      {/* Modais de Aprofundamento e Áudio */}
      <DeepenModal
        isOpen={deepenOpen}
        onClose={() => setDeepenOpen(false)}
        initialTopic={selectedTextForDeepen}
        contextText={allChapterText.slice(0, 400)}
      />

      <AudioPlayerModal
        isOpen={audioOpen}
        onClose={() => setAudioOpen(false)}
        textToRead={allChapterText}
        chapterTitle={`${book.meta.title} — Cap. ${currentChapter.number}: ${currentChapter.title}`}
      />
    </div>
  );
}
