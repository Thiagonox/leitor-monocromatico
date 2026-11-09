'use client';

import React, { useState } from 'react';
import {
  ShieldAlert,
  Sparkles,
  CheckCircle2,
  AlertTriangle,
  XCircle,
  Copy,
  Check,
  RefreshCw,
  FileText,
  ChevronDown,
  ChevronUp,
  Award,
  Zap,
} from 'lucide-react';
import { evaluateEssay } from '@/lib/api';
import { EssayCorrectionResult } from '@mono-reader/shared';

const THEME_PRESETS = [
  'Invisibilidade do trabalho de cuidado realizado pela mulher no Brasil',
  'Desafios para a valorização de comunidades e povos tradicionais no Brasil',
  'Democratização do acesso ao cinema no Brasil',
  'Manipulação do comportamento do usuário pelo controle de dados na internet',
  'Impactos da inteligência artificial na formação educacional e no trabalho',
  'Caminhos para combater a intolerância religiosa no Brasil',
  'A persistência da violência contra a mulher na sociedade brasileira',
];

const SAMPLE_ESSAY = `Na obra "Cidadão de Papel", o jornalista Gilberto Dimenstein afirma que a legislação brasileira, embora moderna, muitas vezes não se concretiza na prática, gerando cidadãos que usufruem apenas de direitos fictícios. Esse cenário reflete com precisão os desafios da invisibilidade do trabalho de cuidado no Brasil, uma vez que a sobrecarga histórica imposta às mulheres perpetua a desigualdade de gênero e o desamparo social. Nesse contexto, torna-se imperativo analisar tanto a omissão estatal quanto a persistência de raízes culturais patriarcais como motores dessa problemática.

Em primeiro lugar, cabe pontuar a inércia do Poder Público como fator agravante. De acordo com o filósofo Zygmunt Bauman, a modernidade contemporânea é marcada pela perda de solidez das instituições públicas, as quais falham em amparar os mais vulneráveis. Sob essa ótica, a escassez de creches em tempo integral e de centros de acolhimento para idosos sobrecarrega as famílias — em especial as mulheres de baixa renda —, impedindo sua inserção plena no mercado de trabalho e reforçando ciclos de pobreza.

Ademais, a herança cultural machista atua como barreira silenciosa. Desde o período colonial, naturalizou-se a divisão sexual do trabalho, delegando à figura feminina as tarefas domésticas e de assistência como uma suposta obrigação afetiva. Essa construção histórica desvaloriza economicamente atividades fundamentais para a reprodução da sociedade, invisibilizando o esgotamento físico e mental de milhões de brasileiras que acumulam jornadas duplas ou triplas sem qualquer remuneração ou reconhecimento formal.

Portanto, medidas são urgentes para reverter essa chaga social. Para tanto, cabe ao Ministério do Desenvolvimento Social, em cooperação com as Secretarias de Educação, instituir o Programa Nacional de Apoio ao Cuidado, mediante a expansão da rede pública de creches e centros de convivência comunitária — com investimento prioritário em bairros periféricos —, a fim de aliviar a sobrecarga feminina e assegurar a dignidade das famílias. Dessa forma, o país poderá transformar a cidadania de papel em realidade concreta para todas as mulheres.`;

export function EnemEssayCorrector() {
  const [theme, setTheme] = useState(THEME_PRESETS[0]);
  const [customTheme, setCustomTheme] = useState('');
  const [isCustom, setIsCustom] = useState(false);
  const [essayText, setEssayText] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<EssayCorrectionResult | null>(null);
  const [copied, setCopied] = useState(false);
  const [expandedComp, setExpandedComp] = useState<number | null>(null);

  // Estatísticas do texto em digitação
  const words = essayText.match(/\b[A-Za-zÀ-ÿ0-9-]+\b/g) || [];
  const wordCount = words.length;
  const estimatedLines = Math.min(30, Math.max(0, Math.round(wordCount / 12.5)));
  const paragraphsCount = essayText
    .split(/\n\s*\n|\n/)
    .map((p) => p.trim())
    .filter((p) => p.length > 25).length;

  const activeTheme = isCustom ? customTheme.trim() || 'Tema Livre do ENEM' : theme;

  const handleEvaluate = async () => {
    if (wordCount < 40) {
      setError('A redação precisa ter ao menos um parágrafo estruturado (mínimo de 40 palavras) para avaliação oficial.');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const evaluation = await evaluateEssay({
        essayText,
        theme: activeTheme,
      });
      setResult(evaluation);
    } catch (err: any) {
      setError(err?.message || 'Falha ao processar avaliação com a banca. Tente novamente.');
    } finally {
      setLoading(false);
    }
  };

  const handleLoadSample = () => {
    setTheme(THEME_PRESETS[0]);
    setIsCustom(false);
    setEssayText(SAMPLE_ESSAY);
    setError(null);
  };

  const handleCopyReport = () => {
    if (!result) return;
    const report = `CORREÇÃO OFICIAL ENEM • NOTA FINAL: ${result.totalScore} / 1000
Tema: ${result.theme}
Palavras: ${result.wordCount} | Parágrafos: ${result.paragraphCount}

COMPETÊNCIAS:
${result.competencies
  .map((c) => `C${c.number} (${c.name}): ${c.score}/200 - ${c.level}\n→ ${c.feedback}`)
  .join('\n\n')}

PROPOSTA DE INTERVENÇÃO (C5):
- Agente: ${result.c5Checklist.agente.text}
- Ação: ${result.c5Checklist.acao.text}
- Meio/Modo: ${result.c5Checklist.meio.text}
- Efeito/Finalidade: ${result.c5Checklist.efeito.text}
- Detalhamento: ${result.c5Checklist.detalhamento.text}

PARECER DO DR. VIKTOR:
${result.generalVerdict}`;

    navigator.clipboard.writeText(report);
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  };

  const getScoreBadgeClass = (score: number) => {
    if (score >= 900) return 'bg-[var(--text-primary)] text-[var(--bg-primary)] border-[var(--text-primary)]';
    if (score >= 760) return 'bg-[var(--bg-secondary)] text-[var(--text-primary)] border-[var(--border-strong)]';
    return 'bg-[var(--bg-surface)] text-[var(--text-secondary)] border-[var(--border-color)]';
  };

  return (
    <section className="mb-12 border border-[var(--border-strong)] bg-[var(--bg-surface)] rounded-xl p-5 sm:p-7 shadow-sm transition-all">
      {/* Cabeçalho da Ferramenta */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 pb-5 border-b border-[var(--border-color)]">
        <div className="flex items-center gap-3">
          <span className="p-2.5 rounded-lg border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] shadow-sm">
            <ShieldAlert className="w-5 h-5" />
          </span>
          <div>
            <div className="flex items-center gap-2">
              <h2 className="font-serif text-lg sm:text-xl font-bold tracking-tight">
                Banca de Correção Oficial ENEM
              </h2>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded border border-[var(--border-strong)] bg-[var(--bg-secondary)] font-bold">
                Dr. Viktor AI
              </span>
            </div>
            <p className="text-xs text-[var(--text-secondary)] font-sans mt-0.5">
              Avaliação cirúrgica e objetiva de 0 a 1000 pontos segundo os critérios estritos do INEP.
            </p>
          </div>
        </div>

        <button
          onClick={handleLoadSample}
          type="button"
          className="text-xs font-mono px-3 py-1.5 rounded border border-dashed border-[var(--border-strong)] hover:bg-[var(--bg-secondary)] text-[var(--text-secondary)] hover:text-[var(--text-primary)] transition-colors flex items-center gap-1.5 self-end sm:self-auto"
        >
          <FileText className="w-3.5 h-3.5" />
          <span>Carregar Exemplo Real</span>
        </button>
      </div>

      {/* Formulário de Envio */}
      <div className="mt-5 space-y-4">
        {/* Seletor de Tema */}
        <div>
          <div className="flex items-center justify-between mb-1.5">
            <label className="font-mono text-xs font-bold uppercase tracking-wider text-[var(--text-primary)]">
              Proposta Temática:
            </label>
            <button
              onClick={() => setIsCustom(!isCustom)}
              className="text-[11px] font-mono text-[var(--text-muted)] hover:text-[var(--text-primary)] underline"
            >
              {isCustom ? '← Escolher tema histórico' : '✎ Digitar meu próprio tema'}
            </button>
          </div>

          {isCustom ? (
            <input
              type="text"
              value={customTheme}
              onChange={(e) => setCustomTheme(e.target.value)}
              placeholder="Digite a frase-tema completa da redação..."
              className="w-full px-3 py-2 text-xs sm:text-sm font-sans rounded border border-[var(--border-color)] bg-[var(--bg-primary)] text-[var(--text-primary)] focus:outline-none focus:border-[var(--border-strong)]"
            />
          ) : (
            <select
              value={theme}
              onChange={(e) => setTheme(e.target.value)}
              className="w-full px-3 py-2 text-xs sm:text-sm font-sans rounded border border-[var(--border-color)] bg-[var(--bg-primary)] text-[var(--text-primary)] focus:outline-none focus:border-[var(--border-strong)] cursor-pointer"
            >
              {THEME_PRESETS.map((t) => (
                <option key={t} value={t}>
                  {t}
                </option>
              ))}
            </select>
          )}
        </div>

        {/* Campo de Texto da Redação */}
        <div>
          <div className="flex items-center justify-between mb-1.5">
            <label className="font-mono text-xs font-bold uppercase tracking-wider text-[var(--text-primary)]">
              Texto da Redação:
            </label>
            <div className="flex items-center gap-3 text-[11px] font-mono text-[var(--text-muted)]">
              <span>{wordCount} palavras</span>
              <span>•</span>
              <span>~{estimatedLines} linhas {estimatedLines > 30 ? '⚠️ (Excedeu 30)' : ''}</span>
              <span>•</span>
              <span>{paragraphsCount} parágrafos</span>
            </div>
          </div>

          <textarea
            value={essayText}
            onChange={(e) => setEssayText(e.target.value)}
            rows={11}
            placeholder="Cole ou digite sua redação completa aqui (Introdução, D1, D2 e Conclusão com a proposta de intervenção)..."
            className="w-full p-4 font-serif text-sm sm:text-base leading-relaxed rounded border border-[var(--border-color)] bg-[var(--bg-primary)] text-[var(--text-primary)] focus:outline-none focus:border-[var(--border-strong)] transition-all resize-y"
          />

          {error && (
            <div className="mt-2 p-3 rounded bg-red-950/20 border border-red-500/40 text-red-400 text-xs font-sans flex items-center gap-2">
              <AlertTriangle className="w-4 h-4 shrink-0" />
              <span>{error}</span>
            </div>
          )}
        </div>

        {/* Botão de Disparo */}
        <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2">
          <p className="text-[11px] font-mono text-[var(--text-muted)] text-center sm:text-left">
            Correção rigorosa: gramática (C1), repertório (C2), tese (C3), conectivos (C4) e os 5 elementos (C5).
          </p>

          <button
            onClick={handleEvaluate}
            disabled={loading || wordCount < 30}
            className="w-full sm:w-auto px-6 py-2.5 rounded font-mono text-xs font-bold uppercase tracking-wider border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] hover:opacity-90 disabled:opacity-40 transition-all flex items-center justify-center gap-2 shadow-sm"
          >
            {loading ? (
              <>
                <RefreshCw className="w-4 h-4 animate-spin" />
                <span>Dr. Viktor Avaliando Critérios...</span>
              </>
            ) : (
              <>
                <Zap className="w-4 h-4" />
                <span>Avaliar com a Banca (0 a 1000)</span>
              </>
            )}
          </button>
        </div>
      </div>

      {/* Relatório de Avaliação Oficial */}
      {result && (
        <div className="mt-8 pt-8 border-t-2 border-[var(--border-strong)] animate-fade-in space-y-6">
          {/* Card Principal de Nota */}
          <div className="p-5 sm:p-6 rounded-xl border border-[var(--border-strong)] bg-[var(--bg-card)] flex flex-col sm:flex-row items-center justify-between gap-6">
            <div className="text-center sm:text-left">
              <span className="font-mono text-xs uppercase tracking-wider text-[var(--text-muted)] font-bold">
                Nota Final do Candidato
              </span>
              <div className="flex items-baseline justify-center sm:justify-start gap-2 mt-1">
                <span className="font-serif text-5xl sm:text-6xl font-bold tracking-tight">
                  {result.totalScore}
                </span>
                <span className="font-mono text-lg text-[var(--text-muted)] font-semibold">
                  / 1000
                </span>
              </div>
              <p className="font-sans text-xs sm:text-sm text-[var(--text-secondary)] mt-1.5 max-w-md">
                {result.generalVerdict}
              </p>
            </div>

            <div className="flex flex-col items-center sm:items-end gap-2.5 shrink-0">
              <span className={`px-4 py-1.5 rounded-full font-mono text-xs font-bold border ${getScoreBadgeClass(result.totalScore)}`}>
                {result.totalScore >= 900
                  ? '🏆 Faixa 900+ (Excelência ENEM)'
                  : result.totalScore >= 760
                  ? '⚡ Faixa 760–880 (Competitivo)'
                  : '⚠️ Faixa em Desenvolvimento'}
              </span>

              <button
                onClick={handleCopyReport}
                className="text-xs font-mono px-3 py-1.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] text-[var(--text-secondary)] hover:text-[var(--text-primary)] transition-colors flex items-center gap-1.5"
              >
                {copied ? <Check className="w-3.5 h-3.5 text-green-500" /> : <Copy className="w-3.5 h-3.5" />}
                <span>{copied ? 'Copiado para o Clipboard!' : 'Copiar Diagnóstico Completo'}</span>
              </button>
            </div>
          </div>

          {/* Checklist dos 5 Elementos da Proposta de Intervenção (C5) */}
          <div className="p-5 rounded-lg border border-[var(--border-color)] bg-[var(--bg-surface)]">
            <div className="flex items-center justify-between mb-3">
              <h3 className="font-serif text-sm sm:text-base font-bold flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4" />
                <span>Auditoria dos 5 Elementos da Proposta (Competência 5)</span>
              </h3>
              <span className="font-mono text-xs font-bold">
                {result.competencies.find((c) => c.number === 5)?.score || 0} / 200 pts
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-5 gap-2.5">
              {[
                { label: '1. Agente (Quem)', data: result.c5Checklist.agente },
                { label: '2. Ação (O quê)', data: result.c5Checklist.acao },
                { label: '3. Meio (Como)', data: result.c5Checklist.meio },
                { label: '4. Efeito (Para quê)', data: result.c5Checklist.efeito },
                { label: '5. Detalhamento', data: result.c5Checklist.detalhamento },
              ].map((item, i) => (
                <div
                  key={i}
                  className={`p-3 rounded border text-xs font-sans transition-all ${
                    item.data.present
                      ? 'border-[var(--border-strong)] bg-[var(--bg-primary)]'
                      : 'border-red-500/30 bg-red-950/10 text-red-300'
                  }`}
                >
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-mono font-bold text-[11px]">{item.label}</span>
                    {item.data.present ? (
                      <Check className="w-3.5 h-3.5 text-green-500 shrink-0" />
                    ) : (
                      <XCircle className="w-3.5 h-3.5 text-red-500 shrink-0" />
                    )}
                  </div>
                  <p className="text-[11px] text-[var(--text-secondary)] line-clamp-2" title={item.data.text}>
                    {item.data.text}
                  </p>
                </div>
              ))}
            </div>
          </div>

          {/* Desmembramento das 5 Competências */}
          <div>
            <h3 className="font-mono text-xs uppercase tracking-wider font-bold mb-3 text-[var(--text-muted)]">
              Desdobramento por Competência Oficial (INEP):
            </h3>

            <div className="space-y-3">
              {result.competencies.map((comp) => {
                const isExpanded = expandedComp === comp.number;
                return (
                  <div
                    key={comp.number}
                    className="border border-[var(--border-color)] bg-[var(--bg-surface)] rounded-lg overflow-hidden transition-all"
                  >
                    <div
                      onClick={() => setExpandedComp(isExpanded ? null : comp.number)}
                      className="p-4 flex items-center justify-between gap-3 cursor-pointer hover:bg-[var(--bg-secondary)]/50 transition-colors"
                    >
                      <div className="flex items-center gap-3 min-w-0">
                        <span className="font-mono text-xs font-bold px-2 py-0.5 rounded border border-[var(--border-strong)] bg-[var(--bg-secondary)] shrink-0">
                          C{comp.number}
                        </span>
                        <div className="min-w-0">
                          <h4 className="font-serif text-sm font-bold truncate">{comp.name}</h4>
                          <p className="text-xs text-[var(--text-muted)] font-mono">{comp.level}</p>
                        </div>
                      </div>

                      <div className="flex items-center gap-3 shrink-0">
                        <div className="text-right">
                          <span className="font-mono text-sm font-bold">{comp.score}</span>
                          <span className="font-mono text-xs text-[var(--text-muted)]"> / 200</span>
                        </div>
                        {isExpanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                      </div>
                    </div>

                    {/* Barra de Progresso Visual */}
                    <div className="h-1 w-full bg-[var(--border-color)]">
                      <div
                        className="h-full bg-[var(--text-primary)] transition-all duration-500"
                        style={{ width: `${(comp.score / 200) * 100}%` }}
                      />
                    </div>

                    {/* Conteúdo Expandido */}
                    {isExpanded && (
                      <div className="p-4 pt-3 border-t border-[var(--border-color)] bg-[var(--bg-primary)]/40 space-y-3 text-xs font-sans">
                        <p className="text-[var(--text-primary)] leading-relaxed italic">
                          &ldquo;{comp.feedback}&rdquo;
                        </p>

                        {comp.positives && comp.positives.length > 0 && (
                          <div>
                            <span className="font-mono text-[10px] uppercase font-bold text-green-500 block mb-1">
                              ✓ Pontos Fortes Notados pela Banca:
                            </span>
                            <ul className="list-disc list-inside space-y-0.5 text-[var(--text-secondary)]">
                              {comp.positives.map((p, idx) => (
                                <li key={idx}>{p}</li>
                              ))}
                            </ul>
                          </div>
                        )}

                        {comp.deviations && comp.deviations.length > 0 && (
                          <div>
                            <span className="font-mono text-[10px] uppercase font-bold text-red-400 block mb-1">
                              ⚠️ Desvios e Falhas que Custaram Pontos:
                            </span>
                            <ul className="list-disc list-inside space-y-0.5 text-red-300">
                              {comp.deviations.map((d, idx) => (
                                <li key={idx}>{d}</li>
                              ))}
                            </ul>
                          </div>
                        )}

                        {comp.improvement && (
                          <div className="p-3 rounded border border-[var(--border-color)] bg-[var(--bg-secondary)]">
                            <span className="font-mono text-[10px] uppercase font-bold text-[var(--text-primary)] block mb-0.5">
                              🎯 Como Subir para 200 Pontos nesta Competência:
                            </span>
                            <p className="text-[var(--text-secondary)]">{comp.improvement}</p>
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>

          {/* Destaques e Correções Críticas */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <div className="p-4 rounded-lg border border-[var(--border-color)] bg-[var(--bg-surface)]">
              <span className="font-mono text-xs font-bold uppercase tracking-wider text-green-500 flex items-center gap-1.5 mb-2">
                <CheckCircle2 className="w-4 h-4" />
                <span>Pontos Fortes da Redação</span>
              </span>
              <ul className="space-y-1.5 text-xs text-[var(--text-secondary)] font-sans">
                {result.strengths.map((s, idx) => (
                  <li key={idx} className="flex items-start gap-1.5">
                    <span className="text-[var(--text-muted)] font-mono">•</span>
                    <span>{s}</span>
                  </li>
                ))}
              </ul>
            </div>

            <div className="p-4 rounded-lg border border-[var(--border-color)] bg-[var(--bg-surface)]">
              <span className="font-mono text-xs font-bold uppercase tracking-wider text-red-400 flex items-center gap-1.5 mb-2">
                <AlertTriangle className="w-4 h-4" />
                <span>Correções Cirúrgicas Urgentes</span>
              </span>
              <ul className="space-y-1.5 text-xs text-red-300 font-sans">
                {result.criticalCorrections.map((c, idx) => (
                  <li key={idx} className="flex items-start gap-1.5">
                    <span className="font-mono text-red-400">!</span>
                    <span>{c}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
