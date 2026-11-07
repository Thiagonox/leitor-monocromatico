'use client';

import React, { useEffect, useState, useRef, use, useMemo, useCallback } from 'react';
import Link from 'next/link';
import {
  ArrowLeft,
  Layers,
  List,
  Volume2,
  Pencil,
  Loader2,
} from 'lucide-react';
import { fetchBook, requestContinueStream } from '@/lib/api';
import { BookDoc, Chapter, Section } from '@mono-reader/shared';
import { ThemeToggle } from '@/components/ThemeToggle';
import { TocDrawer } from '@/components/TocDrawer';
import { AudioPlayerModal, AudioPlaybackState, AudioBlockItem } from '@/components/AudioPlayerModal';
import { ReadingPencilGuide } from '@/components/ReadingPencilGuide';

const LAYERS = [
  { id: 1, title: 'Resumo Rápido', subtitle: 'Essência direta para absorção imediata' },
  { id: 2, title: 'Conceito → Aplicação', subtitle: 'Desdobramento estruturado em passos' },
  { id: 3, title: 'Imersão Completa', subtitle: 'Fluxo contínuo integral aprofundado' },
];

interface LayeredStreamBlock {
  blockIndex: number;
  id: string;
  chapterIndex: number;
  type: 'title' | 'heading' | 'paragraph' | 'callout' | 'step';
  stepNumber?: number;
  title?: string;
  content: string;
  epigraphText?: string;
  epigraphAuthor?: string;
  spokenText: string;
  label: string;
}

export default function LayeredReaderPage({ params }: { params: Promise<{ id: string }> }) {
  const resolvedParams = use(params);

  const [book, setBook] = useState<BookDoc | null>(null);
  const [extraSections, setExtraSections] = useState<Section[]>([]);
  const [continuationStep, setContinuationStep] = useState(1);
  const [isGeneratingMore, setIsGeneratingMore] = useState(false);

  const [currentChapterIndex, setCurrentChapterIndex] = useState(0);
  const [visibleBlockIndex, setVisibleBlockIndex] = useState(0);
  const [activeAudioBlockIndex, setActiveAudioBlockIndex] = useState(0);

  const [activeLayer, setActiveLayer] = useState<number>(3);
  const [loading, setLoading] = useState(true);
  const [tocOpen, setTocOpen] = useState(false);
  const [audioOpen, setAudioOpen] = useState(false);
  const [pencilEnabled, setPencilEnabled] = useState(true);
  const [audioPlayback, setAudioPlayback] = useState<AudioPlaybackState>({
    isPlaying: false,
    currentTime: 0,
    duration: 0,
    isLoading: false,
    activeBlockIndex: 0,
    totalBlocks: 0,
  });

  const contentRef = useRef<HTMLElement | null>(null);
  const blockRefs = useRef<(HTMLElement | null)[]>([]);
  const activeBlockContainerRef = useRef<HTMLElement | null>(null);
  const sentinelRef = useRef<HTMLDivElement | null>(null);
  const loadingMoreRef = useRef(false);

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

  // Constrói os blocos contínuos da camada ativa (sem paginação)
  const streamBlocks: LayeredStreamBlock[] = useMemo(() => {
    if (!book) return [];
    const list: LayeredStreamBlock[] = [];
    let idx = 0;

    book.chapters.forEach((ch: Chapter, cIdx: number) => {
      const epText = ch.epigraph?.text ? ` "${ch.epigraph.text}"` : '';
      list.push({
        blockIndex: idx,
        id: `${book.meta.id}-L${activeLayer}-b-${idx}`,
        chapterIndex: cIdx,
        type: 'title',
        content: ch.title,
        epigraphText: ch.epigraph?.text,
        epigraphAuthor: ch.epigraph?.author,
        spokenText: `${ch.title}.${epText}`,
        label: ch.title,
      });
      idx++;

      const paragraphs = (ch.sections || []).filter((s) => s.type === 'paragraph');
      const callouts = (ch.sections || []).filter((s) => s.type === 'callout');

      if (activeLayer === 1) {
        paragraphs.slice(0, 2).forEach((p) => {
          const pText = (p.content || '').trim();
          if (!pText) return;
          list.push({
            blockIndex: idx,
            id: `${book.meta.id}-L1-b-${idx}`,
            chapterIndex: cIdx,
            type: 'paragraph',
            content: pText,
            spokenText: pText,
            label: pText.slice(0, 50),
          });
          idx++;
        });
        if (callouts[0]) {
          const cText = (callouts[0].content || '').trim();
          if (cText) {
            list.push({
              blockIndex: idx,
              id: `${book.meta.id}-L1-b-${idx}`,
              chapterIndex: cIdx,
              type: 'callout',
              title: callouts[0].title || 'Ponto Central',
              content: cText,
              spokenText: `${callouts[0].title || 'Ponto Central'}. ${cText}`,
              label: callouts[0].title || 'Ponto Central',
            });
            idx++;
          }
        }
      } else if (activeLayer === 2) {
        const steps = [
          { num: 1, title: 'O Conceito Fundamental', text: paragraphs[0]?.content || '' },
          { num: 2, title: 'O Exemplo em Ação', text: paragraphs[1]?.content || '' },
          { num: 3, title: 'Como Aplicar na Prática', text: paragraphs[2]?.content || '' },
        ];
        steps.forEach((st) => {
          if (!st.text) return;
          list.push({
            blockIndex: idx,
            id: `${book.meta.id}-L2-b-${idx}`,
            chapterIndex: cIdx,
            type: 'step',
            stepNumber: st.num,
            title: st.title,
            content: st.text,
            spokenText: `${st.title}. ${st.text}`,
            label: st.title,
          });
          idx++;
        });
      } else {
        (ch.sections || []).forEach((sec: Section) => {
          const text = (sec.content || '').trim();
          if (!text) return;
          list.push({
            blockIndex: idx,
            id: `${book.meta.id}-L3-b-${idx}`,
            chapterIndex: cIdx,
            type: sec.type === 'heading' ? 'heading' : sec.type === 'callout' ? 'callout' : 'paragraph',
            title: sec.title,
            content: text,
            spokenText: sec.title ? `${sec.title}. ${text}` : text,
            label: sec.title || text.slice(0, 50),
          });
          idx++;
        });
      }
    });

    extraSections.forEach((sec: Section) => {
      const text = (sec.content || '').trim();
      if (!text) return;
      list.push({
        blockIndex: idx,
        id: `${book.meta.id}-L${activeLayer}-b-${idx}`,
        chapterIndex: book.chapters.length - 1,
        type: sec.type === 'heading' ? 'heading' : sec.type === 'callout' ? 'callout' : 'paragraph',
        title: sec.title,
        content: text,
        spokenText: sec.title ? `${sec.title}. ${text}` : text,
        label: sec.title || text.slice(0, 50),
      });
      idx++;
    });

    return list;
  }, [book, activeLayer, extraSections]);

  const audioBlocks: AudioBlockItem[] = useMemo(() => {
    return streamBlocks.map((b) => ({
      index: b.blockIndex,
      id: b.id,
      text: b.spokenText,
      label: b.label,
    }));
  }, [streamBlocks]);

  useEffect(() => {
    const targetIdx = audioOpen ? activeAudioBlockIndex : visibleBlockIndex;
    activeBlockContainerRef.current = blockRefs.current[targetIdx] || contentRef.current;
  }, [audioOpen, activeAudioBlockIndex, visibleBlockIndex, streamBlocks.length]);

  useEffect(() => {
    if (!audioPlayback.isPlaying) return;
    const el = blockRefs.current[activeAudioBlockIndex];
    if (el) {
      const rect = el.getBoundingClientRect();
      const viewH = window.innerHeight;
      if (rect.top < 110 || rect.bottom > viewH - 180) {
        const y = rect.top + window.pageYOffset - viewH * 0.34;
        window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
      }
    }
  }, [activeAudioBlockIndex, audioPlayback.isPlaying]);

  const loadMoreInfiniteBlocks = useCallback(async () => {
    if (!book || loadingMoreRef.current) return;
    loadingMoreRef.current = true;
    setIsGeneratingMore(true);

    try {
      const tailBlocks = streamBlocks.slice(-3).map((b) => b.spokenText).join('\n\n');
      const res = await requestContinueStream({
        bookTitle: book.meta.title,
        bookSubtitle: book.meta.subtitle,
        previousContext: tailBlocks,
        continuationStep,
      });

      if (res.sections && res.sections.length > 0) {
        setExtraSections((prev) => [...prev, ...res.sections]);
        setContinuationStep((prev) => prev + 1);
      }
    } catch (err) {
      console.warn('Aviso ao expandir fluxo infinito em camadas:', err);
    } finally {
      setIsGeneratingMore(false);
      loadingMoreRef.current = false;
    }
  }, [book, continuationStep, streamBlocks]);

  useEffect(() => {
    if (!book || loading || !sentinelRef.current) return;

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting && !loadingMoreRef.current) {
            loadMoreInfiniteBlocks();
          }
        }
      },
      {
        rootMargin: '0px 0px 900px 0px',
        threshold: 0,
      }
    );

    observer.observe(sentinelRef.current);
    return () => observer.disconnect();
  }, [book, loading, loadMoreInfiniteBlocks]);

  useEffect(() => {
    if (!book || loading || streamBlocks.length === 0) return;

    const elements = document.querySelectorAll<HTMLElement>('[data-block-index]');
    if (!elements.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            const bIdxStr = entry.target.getAttribute('data-block-index');
            const cIdxStr = entry.target.getAttribute('data-chapter-index');
            if (bIdxStr !== null) {
              setVisibleBlockIndex(parseInt(bIdxStr, 10));
            }
            if (cIdxStr !== null) {
              setCurrentChapterIndex(parseInt(cIdxStr, 10));
            }
          }
        }
      },
      {
        rootMargin: '-15% 0px -70% 0px',
        threshold: 0,
      }
    );

    elements.forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, [book, loading, streamBlocks.length]);

  const handleSelectChapter = (index: number) => {
    setCurrentChapterIndex(index);
    setTocOpen(false);
    const targetBlock = streamBlocks.find((b) => b.chapterIndex === index && b.type === 'title');
    if (targetBlock) {
      const el = blockRefs.current[targetBlock.blockIndex];
      if (el) {
        const y = el.getBoundingClientRect().top + window.pageYOffset - 115;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
      setActiveAudioBlockIndex(targetBlock.blockIndex);
    }
  };

  const handleOpenAudio = () => {
    if (!audioOpen && !audioPlayback.isPlaying) {
      setActiveAudioBlockIndex(visibleBlockIndex);
    }
    setAudioOpen(true);
  };

  const currentChapter: Chapter | undefined = book?.chapters[currentChapterIndex];

  if (loading) {
    return (
      <div className="min-h-screen bg-[var(--bg-primary)] flex items-center justify-center font-mono text-xs text-[var(--text-muted)]">
        Carregando leitor contínuo infinito em camadas...
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
    <div className="min-h-screen bg-[var(--bg-primary)] text-[var(--text-primary)] w-full max-w-full overflow-x-hidden">
      {/* Top Header */}
      <header className="sticky top-0 z-40 bg-[var(--bg-primary)]/95 backdrop-blur-sm border-b border-[var(--border-color)]">
        <div className="max-w-4xl mx-auto px-4 h-14 flex items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <Link
              href={`/reader/${book.meta.id}`}
              className="p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono"
              title="Voltar ao Leitor Contínuo Padrão"
            >
              <ArrowLeft className="w-4 h-4" />
              <span className="hidden sm:inline">Leitor Padrão</span>
            </Link>

            <button
              onClick={() => setTocOpen(true)}
              className="p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono"
              title="Índice de Tópicos"
            >
              <List className="w-4 h-4" />
              <span className="hidden sm:inline">Tópicos</span>
            </button>
          </div>

          <div className="hidden md:block text-center font-mono text-xs text-[var(--text-secondary)] line-clamp-1 max-w-sm">
            {book.meta.title} · {currentChapter?.title}
          </div>

          <div className="flex items-center gap-2">
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
              onClick={handleOpenAudio}
              className={`p-1.5 sm:px-2 sm:py-1.5 rounded transition-colors flex items-center gap-1 text-xs font-mono border ${
                audioPlayback.isPlaying
                  ? 'border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
                  : 'border-[var(--border-color)] hover:bg-[var(--bg-secondary)] text-[var(--text-primary)]'
              }`}
              title="Ouvir Bloco por Bloco em Sequência Gapless"
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
                onClick={() => {
                  setActiveLayer(layer.id);
                  setActiveAudioBlockIndex(0);
                }}
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

      {/* Drawer de Tópicos */}
      <TocDrawer
        isOpen={tocOpen}
        onClose={() => setTocOpen(false)}
        chapters={book.chapters}
        currentChapterIndex={currentChapterIndex}
        onSelectChapter={handleSelectChapter}
        bookTitle={book.meta.title}
      />

      {/* Conteúdo Principal em Scroll Infinito Contínuo (Zero Paginação) */}
      <main ref={contentRef} className="max-w-2xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
        <div className="space-y-6">
          {streamBlocks.map((block) => {
            const isSpeakingThisBlock =
              audioOpen && audioPlayback.isPlaying && activeAudioBlockIndex === block.blockIndex;
            const highlightClass = isSpeakingThisBlock
              ? 'ring-1 ring-[var(--border-strong)] bg-[var(--bg-secondary)]/45 rounded-md px-3 -mx-3 py-1.5 transition-all'
              : '';

            if (block.type === 'title') {
              return (
                <div
                  key={block.id}
                  id={`reader-block-${block.blockIndex}`}
                  data-block-index={block.blockIndex}
                  data-chapter-index={block.chapterIndex}
                  ref={(el) => {
                    blockRefs.current[block.blockIndex] = el;
                  }}
                  onClick={() => audioOpen && setActiveAudioBlockIndex(block.blockIndex)}
                  className={`pt-8 pb-3 border-b border-[var(--border-color)] ${highlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
                >
                  <h2 className="font-serif text-2xl sm:text-3xl font-bold tracking-tight text-[var(--text-primary)] mb-2 leading-tight">
                    {block.content}
                  </h2>
                  {block.epigraphText && (
                    <blockquote className="border-l-2 border-[var(--border-strong)] pl-4 my-2 font-serif italic text-xs sm:text-sm text-[var(--text-secondary)]">
                      &ldquo;{block.epigraphText}&rdquo;
                      {block.epigraphAuthor && (
                        <cite className="block text-xs font-mono text-[var(--text-muted)] mt-1 not-italic">
                          — {block.epigraphAuthor}
                        </cite>
                      )}
                    </blockquote>
                  )}
                </div>
              );
            }

            if (block.type === 'step') {
              return (
                <div
                  key={block.id}
                  id={`reader-block-${block.blockIndex}`}
                  data-block-index={block.blockIndex}
                  data-chapter-index={block.chapterIndex}
                  ref={(el) => {
                    blockRefs.current[block.blockIndex] = el;
                  }}
                  onClick={() => audioOpen && setActiveAudioBlockIndex(block.blockIndex)}
                  className={`space-y-2 pb-4 border-b border-[var(--border-color)] ${highlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
                >
                  <div className="flex items-center gap-2 font-mono text-xs font-bold uppercase text-[var(--text-primary)]">
                    <span className="w-5 h-5 rounded-full border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] flex items-center justify-center text-[10px]">
                      {block.stepNumber}
                    </span>
                    <span>{block.title}</span>
                  </div>
                  <p className="font-serif text-base sm:text-lg leading-relaxed text-[var(--text-primary)]">
                    {block.content}
                  </p>
                </div>
              );
            }

            if (block.type === 'heading') {
              return (
                <h3
                  key={block.id}
                  id={`reader-block-${block.blockIndex}`}
                  data-block-index={block.blockIndex}
                  data-chapter-index={block.chapterIndex}
                  ref={(el) => {
                    blockRefs.current[block.blockIndex] = el;
                  }}
                  onClick={() => audioOpen && setActiveAudioBlockIndex(block.blockIndex)}
                  className={`font-serif text-xl sm:text-2xl font-bold mt-6 mb-2 text-[var(--text-primary)] ${highlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
                >
                  {block.content}
                </h3>
              );
            }

            if (block.type === 'callout') {
              return (
                <div
                  key={block.id}
                  id={`reader-block-${block.blockIndex}`}
                  data-block-index={block.blockIndex}
                  data-chapter-index={block.chapterIndex}
                  ref={(el) => {
                    blockRefs.current[block.blockIndex] = el;
                  }}
                  onClick={() => audioOpen && setActiveAudioBlockIndex(block.blockIndex)}
                  className={`p-4 rounded border border-[var(--border-strong)] bg-[var(--bg-card)] my-4 ${highlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
                >
                  {block.title && (
                    <div className="font-mono text-xs uppercase tracking-wider font-bold mb-1 text-[var(--text-primary)]">
                      📌 {block.title}
                    </div>
                  )}
                  <p className="font-serif text-sm sm:text-base leading-relaxed text-[var(--text-secondary)]">
                    {block.content}
                  </p>
                </div>
              );
            }

            return (
              <p
                key={block.id}
                id={`reader-block-${block.blockIndex}`}
                data-block-index={block.blockIndex}
                data-chapter-index={block.chapterIndex}
                ref={(el) => {
                  blockRefs.current[block.blockIndex] = el;
                }}
                onClick={() => audioOpen && setActiveAudioBlockIndex(block.blockIndex)}
                className={`font-serif text-base sm:text-lg leading-relaxed text-[var(--text-primary)] ${highlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
              >
                {block.content}
              </p>
            );
          })}
        </div>

        {/* Sentinela Invisível de Scroll Infinito */}
        <div ref={sentinelRef} className="py-12 flex items-center justify-center">
          {isGeneratingMore && (
            <div className="flex items-center gap-2 text-xs font-mono text-[var(--text-muted)]">
              <Loader2 className="w-3.5 h-3.5 animate-spin" />
              <span>Expandindo fluxo contínuo em camadas...</span>
            </div>
          )}
        </div>
      </main>

      {/* Player de Áudio Gapless Bloco a Bloco */}
      <AudioPlayerModal
        isOpen={audioOpen}
        onClose={() => setAudioOpen(false)}
        blocks={audioBlocks}
        activeBlockIndex={activeAudioBlockIndex}
        onActiveBlockChange={setActiveAudioBlockIndex}
        bookTitle={book.meta.title}
        onPlaybackUpdate={setAudioPlayback}
        onNearEnd={loadMoreInfiniteBlocks}
      />

      {/* Guia Animado do Lápis Editorial */}
      <ReadingPencilGuide
        containerRef={activeBlockContainerRef}
        isPlaying={audioPlayback.isPlaying}
        currentTime={audioPlayback.currentTime}
        duration={audioPlayback.duration}
        isLoading={audioPlayback.isLoading}
        enabled={pencilEnabled}
        activeBlockKey={audioOpen ? activeAudioBlockIndex : visibleBlockIndex}
      />
    </div>
  );
}