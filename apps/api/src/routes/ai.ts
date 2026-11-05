import { Router, Request, Response } from 'express';
import {
  callOpenRouterLlm,
  callNvidiaLlm,
  generateLayeredFallbackPayload,
  getMasterRedacaoBook
} from '../services/llm.js';
import { BookDoc, Chapter } from '@mono-reader/shared';

export const aiRouter = Router();

aiRouter.post('/generate-layered', async (req: Request, res: Response) => {
  const { topic, depth = 'enem_elite', chaptersCount = 3, apiKey, model, baseUrl } = req.body;

  if (!topic || typeof topic !== 'string' || !topic.trim()) {
    return res.status(400).json({ status: 'error', message: "O campo 'topic' é obrigatório." });
  }

  const cleanTopic = topic.replace(/\[\[|\]\]/g, '').trim();
  const lower = cleanTopic.toLowerCase();

  // Se for o tema prioritário de redação / dissertativo / enem, entrega o acervo mestre oficial
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
    if (master) {
      return res.json({
        status: 'ok',
        model: 'Manual Vivo Oficial (Redação ENEM Nota 1000)',
        book: master,
        usedFallback: false
      });
    }
  }

  const systemPrompt = `Você é um professor e autor didático de excelência (no mesmo estilo claro, fluido e direto do 'Manual Vivo de Interpretação'). 
Sua missão é gerar um livro de estudo completo, bem feito e FÁCIL DE DIGERIR para o leitor padrão, usando EXCLUSIVAMENTE estas duas estratégias pedagógicas:
1. LEITURA EM CAMADAS (Layered Reading):
   - Capítulo I: Camada 1 — Resumo Rápido: Panorama direto, simples e cristalino de todo o tema para reduzir a resistência inicial.
   - Capítulo II: Camada 2 — Versão Intermediária com PROGRESSIVE DISCLOSURE.
   - Capítulo III (e seguintes): Camada 3 — Texto Completo e Aprofundado: Explicação completa, conversada, detalhada e fluida de todos os pontos pedidos pelo usuário.
2. PROGRESSIVE DISCLOSURE (Revelação Progressiva):
   - Em vez de blocos pesados ou jargão acadêmico artificial, revele cada subtópico em pequenas partes fáceis de digerir seguindo SEMPRE a sequência:
     • O Conceito (o que é, de forma simples e direta)
     • O Exemplo (um caso concreto ou modelo prático real)
     • A Aplicação (como usar na prática, na redação ou na prova)
     • Depois o próximo conceito.
REGRAS CRÍTICAS DE ESTILO:
- NUNCA inclua contagem ou menção de minutos em títulos, subtítulos ou capítulos (ex: NUNCA escreva '(2 a 5 min)', '(10 a 15 min)', '2 min (Resumo)', etc.). Use títulos limpos, elegantes e didáticos.
- PROIBIDO usar títulos rebuscados vazios como 'Gênese, Premissas Epistemológicas'. Escreva com clareza, profundidade real e didática impecável.
Responda APENAS com um objeto JSON válido, sem markdown antes ou depois.`;

  const userPrompt = `Gere uma obra completa em JSON sobre o tema/pauta abaixo:

${cleanTopic}

Use exatamente esta estrutura JSON (NUNCA inclua contagem de minutos em títulos ou subtítulos):
{
  "title": "Título Claro, Direto e Didático da Obra",
  "subtitle": "Guia Prático em Camadas & Progressive Disclosure",
  "category": "Área do Conhecimento",
  "description": "Resumo claro de 2 frases sobre o que o leitor vai aprender.",
  "chapters": [
    {
      "number": "I",
      "title": "Camada 1 — Resumo Rápido: Visão Geral Direta",
      "epigraph": {"text": "Frase síntese inspiradora e clara sobre o tema.", "author": "Autor ou Referência"},
      "sections": [
        {"type": "heading", "level": 3, "content": "1. O Panorama Essencial"},
        {"type": "paragraph", "content": "Explicação curta, clara e direta..."},
        {"type": "callout", "title": "Ideia Central", "content": "Resumo prático fácil de guardar..."}
      ]
    },
    {
      "number": "II",
      "title": "Camada 2 — Versão Intermediária: Conceito, Exemplo e Aplicação",
      "epigraph": {"text": "Dividir para compreender sem esforço.", "author": "Progressive Disclosure"},
      "sections": [
        {"type": "heading", "level": 3, "content": "Bloco 1: [Nome do 1º Tópico]"},
        {"type": "paragraph", "content": "O CONCEITO: explicação direta. O EXEMPLO: caso concreto. A APLICAÇÃO: como usar na prática."},
        {"type": "callout", "title": "Aplicação Prática", "content": "Passo a passo direto..."}
      ]
    },
    {
      "number": "III",
      "title": "Camada 3 — Texto Completo: Domínio Aprofundado Passo a Passo",
      "epigraph": {"text": "Depois da base construída, a leitura profunda flui naturalmente.", "author": "Leitura em Camadas"},
      "sections": [
        {"type": "heading", "level": 3, "content": "1. Aprofundamento Completo"},
        {"type": "paragraph", "content": "Desenvolvimento completo, claro, conversado e detalhado de todos os pontos..."}
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
      subtitle: parsedBook.subtitle || "Leitura em Camadas & Progressive Disclosure",
      author: parsedBook.author || "Manual Vivo · Leitura em Camadas",
      date: new Date().getFullYear().toString(),
      category: parsedBook.category || "Leitura em Camadas & Progressive Disclosure",
      chaptersCount: chapters.length,
      estimatedReadingTime: parsedBook.estimatedReadingTime || `Aprox. ${chapters.length * 8} min de leitura`,
      description: parsedBook.description || "Conteúdo estruturado em camadas progressivas para assimilação natural e profunda.",
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

aiRouter.post('/deepen', async (req: Request, res: Response) => {
  const { topic, contextText = '', style = 'didatico', level = 1, apiKey, model } = req.body;

  if (!topic) {
    return res.status(400).json({ status: 'error', message: "O campo 'topic' é obrigatório." });
  }

  const prompt = `Aprofunde com máxima clareza, rigor e didática o seguinte conceito no contexto de leitura:
Conceito: "${topic}"
Contexto atual: "${contextText.slice(0, 500)}"
Estilo: ${style} (Nível de aprofundamento: ${level})

Estruture a resposta com:
1. Definição Essencial e Intuição Central (analogia cotidiana)
2. Mecanismo Explicativo (causas, relações conceituais, contexto histórico/científico)
3. Aplicação Concreta (exemplo real em exames, redações ou na prática)
4. Armadilhas Comuns / Distratores a Evitar`;

  const { text, error } = await callNvidiaLlm([
    { role: 'system', content: 'Você é um professor e autor didático de excelência.' },
    { role: 'user', content: prompt }
  ], apiKey, model);

  if (text) {
    return res.json({ status: 'ok', content: text, model });
  }

  // Fallback
  const fallback = `### ${topic}\n\n**Definição Essencial:** Este conceito representa um ponto nodal na compreensão profunda do tema. Em linguagem direta, estabelece as relações entre causas materiais e impactos práticos.\n\n**Mecanismo:** Ao analisar criticamente, percebe-se que as premissas deste conceito conectam a teoria à realidade sem recorrer a fórmulas decoradas.\n\n**Aplicação Prática:** Em avaliações e redações, utilize este conceito como evidência sólida para sustentar argumentos sem cometer generalizações indevidas.`;
  return res.json({ status: 'ok', content: fallback, model: 'Motor Didático Fallback' });
});

import {
  getAudioCacheKey,
  isAudioCached,
  getAudioFilePath,
  generateAiAudioDescriptionScript,
  synthesizeAndCacheAudio,
  ensureCacheDir,
} from '../services/tts.js';
import fs from 'fs';
import path from 'path';

aiRouter.post('/tts', async (req: Request, res: Response) => {
  const {
    text,
    chapterTitle = 'Capítulo',
    chapterId,
    mode = 'audiodescricao', // 'audiodescricao' ou 'direct'
  } = req.body;

  if (!text) {
    return res.status(400).json({ status: 'error', message: "O campo 'text' é obrigatório." });
  }

  try {
    const cacheKey = getAudioCacheKey(text, mode, chapterId);
    const cached = isAudioCached(cacheKey);

    if (cached) {
      console.log(`[TTS Cache HIT] Servindo áudio existente: ${cacheKey}.mp3`);
      return res.json({
        status: 'ok',
        cached: true,
        cacheKey,
        audioUrl: `/api/ai/audio/${cacheKey}.mp3`,
        mode,
      });
    }

    console.log(`[TTS Cache MISS] Gerando novo áudio via IA (${mode}) para "${chapterTitle}"...`);

    let speechText = text;
    let generatedScript: string | undefined = undefined;

    if (mode === 'audiodescricao') {
      // 1. Gera o roteiro didático de audiodescrição com o LLM
      generatedScript = await generateAiAudioDescriptionScript(chapterTitle, text);
      speechText = generatedScript;
    }

    // 2. Sintetiza a voz em MP3 e salva no bucket/volume persistente
    const { durationEstimateSec } = await synthesizeAndCacheAudio(speechText, cacheKey);

    return res.json({
      status: 'ok',
      cached: false,
      cacheKey,
      audioUrl: `/api/ai/audio/${cacheKey}.mp3`,
      script: generatedScript,
      durationEstimateSec,
      mode,
    });
  } catch (err: any) {
    console.error('[TTS Error]', err);
    return res.status(500).json({
      status: 'error',
      message: 'Falha ao processar audiodescrição: ' + (err?.message || String(err)),
    });
  }
});

// Endpoint que serve o áudio com suporte a streaming e HTTP Range (pause, seek, scrubber)
aiRouter.get('/audio/:filename', (req: Request, res: Response) => {
  const rawFilename = req.params.filename;
  const filenameStr = Array.isArray(rawFilename) ? rawFilename[0] : (rawFilename || '');
  const sanitized = path.basename(filenameStr);
  const cacheDir = ensureCacheDir();
  const filePath = path.join(cacheDir, sanitized);

  if (!fs.existsSync(filePath)) {
    return res.status(404).json({ status: 'error', message: 'Áudio não encontrado no bucket.' });
  }

  const stat = fs.statSync(filePath);
  const fileSize = stat.size;
  const range = req.headers.range;

  if (range) {
    const parts = range.replace(/bytes=/, '').split('-');
    const start = parseInt(parts[0], 10);
    const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;
    const chunksize = end - start + 1;
    const file = fs.createReadStream(filePath, { start, end });
    const head = {
      'Content-Range': `bytes ${start}-${end}/${fileSize}`,
      'Accept-Ranges': 'bytes',
      'Content-Length': chunksize,
      'Content-Type': 'audio/mpeg',
      'Cache-Control': 'public, max-age=31536000, immutable',
    };
    res.writeHead(206, head);
    file.pipe(res);
  } else {
    const head = {
      'Content-Length': fileSize,
      'Content-Type': 'audio/mpeg',
      'Cache-Control': 'public, max-age=31536000, immutable',
      'Accept-Ranges': 'bytes',
    };
    res.writeHead(200, head);
    fs.createReadStream(filePath).pipe(res);
  }
});
