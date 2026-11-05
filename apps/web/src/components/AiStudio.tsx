'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import {
  Sparkles,
  ArrowRight,
  Loader2,
  BookOpen,
  GraduationCap,
  Zap,
  Coffee,
  ShieldAlert,
} from 'lucide-react';
import { generateLayeredBook } from '@/lib/api';
import { addCustomCatalogBook } from '@/lib/storage';
import { AGENT_LIST, AgentId, AGENT_PERSONAS } from '@mono-reader/shared';

const AGENT_ICONS: Record<AgentId, React.ElementType> = {
  professor: GraduationCap,
  curseiro: Zap,
  simplificador: Coffee,
  corretor: ShieldAlert,
};

export function AiStudio({ onBookGenerated }: { onBookGenerated?: () => void }) {
  const router = useRouter();
  const [prompt, setPrompt] = useState('');
  const [chaptersCount, setChaptersCount] = useState(3);
  const [selectedAgent, setSelectedAgent] = useState<AgentId>('curseiro');
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [progressText, setProgressText] = useState('');
  const [subtext, setSubtext] = useState('');
  const [error, setError] = useState<string | null>(null);

  const activePersona = AGENT_PERSONAS[selectedAgent];

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!prompt.trim() || loading) return;

    setLoading(true);
    setError(null);
    setProgress(15);
    setProgressText(`1/3. ${activePersona.name} construindo Camada 1 — Resumo Panorâmico...`);
    setSubtext(`${activePersona.tagline}`);

    const timer1 = setTimeout(() => {
      setProgress(45);
      setProgressText(`2/3. Estruturando Camada 2 no estilo ${activePersona.badge}...`);
      setSubtext('Organizando Conceito → Exemplo Prático → Aplicação...');
    }, 1600);

    const timer2 = setTimeout(() => {
      setProgress(80);
      setProgressText('3/3. Finalizando Camada 3 — Texto Didático Completo...');
      setSubtext('Polindo estilo autoral e desafios de fixação...');
    }, 3600);

    try {
      const { book } = await generateLayeredBook({
        topic: prompt.trim(),
        chaptersCount,
        depth: 'enem_elite',
        agentId: selectedAgent,
      });

      clearTimeout(timer1);
      clearTimeout(timer2);
      setProgress(100);
      setProgressText('Obra concluída!');
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
        author: book.meta.author || activePersona.authorLabel,
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
    <div className="p-4 sm:p-6 rounded-lg border border-[var(--border-strong)] bg-[var(--bg-card)] mb-10 shadow-sm">
      <div className="flex items-center gap-2 mb-2 text-xs font-mono uppercase tracking-wider text-[var(--text-muted)]">
        <Sparkles className="w-3.5 h-3.5" />
        <span>Estúdio de Criação com Agentes Especializados</span>
      </div>

      <h2 className="font-serif text-xl sm:text-2xl font-bold mb-2 text-[var(--text-primary)]">
        Gerar Obra Autoral em Camadas
      </h2>

      <p className="text-xs text-[var(--text-secondary)] font-sans mb-4 max-w-2xl leading-relaxed">
        Escolha o agente que será o <strong>autor e mentor</strong> da obra. Cada agente escreve com tom, vocabulário e metodologia próprios: do rigor acadêmico aos macetes rápidos de prova.
      </p>

      {/* Seletor de Agentes / Personas */}
      <div className="mb-4">
        <label className="block text-xs font-mono text-[var(--text-muted)] mb-2 font-bold uppercase tracking-wider">
          Selecione o Agente Autor:
        </label>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2.5">
          {AGENT_LIST.map((agent) => {
            const Icon = AGENT_ICONS[agent.id] || Sparkles;
            const isSelected = selectedAgent === agent.id;
            return (
              <button
                key={agent.id}
                type="button"
                onClick={() => setSelectedAgent(agent.id)}
                disabled={loading}
                className={`p-3 rounded-lg border text-left transition-all ${
                  isSelected
                    ? 'border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] shadow-sm'
                    : 'border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-primary)] hover:border-[var(--border-strong)]'
                }`}
              >
                <div className="flex items-center gap-2 mb-1.5">
                  <Icon className="w-4 h-4 shrink-0" />
                  <span className="font-serif font-bold text-xs truncate">{agent.name}</span>
                </div>
                <div className={`text-[10px] font-mono mb-1 truncate ${isSelected ? 'opacity-90' : 'text-[var(--text-muted)]'}`}>
                  {agent.badge}
                </div>
                <p className={`text-[11px] font-sans line-clamp-2 leading-tight ${isSelected ? 'opacity-85' : 'text-[var(--text-secondary)]'}`}>
                  {agent.tagline}
                </p>
              </button>
            );
          })}
        </div>
      </div>

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="block text-xs font-mono text-[var(--text-muted)] mb-1">
            Tema, Edital ou Assunto:
          </label>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder={`Exemplo: Redação ENEM nota 1000 — tese, proposta de intervenção de 5 elementos e repertórios coringas...`}
            rows={3}
            disabled={loading}
            className="w-full p-3 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-primary)] font-serif text-sm focus:outline-none focus:border-[var(--border-strong)] resize-none"
          />
        </div>

        <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
          <div className="flex flex-wrap items-center gap-2 text-xs font-mono">
            <span className="text-[var(--text-muted)]">Extensão:</span>
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
              className="flex items-center gap-2 px-5 py-2.5 rounded bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90 disabled:opacity-50 transition-opacity shadow-sm"
            >
              {loading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>{activePersona.name} Escrevendo...</span>
                </>
              ) : (
                <>
                  <BookOpen className="w-4 h-4" />
                  <span>Gerar com {activePersona.name}</span>
                  <ArrowRight className="w-3.5 h-3.5 ml-1" />
                </>
              )}
            </button>
          </div>
        </div>

        {/* Sugestões Rápidas contextualizadas com o agente */}
        {!loading && (
          <div className="mt-3.5 pt-3 border-t border-[var(--border-light)] flex flex-wrap items-center gap-2">
            <span className="text-[11px] font-mono text-[var(--text-muted)]">Sugestões rápidas:</span>
            {activePersona.quickPrompts.map((q, idx) => (
              <button
                key={idx}
                type="button"
                onClick={() => handleQuickPrompt(`${q}: Redação ENEM & Argumentação`)}
                className="text-[11px] font-sans px-2.5 py-1 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-secondary)] hover:border-[var(--border-strong)] transition-colors truncate max-w-xs"
              >
                ✦ {q}
              </button>
            ))}
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