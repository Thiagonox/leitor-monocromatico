import { Router, Request, Response } from 'express';
import {
  callOpenRouterLlm,
  callNvidiaLlm,
  generateLayeredFallbackPayload,
  getMasterRedacaoBook
} from '../services/llm.js';
import { evaluateEssayWithAi } from '../services/essayEvaluator.js';
import { BookDoc, Chapter, AGENT_PERSONAS, AgentId } from '@mono-reader/shared';

export const aiRouter = Router();

aiRouter.post('/generate-layered', async (req: Request, res: Response) => {
  const { topic, depth = 'enem_elite', chaptersCount = 3, agentId = 'professor', apiKey, model, baseUrl } = req.body;

  if (!topic || typeof topic !== 'string' || !topic.trim()) {
    return res.status(400).json({ status: 'error', message: "O campo 'topic' é obrigatório." });
  }

  const cleanTopic = topic.replace(/\[\[|\]\]/g, '').trim();
  const lower = cleanTopic.toLowerCase();
  const validAgentId: AgentId = (agentId in AGENT_PERSONAS) ? (agentId as AgentId) : 'professor';
  const agent = AGENT_PERSONAS[validAgentId];

  // Se for o tema mestre padrão sem agente específico e sem personalização customizada, entrega o acervo oficial
  if (
    agentId === 'professor' && (
      lower === 'redação' ||
      lower === 'redacao' ||
      lower === 'redação enem' ||
      lower === 'redacao enem' ||
      lower.includes('manual vivo de redação')
    )
  ) {
    const master = getMasterRedacaoBook();
    if (master) {
      return res.json({
        status: 'ok',
        model: 'Manual Vivo Oficial (Redação ENEM Nota 1000)',
        book: master,
        usedFallback: false
      });
    }
  }

  const systemPrompt = `${agent.systemPrompt}
Sua missão agora é gerar um livro de estudo completo, bem feito e estruturado em LEITURA EM CAMADAS (Layered Reading) e PROGRESSIVE DISCLOSURE sobre o tema solicitado.
Mantenha rigorosamente sua personalidade como ${agent.name} (${agent.role}) em todos os títulos, callouts, exemplos e epígrafes da obra!

ESTRATÉGIAS PEDAGÓGICAS OBRIGATÓRIAS:
1. LEITURA EM CAMADAS:
   - Capítulo I: Camada 1 — Resumo Rápido: Panorama direto e cristalino sob sua ótica para reduzir a resistência inicial.
   - Capítulo II: Camada 2 — Versão Intermediária com PROGRESSIVE DISCLOSURE.
   - Capítulo III (e seguintes): Camada 3 — Texto Completo e Aprofundado: Explicação completa no seu estilo inconfundível.
2. PROGRESSIVE DISCLOSURE:
   - Revele cada subtópico em partes fáceis de assimilar: O Conceito → O Exemplo Concreto → A Aplicação Prática.
REGRAS CRÍTICAS:
- NUNCA inclua contagem ou menção de minutos em títulos, subtítulos ou capítulos (ex: NUNCA escreva '(2 a 5 min)').
- Responda APENAS com um objeto JSON válido, sem markdown antes ou depois.`;

  const userPrompt = `Gere uma obra completa em JSON escrita por ${agent.name} sobre o tema/pauta abaixo:

${cleanTopic}

Use exatamente esta estrutura JSON (NUNCA inclua contagem de minutos em títulos ou subtítulos):
{
  "title": "Título Claro e Didático no Estilo de ${agent.name}",
  "subtitle": "${agent.tagline}",
  "category": "Estudo Estratégico",
  "description": "Resumo claro de 2 frases sobre o que o leitor vai dominar.",
  "chapters": [
    {
      "number": "I",
      "title": "Camada 1 — Visão Panorâmica: O Essencial em Poucos Minutos",
      "epigraph": {"text": "Frase de efeito marcante no tom de ${agent.name}.", "author": "${agent.name}"},
      "sections": [
        {"type": "heading", "level": 3, "content": "1. O Ponto de Partida"},
        {"type": "paragraph", "content": "Explicação fluida no seu tom característico..."},
        {"type": "callout", "title": "Sacada Central", "content": "Destaque prático fundamental..."}
      ]
    },
    {
      "number": "II",
      "title": "Camada 2 — Passo a Passo: Conceito, Exemplo e Aplicação",
      "epigraph": {"text": "A teoria só tem valor quando vira resultado.", "author": "${agent.name}"},
      "sections": [
        {"type": "heading", "level": 3, "content": "Bloco 1: [Primeiro Fundamento]"},
        {"type": "paragraph", "content": "O CONCEITO: explicação direta. O EXEMPLO: caso prático. A APLICAÇÃO: como usar."},
        {"type": "callout", "title": "Regra de Ouro", "content": "Checklist de aplicação imediata..."}
      ]
    },
    {
      "number": "III",
      "title": "Camada 3 — Domínio Completo: Imersão Aprofundada",
      "epigraph": {"text": "A excelência é a repetição consciente do método certo.", "author": "${agent.name}"},
      "sections": [
        {"type": "heading", "level": 3, "content": "1. O Aprofundamento Definitivo"},
        {"type": "paragraph", "content": "Desenvolvimento completo, detalhado e conversado de todos os pontos..."}
      ]
    }
  ]
}`;

  let parsedBook: any = null;
  let usedModel = "Motor Editorial em Camadas";

  try {
    const { text, model: outModel } = await callOpenRouterLlm(
      [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt }
      ],
      5000,
      0.5,
      20000
    );

    if (text) {
      let cleaned = text.trim();
      if (cleaned.startsWith('```')) {
        cleaned = cleaned.replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '');
      }
      const sIdx = cleaned.indexOf('{');
      const eIdx = cleaned.lastIndexOf('}');
      if (sIdx !== -1 && eIdx !== -1) {
        cleaned = cleaned.slice(sIdx, eIdx + 1);
      }
      const rawObj = JSON.parse(cleaned);
      if (Array.isArray(rawObj.chapters) && rawObj.chapters.length >= 2) {
        parsedBook = rawObj;
        usedModel = outModel || 'OpenRouter';
      }
    }
  } catch (err) {
    console.warn('Erro ao chamar ou validar JSON da IA:', err);
  }

  if (!parsedBook) {
    parsedBook = generateLayeredFallbackPayload(cleanTopic, depth, Number(chaptersCount));
  }

  const bookId = `obra-${Date.now()}`;
  const roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"];

  const chapters: Chapter[] = (parsedBook.chapters || []).map((ch: any, i: number) => ({
    id: `capitulo-${i + 1}`,
    number: ch.number || roman[i] || `${i + 1}`,
    title: ch.title || `Capítulo ${i + 1}`,
    epigraph: ch.epigraph || { text: "Do resumo rápido ao texto completo, um conceito por vez.", author: "Leitura em Camadas" },
    sections: ch.sections || []
  }));

  const formattedBook: BookDoc = {
    meta: {
      id: bookId,
      title: parsedBook.title || cleanTopic.slice(0, 60),
      subtitle: parsedBook.subtitle || agent.tagline,
      author: agent.authorLabel,
      date: new Date().getFullYear().toString(),
      category: parsedBook.category || "Leitura em Camadas & Progressive Disclosure",
      chaptersCount: chapters.length,
      estimatedReadingTime: parsedBook.estimatedReadingTime || `Aprox. ${chapters.length * 8} min de leitura`,
      description: parsedBook.description || `Obra estruturada por ${agent.name} (${agent.role}): ${agent.description}`,
      isGeneratedByAI: true,
      createdAt: new Date().toISOString()
    },
    settings: { defaultFont: "serif", defaultTheme: "eink", defaultWidth: "680px" },
    chapters,
    quiz: parsedBook.quiz || []
  };

  return res.json({
    status: 'ok',
    book: formattedBook,
    model: usedModel,
    usedFallback: !!parsedBook._isFallback
  });
});

// Endpoint de Chat Conversacional com Agentes Especializados (Prof. Elias, Lucas "Hack", Lia, Dr. Viktor)
aiRouter.post('/chat', async (req: Request, res: Response) => {
  const {
    messages = [],
    agentId = 'professor',
    topic = '',
    contextText = '',
    apiKey,
    model,
  } = req.body;

  const validAgentId: AgentId = (agentId in AGENT_PERSONAS) ? (agentId as AgentId) : 'professor';
  const agent = AGENT_PERSONAS[validAgentId];

  let systemPrompt = agent.systemPrompt;
  if (topic || contextText) {
    systemPrompt += `\n\nCONTEXTO DE LEITURA ATUAL:\n`;
    if (topic) systemPrompt += `- Tópico/Conceito em foco: "${topic}"\n`;
    if (contextText) systemPrompt += `- Trecho do texto que o usuário está lendo: "${contextText.slice(0, 800)}"\n`;
    systemPrompt += `Responda mantendo rigorosamente sua personalidade como ${agent.name} (${agent.role}), fazendo referência ao contexto de leitura quando apropriado.`;
  }

  const formattedMessages: { role: 'system' | 'user' | 'assistant'; content: string }[] = [
    { role: 'system', content: systemPrompt },
    ...messages
      .map((m: any) => ({
        role: m.role === 'assistant' ? 'assistant' : 'user',
        content: String(m.content || ''),
      }))
      .slice(-10),
  ];

  try {
    const { text, model: outModel } = await callOpenRouterLlm(formattedMessages, 2500, 0.7, 18000);
    if (text) {
      return res.json({
        status: 'ok',
        message: { role: 'assistant', content: text },
        agent: {
          id: agent.id,
          name: agent.name,
          role: agent.role,
          badge: agent.badge,
        },
        model: outModel || 'OpenRouter',
      });
    }
  } catch (e) {}

  try {
    const { text, model: outModel } = await callNvidiaLlm(formattedMessages, apiKey, model);
    if (text) {
      return res.json({
        status: 'ok',
        message: { role: 'assistant', content: text },
        agent: {
          id: agent.id,
          name: agent.name,
          role: agent.role,
          badge: agent.badge,
        },
        model: outModel || 'Nvidia',
      });
    }
  } catch (e) {}

  // Fallback baseado na persona do agente
  let fallbackText = '';
  if (validAgentId === 'curseiro') {
    fallbackText = `Fala mestre! Pega a visão sobre "${topic || 'este ponto'}":\n\n1. **O Pulo do Gato:** Em vez de perder tempo com teoria vazia, grava isto: a banca quer palavras-chave explícitas e causa-consequência.\n2. **Template Pronto:** *"Diante disso, nota-se que [fato], o que gera [impacto direto], evidenciando [tese].*\n3. **Armadilha:** Não inventa palavras rebuscadas se você não domina a regência. Clareza direta é nota 1000!`;
  } else if (validAgentId === 'simplificador') {
    fallbackText = `Pensa nisso como se estivéssemos tomando um café:\n\nImagina que "${topic || 'este tema'}" é como organizar as compras na geladeira. Você não joga o queijo em cima dos ovos. Quando você separa causa e efeito, o assunto fica natural e fácil de entender.\n\nViu só? Ficou bem mais leve!`;
  } else if (validAgentId === 'corretor') {
    fallbackText = `Atenção cirúrgica ao critério da banca sobre "${topic || 'este ponto'}":\n\nO erro mais comum aqui é o tangenciamento: falar do assunto de forma genérica sem atacar o recorte específico.\n\n- **Onde o candidato perde pontos:** Afirmações vazias sem comprovação documental ou nexo causal.\n- **Como blindar sua nota:** Nomeie o agente social, a ação concreta e o efeito prático.`;
  } else {
    fallbackText = `Como observamos no rigor conceitual pelo Prof. Elias:\n\nAo examinar "${topic || 'este conceito'}", devemos observar as relações de causa material e efeito estrutural. Em vez de aceitar o conceito isoladamente, compreenda-o como parte de um paradigma mais amplo.\n\nNas avaliações de excelência, a articulação coerente entre a premissa e a evidência concreta é o que distingue uma argumentação ordinária de uma exposição magistral.`;
  }

  return res.json({
    status: 'ok',
    message: { role: 'assistant', content: fallbackText },
    agent: {
      id: agent.id,
      name: agent.name,
      role: agent.role,
      badge: agent.badge,
    },
    model: 'Motor de Persona Fallback',
  });
});

aiRouter.post('/evaluate-essay', async (req: Request, res: Response) => {
  const { essayText, theme = '', apiKey, model } = req.body;

  if (!essayText || typeof essayText !== 'string' || !essayText.trim()) {
    return res.status(400).json({
      status: 'error',
      message: 'O texto da redação é obrigatório para avaliação da banca.',
    });
  }

  try {
    const evaluation = await evaluateEssayWithAi(essayText, theme, apiKey, model);
    return res.json({
      status: 'ok',
      evaluation,
    });
  } catch (err: any) {
    return res.status(500).json({
      status: 'error',
      message: err?.message || 'Falha ao avaliar a redação.',
    });
  }
});

aiRouter.post('/deepen', async (req: Request, res: Response) => {
  const { topic, contextText = '', agentId = 'professor', style = 'didatico', level = 1, apiKey, model } = req.body;

  if (!topic) {
    return res.status(400).json({ status: 'error', message: "O campo 'topic' é obrigatório." });
  }

  const validAgentId: AgentId = (agentId in AGENT_PERSONAS) ? (agentId as AgentId) : 'professor';
  const agent = AGENT_PERSONAS[validAgentId];

  const prompt = `Aprofunde o seguinte conceito no contexto da leitura atual:
Conceito: "${topic}"
Contexto atual: "${contextText.slice(0, 500)}"

Mantenha sua identidade inconfundível como ${agent.name} (${agent.role}, ${agent.badge}).
Estruture sua explicação conforme sua metodologia e tom característico.`;

  const messages: { role: 'system' | 'user' | 'assistant'; content: string }[] = [
    { role: 'system', content: agent.systemPrompt },
    { role: 'user', content: prompt }
  ];

  try {
    const { text, model: outModel } = await callOpenRouterLlm(messages, 2500, 0.7, 18000);
    if (text) {
      return res.json({
        status: 'ok',
        content: text,
        agent: { id: agent.id, name: agent.name, role: agent.role, badge: agent.badge },
        model: outModel
      });
    }
  } catch (e) {}

  const { text, error } = await callNvidiaLlm(messages, apiKey, model);
  if (text) {
    return res.json({
      status: 'ok',
      content: text,
      agent: { id: agent.id, name: agent.name, role: agent.role, badge: agent.badge },
      model
    });
  }

  // Fallback de persona
  let fallback = '';
  if (validAgentId === 'curseiro') {
    fallback = `### ${topic} — O Macete do Curseiro\n\n**O Pulo do Gato:** Em vez de perder horas decorando teorias, foca nisto: se a prova pedir ${topic}, você joga o conceito de causa e efeito imediato.\n\n**Template Aplicável:** *"Diante da problemática de ${topic}, verifica-se um quadro de inação institucional, demandando intervenção imediata."*\n\n**Não Caia Nessa:** Nunca use ${topic} sem articular com o tema principal.`;
  } else if (validAgentId === 'simplificador') {
    fallback = `### ${topic} — Descomplicando Sem Mistério\n\n**Pensa comigo:** Imagina que ${topic} é como o motor de um carro. Se a gasolina não chega na quantidade certa, o carro engasga.\n\n**O que significa na prática:** É simplesmente a engrenagem que conecta o problema ao seu resultado. Simples assim, sem jargão enrolado!`;
  } else if (validAgentId === 'corretor') {
    fallback = `### ${topic} — O Diagnóstico da Banca\n\n**Raio-X:** O conceito de ${topic} é avaliado sob a ótica da consistência e não do volume de palavras.\n\n**Falha Comum:** Citar autores sem explicar como eles se relacionam com ${topic}.\n\n**Como Blindar:** Justifique cada adjetivo atribuído a ${topic} com um fato concreto.`;
  } else {
    fallback = `### ${topic} — Fundamentação pelo Prof. Elias\n\n**Definição Essencial:** Este conceito representa um ponto nodal na compreensão profunda do tema. Em linguagem direta, estabelece as relações entre causas materiais e impactos práticos.\n\n**Mecanismo Lógico:** Ao analisar criticamente, percebe-se que as premissas deste conceito conectam a teoria à realidade sem recorrer a fórmulas decoradas.\n\n**Aplicação Prática:** Em avaliações e redações, utilize este conceito como evidência sólida para sustentar argumentos sem cometer generalizações indevidas.`;
  }

  return res.json({
    status: 'ok',
    content: fallback,
    agent: { id: agent.id, name: agent.name, role: agent.role, badge: agent.badge },
    model: 'Motor Didático Fallback'
  });
});

// Endpoint de Continuidade de Leitura (Scroll Infinito Contínuo sem Paginação)
aiRouter.post('/continue-stream', async (req: Request, res: Response) => {
  const {
    bookTitle = 'Estudo Aprofundado',
    bookSubtitle = '',
    previousContext = '',
    continuationStep = 1,
    agentId = 'professor',
    apiKey,
    model,
  } = req.body;

  const validAgentId: AgentId = (agentId in AGENT_PERSONAS) ? (agentId as AgentId) : 'professor';
  const agent = AGENT_PERSONAS[validAgentId];
  const stepNum = Math.max(1, Number(continuationStep) || 1);

  const angles = [
    'Estudos de Caso Reais, Repertório Sociocultural e Exemplos Concretos de Alta Nota',
    'Erros Invisíveis, Distratores Clássicos e Como Blindar Cada Argumento na Prática',
    'Conexões Interdisciplinares: Filosofia, Sociologia, Direito Constitucional e Atualidades',
    'Engenharia Sintática, Coesão Referencial, Operadores Argumentativos e Fluidez Textual',
    'Simulação Prática Comentada: Do Rascunho Bruto à Versão Lapidada Nota 1000',
    'Fronteiras Avançadas do Tema: Dilemas Contemporâneos e Impactos Estruturais',
  ];
  const currentAngle = angles[(stepNum - 1) % angles.length];

  const systemPrompt = `${agent.systemPrompt}
Você está escrevendo a continuação fluida de um fluxo de leitura infinito (sem paginação e sem cortes) da obra "${bookTitle}".
Mantenha total continuidade com o que já foi lido, explorando agora o eixo: "${currentAngle}".
Responda APENAS com um objeto JSON válido contendo um array "sections" com 5 a 6 novos blocos editoriais (heading, paragraph, callout, quote).`;

  const userPrompt = `Continue o fluxo contínuo da obra "${bookTitle}" (${bookSubtitle}).
Trecho imediatamente anterior:
"${String(previousContext).slice(-600)}"

Eixo de aprofundamento desta sequência (#${stepNum}): ${currentAngle}.

Retorne APENAS um JSON válido neste formato exato:
{
  "sections": [
    {"type": "heading", "level": 2, "content": "Subtítulo instigante dando sequência natural ao texto"},
    {"type": "paragraph", "content": "Parágrafo denso, fluido e didático conectando o ponto anterior ao novo ângulo..."},
    {"type": "paragraph", "content": "Segundo parágrafo com exemplo concreto, aplicação real ou análise detalhada..."},
    {"type": "callout", "title": "Síntese Estratégica", "content": "Ponto-chave prático para aplicação imediata..."},
    {"type": "quote", "content": "Reflexão ou citação pertinente ao argumento desenvolvido.", "author": "Referência Clássica / ${agent.name}"},
    {"type": "paragraph", "content": "Parágrafo de transição mantendo o ritmo contínuo da leitura..."}
  ]
}`;

  try {
    const { text, model: outModel } = await callOpenRouterLlm(
      [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt },
      ],
      2800,
      0.65,
      16000
    );

    if (text) {
      let cleaned = text.trim();
      if (cleaned.startsWith('```')) {
        cleaned = cleaned.replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '');
      }
      const sIdx = cleaned.indexOf('{');
      const eIdx = cleaned.lastIndexOf('}');
      if (sIdx !== -1 && eIdx !== -1) {
        cleaned = cleaned.slice(sIdx, eIdx + 1);
      }
      const parsed = JSON.parse(cleaned);
      if (Array.isArray(parsed.sections) && parsed.sections.length >= 2) {
        return res.json({
          status: 'ok',
          sections: parsed.sections,
          model: outModel || 'OpenRouter',
        });
      }
    }
  } catch (e) {
    console.warn('[Continue Stream OpenRouter Warn]:', e);
  }

  try {
    const { text, model: outModel } = await callNvidiaLlm(
      [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt },
      ],
      apiKey,
      model
    );
    if (text) {
      const sIdx = text.indexOf('{');
      const eIdx = text.lastIndexOf('}');
      if (sIdx !== -1 && eIdx !== -1) {
        const parsed = JSON.parse(text.slice(sIdx, eIdx + 1));
        if (Array.isArray(parsed.sections) && parsed.sections.length >= 2) {
          return res.json({
            status: 'ok',
            sections: parsed.sections,
            model: outModel || 'Nvidia',
          });
        }
      }
    }
  } catch (e) {}

  // Continuação Determinística Contextual Rica (garante que o scroll infinito nunca pare)
  const fallbackSections = [
    {
      type: 'heading',
      level: 2,
      content: `${currentAngle}`,
    },
    {
      type: 'paragraph',
      content: `Avançando organicamente na análise de ${bookTitle}, é indispensável observar como a teoria se materializa quando submetida a situações reais de pressão argumentativa. Não basta enunciar uma premissa; a maturidade intelectual exige que cada afirmação seja sustentada por um mecanismo causal explícito — demonstrando por que o fenômeno ocorre, quais forças institucionais o alimentam e quais consequências concretas dele decorrem.`,
    },
    {
      type: 'paragraph',
      content: `Sob a ótica de ${agent.name}, a diferença entre uma leitura superficial e o domínio completo de ${bookTitle} reside na capacidade de conectar conceitos abstratos a fatos observáveis. Quando você articula repertório legítimo com precisão vocabular, o texto deixa de ser uma sequência de opiniões e passa a operar como uma demonstração lógica irrefutável.`,
    },
    {
      type: 'callout',
      title: `Diretriz de Continuidade · Sequência #${stepNum}`,
      content: `Ao aplicar este eixo (${currentAngle}), verifique sempre três pilares: 1) A clareza do recorte temático; 2) A pertinência produtiva do repertório mobilizado; 3) O encadeamento fluido entre a causa diagnosticada e a intervenção proposta.`,
    },
    {
      type: 'quote',
      content: `A clareza não é o ornamento do pensamento, mas a própria prova de que o conceito foi compreendido até a sua raiz.`,
      author: agent.authorLabel,
    },
    {
      type: 'paragraph',
      content: `Prosseguindo nessa linha de raciocínio, observe nos parágrafos seguintes como cada camada de aprofundamento amplia seu repertório ativo sem quebrar a cadência da leitura contínua.`,
    },
  ];

  return res.json({
    status: 'ok',
    sections: fallbackSections,
    model: 'Motor de Fluxo Infinito Contínuo',
  });
});

import {
  getAudioCacheKey,
  isAudioInBucket,
  saveAudioToBucket,
  getAudioFromBucket,
  synthesizeHeyGenAudio,
} from '../services/tts.js';
import path from 'path';

const inflightTtsJobs = new Map<string, Promise<{ cached: boolean; model: string }>>();

aiRouter.post('/tts', async (req: Request, res: Response) => {
  const {
    text,
    voice = 'nadine',
    chapterId,
    apiKey,
  } = req.body;

  if (!text) {
    return res.status(400).json({ status: 'error', message: "O campo 'text' é obrigatório." });
  }

  try {
    const cacheKey = getAudioCacheKey(text, voice, chapterId);
    let job = inflightTtsJobs.get(cacheKey);

    if (!job) {
      job = (async () => {
        const cached = await isAudioInBucket(cacheKey);
        if (cached) {
          console.log(`[Railway Bucket HIT] Áudio HeyGen encontrado no Bucket: ${cacheKey}.wav`);
          return { cached: true, model: 'heygen/heygen-voice-1-turbo:free' };
        }

        console.log(`[Railway Bucket MISS] Gerando áudio exclusivamente com heygen/heygen-voice-1-turbo:free (voz: ${voice})...`);
        const { audioBuffer, model } = await synthesizeHeyGenAudio(text, voice, apiKey);
        await saveAudioToBucket(cacheKey, audioBuffer);
        return { cached: false, model };
      })().finally(() => {
        inflightTtsJobs.delete(cacheKey);
      });
      inflightTtsJobs.set(cacheKey, job);
    }

    const result = await job;

    return res.json({
      status: 'ok',
      cached: result.cached,
      cacheKey,
      audioUrl: `/api/ai/audio/${cacheKey}.wav`,
      model: result.model,
      voice,
    });
  } catch (err: any) {
    console.error('[HeyGen TTS Error]', err.message);
    return res.status(502).json({
      status: 'error',
      model: 'heygen/heygen-voice-1-turbo:free',
      message: err?.message || String(err),
    });
  }
});

// Endpoint que serve o áudio direto do Bucket S3 com streaming e HTTP Range (pause, seek, scrubber)
aiRouter.get('/audio/:filename', async (req: Request, res: Response) => {
  const rawFilename = req.params.filename;
  const filenameStr = Array.isArray(rawFilename) ? rawFilename[0] : (rawFilename || '');
  const sanitized = path.basename(filenameStr);
  const range = req.headers.range;

  const result = await getAudioFromBucket(sanitized, range);

  if (!result) {
    return res.status(404).json({ status: 'error', message: 'Áudio não encontrado no Bucket Railway.' });
  }

  const headers: Record<string, any> = {
    'Content-Type': result.contentType,
    'Accept-Ranges': 'bytes',
    'Cache-Control': 'public, max-age=31536000, immutable',
  };

  if (result.contentLength !== undefined) {
    headers['Content-Length'] = result.contentLength;
  }
  if (result.contentRange) {
    headers['Content-Range'] = result.contentRange;
  }

  res.writeHead(result.status, headers);
  result.stream.pipe(res);
});
