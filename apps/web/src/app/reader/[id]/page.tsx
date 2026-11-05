'use client';

import React, { useEffect, useState, useRef, use } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import {
  ArrowLeft,
  List,
  Layers,
  Volume2,
  Sparkles,
  Type,
  Pencil,
  Eye,
} from 'lucide-react';
import { fetchBook } from '@/lib/api';
import { BookDoc, Chapter, Section } from '@mono-reader/shared';
import {
  getStoredFont,
  setStoredFont,
  getStoredFontSize,
  setStoredFontSize,
  getBookProgress,
  setBookProgress,
  FontMode,
} from '@/lib/storage';
import { ThemeToggle } from '@/components/ThemeToggle';
import { TocDrawer } from '@/components/TocDrawer';
import { QuizBlock } from '@/components/QuizBlock';
import { DeepenModal } from '@/components/DeepenModal';
import { AudioPlayerModal, AudioPlaybackState } from '@/components/AudioPlayerModal';
import { ReadingPencilGuide } from '@/components/ReadingPencilGuide';
import { ReadingRuler } from '@/components/ReadingRuler';

export default function ReaderPage({ params }: { params: Promise<{ id: string }> }) {
  const resolvedParams = use(params);
  const router = useRouter();

  const [book, setBook] = useState<BookDoc | null>(null);
  const [currentChapterIndex, setCurrentChapterIndex] = useState(0);
  const [audioChapterIndex, setAudioChapterIndex] = useState(0);
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
  });

  const contentRef = useRef<HTMLDivElement | null>(null);
  const chapterRefs = useRef<(HTMLElement | null)[]>([]);
  const activeChapterContainerRef = useRef<HTMLElement | null>(null);

  // Mantém a referência do container do capítulo ativo para o lápis de leitura
  // Se o áudio estiver reproduzindo, o lápis acompanha o capítulo de áudio; senão, o visual
  useEffect(() => {
    const activeIdx = audioPlayback.isPlaying ? audioChapterIndex : currentChapterIndex;
    activeChapterContainerRef.current = chapterRefs.current[activeIdx] || contentRef.current;
  }, [audioPlayback.isPlaying, audioChapterIndex, currentChapterIndex]);

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
            // Se havia progresso salvo anterior a 0, rola suavemente após renderizar
            if (progress.chapterIndex > 0) {
              setTimeout(() => {
                const targetChapter = doc.chapters[progress.chapterIndex];
                const el = document.getElementById(`chapter-${targetChapter.id || progress.chapterIndex}`);
                if (el) {
                  const y = el.getBoundingClientRect().top + window.pageYOffset - 72;
                  window.scrollTo({ top: y, behavior: 'smooth' });
                }
              }, 400);
            }
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

  // Observa os capítulos em tela para atualizar o cabeçalho e progresso automaticamente sem saltos
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
              setBookProgress(book.meta.id, idx, 0);
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
  }, [book, loading]);

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

  // Navega suavemente até o capítulo desejado no fluxo contínuo
  const handleSelectChapter = (index: number) => {
    setCurrentChapterIndex(index);
    setTocOpen(false);
    const targetChapter = book?.chapters[index];
    if (targetChapter) {
      const el = document.getElementById(`chapter-${targetChapter.id || index}`);
      if (el) {
        const y = el.getBoundingClientRect().top + window.pageYOffset - 72;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }
  };

  // Avança para o próximo capítulo no áudio player sem cortar a leitura
  const handleAudioNextChapter = () => {
    if (!book) return;
    if (audioChapterIndex < book.chapters.length - 1) {
      const nextIdx = audioChapterIndex + 1;
      setAudioChapterIndex(nextIdx);
      const targetChapter = book.chapters[nextIdx];
      const el = document.getElementById(`chapter-${targetChapter.id || nextIdx}`);
      if (el) {
        const y = el.getBoundingClientRect().top + window.pageYOffset - 72;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }
  };

  // Volta para o capítulo anterior no áudio player
  const handleAudioPreviousChapter = () => {
    if (!book) return;
    if (audioChapterIndex > 0) {
      const prevIdx = audioChapterIndex - 1;
      setAudioChapterIndex(prevIdx);
      const targetChapter = book.chapters[prevIdx];
      const el = document.getElementById(`chapter-${targetChapter.id || prevIdx}`);
      if (el) {
        const y = el.getBoundingClientRect().top + window.pageYOffset - 72;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }
  };

  const currentChapter: Chapter | undefined = book?.chapters[currentChapterIndex];
  const allCurrentChapterText = currentChapter?.sections.map((s) => s.content || '').join('\n\n') || '';

  const audioChapter: Chapter | undefined = book?.chapters[audioChapterIndex];
  const allAudioChapterText = audioChapter?.sections.map((s) => s.content || '').join('\n\n') || '';

  const handleOpenAudio = () => {
    if (!audioPlayback.isPlaying) {
      setAudioChapterIndex(currentChapterIndex);
    }
    setAudioOpen(true);
  };

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
        Carregando obra no leitor monocromático infinito...
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
          {/* Voltar & Sumário */}
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
              title="Abrir Sumário"
            >
              <List className="w-4 h-4" />
              <span className="hidden md:inline">Sumário</span>
            </button>
          </div>

          {/* Título Central Dinâmico Truncado (Acompanha o Scroll) */}
          <div className="hidden lg:block text-center flex-1 mx-4 min-w-0">
            <span className="font-serif text-xs italic text-[var(--text-secondary)] truncate block">
              {book.meta.title} — Cap. {currentChapter?.number}: {currentChapter?.title}
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
              title="Aprofundar com Agentes Especializados (Prof. Elias, Lucas Hack, Lia, Dr. Viktor)"
            >
              <Sparkles className="w-4 h-4" />
              <span className="hidden md:inline">Agentes IA</span>
            </button>

            {/* Ouvir (HeyGen Turbo + Bucket S3) */}
            <button
              onClick={handleOpenAudio}
              className={`p-1.5 sm:px-2 sm:py-1.5 rounded border transition-colors flex items-center gap-1 text-xs font-mono shrink-0 ${
                audioPlayback.isPlaying
                  ? 'border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
                  : 'border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] text-[var(--text-primary)]'
              }`}
              title="Audiodescrição com IA do Capítulo (HeyGen Voice Turbo)"
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

      {/* Sumário Drawer */}
      <TocDrawer
        isOpen={tocOpen}
        onClose={() => setTocOpen(false)}
        chapters={book.chapters}
        currentChapterIndex={currentChapterIndex}
        onSelectChapter={handleSelectChapter}
        bookTitle={book.meta.title}
      />

      {/* Coluna Central de Leitura Contínua (Scroll Infinito Sem Cortes) */}
      <main ref={contentRef} className="reader-container py-8 sm:py-12 md:py-16">
        {book.chapters.map((chapter: Chapter, cIdx: number) => (
          <section
            key={chapter.id || cIdx}
            id={`chapter-${chapter.id || cIdx}`}
            data-chapter-index={cIdx}
            ref={(el) => {
              chapterRefs.current[cIdx] = el;
            }}
            className="chapter-section pt-8 sm:pt-14 pb-12 sm:pb-16 border-b border-[var(--border-color)] last:border-b-0"
          >
            {/* Cabeçalho Editorial do Capítulo */}
            <header className="mb-8 sm:mb-10 text-center">
              <div className="font-mono text-xs uppercase tracking-widest text-[var(--text-muted)] mb-3">
                Capítulo {chapter.number} de {book.chapters.length}
              </div>
              <h2 className="reader-heading-1 font-serif text-3xl sm:text-4xl leading-tight">
                {chapter.title}
              </h2>

              {/* Epígrafe */}
              {chapter.epigraph && (
                <div className="reader-epigraph font-serif text-sm">
                  <p className="italic">&ldquo;{chapter.epigraph.text}&rdquo;</p>
                  {chapter.epigraph.author && (
                    <span className="reader-epigraph-author">
                      — {chapter.epigraph.author}
                    </span>
                  )}
                </div>
              )}
            </header>

            {/* Seções do Capítulo */}
            <article className="space-y-6">
              {chapter.sections.map((sec: Section, sIdx: number) => {
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

            {/* Quizzes de Fixação do Capítulo (Discretos e Opcionais) */}
            {chapter.quiz && chapter.quiz.length > 0 && (
              <div className="mt-10 pt-6 border-t border-[var(--border-color)]">
                <h3 className="font-serif text-xl font-bold mb-3">
                  Recuperação Ativa & Fixação
                </h3>
                {chapter.quiz.map((q, qIdx) => (
                  <QuizBlock key={qIdx} quiz={q} index={qIdx + 1} />
                ))}
              </div>
            )}
          </section>
        ))}

        {/* Colofão / Conclusão Contínua da Obra */}
        <div className="py-16 text-center border-t-2 border-[var(--border-strong)] mt-8">
          <div className="font-mono text-xs uppercase tracking-widest text-[var(--text-muted)] mb-2">
            Fim do Manual
          </div>
          <h3 className="font-serif text-2xl font-bold mb-3">
            {book.meta.title}
          </h3>
          <p className="text-xs text-[var(--text-secondary)] font-sans max-w-md mx-auto mb-6">
            Você completou a leitura contínua de todos os capítulos. Pratique os conceitos e revise pontos específicos no Sumário.
          </p>

          {/* Quizzes Globais da Obra */}
          {book.quiz && book.quiz.length > 0 && (
            <div className="mt-8 pt-8 border-t border-[var(--border-color)] text-left">
              <h4 className="font-serif text-xl font-bold mb-2">
                Desafio Geral da Obra
              </h4>
              <p className="text-xs text-[var(--text-secondary)] font-sans mb-6">
                Teste sua fixação final com as questões fundamentais do manual.
              </p>
              {book.quiz.map((q, qIdx) => (
                <QuizBlock key={`global-${qIdx}`} quiz={q} index={qIdx + 1} />
              ))}
            </div>
          )}
        </div>
      </main>

      {/* Modais de Aprofundamento e Áudio */}
      <DeepenModal
        isOpen={deepenOpen}
        onClose={() => setDeepenOpen(false)}
        initialTopic={selectedTextForDeepen}
        contextText={allCurrentChapterText.slice(0, 400)}
      />

      <AudioPlayerModal
        isOpen={audioOpen}
        onClose={() => setAudioOpen(false)}
        textToRead={allAudioChapterText}
        chapterTitle={`${book.meta.title} — Cap. ${audioChapter?.number || (audioChapterIndex + 1)}: ${audioChapter?.title || ''}`}
        chapterId={`${book.meta.id}-${audioChapter?.id || audioChapterIndex}`}
        onPlaybackUpdate={setAudioPlayback}
        onNextChapter={handleAudioNextChapter}
        onPreviousChapter={handleAudioPreviousChapter}
        hasNextChapter={audioChapterIndex < book.chapters.length - 1}
        hasPreviousChapter={audioChapterIndex > 0}
      />

      {/* Guia Animado do Lápis Editorial (Acompanha a voz palavra por palavra no capítulo ativo) */}
      <ReadingPencilGuide
        containerRef={activeChapterContainerRef}
        isPlaying={audioPlayback.isPlaying}
        currentTime={audioPlayback.currentTime}
        duration={audioPlayback.duration}
        isLoading={audioPlayback.isLoading}
        enabled={pencilEnabled}
      />

      {/* Régua de Foco Ocular */}
      <ReadingRuler isActive={rulerEnabled} />
    </div>
  );
}
