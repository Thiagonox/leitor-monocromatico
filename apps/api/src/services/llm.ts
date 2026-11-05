import fs from 'fs';
import path from 'path';
import { CONFIG } from '../config.js';
import { BookDoc } from '@mono-reader/shared';

interface ChatMessage {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export async function callOpenRouterLlm(
  messages: ChatMessage[],
  maxTokens: number = 4500,
  temperature: number = 0.55,
  timeoutMs: number = 20000
): Promise<{ text: string | null; model: string | null; error: string | null }> {
  for (const modelName of CONFIG.OPENROUTER_TEXT_MODELS) {
    try {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), timeoutMs);

      const resp = await fetch('https://openrouter.ai/api/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${CONFIG.DEFAULT_HEYGEN_API_KEY}`,
          'HTTP-Referer': 'https://leitor-monocromatico.local',
          'X-Title': 'Leitor Monocromatico Next'
        },
        body: JSON.stringify({
          model: modelName,
          messages,
          max_tokens: maxTokens,
          temperature,
          reasoning: { max_tokens: 0 }
        }),
        signal: controller.signal
      });

      clearTimeout(timeout);

      if (resp.ok) {
        const data = await resp.json() as any;
        const text = data?.choices?.[0]?.message?.content;
        if (text && text.trim().length > 0) {
          return { text: text.trim(), model: modelName, error: null };
        }
      }
    } catch (err: any) {
      // try next model
    }
  }
  return { text: null, model: null, error: 'Falha em todos os modelos OpenRouter' };
}

export async function callNvidiaLlm(
  messages: ChatMessage[],
  apiKey: string = CONFIG.DEFAULT_NVIDIA_API_KEY,
  model: string = CONFIG.DEFAULT_MODEL,
  baseUrl: string = CONFIG.DEFAULT_BASE_URL,
  maxTokens: number = 3000,
  temperature: number = 0.4
): Promise<{ text: string | null; model: string; error: string | null }> {
  try {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 22000);

    const resp = await fetch(`${baseUrl.replace(/\/+$/, '')}/chat/completions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model,
        messages,
        max_tokens: maxTokens,
        temperature,
        stream: false
      }),
      signal: controller.signal
    });

    clearTimeout(timeout);

    if (resp.ok) {
      const data = await resp.json() as any;
      const text = data?.choices?.[0]?.message?.content;
      if (text) {
        return { text: text.trim(), model, error: null };
      }
    }
    return { text: null, model, error: `Status ${resp.status}` };
  } catch (err: any) {
    return { text: null, model, error: err.message || 'Erro de conexão' };
  }
}

export function getMasterRedacaoBook(): BookDoc | null {
  try {
    const filePath = path.join(CONFIG.DATA_DIR, 'redacao-enem.json');
    if (fs.existsSync(filePath)) {
      const raw = fs.readFileSync(filePath, 'utf-8');
      return JSON.parse(raw);
    }
  } catch (e) {
    console.error('Erro ao ler redacao-enem.json:', e);
  }
  return null;
}

export function generateLayeredFallbackPayload(
  topic: string,
  depth: string = 'enem_elite',
  chaptersCount: number = 3
): BookDoc {
  const cleanTopic = topic.replace(/\[\[|\]\]/g, '').trim();
  const lower = cleanTopic.toLowerCase();

  // Se o tema for sobre redação / enem / dissertativo, retorna a obra mestra oficial
  if (
    lower.includes('redação') ||
    lower.includes('redacao') ||
    lower.includes('dissertativo') ||
    lower.includes('enem') ||
    lower.includes('competências') ||
    lower.includes('competencias') ||
    lower.includes('repertório') ||
    lower.includes('repertorio')
  ) {
    const master = getMasterRedacaoBook();
    if (master) return master;
  }

  const rawLines = cleanTopic
    .split(/\r?\n/)
    .map(l => l.replace(/^[-•*\s]+/, '').trim())
    .filter(Boolean);

  const mainTitle = rawLines[0] || cleanTopic.slice(0, 65);
  let subItems = rawLines.slice(1).filter(l => l.length > 2).slice(0, 10);
  if (!subItems.length) {
    subItems = [
      `Conceito central e visão geral de ${mainTitle}`,
      `Como ${mainTitle} funciona na prática e causas principais`,
      `Exemplos reais e aplicações diretas de ${mainTitle}`,
      `Como utilizar esse conhecimento em provas e redações`
    ];
  }

  const progressiveSections = subItems.flatMap((item, idx) => [
    { type: 'heading' as const, level: 3, content: `Bloco ${idx + 1}: ${item}` },
    {
      type: 'paragraph' as const,
      content: `• O CONCEITO: ${item} representa um dos pontos essenciais para compreender ${mainTitle} sem confusão. Em linguagem direta, trata-se de identificar o mecanismo fundamental que explica por que esse fenômeno acontece.\n• O EXEMPLO: Na prática, você identifica ${item} ao comparar uma explicação superficial com uma análise embasada em causas e impactos reais.\n• A APLICAÇÃO: Ao estudar ou responder questões sobre ${item}, questione sempre: qual é o fundamento central, qual é a consequência prática e como conectar esse ponto com clareza.`
    }
  ]);

  const deepSections = subItems.flatMap((item, idx) => [
    { type: 'heading' as const, level: 3, content: `${idx + 1}. Aprofundamento Completo: ${item}` },
    {
      type: 'paragraph' as const,
      content: `Após compreender a visão panorâmica e os blocos de Conceito, Exemplo e Aplicação, avançamos para o domínio aprofundado de ${item}. Dentro do estudo de ${mainTitle}, este ponto conecta a teoria aos desafios reais, permitindo raciocinar com segurança, fundamentar argumentos e evitar simplificações equivocadas.`
    }
  ]);

  return {
    _isFallback: true,
    meta: {
      id: `obra-${Date.now()}`,
      title: `Guia Didático e Progressivo: ${mainTitle.slice(0, 65)}`,
      subtitle: "Guia Prático em Camadas & Progressive Disclosure",
      author: "Manual Vivo · Leitura em Camadas",
      date: new Date().getFullYear().toString(),
      category: "Leitura em Camadas & Progressive Disclosure",
      chaptersCount: 3,
      estimatedReadingTime: "Leitura Didática Completa",
      description: `Estudo estruturado em camadas progressivas sobre ${mainTitle}, revelando cada tópico em pequenas partes (Conceito, Exemplo e Aplicação) até o texto completo.`,
      isGeneratedByAI: true,
      createdAt: new Date().toISOString()
    },
    settings: { defaultFont: "serif", defaultTheme: "eink", defaultWidth: "680px" },
    chapters: [
      {
        id: "capitulo-1",
        number: "I",
        title: "Camada 1 — Resumo Rápido: Visão Geral Direta",
        epigraph: {
          text: "Comece pelo mapa simples: compreender o panorama essencial elimina a resistência inicial da leitura.",
          author: "Leitura em Camadas (Layered Reading)"
        },
        sections: [
          { type: "heading", level: 3, content: `1. O Que Você Precisa Saber de Imediato sobre ${mainTitle}` },
          {
            type: "paragraph",
            content: `Esta primeira camada oferece a visão panorâmica essencial de ${mainTitle} antes de entrarmos nos detalhes. Em vez de encarar um texto denso de uma vez, veja os pontos essenciais que formam a espinha dorsal deste tema:`
          },
          {
            type: "callout",
            title: "Roteiro Rápido dos Pontos Principais",
            content: subItems.map(it => `• ${it}`).join('\n')
          }
        ]
      },
      {
        id: "capitulo-2",
        number: "II",
        title: "Camada 2 — Versão Intermediária: Conceito, Exemplo e Aplicação",
        epigraph: {
          text: "Um conceito. Um exemplo. Uma aplicação. Depois o próximo conceito.",
          author: "Progressive Disclosure"
        },
        sections: progressiveSections
      },
      {
        id: "capitulo-3",
        number: "III",
        title: "Camada 3 — Texto Completo: Domínio Aprofundado e Integrado",
        epigraph: {
          text: "Com a base construída em blocos curtos, o texto completo torna-se leve, claro e natural.",
          author: "Leitura Profunda"
        },
        sections: deepSections
      }
    ]
  };
}
