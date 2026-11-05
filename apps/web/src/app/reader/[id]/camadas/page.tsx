'use client';

import React, { useEffect, useState, useRef, use } from 'react';
import Link from 'next/link';
import {
  ArrowLeft,
  List,
  Volume2,
  Layers,
  Pencil,
} from 'lucide-react';
import { fetchBook } from '@/lib/api';
import { BookDoc, Chapter, Section } from '@mono-reader/shared';
import { ThemeToggle } from '@/components/ThemeToggle';
import { TocDrawer } from '@/components/TocDrawer';
import { AudioPlayerModal, AudioPlaybackState } from '@/components/AudioPlayerModal';
import { ReadingPencilGuide } from '@/components/ReadingPencilGuide';

const LAYERS = [
  { id: 1, title: 'Resumo Essencial', subtitle: 'Visão direta e rápida dos pontos-chave' },
  { id: 2, title: 'Versão Intermediária', subtitle: 'Conceito, Exemplo e Aplicação' },
  { id: 3, title: 'Texto Completo', subtitle: 'Imersão detalhada e aprofundada' },
];

export default function LayeredReaderPage({ params }: { params: Promise<{ id: string }> }) {
  const resolvedParams = use(params);

  const [book, setBook] = useState<BookDoc | null>(null);
  const [currentChapterIndex, setCurrentChapterIndex] = useState(0);
  const [activeLayer, setActiveLayer] = useState<number>(1);
  const [loading, setLoading] = useState(true);
  const [tocOpen, setTocOpen] = useState(false);
  const [audioOpen, setAudioOpen] = useState(false);
  const [pencilEnabled, setPencilEnabled] = useState(true);
  const [audioPlayback, setAudioPlayback] = useState<AudioPlaybackState>({
    isPlaying: false,
    currentTime: 0,
    duration: 0,
    isLoading: false,
  });

  const contentRef = useRef<HTMLElement | null>(null);
  const chapterRefs = useRef<(HTMLElement | null)[]>([]);
  const activeChapterContainerRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    activeChapterContainerRef.current = chapterRefs.current[currentChapterIndex] || contentRef.current;
  }, [currentChapterIndex]);

  useEffect(() => {
    let active = true;
    async function load() {
      setLoading(true);
      const doc = await fetchBook(resolvedParams.id);
      if (active) {
        if (doc) {
          setBook(doc);
        }
        setLoading(false);
      }
    }
    load();
    return () => {
      active = false;
    };
  }, [resolvedParams.id]);

  // Observa os capítulos em tela para atualizar o cabeçalho no fluxo contínuo
  useEffect(() => {
    if (!book || loading) return;

    const sections = document.querySelectorAll<HTMLElement>('.chapter-section');
    if (!sections.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            const idxStr = entry.target.getAttribute('data-chapter-index');
            if (idxStr !== null) {
              const idx = parseInt(idxStr, 10);
              setCurrentChapterIndex(idx);
            }
          }
        }
      },
      {
        rootMargin: '-10% 0px -70% 0px',
        threshold: 0,
      }
    );

    sections.forEach((sec) => observer.observe(sec));

    return () => observer.disconnect();
  }, [book, loading, activeLayer]);

  const handleSelectChapter = (index: number) => {
    setCurrentChapterIndex(index);
    setTocOpen(false);
    const targetChapter = book?.chapters[index];
    if (targetChapter) {
      const el = document.getElementById(`chapter-${targetChapter.id || index}`);
      if (el) {
        const y = el.getBoundingClientRect().top + window.pageYOffset - 110;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }
  };

  const handleNextChapter = () => {
    if (!book) return;
    if (currentChapterIndex < book.chapters.length - 1) {
      const nextIdx = currentChapterIndex + 1;
      setCurrentChapterIndex(nextIdx);
      const targetChapter = book.chapters[nextIdx];
      const el = document.getElementById(`chapter-${targetChapter.id || nextIdx}`);
      if (el) {
        const y = el.getBoundingClientRect().top + window.pageYOffset - 110;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }
  };

  const handlePreviousChapter = () => {
    if (!book) return;
    if (currentChapterIndex > 0) {
      const prevIdx = currentChapterIndex - 1;
      setCurrentChapterIndex(prevIdx);
      const targetChapter = book.chapters[prevIdx];
      const el = document.getElementById(`chapter-${targetChapter.id || prevIdx}`);
      if (el) {
        const y = el.getBoundingClientRect().top + window.pageYOffset - 110;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }
  };

  const currentChapter: Chapter | undefined = book?.chapters[currentChapterIndex];
  const allCurrentChapterText = currentChapter?.sections.map((s) => s.content || '').join('\n\n') || '';

  if (loading) {
    return (
      <div className="min-h-screen bg-[var(--bg-primary)] flex items-center justify-center font-mono text-xs text-[var(--text-muted)]">
        Carregando leitor contínuo em camadas...
      </div>
    );
  }

  if (!book || !book.chapters || book.chapters.length === 0) {
    return (
      <div className="min-h-screen bg-[var(--bg-primary)] flex flex-col items-center justify-center p-6 text-center text-[var(--text-primary)]">
        <h2 className="font-serif text-2xl font-bold mb-3">Obra não encontrada</h2>
        <Link
          href="/"
          className="px-4 py-2 border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs rounded"
        >
          Voltar à Biblioteca
        </Link>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[var(--bg-primary)] text-[var(--text-primary)]">
      {/* Top Header */}
      <header className="sticky top-0 z-40 bg-[var(--bg-primary)]/95 backdrop-blur-sm border-b border-[var(--border-color)]">
        <div className="max-w-4xl mx-auto px-4 h-14 flex items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <Link
              href={`/reader/${book.meta.id}`}
              className="p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono"
              title="Voltar ao Leitor Padrão"
            >
              <ArrowLeft className="w-4 h-4" />
              <span className="hidden sm:inline">Leitor Padrão</span>
            </Link>

            <button
              onClick={() => setTocOpen(true)}
              className="p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono"
              title="Sumário de Capítulos"
            >
              <List className="w-4 h-4" />
              <span className="hidden sm:inline">Capítulos</span>
            </button>
          </div>

          <div className="hidden md:block text-center font-mono text-xs text-[var(--text-secondary)] line-clamp-1 max-w-sm">
            Cap. {currentChapter?.number}: {currentChapter?.title}
          </div>

          <div className="flex items-center gap-2">
            {/* Lápis Guia de Leitura */}
            <button
              onClick={() => setPencilEnabled(!pencilEnabled)}
              className={`p-1.5 rounded transition-colors text-xs font-mono flex items-center gap-1 ${
                pencilEnabled
                  ? 'bg-[var(--border-strong)] text-[var(--bg-primary)]'
                  : 'hover:bg-[var(--bg-secondary)] text-[var(--text-muted)]'
              }`}
              title={pencilEnabled ? 'Desativar Lápis de Leitura' : 'Ativar Lápis de Leitura'}
            >
              <Pencil className="w-3.5 h-3.5" />
              <span className="hidden lg:inline">Lápis</span>
            </button>

            <button
              onClick={() => setAudioOpen(true)}
              className="p-1.5 sm:px-2 sm:py-1.5 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1 text-xs font-mono border border-[var(--border-color)]"
              title="Audiodescrição com IA do Capítulo"
            >
              <Volume2 className="w-4 h-4" />
              <span className="hidden sm:inline">Ouvir</span>
            </button>

            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Seletor Editorial de Camadas Fixo */}
      <div className="border-b border-[var(--border-color)] bg-[var(--bg-surface)] sticky top-14 z-30">
        <div className="max-w-3xl mx-auto px-4 py-2 flex items-center justify-between gap-2">
          {LAYERS.map((layer) => {
            const isActive = activeLayer === layer.id;
            return (
              <button
                key={layer.id}
                onClick={() => setActiveLayer(layer.id)}
                className={`flex-1 py-2 px-3 text-left rounded border transition-all ${
                  isActive
                    ? 'border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] shadow-sm'
                    : 'border-[var(--border-color)] hover:bg-[var(--bg-secondary)] text-[var(--text-primary)]'
                }`}
              >
                <div className="font-mono text-[11px] sm:text-xs font-bold uppercase tracking-wider mb-0.5 truncate">
                  {layer.id}. {layer.title}
                </div>
                <div
                  className={`text-[11px] font-sans line-clamp-1 hidden sm:block ${
                    isActive ? 'opacity-90' : 'text-[var(--text-muted)]'
                  }`}
                >
                  {layer.subtitle}
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* Drawer de Capítulos */}
      <TocDrawer
        isOpen={tocOpen}
        onClose={() => setTocOpen(false)}
        chapters={book.chapters}
        currentChapterIndex={currentChapterIndex}
        onSelectChapter={handleSelectChapter}
        bookTitle={book.meta.title}
      />

      {/* Conteúdo Principal Monocromático em Scroll Contínuo Infinito */}
      <main ref={contentRef} className="max-w-2xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
        {book.chapters.map((chapter: Chapter, cIdx: number) => {
          const paragraphs = chapter.sections.filter((s) => s.type === 'paragraph');
          const callouts = chapter.sections.filter((s) => s.type === 'callout');
          const summaryParagraphs = paragraphs.slice(0, 2);
          const mainCallout = callouts[0] || null;

          return (
            <section
              key={chapter.id || cIdx}
              id={`chapter-${chapter.id || cIdx}`}
              data-chapter-index={cIdx}
              ref={(el) => {
                chapterRefs.current[cIdx] = el;
              }}
              className="chapter-section pt-8 sm:pt-14 pb-12 sm:pb-16 border-b border-[var(--border-color)] last:border-b-0"
            >
              {/* Cabeçalho do Capítulo */}
              <div className="mb-8 pb-4 border-b border-[var(--border-color)]">
                <div className="flex items-center gap-2 mb-2 font-mono text-xs text-[var(--text-muted)] uppercase tracking-widest">
                  <Layers className="w-3.5 h-3.5" />
                  <span>
                    Capítulo {chapter.number} de {book.chapters.length} · {LAYERS[activeLayer - 1].title}
                  </span>
                </div>

                <h2 className="font-serif text-2xl sm:text-3xl font-bold tracking-tight text-[var(--text-primary)] mb-3 leading-tight">
                  {chapter.title}
                </h2>

                {chapter.epigraph && (
                  <blockquote className="border-l-2 border-[var(--border-strong)] pl-4 my-3 font-serif italic text-xs sm:text-sm text-[var(--text-secondary)]">
                    &ldquo;{chapter.epigraph.text}&rdquo;
                    {chapter.epigraph.author && (
                      <cite className="block text-xs font-mono text-[var(--text-muted)] mt-1 not-italic">
                        — {chapter.epigraph.author}
                      </cite>
                    )}
                  </blockquote>
                )}
              </div>

              {/* CAMADA 1: RESUMO ESSENCIAL */}
              {activeLayer === 1 && (
                <div className="space-y-4">
                  {summaryParagraphs.map((p, idx) => (
                    <p key={idx} className="font-serif text-base sm:text-lg leading-relaxed text-[var(--text-primary)]">
                      {p.content}
                    </p>
                  ))}

                  {mainCallout && (
                    <div className="p-4 rounded border border-[var(--border-strong)] bg-[var(--bg-card)] my-4">
                      <span className="font-mono text-xs font-bold uppercase tracking-wider text-[var(--text-primary)] block mb-1">
                        📌 {mainCallout.title || 'Ponto Central'}
                      </span>
                      <p className="font-serif text-sm sm:text-base leading-relaxed text-[var(--text-secondary)]">
                        {mainCallout.content}
                      </p>
                    </div>
                  )}
                </div>
              )}

              {/* CAMADA 2: VERSÃO INTERMEDIÁRIA (CONCEITO, EXEMPLO E APLICAÇÃO) */}
              {activeLayer === 2 && (
                <div className="space-y-6">
                  <div className="space-y-2 pb-4 border-b border-[var(--border-color)]">
                    <div className="flex items-center gap-2 font-mono text-xs font-bold uppercase text-[var(--text-primary)]">
                      <span className="w-5 h-5 rounded-full border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] flex items-center justify-center text-[10px]">1</span>
                      <span>O Conceito Fundamental</span>
                    </div>
                    <p className="font-serif text-base sm:text-lg leading-relaxed text-[var(--text-primary)]">
                      {paragraphs[0]?.content || 'Compreender a base estrutural deste capítulo antes de avançar para a execução prática.'}
                    </p>
                  </div>

                  <div className="space-y-2 pb-4 border-b border-[var(--border-color)]">
                    <div className="flex items-center gap-2 font-mono text-xs font-bold uppercase text-[var(--text-primary)]">
                      <span className="w-5 h-5 rounded-full border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] flex items-center justify-center text-[10px]">2</span>
                      <span>O Exemplo em Ação</span>
                    </div>
                    <p className="font-serif text-base sm:text-lg leading-relaxed text-[var(--text-primary)]">
                      {paragraphs[1]?.content || 'Observe como a teoria se manifesta em situações reais de avaliação e análise argumentativa.'}
                    </p>
                  </div>

                  <div className="space-y-2 pb-4 border-b border-[var(--border-color)]">
                    <div className="flex items-center gap-2 font-mono text-xs font-bold uppercase text-[var(--text-primary)]">
                      <span className="w-5 h-5 rounded-full border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] flex items-center justify-center text-[10px]">3</span>
                      <span>Como Aplicar no Seu Rascunho</span>
                    </div>
                    <p className="font-serif text-base sm:text-lg leading-relaxed text-[var(--text-primary)]">
                      {paragraphs[2]?.content || 'Transponha este princípio diretamente para a construção da sua redação ou estudo diário.'}
                    </p>
                  </div>
                </div>
              )}

              {/* CAMADA 3: TEXTO COMPLETO E APROFUNDADO */}
              {activeLayer === 3 && (
                <div className="space-y-5">
                  {chapter.sections.map((sec: Section, sIdx: number) => {
                    if (sec.type === 'heading') {
                      return (
                        <h3 key={sIdx} className="font-serif text-xl sm:text-2xl font-bold mt-6 mb-2 text-[var(--text-primary)]">
                          {sec.content}
                        </h3>
                      );
                    }

                    if (sec.type === 'callout') {
                      return (
                        <div key={sIdx} className="p-4 rounded border border-[var(--border-color)] bg-[var(--bg-card)] my-4">
                          {sec.title && (
                            <div className="font-mono text-xs uppercase tracking-wider font-bold mb-1 text-[var(--text-primary)]">
                              💡 {sec.title}
                            </div>
                          )}
                          <p className="font-serif text-sm sm:text-base leading-relaxed text-[var(--text-secondary)]">
                            {sec.content}
                          </p>
                        </div>
                      );
                    }

                    return (
                      <p key={sIdx} className="font-serif text-base sm:text-lg leading-relaxed text-[var(--text-primary)]">
                        {sec.content}
                      </p>
                    );
                  })}
                </div>
              )}
            </section>
          );
        })}

        {/* Fim da Leitura em Camadas */}
        <div className="py-12 text-center border-t-2 border-[var(--border-strong)] mt-8">
          <div className="font-mono text-xs uppercase tracking-widest text-[var(--text-muted)] mb-2">
            Fim da Leitura em Camadas
          </div>
          <h3 className="font-serif text-2xl font-bold mb-2">
            {book.meta.title}
          </h3>
          <p className="text-xs text-[var(--text-secondary)] font-sans max-w-md mx-auto">
            Você percorreu todos os capítulos nesta camada de forma contínua. Alterne para outra camada no topo sempre que desejar outro nível de profundidade.
          </p>
        </div>
      </main>

      {/* Modal de Audiodescrição com IA */}
      <AudioPlayerModal
        isOpen={audioOpen}
        onClose={() => setAudioOpen(false)}
        textToRead={allCurrentChapterText}
        chapterTitle={`${book.meta.title} — Cap. ${currentChapter?.number}: ${currentChapter?.title}`}
        chapterId={`${book.meta.id}-${currentChapter?.id}`}
        onPlaybackUpdate={setAudioPlayback}
        onNextChapter={handleNextChapter}
        onPreviousChapter={handlePreviousChapter}
        hasNextChapter={currentChapterIndex < book.chapters.length - 1}
        hasPreviousChapter={currentChapterIndex > 0}
      />

      {/* Guia Animado do Lápis Editorial */}
      <ReadingPencilGuide
        containerRef={activeChapterContainerRef}
        isPlaying={audioPlayback.isPlaying}
        currentTime={audioPlayback.currentTime}
        duration={audioPlayback.duration}
        isLoading={audioPlayback.isLoading}
        enabled={pencilEnabled}
      />
    </div>
  );
}
