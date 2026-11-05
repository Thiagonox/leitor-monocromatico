'use client';

import React, { useEffect, useState, use } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import {
  ArrowLeft,
  BookOpen,
  HelpCircle,
  Zap,
  Lightbulb,
  Cpu,
  BookCheck,
  ChevronLeft,
  ChevronRight,
  List
} from 'lucide-react';
import { fetchBook } from '@/lib/api';
import { BookDoc, Chapter, Section } from '@mono-reader/shared';
import { ThemeToggle } from '@/components/ThemeToggle';
import { TocDrawer } from '@/components/TocDrawer';

const STAGES = [
  { id: 0, label: 'Desafio', sub: 'Priming', icon: HelpCircle },
  { id: 1, label: 'Flash', sub: '30s', icon: Zap },
  { id: 2, label: 'Conceito', sub: '1 min', icon: Lightbulb },
  { id: 3, label: 'Mecanismo', sub: '3 min', icon: Cpu },
  { id: 4, label: 'Capítulo Completo', sub: 'Aprofundado', icon: BookOpen },
  { id: 5, label: 'Active Recall', sub: 'Fixação', icon: BookCheck },
];

export default function LayeredReaderPage({ params }: { params: Promise<{ id: string }> }) {
  const resolvedParams = use(params);
  const router = useRouter();

  const [book, setBook] = useState<BookDoc | null>(null);
  const [currentChapterIndex, setCurrentChapterIndex] = useState(0);
  const [currentStage, setCurrentStage] = useState(0);
  const [loading, setLoading] = useState(true);
  const [tocOpen, setTocOpen] = useState(false);

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
    return () => { active = false; };
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
      <div className="min-h-screen bg-[var(--bg-primary)] flex flex-col items-center justify-center p-6 text-center">
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

  // Extrai primeiro parágrafo como flash/resumo rápido se não houver camada explícita
  const firstParagraph = currentChapter.sections.find(s => s.type === 'paragraph')?.content || '';
  const firstCallout = currentChapter.sections.find(s => s.type === 'callout')?.content || '';
  const headings = currentChapter.sections.filter(s => s.type === 'heading');

  return (
    <div className="min-h-screen bg-[var(--bg-primary)] text-[var(--text-primary)]">
      {/* Top Header */}
      <header className="sticky top-0 z-40 bg-[var(--bg-primary)]/95 backdrop-blur-sm border-b border-[var(--border-color)]">
        <div className="max-w-4xl mx-auto px-4 h-14 flex items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <Link
              href={`/reader/${book.meta.id}`}
              className="p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Leitor Padrão</span>
            </Link>

            <button
              onClick={() => setTocOpen(true)}
              className="p-2 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-primary)] transition-colors flex items-center gap-1.5 text-xs font-mono"
            >
              <List className="w-4 h-4" />
              <span className="hidden sm:inline">Capítulos</span>
            </button>
          </div>

          <div className="text-center font-mono text-xs text-[var(--text-secondary)] line-clamp-1">
            Cap. {currentChapter.number}: {currentChapter.title}
          </div>

          <div className="flex items-center gap-2">
            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Seletor de Camadas Cognitivas */}
      <div className="border-b border-[var(--border-color)] bg-[var(--bg-surface)] sticky top-14 z-30 overflow-x-auto">
        <div className="max-w-4xl mx-auto px-4 py-2 flex items-center justify-between gap-1">
          {STAGES.map((stg) => {
            const Icon = stg.icon;
            const isActive = currentStage === stg.id;
            return (
              <button
                key={stg.id}
                onClick={() => setCurrentStage(stg.id)}
                className={`flex-1 min-w-[90px] py-2 px-1 text-center rounded border transition-colors ${
                  isActive
                    ? 'border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
                    : 'border-transparent text-[var(--text-secondary)] hover:bg-[var(--bg-secondary)]'
                }`}
              >
                <div className="flex items-center justify-center gap-1 mb-0.5">
                  <Icon className="w-3.5 h-3.5" />
                  <span className="font-mono text-xs">{stg.label}</span>
                </div>
                <div className={`text-[10px] font-mono ${isActive ? 'text-[var(--bg-primary)] opacity-80' : 'text-[var(--text-muted)]'}`}>
                  {stg.sub}
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* Sumário Drawer */}
      <TocDrawer
        isOpen={tocOpen}
        onClose={() => setTocOpen(false)}
        chapters={book.chapters}
        currentChapterIndex={currentChapterIndex}
        onSelectChapter={(idx) => {
          setCurrentChapterIndex(idx);
          setCurrentStage(0);
        }}
        bookTitle={book.meta.title}
      />

      {/* Conteúdo da Camada Ativa */}
      <main className="max-w-3xl mx-auto px-6 py-12">
        {/* Camada 0: Desafio / Priming */}
        {currentStage === 0 && (
          <div className="space-y-6">
            <div className="font-mono text-xs uppercase tracking-wider text-[var(--text-muted)]">
              Camada 0 de 5 — Priming Cognitivo
            </div>
            <h2 className="font-serif text-3xl font-bold leading-tight">
              Antes de ler o texto completo, ative o radar do seu cérebro.
            </h2>
            <p className="font-serif text-base text-[var(--text-secondary)] leading-relaxed italic">
              Estudos de neurociência demonstram que reter um conteúdo denso é 3x mais eficiente quando você parte de uma pergunta orientadora em vez de uma leitura passiva.
            </p>

            <div className="p-6 rounded border border-[var(--border-strong)] bg-[var(--bg-card)]">
              <span className="font-mono text-xs font-bold uppercase tracking-wider text-[var(--text-primary)] block mb-2">
                🎯 Pergunta Orientadora deste Capítulo
              </span>
              <p className="font-serif text-lg font-bold mb-4">
                &ldquo;Qual é a engrenagem ou tese central discutida em &lsquo;{currentChapter.title}&rsquo; e qual armadilha analítica deve ser evitada?&rdquo;
              </p>
              <div className="text-xs font-mono text-[var(--text-muted)]">
                Guarde esta pergunta na mente antes de avançar para as próximas camadas.
              </div>
            </div>

            <div className="flex justify-end pt-4">
              <button
                onClick={() => setCurrentStage(1)}
                className="px-5 py-2.5 rounded bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90"
              >
                Próxima Camada (Flash 30s) →
              </button>
            </div>
          </div>
        )}

        {/* Camada 1: Flash 30s */}
        {currentStage === 1 && (
          <div className="space-y-6">
            <div className="font-mono text-xs uppercase tracking-wider text-[var(--text-muted)]">
              Camada 1 de 5 — Flash 30 Segundos
            </div>
            <h2 className="font-serif text-2xl sm:text-3xl font-bold leading-tight">
              O Takeaway Dourado
            </h2>

            <div className="p-6 rounded border-2 border-[var(--border-strong)] bg-[var(--bg-surface)]">
              <div className="font-serif text-lg font-medium leading-relaxed mb-4">
                {firstCallout || firstParagraph.slice(0, 320)}
              </div>
              <div className="pt-3 border-t border-[var(--border-color)] text-xs font-mono text-[var(--text-muted)]">
                Tempo estimado: 30 segundos • Base de assimilação inicial
              </div>
            </div>

            <div className="flex justify-between pt-4">
              <button
                onClick={() => setCurrentStage(0)}
                className="px-4 py-2 rounded border border-[var(--border-color)] font-mono text-xs"
              >
                ← Voltar ao Desafio
              </button>
              <button
                onClick={() => setCurrentStage(2)}
                className="px-5 py-2.5 rounded bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90"
              >
                Próxima Camada (Conceito 1m) →
              </button>
            </div>
          </div>
        )}

        {/* Camada 2: Conceito 1m */}
        {currentStage === 2 && (
          <div className="space-y-6">
            <div className="font-mono text-xs uppercase tracking-wider text-[var(--text-muted)]">
              Camada 2 de 5 — Conceito Central (1 Minuto)
            </div>
            <h2 className="font-serif text-2xl sm:text-3xl font-bold leading-tight">
              A Definição & Analogia
            </h2>

            <div className="space-y-4 font-serif text-base leading-relaxed">
              <p className="reader-paragraph">
                {firstParagraph}
              </p>
              {currentChapter.sections.slice(1, 3).map((s, idx) => (
                <div key={idx} className="p-4 rounded border border-[var(--border-color)] bg-[var(--bg-card)]">
                  {s.title && <div className="font-mono text-xs font-bold mb-1">{s.title}</div>}
                  <p className="text-sm">{s.content}</p>
                </div>
              ))}
            </div>

            <div className="flex justify-between pt-4">
              <button
                onClick={() => setCurrentStage(1)}
                className="px-4 py-2 rounded border border-[var(--border-color)] font-mono text-xs"
              >
                ← Voltar ao Flash
              </button>
              <button
                onClick={() => setCurrentStage(3)}
                className="px-5 py-2.5 rounded bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90"
              >
                Próxima Camada (Mecanismo 3m) →
              </button>
            </div>
          </div>
        )}

        {/* Camada 3: Mecanismo 3m */}
        {currentStage === 3 && (
          <div className="space-y-6">
            <div className="font-mono text-xs uppercase tracking-wider text-[var(--text-muted)]">
              Camada 3 de 5 — Mecanismo e Aplicação (3 Minutos)
            </div>
            <h2 className="font-serif text-2xl sm:text-3xl font-bold leading-tight">
              Como Funciona & Armadilhas a Evitar
            </h2>

            <div className="space-y-4">
              {currentChapter.sections.filter(s => s.type === 'callout' || s.type === 'heading').map((s, idx) => (
                <div key={idx} className="p-5 rounded border border-[var(--border-strong)] bg-[var(--bg-card)]">
                  <div className="font-mono text-xs font-bold uppercase tracking-wider mb-2">
                    {s.title || s.content}
                  </div>
                  {s.title && <p className="font-serif text-sm leading-relaxed">{s.content}</p>}
                </div>
              ))}
            </div>

            <div className="flex justify-between pt-4">
              <button
                onClick={() => setCurrentStage(2)}
                className="px-4 py-2 rounded border border-[var(--border-color)] font-mono text-xs"
              >
                ← Voltar ao Conceito
              </button>
              <button
                onClick={() => setCurrentStage(4)}
                className="px-5 py-2.5 rounded bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90"
              >
                Ler Capítulo Completo →
              </button>
            </div>
          </div>
        )}

        {/* Camada 4: Capítulo Completo */}
        {currentStage === 4 && (
          <div className="space-y-6">
            <div className="font-mono text-xs uppercase tracking-wider text-[var(--text-muted)]">
              Camada 4 de 5 — Leitura Aprofundada Completa
            </div>
            <h1 className="font-serif text-3xl font-bold leading-tight">
              {currentChapter.title}
            </h1>

            <article className="space-y-6 mt-6">
              {currentChapter.sections.map((sec: Section, idx: number) => {
                if (sec.type === 'heading') {
                  return (
                    <h3 key={idx} className="reader-heading-3">
                      {sec.content}
                    </h3>
                  );
                }
                if (sec.type === 'callout') {
                  return (
                    <div key={idx} className="reader-callout font-sans text-sm">
                      {sec.title && <div className="font-mono text-xs font-bold uppercase mb-1">{sec.title}</div>}
                      <p className="whitespace-pre-line">{sec.content}</p>
                    </div>
                  );
                }
                return (
                  <p key={idx} className="reader-paragraph">
                    {sec.content}
                  </p>
                );
              })}
            </article>

            <div className="flex justify-between pt-8 border-t border-[var(--border-color)]">
              <button
                onClick={() => setCurrentStage(3)}
                className="px-4 py-2 rounded border border-[var(--border-color)] font-mono text-xs"
              >
                ← Voltar ao Mecanismo
              </button>
              <button
                onClick={() => setCurrentStage(5)}
                className="px-5 py-2.5 rounded bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90"
              >
                Checagem de Fixação (Active Recall) →
              </button>
            </div>
          </div>
        )}

        {/* Camada 5: Active Recall */}
        {currentStage === 5 && (
          <div className="space-y-6">
            <div className="font-mono text-xs uppercase tracking-wider text-[var(--text-muted)]">
              Camada 5 de 5 — Recuperação Ativa (Active Recall)
            </div>
            <h2 className="font-serif text-2xl sm:text-3xl font-bold leading-tight">
              Feche as anotações e responda para consolidar
            </h2>

            <div className="p-6 rounded border border-[var(--border-strong)] bg-[var(--bg-card)]">
              <h3 className="font-serif text-lg font-bold mb-3">
                Síntese em Uma Frase
              </h3>
              <p className="text-sm font-sans text-[var(--text-secondary)] mb-4">
                Em suas próprias palavras: qual é a regra, conceito ou tese mais importante que você aprendeu neste capítulo?
              </p>
              <textarea
                placeholder="Escreva seu resumo ativo aqui..."
                rows={3}
                className="w-full p-3 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-primary)] text-sm font-serif focus:outline-none focus:border-[var(--border-strong)]"
              />
            </div>

            <div className="flex justify-between pt-6 border-t border-[var(--border-color)]">
              <button
                onClick={() => setCurrentStage(4)}
                className="px-4 py-2 rounded border border-[var(--border-color)] font-mono text-xs"
              >
                ← Voltar ao Texto Completo
              </button>
              {currentChapterIndex < book.chapters.length - 1 ? (
                <button
                  onClick={() => {
                    setCurrentChapterIndex(prev => prev + 1);
                    setCurrentStage(0);
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                  }}
                  className="px-5 py-2.5 rounded bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90"
                >
                  Próximo Capítulo →
                </button>
              ) : (
                <Link
                  href="/"
                  className="px-5 py-2.5 rounded bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90"
                >
                  Concluir Leitura da Obra ✓
                </Link>
              )}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
