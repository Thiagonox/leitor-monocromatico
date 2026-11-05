'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Sparkles, ArrowRight, Loader2, BookOpen } from 'lucide-react';
import { generateLayeredBook } from '@/lib/api';
import { addCustomCatalogBook } from '@/lib/storage';

export function AiStudio({ onBookGenerated }: { onBookGenerated?: () => void }) {
  const router = useRouter();
  const [prompt, setPrompt] = useState('');
  const [chaptersCount, setChaptersCount] = useState(3);
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [progressText, setProgressText] = useState('');
  const [subtext, setSubtext] = useState('');
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!prompt.trim() || loading) return;

    setLoading(true);
    setError(null);
    setProgress(15);
    setProgressText('1/3. Construindo Camada 1 — Resumo Rápido...');
    setSubtext('Reduzindo a resistência inicial com uma visão panorâmica direta...');

    const timer1 = setTimeout(() => {
      setProgress(45);
      setProgressText('2/3. Estruturando Camada 2 — Progressive Disclosure...');
      setSubtext('Dividindo tópicos: Conceito → Exemplo → Aplicação...');
    }, 1500);

    const timer2 = setTimeout(() => {
      setProgress(80);
      setProgressText('3/3. Finalizando Camada 3 — Texto Completo...');
      setSubtext('Consolidando a explicação aprofundada para o leitor padrão...');
    }, 3500);

    try {
      const { book } = await generateLayeredBook({
        topic: prompt.trim(),
        chaptersCount,
        depth: 'enem_elite'
      });

      clearTimeout(timer1);
      clearTimeout(timer2);
      setProgress(100);
      setProgressText('Concluído!');
      setSubtext('Abrindo obra no leitor padrão...');

      // Salva no localStorage
      if (typeof window !== 'undefined') {
        localStorage.setItem(`book_json_${book.meta.id}`, JSON.stringify(book));
      }

      // Adiciona ao catálogo
      addCustomCatalogBook({
        id: book.meta.id,
        title: book.meta.title,
        subtitle: book.meta.subtitle,
        author: book.meta.author || 'Manual Vivo · Leitura em Camadas',
        category: book.meta.category || 'Leitura em Camadas',
        chaptersCount: book.chapters.length,
        estimatedTime: book.meta.estimatedReadingTime || 'Leitura Didática Completa',
        file: `/data/${book.meta.id}.json`,
        description: book.meta.description,
        isPriority: true,
        isGeneratedByAI: true,
        createdAt: new Date().toISOString()
      });

      if (onBookGenerated) onBookGenerated();

      await new Promise(r => setTimeout(r, 400));
      router.push(`/reader/${book.meta.id}`);
    } catch (err: any) {
      clearTimeout(timer1);
      clearTimeout(timer2);
      console.error('Erro ao gerar:', err);
      setError(err.message || 'Erro ao gerar conteúdo. Tente novamente.');
      setLoading(false);
    }
  };

  const handleQuickPrompt = (text: string) => {
    setPrompt(text);
  };

  return (
    <div className="p-6 rounded border border-[var(--border-strong)] bg-[var(--bg-card)] mb-10 shadow-sm">
      <div className="flex items-center gap-2 mb-2 text-xs font-mono uppercase tracking-wider text-[var(--text-muted)]">
        <Sparkles className="w-3.5 h-3.5" />
        <span>Estúdio de Criação Didática por IA</span>
      </div>

      <h2 className="font-serif text-2xl font-bold mb-2 text-[var(--text-primary)]">
        Gerar Obra em Camadas e Progressive Disclosure
      </h2>

      <p className="text-xs text-[var(--text-secondary)] font-sans mb-4 max-w-2xl leading-relaxed">
        Digite um tema, matéria ou edital (ex: Redação ENEM, Termodinâmica, Revolução Francesa). A IA estruturará uma obra completa no leitor em camadas: <strong>Resumo Rápido</strong>, <strong>Conceito + Exemplo + Aplicação</strong> e <strong>Texto Completo</strong>.
      </p>

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Exemplo: Redação (PRIORIDADE MÁXIMA): Estrutura dissertativa, tese, introdução, intervenção, competências e repertórios coringas..."
            rows={3}
            disabled={loading}
            className="w-full p-3 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-primary)] font-serif text-sm focus:outline-none focus:border-[var(--border-strong)] resize-none"
          />
        </div>

        <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
          <div className="flex flex-wrap items-center gap-2 text-xs font-mono">
            <span className="text-[var(--text-muted)]">Capítulos:</span>
            {[3, 4, 5].map((cnt) => (
              <button
                key={cnt}
                type="button"
                onClick={() => setChaptersCount(cnt)}
                disabled={loading}
                className={`px-2.5 py-1 rounded border text-xs ${
                  chaptersCount === cnt
                    ? 'border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold'
                    : 'border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-secondary)]'
                }`}
              >
                {cnt} caps
              </button>
            ))}
          </div>

          <div className="flex items-center gap-2">
            <button
              type="submit"
              disabled={loading || !prompt.trim()}
              className="flex items-center gap-2 px-5 py-2.5 rounded bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90 disabled:opacity-50 transition-opacity"
            >
              {loading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>Estruturando Camadas...</span>
                </>
              ) : (
                <>
                  <BookOpen className="w-4 h-4" />
                  <span>Gerar no Leitor</span>
                  <ArrowRight className="w-3.5 h-3.5 ml-1" />
                </>
              )}
            </button>
          </div>
        </div>

        {/* Sugestões Rápidas */}
        {!loading && (
          <div className="mt-3 pt-3 border-t border-[var(--border-light)] flex flex-wrap items-center gap-2">
            <span className="text-[11px] font-mono text-[var(--text-muted)]">Sugestões rápidas:</span>
            <button
              type="button"
              onClick={() => handleQuickPrompt("Redação ENEM: Estrutura dissertativo-argumentativa, tese, proposta de intervenção e repertórios socioculturais")}
              className="text-[11px] font-sans px-2 py-0.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-secondary)] hover:border-[var(--border-strong)] transition-colors"
            >
              ✦ Redação ENEM Completa
            </button>
            <button
              type="button"
              onClick={() => handleQuickPrompt("Interpretação de Texto: Figuras de linguagem, coesão, coerência e inferência")}
              className="text-[11px] font-sans px-2 py-0.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-secondary)] hover:border-[var(--border-strong)] transition-colors"
            >
              ✦ Interpretação & Coesão
            </button>
            <button
              type="button"
              onClick={() => handleQuickPrompt("Constituição Federal de 1988: Direitos sociais, cidadania e dignidade humana")}
              className="text-[11px] font-sans px-2 py-0.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-secondary)] hover:border-[var(--border-strong)] transition-colors"
            >
              ✦ CF/88 & Cidadania
            </button>
          </div>
        )}

        {/* Barra de Progresso */}
        {loading && (
          <div className="mt-4 p-4 rounded border border-[var(--border-color)] bg-[var(--bg-surface)]">
            <div className="flex items-center justify-between text-xs font-mono mb-2">
              <span className="font-bold text-[var(--text-primary)]">{progressText}</span>
              <span className="text-[var(--text-muted)]">{progress}%</span>
            </div>
            <div className="w-full bg-[var(--border-light)] h-2 rounded overflow-hidden mb-2">
              <div
                className="bg-[var(--text-primary)] h-full transition-all duration-300"
                style={{ width: `${progress}%` }}
              />
            </div>
            <p className="text-[11px] text-[var(--text-muted)] font-mono">{subtext}</p>
          </div>
        )}

        {error && (
          <div className="mt-3 p-3 rounded border border-red-500 bg-red-50 dark:bg-red-950 text-red-700 dark:text-red-300 text-xs font-mono">
            {error}
          </div>
        )}
      </form>
    </div>
  );
}
