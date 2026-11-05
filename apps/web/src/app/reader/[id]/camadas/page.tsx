'use client';

import React, { useEffect, useState, useRef, use } from 'react';
import Link from 'next/link';
import {
  ArrowLeft,
  BookOpen,
  List,
  Volume2,
  Sparkles,
  ChevronLeft,
  ChevronRight,
  Layers,
  CheckCircle2,
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

  const currentChapter = book?.chapters[currentChapterIndex];

  if (loading) {
    return (
      <div className="min-h-screen bg-[var(--bg-primary)] flex items-center justify-center font-mono text-xs text-[var(--text-muted)]">
        Carregando leitura em camadas...
      </div>
    );
  }

  if (!book || !currentChapter) {
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

  // Prepara o texto integral do capítulo para audiodescrição
  const chapterFullText = currentChapter.sections
    .map((s) => s.content)
    .join('\n\n');

  // Camada 1: Resumo (1º parágrafo + callout ou síntese)
  const paragraphs = currentChapter.sections.filter((s) => s.type === 'paragraph');
  const callouts = currentChapter.sections.filter((s) => s.type === 'callout');
  const headings = currentChapter.sections.filter((s) => s.type === 'heading');

  const summaryParagraphs = paragraphs.slice(0, 2);
  const mainCallout = callouts[0] || null;

  return (
    <div className="min-h-screen bg-[var(--bg-primary)] text-[var(--text-primary)]">
      {/* Top Header - Idêntico ao Leitor Padrão */}
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

          <div className="text-center font-mono text-xs text-[var(--text-secondary)] line-clamp-1 max-w-[200px] sm:max-w-sm">
            Cap. {currentChapter.number}: {currentChapter.title}
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setAudioOpen(true)}
              className="p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono border border-[var(--border-color)]"
              title="Audiodescrição com IA do Capítulo"
            >
              <Volume2 className="w-4 h-4" />
              <span className="hidden sm:inline">Audiodescrição</span>
            </button>

            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Seletor Editorial de Camadas (3 Camadas Limpas) */}
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
                <div className="font-mono text-xs font-bold uppercase tracking-wider mb-0.5">
                  {layer.id}. {layer.title}
                </div>
                <div
                  className={`text-[11px] font-sans line-clamp-1 ${
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
        onSelectChapter={(idx) => {
          setCurrentChapterIndex(idx);
          setTocOpen(false);
        }}
        bookTitle={book.meta.title}
      />

      {/* Conteúdo Principal Monocromático */}
      <main ref={contentRef} className="max-w-2xl mx-auto px-6 py-12">
        {/* Cabeçalho do Capítulo */}
        <div className="mb-10 pb-6 border-b border-[var(--border-color)]">
          <div className="flex items-center gap-2 mb-2 font-mono text-xs text-[var(--text-muted)] uppercase tracking-widest">
            <Layers className="w-3.5 h-3.5" />
            <span>Capítulo {currentChapter.number} · {LAYERS[activeLayer - 1].title}</span>
          </div>

          <h1 className="font-serif text-3xl sm:text-4xl font-bold tracking-tight text-[var(--text-primary)] mb-4 leading-tight">
            {currentChapter.title}
          </h1>

          {currentChapter.epigraph && (
            <blockquote className="border-l-2 border-[var(--border-strong)] pl-4 my-4 font-serif italic text-sm text-[var(--text-secondary)]">
              "{currentChapter.epigraph.text}"
              {currentChapter.epigraph.author && (
                <cite className="block text-xs font-mono text-[var(--text-muted)] mt-1.5 not-italic">
                  — {currentChapter.epigraph.author}
                </cite>
              )}
            </blockquote>
          )}
        </div>

        {/* CAMADA 1: RESUMO ESSENCIAL */}
        {activeLayer === 1 && (
          <div className="space-y-6">
            <div className="p-4 rounded border border-[var(--border-strong)] bg-[var(--bg-surface)]">
              <span className="font-mono text-xs font-bold uppercase tracking-wider text-[var(--text-primary)] block mb-1">
                💡 Síntese Panorâmica
              </span>
              <p className="font-sans text-xs text-[var(--text-secondary)]">
                Leia este resumo essencial para ancorar o tema sem esforço. Quando estiver pronto, avance para a versão intermediária ou texto completo.
              </p>
            </div>

            {summaryParagraphs.map((p, idx) => (
              <p key={idx} className="font-serif text-lg leading-relaxed text-[var(--text-primary)]">
                {p.content}
              </p>
            ))}

            {mainCallout && (
              <div className="p-5 rounded border border-[var(--border-strong)] bg-[var(--bg-card)] my-6">
                <span className="font-mono text-xs font-bold uppercase tracking-wider text-[var(--text-primary)] block mb-2">
                  📌 {mainCallout.title || 'Ponto Central'}
                </span>
                <p className="font-serif text-base leading-relaxed text-[var(--text-secondary)]">
                  {mainCallout.content}
                </p>
              </div>
            )}

            <div className="pt-8 border-t border-[var(--border-color)] flex justify-end">
              <button
                onClick={() => setActiveLayer(2)}
                className="px-4 py-2 border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs rounded font-bold hover:opacity-90 transition-opacity"
              >
                Avançar para Camada 2: Intermediário →
              </button>
            </div>
          </div>
        )}

        {/* CAMADA 2: VERSÃO INTERMEDIÁRIA (CONCEITO, EXEMPLO E APLICAÇÃO) */}
        {activeLayer === 2 && (
          <div className="space-y-8">
            <div className="p-4 rounded border border-[var(--border-strong)] bg-[var(--bg-surface)]">
              <span className="font-mono text-xs font-bold uppercase tracking-wider text-[var(--text-primary)] block mb-1">
                🧩 Progressive Disclosure
              </span>
              <p className="font-sans text-xs text-[var(--text-secondary)]">
                O conteúdo estruturado em pequenas partes fáceis de digerir: <strong>O Conceito</strong>, <strong>O Exemplo Prático</strong> e <strong>A Aplicação Imediata</strong>.
              </p>
            </div>

            {/* Bloco 1: Conceito */}
            <div className="space-y-3 pb-6 border-b border-[var(--border-color)]">
              <div className="flex items-center gap-2 font-mono text-xs font-bold uppercase text-[var(--text-primary)]">
                <span className="w-5 h-5 rounded-full border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] flex items-center justify-center text-[10px]">1</span>
                <span>O Conceito Fundamental</span>
              </div>
              <p className="font-serif text-lg leading-relaxed text-[var(--text-primary)]">
                {paragraphs[0]?.content || 'Compreender a base estrutural deste capítulo antes de avançar para a execução prática.'}
              </p>
            </div>

            {/* Bloco 2: Exemplo */}
            <div className="space-y-3 pb-6 border-b border-[var(--border-color)]">
              <div className="flex items-center gap-2 font-mono text-xs font-bold uppercase text-[var(--text-primary)]">
                <span className="w-5 h-5 rounded-full border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] flex items-center justify-center text-[10px]">2</span>
                <span>O Exemplo em Ação</span>
              </div>
              <p className="font-serif text-lg leading-relaxed text-[var(--text-primary)]">
                {paragraphs[1]?.content || 'Observe como a teoria se manifesta em situações reais de avaliação e análise argumentativa.'}
              </p>
            </div>

            {/* Bloco 3: Aplicação Prática */}
            <div className="space-y-3 pb-6 border-b border-[var(--border-color)]">
              <div className="flex items-center gap-2 font-mono text-xs font-bold uppercase text-[var(--text-primary)]">
                <span className="w-5 h-5 rounded-full border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] flex items-center justify-center text-[10px]">3</span>
                <span>Como Aplicar no Seu Rascunho</span>
              </div>
              <p className="font-serif text-lg leading-relaxed text-[var(--text-primary)]">
                {paragraphs[2]?.content || 'Transponha este princípio diretamente para a construção da sua redação ou estudo diário.'}
              </p>
            </div>

            {/* Callouts do Capítulo */}
            {callouts.map((callout, idx) => (
              <div key={idx} className="p-5 rounded border border-[var(--border-strong)] bg-[var(--bg-card)]">
                <span className="font-mono text-xs font-bold uppercase tracking-wider text-[var(--text-primary)] block mb-1">
                  📌 {callout.title || 'Destaque de Fixação'}
                </span>
                <p className="font-serif text-base text-[var(--text-secondary)] leading-relaxed">
                  {callout.content}
                </p>
              </div>
            ))}

            <div className="pt-4 flex items-center justify-between">
              <button
                onClick={() => setActiveLayer(1)}
                className="px-4 py-2 border border-[var(--border-color)] text-[var(--text-secondary)] hover:text-[var(--text-primary)] font-mono text-xs rounded transition-colors"
              >
                ← Voltar ao Resumo
              </button>
              <button
                onClick={() => setActiveLayer(3)}
                className="px-4 py-2 border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs rounded font-bold hover:opacity-90 transition-opacity"
              >
                Avançar para Texto Completo →
              </button>
            </div>
          </div>
        )}

        {/* CAMADA 3: TEXTO COMPLETO APROFUNDADO */}
        {activeLayer === 3 && (
          <div className="space-y-6">
            {currentChapter.sections.map((section, idx) => {
              if (section.type === 'heading') {
                return (
                  <h2
                    key={idx}
                    className="font-serif text-2xl font-bold tracking-tight text-[var(--text-primary)] mt-10 mb-4 pt-4 border-t border-[var(--border-color)]"
                  >
                    {section.content}
                  </h2>
                );
              }

              if (section.type === 'callout') {
                return (
                  <div
                    key={idx}
                    className="p-5 rounded border border-[var(--border-strong)] bg-[var(--bg-card)] my-6"
                  >
                    {section.title && (
                      <span className="font-mono text-xs font-bold uppercase tracking-wider text-[var(--text-primary)] block mb-2">
                        {section.title}
                      </span>
                    )}
                    <p className="font-serif text-base leading-relaxed text-[var(--text-secondary)]">
                      {section.content}
                    </p>
                  </div>
                );
              }

              return (
                <p
                  key={idx}
                  className="font-serif text-lg leading-relaxed text-[var(--text-primary)]"
                >
                  {section.content}
                </p>
              );
            })}

            <div className="pt-8 border-t border-[var(--border-color)] flex justify-start">
              <button
                onClick={() => setActiveLayer(1)}
                className="px-4 py-2 border border-[var(--border-color)] text-[var(--text-secondary)] hover:text-[var(--text-primary)] font-mono text-xs rounded transition-colors"
              >
                ← Voltar ao Resumo Panorâmico
              </button>
            </div>
          </div>
        )}

        {/* Navegação entre Capítulos - Idêntico ao Leitor Padrão */}
        <div className="mt-16 pt-8 border-t border-[var(--border-color)] flex items-center justify-between">
          {currentChapterIndex > 0 ? (
            <button
              onClick={() => {
                setCurrentChapterIndex((prev) => prev - 1);
                setActiveLayer(1);
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="flex items-center gap-2 px-4 py-2 rounded border border-[var(--border-color)] hover:border-[var(--border-strong)] text-xs font-mono transition-colors"
            >
              <ChevronLeft className="w-4 h-4" />
              <span>Capítulo Anterior</span>
            </button>
          ) : (
            <div />
          )}

          {currentChapterIndex < book.chapters.length - 1 ? (
            <button
              onClick={() => {
                setCurrentChapterIndex((prev) => prev + 1);
                setActiveLayer(1);
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="flex items-center gap-2 px-4 py-2 rounded border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] text-xs font-mono font-bold transition-opacity hover:opacity-90"
            >
              <span>Próximo Capítulo</span>
              <ChevronRight className="w-4 h-4" />
            </button>
          ) : (
            <div />
          )}
        </div>
      </main>

      {/* Modal de Audiodescrição com IA */}
      <AudioPlayerModal
        isOpen={audioOpen}
        onClose={() => setAudioOpen(false)}
        textToRead={chapterFullText}
        chapterTitle={`${book.meta.title} — Cap. ${currentChapter.number}: ${currentChapter.title}`}
        chapterId={`${book.meta.id}-${currentChapter.id}`}
        onPlaybackUpdate={setAudioPlayback}
      />

      {/* Guia Animado do Lápis Editorial */}
      <ReadingPencilGuide
        containerRef={contentRef}
        isPlaying={audioPlayback.isPlaying}
        currentTime={audioPlayback.currentTime}
        duration={audioPlayback.duration}
        isLoading={audioPlayback.isLoading}
        enabled={pencilEnabled}
      />
    </div>
  );
}
