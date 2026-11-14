'use client';

import React, { useEffect, useState, useRef, use, useMemo, useCallback } from 'react';
import Link from 'next/link';
import {
  ArrowLeft,
  List,
  Layers,
  Sparkles,
  Volume2,
  Type,
  Pencil,
  Eye,
} from 'lucide-react';
import { fetchBook } from '@/lib/api';
import {
  getBookProgress,
  setBookProgress,
  getStoredFontSize,
  setStoredFontSize,
  getStoredFont,
  setStoredFont,
  FontMode,
} from '@/lib/storage';
import { BookDoc, Chapter, Section } from '@mono-reader/shared';
import { ThemeToggle } from '@/components/ThemeToggle';
import { TocDrawer } from '@/components/TocDrawer';
import { DeepenModal } from '@/components/DeepenModal';
import { AudioPlayerModal, AudioPlaybackState, AudioBlockItem } from '@/components/AudioPlayerModal';
import { ReadingPencilGuide } from '@/components/ReadingPencilGuide';
import { ReadingRuler } from '@/components/ReadingRuler';

function renderFormattedInline(text: string): React.ReactNode {
  if (!text || (!text.includes('*') && !text.includes('`'))) return text;
  const parts = text.split(/(\*\*[^\n*]+?\*\*|\*(?!\s)[^\n*]+?(?<!\s)\*|`[^`\n]+`)/g);
  return parts.map((part, idx) => {
    if (part.startsWith('**') && part.endsWith('**') && part.length > 4) {
      return (
        <strong key={idx} className="font-semibold text-[var(--text-primary)]">
          {part.slice(2, -2)}
        </strong>
      );
    }
    if (part.startsWith('*') && part.endsWith('*') && part.length > 2) {
      return (
        <em key={idx} className="italic">
          {part.slice(1, -1)}
        </em>
      );
    }
    if (part.startsWith('`') && part.endsWith('`') && part.length > 2) {
      return (
        <code
          key={idx}
          className="font-mono text-[0.9em] px-1 py-0.5 rounded bg-[var(--bg-secondary)]"
        >
          {part.slice(1, -1)}
        </code>
      );
    }
    return part;
  });
}

interface StreamBlock {
  blockIndex: number;
  id: string;
  chapterIndex: number;
  type: 'chapter-title' | 'heading' | 'paragraph' | 'callout' | 'quote';
  level?: number;
  title?: string;
  content: string;
  author?: string;
  epigraphText?: string;
  epigraphAuthor?: string;
  spokenText: string;
  label: string;
}

export default function ReaderPage({ params }: { params: Promise<{ id: string }> }) {
  const resolvedParams = use(params);

  const [book, setBook] = useState<BookDoc | null>(null);

  const [currentChapterIndex, setCurrentChapterIndex] = useState(0);
  const [visibleBlockIndex, setVisibleBlockIndex] = useState(0);
  const [activeAudioBlockIndex, setActiveAudioBlockIndex] = useState(0);

  const [loading, setLoading] = useState(true);
  const [tocOpen, setTocOpen] = useState(false);
  const [deepenOpen, setDeepenOpen] = useState(false);
  const [audioOpen, setAudioOpen] = useState(false);
  const [typographyOpen, setTypographyOpen] = useState(false);
  const [fontSize, setFontSizeState] = useState(20);
  const [fontMode, setFontModeState] = useState<FontMode>('serif');
  const [selectedTextForDeepen, setSelectedTextForDeepen] = useState('');

  // Guias de leitura: Lápis Editorial e Régua de Foco Ocular
  const [pencilEnabled, setPencilEnabled] = useState(true);
  const [rulerEnabled, setRulerEnabled] = useState(false);
  const [audioPlayback, setAudioPlayback] = useState<AudioPlaybackState>({
    isPlaying: false,
    currentTime: 0,
    duration: 0,
    isLoading: false,
    activeBlockIndex: 0,
    totalBlocks: 0,
  });

  const contentRef = useRef<HTMLDivElement | null>(null);
  const blockRefs = useRef<(HTMLElement | null)[]>([]);
  const activeBlockContainerRef = useRef<HTMLElement | null>(null);
  const lastUserScrollRef = useRef(0);

  // Remove qualquer Service Worker legado de PWA que possa ter ficado em cache no navegador
  useEffect(() => {
    if (typeof window !== 'undefined' && 'serviceWorker' in navigator) {
      navigator.serviceWorker.getRegistrations().then((regs) => {
        for (const r of regs) {
          r.unregister();
        }
      }).catch(() => {});
    }
  }, []);

  // Constrói o fluxo contínuo unificado de blocos (sem paginação)
  const streamBlocks: StreamBlock[] = useMemo(() => {
    if (!book) return [];
    const list: StreamBlock[] = [];
    let idx = 0;

    book.chapters.forEach((ch: Chapter, cIdx: number) => {
      const epText = ch.epigraph?.text ? ` "${ch.epigraph.text}"` : '';
      list.push({
        blockIndex: idx,
        id: `${book.meta.id}-b-${idx}`,
        chapterIndex: cIdx,
        type: 'chapter-title',
        content: ch.title,
        epigraphText: ch.epigraph?.text,
        epigraphAuthor: ch.epigraph?.author,
        spokenText: `${ch.title}.${epText}`,
        label: ch.title,
      });
      idx++;

      (ch.sections || []).forEach((sec: Section) => {
        const text = (sec.content || '').trim();
        if (!text) return;
        const prefix = sec.title ? `${sec.title}. ` : '';
        list.push({
          blockIndex: idx,
          id: `${book.meta.id}-b-${idx}`,
          chapterIndex: cIdx,
          type: sec.type as any,
          level: sec.level,
          title: sec.title,
          content: text,
          author: sec.author,
          spokenText: `${prefix}${text}`,
          label: sec.title || text.slice(0, 52),
        });
        idx++;
      });
    });

    return list;
  }, [book]);

  const audioBlocks: AudioBlockItem[] = useMemo(() => {
    return streamBlocks.map((b) => ({
      index: b.blockIndex,
      id: b.id,
      text: b.spokenText,
      label: b.label,
    }));
  }, [streamBlocks]);

  // Controle de acompanhamento automático do áudio (sem flick ou interrupção de scroll do usuário)
  const [autoFollowAudio, setAutoFollowAudio] = useState<boolean>(true);
  const [isAudioOffscreen, setIsAudioOffscreen] = useState<boolean>(false);
  const isProgrammaticScrollRef = useRef<boolean>(false);

  // Aponta o Lápis de Leitura diretamente para o bloco ativo
  useEffect(() => {
    const targetIdx = audioOpen ? activeAudioBlockIndex : visibleBlockIndex;
    activeBlockContainerRef.current =
      document.getElementById(`reader-block-${targetIdx}`) ||
      blockRefs.current[targetIdx] ||
      contentRef.current;
  }, [audioOpen, activeAudioBlockIndex, visibleBlockIndex, streamBlocks.length]);

  // Detecta qualquer rolagem manual do usuário (wheel, touch, scrollbar drag) para pausar o auto-scroll
  useEffect(() => {
    const handleUserScrollAction = () => {
      lastUserScrollRef.current = Date.now();
      if (!isProgrammaticScrollRef.current) {
        setAutoFollowAudio(false);
      }
    };

    window.addEventListener('wheel', handleUserScrollAction, { passive: true });
    window.addEventListener('touchmove', handleUserScrollAction, { passive: true });
    window.addEventListener('scroll', handleUserScrollAction, { passive: true });
    window.addEventListener(
      'keydown',
      (e) => {
        if (['ArrowUp', 'ArrowDown', 'PageUp', 'PageDown', 'Space', 'Home', 'End'].includes(e.code)) {
          handleUserScrollAction();
        }
      },
      { passive: true }
    );

    return () => {
      window.removeEventListener('wheel', handleUserScrollAction);
      window.removeEventListener('touchmove', handleUserScrollAction);
      window.removeEventListener('scroll', handleUserScrollAction);
    };
  }, []);

  // Monitora se o bloco de áudio ativo está fora do campo de visão visível
  useEffect(() => {
    if (!audioOpen || !audioPlayback.isPlaying) {
      setIsAudioOffscreen(false);
      return;
    }

    const checkVisibility = () => {
      const el =
        document.getElementById(`reader-block-${activeAudioBlockIndex}`) ||
        blockRefs.current[activeAudioBlockIndex];
      if (!el) return;
      const rect = el.getBoundingClientRect();
      const viewH = window.innerHeight;
      const isOff = rect.bottom < 40 || rect.top > viewH - 40;
      setIsAudioOffscreen(isOff);
    };

    checkVisibility();
    window.addEventListener('scroll', checkVisibility, { passive: true });
    return () => window.removeEventListener('scroll', checkVisibility);
  }, [audioOpen, audioPlayback.isPlaying, activeAudioBlockIndex]);

  // Rola suavemente para o bloco de áudio ativo
  const scrollToActiveAudioBlock = useCallback(() => {
    const el =
      document.getElementById(`reader-block-${activeAudioBlockIndex}`) ||
      blockRefs.current[activeAudioBlockIndex];
    if (el) {
      isProgrammaticScrollRef.current = true;
      const rect = el.getBoundingClientRect();
      const viewH = window.innerHeight;
      const y = rect.top + window.pageYOffset - viewH * 0.32;
      window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
      setTimeout(() => {
        isProgrammaticScrollRef.current = false;
      }, 700);
      setAutoFollowAudio(true);
    }
  }, [activeAudioBlockIndex]);

  // Acompanha a transição de bloco suavemente SOMENTE quando autoFollowAudio for explicitamente true
  useEffect(() => {
    if (!audioPlayback.isPlaying || !autoFollowAudio) return;

    const el =
      document.getElementById(`reader-block-${activeAudioBlockIndex}`) ||
      blockRefs.current[activeAudioBlockIndex];
    if (el) {
      const rect = el.getBoundingClientRect();
      const viewH = window.innerHeight;
      if (rect.top < 60 || rect.bottom > viewH - 120) {
        isProgrammaticScrollRef.current = true;
        const y = rect.top + window.pageYOffset - viewH * 0.32;
        window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
        setTimeout(() => {
          isProgrammaticScrollRef.current = false;
        }, 700);
      }
    }
  }, [activeAudioBlockIndex, audioPlayback.isPlaying, autoFollowAudio]);

  // Carrega Obra Inicial
  useEffect(() => {
    let active = true;
    async function load() {
      setLoading(true);
      const doc = await fetchBook(resolvedParams.id);
      if (active) {
        if (doc) {
          setBook(doc);
          const progress = getBookProgress(doc.meta.id);
          if (progress && progress.chapterIndex < doc.chapters.length) {
            setCurrentChapterIndex(progress.chapterIndex);
          }
        }
        setLoading(false);
      }
    }
    load();
    return () => {
      active = false;
    };
  }, [resolvedParams.id]);

  // Carrega Preferências de Fonte
  useEffect(() => {
    const sSize = getStoredFontSize();
    setFontSizeState(sSize);
    const sFont = getStoredFont();
    setFontModeState(sFont);
  }, []);

  // Observa qual bloco está visível na tela durante a leitura
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
              const bIdx = parseInt(bIdxStr, 10);
              setVisibleBlockIndex(bIdx);
            }
            if (cIdxStr !== null) {
              const cIdx = parseInt(cIdxStr, 10);
              setCurrentChapterIndex(cIdx);
              setBookProgress(book.meta.id, cIdx, 0);
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

  // Navega suavemente até o ponto desejado no fluxo contínuo
  const handleSelectChapter = (index: number) => {
    setCurrentChapterIndex(index);
    setTocOpen(false);
    const targetBlock = streamBlocks.find((b) => b.chapterIndex === index && b.type === 'chapter-title');
    if (targetBlock) {
      const el = blockRefs.current[targetBlock.blockIndex];
      if (el) {
        const y = el.getBoundingClientRect().top + window.pageYOffset - 76;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
      setActiveAudioBlockIndex(targetBlock.blockIndex);
    }
  };

  const handleOpenAudio = () => {
    if (!audioOpen && !audioPlayback.isPlaying) {
      setActiveAudioBlockIndex(visibleBlockIndex);
    }
    setAutoFollowAudio(true);
    setAudioOpen(true);
  };

  const handleStartAudioFromBlock = (blockIndex: number) => {
    setActiveAudioBlockIndex(blockIndex);
    setAutoFollowAudio(true);
    setAudioOpen(true);
  };

  const currentChapter: Chapter | undefined = book?.chapters[currentChapterIndex];
  const activeContextText = useMemo(() => {
    return streamBlocks
      .slice(Math.max(0, visibleBlockIndex - 1), visibleBlockIndex + 3)
      .map((b) => b.spokenText)
      .join('\n\n');
  }, [streamBlocks, visibleBlockIndex]);

  const handleOpenDeepen = () => {
    const sel = window.getSelection()?.toString().trim();
    if (sel && sel.length > 2) {
      setSelectedTextForDeepen(sel);
    } else {
      setSelectedTextForDeepen(streamBlocks[visibleBlockIndex]?.label || book?.meta.title || '');
    }
    setDeepenOpen(true);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-[var(--bg-primary)] flex items-center justify-center font-mono text-xs text-[var(--text-muted)]">
        Iniciando fluxo de leitura infinito...
      </div>
    );
  }

  if (!book || !book.chapters || book.chapters.length === 0) {
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

  return (
    <div className="min-h-screen bg-[var(--bg-primary)] text-[var(--text-primary)] w-full max-w-full overflow-x-hidden">
      {/* Barra de Ferramentas Superior Fixa */}
      <header className="sticky top-0 z-40 bg-[var(--bg-primary)]/95 backdrop-blur-sm border-b border-[var(--border-color)]">
        <div className="max-w-4xl mx-auto px-3 sm:px-4 h-14 flex items-center justify-between gap-1.5 sm:gap-2">
          {/* Voltar & Índice de Tópicos */}
          <div className="flex items-center gap-1.5 sm:gap-2 shrink-0">
            <Link
              href="/"
              className="p-1.5 sm:p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono"
              title="Voltar à Biblioteca"
            >
              <ArrowLeft className="w-4 h-4" />
              <span className="hidden sm:inline">Biblioteca</span>
            </Link>

            <button
              onClick={() => setTocOpen(true)}
              className="p-1.5 sm:p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono"
              title="Índice de Tópicos do Fluxo"
            >
              <List className="w-4 h-4" />
              <span className="hidden md:inline">Tópicos</span>
            </button>
          </div>

          {/* Título Central Dinâmico Truncado (Acompanha o Fluxo Infinito) */}
          <div className="hidden lg:block text-center flex-1 mx-4 min-w-0">
            <span className="font-serif text-xs italic text-[var(--text-secondary)] truncate block">
              {book.meta.title} — {currentChapter?.title}
            </span>
          </div>

          {/* Controles de Leitura Responsivos */}
          <div className="flex items-center gap-1 sm:gap-1.5 shrink-0">
            {/* Modo Camadas */}
            <Link
              href={`/reader/${book.meta.id}/camadas`}
              className="p-1.5 sm:px-2.5 sm:py-1.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] text-xs font-mono flex items-center gap-1 shrink-0"
              title="Alternar para Modo de Leitura em Camadas"
            >
              <Layers className="w-4 h-4" />
              <span className="hidden sm:inline">Camadas</span>
            </Link>

            {/* Aprofundar com Agentes IA */}
            <button
              onClick={handleOpenDeepen}
              className="p-1.5 sm:px-2 sm:py-1.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] text-xs font-mono flex items-center gap-1 shrink-0"
              title="Conversar com Agentes Especializados (Prof. Elias, Lucas Hack, Lia, Dr. Viktor)"
            >
              <Sparkles className="w-4 h-4" />
              <span className="hidden md:inline">Agentes IA</span>
            </button>

            {/* Ouvir Bloco por Bloco (HeyGen Gapless Stream) */}
            <button
              onClick={handleOpenAudio}
              className={`p-1.5 sm:px-2 sm:py-1.5 rounded border transition-colors flex items-center gap-1 text-xs font-mono shrink-0 ${
                audioPlayback.isPlaying
                  ? 'border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
                  : 'border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] text-[var(--text-primary)]'
              }`}
              title="Ouvir Bloco por Bloco em Sequência Gapless"
            >
              <Volume2 className="w-4 h-4" />
              <span className="hidden md:inline">Ouvir</span>
            </button>

            {/* Lápis Guia de Leitura */}
            <button
              onClick={() => setPencilEnabled(!pencilEnabled)}
              className={`p-1.5 rounded transition-colors text-xs font-mono flex items-center gap-1 shrink-0 ${
                pencilEnabled
                  ? 'bg-[var(--border-strong)] text-[var(--bg-primary)]'
                  : 'hover:bg-[var(--bg-secondary)] text-[var(--text-muted)]'
              }`}
              title={pencilEnabled ? 'Desativar Lápis de Leitura' : 'Ativar Lápis de Leitura'}
            >
              <Pencil className="w-3.5 h-3.5" />
              <span className="hidden lg:inline">Lápis</span>
            </button>

            {/* Régua de Foco Ocular (Desktop) */}
            <button
              onClick={() => setRulerEnabled(!rulerEnabled)}
              className={`hidden sm:flex p-1.5 rounded transition-colors text-xs font-mono items-center gap-1 shrink-0 ${
                rulerEnabled
                  ? 'bg-[var(--border-strong)] text-[var(--bg-primary)]'
                  : 'hover:bg-[var(--bg-secondary)] text-[var(--text-muted)]'
              }`}
              title={rulerEnabled ? 'Desativar Régua de Foco' : 'Ativar Régua de Foco Ocular'}
            >
              <Eye className="w-3.5 h-3.5" />
              <span className="hidden lg:inline">Régua</span>
            </button>

            {/* Alternar Fonte (Desktop) */}
            <button
              onClick={toggleFont}
              className="hidden sm:block p-1.5 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-xs shrink-0"
              title={`Alternar Fonte (Atual: ${fontMode})`}
            >
              <Type className="w-4 h-4" />
            </button>

            {/* Tamanho de Fonte (Desktop) */}
            <div className="hidden md:flex items-center border border-[var(--border-color)] rounded bg-[var(--bg-surface)] text-xs font-mono shrink-0">
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

            {/* Menu Compacto de Tipografia (Mobile) */}
            <div className="sm:hidden relative shrink-0">
              <button
                onClick={() => setTypographyOpen(!typographyOpen)}
                className="p-1.5 border border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] rounded transition-colors text-[var(--text-primary)] flex items-center text-xs font-mono font-bold"
                title="Ajustes de Tipografia e Fonte"
              >
                Aa
              </button>
              {typographyOpen && (
                <div className="absolute right-0 top-full mt-2 w-48 p-2.5 bg-[var(--bg-surface)] border border-[var(--border-strong)] rounded-lg shadow-xl z-50 font-mono text-xs space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="text-[11px] text-[var(--text-muted)]">Tipo:</span>
                    <button
                      onClick={toggleFont}
                      className="px-2 py-0.5 border border-[var(--border-color)] rounded text-xs capitalize hover:bg-[var(--bg-secondary)]"
                    >
                      {fontMode}
                    </button>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-[11px] text-[var(--text-muted)]">Tamanho:</span>
                    <div className="flex items-center border border-[var(--border-color)] rounded">
                      <button
                        onClick={() => changeFontSize(-2)}
                        className="px-2 py-0.5 hover:bg-[var(--bg-secondary)] font-bold"
                      >
                        -
                      </button>
                      <span className="px-1.5 text-[10px]">{fontSize}px</span>
                      <button
                        onClick={() => changeFontSize(2)}
                        className="px-2 py-0.5 hover:bg-[var(--bg-secondary)] font-bold"
                      >
                        +
                      </button>
                    </div>
                  </div>
                </div>
              )}
            </div>

            {/* Alternar Tema */}
            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Índice de Tópicos Drawer */}
      <TocDrawer
        isOpen={tocOpen}
        onClose={() => setTocOpen(false)}
        chapters={book.chapters}
        currentChapterIndex={currentChapterIndex}
        onSelectChapter={handleSelectChapter}
        bookTitle={book.meta.title}
      />

      {/* Fluxo Contínuo de Leitura Infinita (Zero Paginação, Sem Cortes) */}
      <main
        ref={contentRef}
        className="reader-container py-8 sm:py-12 md:py-16"
        style={{ fontSize: `${fontSize}px` }}
        data-font={fontMode}
      >
        {/* Cabeçalho Editorial da Obra */}
        <div className="mb-10 pb-8 border-b border-[var(--border-color)]">
          <div className="font-mono text-xs uppercase tracking-widest text-[var(--text-muted)] mb-2">
            {book.meta.author || 'Leitor Infinito Contínuo'}
          </div>
          <h1 className="font-serif text-3xl sm:text-5xl font-bold tracking-tight leading-tight mb-3">
            {book.meta.title}
          </h1>
          {book.meta.subtitle && (
            <p className="font-serif text-base sm:text-lg italic text-[var(--text-secondary)]">
              {book.meta.subtitle}
            </p>
          )}
        </div>

        {/* Sequência Contínua de Blocos */}
        <article className="space-y-6">
          {streamBlocks.map((block) => {
            const isSpeakingThisBlock =
              audioOpen && audioPlayback.isPlaying && activeAudioBlockIndex === block.blockIndex;

            const blockHighlightClass = isSpeakingThisBlock
              ? 'ring-1 ring-[var(--border-strong)] bg-[var(--bg-secondary)]/45 rounded-md px-3 -mx-3 py-1.5 transition-all duration-200'
              : 'group relative transition-colors';

            if (block.type === 'chapter-title') {
              return (
                <div
                  key={block.id}
                  id={`reader-block-${block.blockIndex}`}
                  data-block-index={block.blockIndex}
                  data-chapter-index={block.chapterIndex}
                  ref={(el) => {
                    blockRefs.current[block.blockIndex] = el;
                  }}
                  onClick={() => audioOpen && handleStartAudioFromBlock(block.blockIndex)}
                  className={`pt-10 pb-4 ${blockHighlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
                >
                  <h2 className="reader-heading-1 font-serif text-2xl sm:text-3xl leading-tight mb-3">
                    {block.content}
                  </h2>
                  {block.epigraphText && (
                    <div className="reader-epigraph font-serif text-sm">
                      <p className="italic">&ldquo;{block.epigraphText}&rdquo;</p>
                      {block.epigraphAuthor && (
                        <span className="reader-epigraph-author">
                          — {block.epigraphAuthor}
                        </span>
                      )}
                    </div>
                  )}
                </div>
              );
            }

            if (block.type === 'heading') {
              if (block.level === 2) {
                return (
                  <h2
                    key={block.id}
                    id={`reader-block-${block.blockIndex}`}
                    data-block-index={block.blockIndex}
                    data-chapter-index={block.chapterIndex}
                    ref={(el) => {
                      blockRefs.current[block.blockIndex] = el;
                    }}
                    onClick={() => audioOpen && handleStartAudioFromBlock(block.blockIndex)}
                    className={`reader-heading-2 pt-4 ${blockHighlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
                  >
                    {renderFormattedInline(block.content)}
                  </h2>
                );
              }
              return (
                <h3
                  key={block.id}
                  id={`reader-block-${block.blockIndex}`}
                  data-block-index={block.blockIndex}
                  data-chapter-index={block.chapterIndex}
                  ref={(el) => {
                    blockRefs.current[block.blockIndex] = el;
                  }}
                  onClick={() => audioOpen && handleStartAudioFromBlock(block.blockIndex)}
                  className={`reader-heading-3 pt-2 ${blockHighlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
                >
                  {renderFormattedInline(block.content)}
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
                  onClick={() => audioOpen && handleStartAudioFromBlock(block.blockIndex)}
                  className={`reader-callout font-sans text-sm ${blockHighlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
                >
                  {block.title && (
                    <div className="font-mono text-xs uppercase tracking-wider font-bold mb-2 text-[var(--text-primary)]">
                      {renderFormattedInline(block.title)}
                    </div>
                  )}
                  <p className="whitespace-pre-line leading-relaxed text-[var(--text-secondary)]">
                    {renderFormattedInline(block.content)}
                  </p>
                </div>
              );
            }

            if (block.type === 'quote') {
              return (
                <blockquote
                  key={block.id}
                  id={`reader-block-${block.blockIndex}`}
                  data-block-index={block.blockIndex}
                  data-chapter-index={block.chapterIndex}
                  ref={(el) => {
                    blockRefs.current[block.blockIndex] = el;
                  }}
                  onClick={() => audioOpen && handleStartAudioFromBlock(block.blockIndex)}
                  className={`reader-blockquote font-serif text-base ${blockHighlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
                >
                  <p className="italic">&ldquo;{renderFormattedInline(block.content)}&rdquo;</p>
                  {block.author && (
                    <cite className="block text-xs font-mono not-italic mt-2 text-[var(--text-muted)]">
                      — {block.author}
                    </cite>
                  )}
                </blockquote>
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
                onClick={() => audioOpen && handleStartAudioFromBlock(block.blockIndex)}
                className={`reader-paragraph ${blockHighlightClass} ${audioOpen ? 'cursor-pointer' : ''}`}
              >
                {renderFormattedInline(block.content)}
              </p>
            );
          })}
        </article>

        {/* Conclusão Elegante e Definitiva da Obra (Final é Final) */}
        <div className="py-20 text-center border-t border-[var(--border-color)] mt-16 space-y-3">
          <div className="text-2xl text-[var(--text-muted)] font-serif select-none">❦</div>
          <p className="font-serif text-base italic text-[var(--text-secondary)]">
            Fim do Livro • {book.meta.title}
          </p>
          <div className="text-xs font-mono text-[var(--text-muted)]">
            {streamBlocks.length} blocos completados
          </div>
        </div>
      </main>

      {/* Modais de Agentes IA e Áudio Gapless por Bloco */}
      <DeepenModal
        isOpen={deepenOpen}
        onClose={() => setDeepenOpen(false)}
        initialTopic={selectedTextForDeepen}
        contextText={activeContextText.slice(0, 600)}
      />

      <AudioPlayerModal
        isOpen={audioOpen}
        onClose={() => setAudioOpen(false)}
        blocks={audioBlocks}
        activeBlockIndex={activeAudioBlockIndex}
        onActiveBlockChange={setActiveAudioBlockIndex}
        bookTitle={book.meta.title}
        onPlaybackUpdate={setAudioPlayback}
      />

      {/* Guia Animado do Lápis Editorial (Sincronizado Bloco a Bloco a 60fps) */}
      <ReadingPencilGuide
        activeBlockId={`reader-block-${audioOpen ? activeAudioBlockIndex : visibleBlockIndex}`}
        activeBlockKey={audioOpen ? activeAudioBlockIndex : visibleBlockIndex}
        containerRef={activeBlockContainerRef}
        isPlaying={audioPlayback.isPlaying}
        currentTime={audioPlayback.currentTime}
        duration={audioPlayback.duration}
        isLoading={audioPlayback.isLoading}
        playbackRate={audioPlayback.playbackRate || 1}
        enabled={pencilEnabled}
      />

      {/* Botão flutuante para voltar ao ponto do áudio quando o usuário scrollar livremente */}
      {audioOpen && audioPlayback.isPlaying && isAudioOffscreen && !autoFollowAudio && (
        <button
          onClick={scrollToActiveAudioBlock}
          className="fixed bottom-24 right-6 z-40 px-3.5 py-2 bg-[var(--text-primary)] text-[var(--bg-primary)] rounded-full shadow-xl font-mono text-xs flex items-center gap-2 hover:opacity-90 active:scale-95 transition-all border border-[var(--border-strong)]"
        >
          <span>📍</span>
          <span>Voltar ao Áudio (Bloco {activeAudioBlockIndex + 1})</span>
        </button>
      )}

      {/* Régua de Foco Ocular */}
      <ReadingRuler isActive={rulerEnabled} />
    </div>
  );
}