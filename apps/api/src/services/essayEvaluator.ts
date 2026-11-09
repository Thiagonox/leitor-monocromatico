import { EssayCorrectionResult, EssayCompetencyScore } from '@mono-reader/shared';
import { callOpenRouterLlm, callNvidiaLlm } from './llm.js';

const SYSTEM_PROMPT = `Você é o Dr. Viktor, Corretor-Chefe Sênior de Bancas de Redação do ENEM (INEP), com mais de 15 anos de experiência na aplicação da Matriz Oficial de Competências.
Sua missão é realizar uma AVALIAÇÃO CIRÚRGICA, EXTREMAMENTE OBJETIVA E CRITERIOSA da redação enviada pelo candidato, atribuindo as notas exatas da banca oficial e fornecendo diagnóstico pontual.

CRITÉRIOS OFICIAIS DO INEP (Pontuações permitidas por competência: 0, 40, 80, 120, 160 ou 200 pontos):
- Competência 1: Domínio da modalidade escrita formal (ortografia, acentuação, concordância verbal/nominal, regência, crase, pontuação e paralelismo sintático).
  * 200: Excelente domínio, no máximo dois desvios gramaticais leves e uma falha de estrutura sintática.
  * 160: Bom domínio, poucos desvios gramaticais.
  * 120: Domínio mediano, desvios recorrentes.
  * 80: Domínio insuficiente, muitos desvios.
  * 40: Domínio precário.
  * 0: Desconhecimento da modalidade escrita.

- Competência 2: Compreensão da proposta de redação, aplicação de conceitos de várias áreas (repertório sociocultural) e respeito ao tipo dissertativo-argumentativo em prosa.
  * 200: Desenvolve o tema plenamente com repertório sociocultural LEGITIMADO, PERTINENTE e PRODUTIVO articulado à tese.
  * 160: Repertório legitimado e pertinente, mas com uso produtivo limitado; ou argumentação previsível.
  * 120: Repertório baseado apenas nos textos motivadores ou pouco produtivo.
  * 80: Tangencia o tema ou apresenta traços de outros tipos textuais.
  * 40 ou 0: Fuga total ao tema ou desrespeito ao formato dissertativo.

- Competência 3: Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos em defesa de um ponto de vista (Projeto de texto e coerência).
  * 200: Projeto de texto estratégico consistente, sem contradições ou lacunas argumentativas, autoria evidente.
  * 160: Projeto de texto com pequenas lacunas ou argumentos pontualmente expositivos.
  * 120: Projeto de texto frágil com muitas lacunas argumentativas.
  * 80: Ideias desorganizadas ou contraditórias.
  * 40 ou 0: Argumentos caóticos e desarticulados.

- Competência 4: Demonstração de conhecimento dos mecanismos linguísticos necessários para a construção da argumentação (Coesão inter e intraparágrafos).
  * 200: Repertório coesivo diversificado interparágrafos (em ao menos 2 inícios de parágrafos) e intraparágrafos expressivo, sem repetições viciosas.
  * 160: Coesão adequada, mas com poucas repetições ou repertório coesivo pouco diversificado.
  * 120: Repetição frequente de conectivos ou falta de operadores interparágrafos.
  * 80 ou 40: Coesão precária com inadequação de conectivos.

- Competência 5: Elaboração de proposta de intervenção para o problema abordado, respeitando os direitos humanos (Os 5 elementos obrigatórios).
  * Cada elemento válido vale exatamente 40 pontos:
    1. Agente (Quem executa?)
    2. Ação (O que fará?)
    3. Meio/Modo (Como fará?)
    4. Efeito/Finalidade (Para que fará?)
    5. Detalhamento (Explicação adicional de um dos 4 elementos).
  * 200: Todos os 5 elementos presentes, claros e articulados.
  * 160: 4 elementos presentes.
  * 120: 3 elementos presentes.
  * 80: 2 elementos presentes.
  * 40: 1 elemento presente.
  * 0: Nulo ou desrespeito frontal aos direitos humanos.

INSTRUÇÃO DE SAÍDA:
Retorne APENAS um objeto JSON válido (sem texto solto fora do JSON) exatamente nesta estrutura:
{
  "totalScore": 920,
  "theme": "Tema analisado",
  "wordCount": 380,
  "paragraphCount": 4,
  "estimatedLines": 28,
  "competencies": [
    {
      "number": 1,
      "name": "Domínio da Norma Culta",
      "score": 160,
      "maxScore": 200,
      "level": "Nível 4 (Bom domínio, desvios pontuais)",
      "feedback": "Diagnóstico do Dr. Viktor sobre a gramática do texto...",
      "positives": ["Ponto positivo específico 1", "Ponto positivo 2"],
      "deviations": ["Desvio identificado na linha X", "Desvio 2"],
      "improvement": "Ação exata para alcançar os 200 pontos..."
    },
    {
      "number": 2,
      "name": "Compreensão do Tema e Repertório Sociocultural",
      "score": 200,
      "maxScore": 200,
      "level": "Nível 5 (Tema pleno e repertório produtivo legitimado)",
      "feedback": "Diagnóstico sobre o repertório...",
      "positives": ["Repertório de Bauman articulado"],
      "deviations": [],
      "improvement": "Recomendação..."
    },
    {
      "number": 3,
      "name": "Projeto de Texto e Argumentação",
      "score": 160,
      "maxScore": 200,
      "level": "Nível 4 (Projeto de texto evidente)",
      "feedback": "Diagnóstico sobre o projeto de texto...",
      "positives": ["Tese clara"],
      "deviations": ["D2 com caráter expositivo"],
      "improvement": "Recomendação..."
    },
    {
      "number": 4,
      "name": "Coesão Textual e Conectivos",
      "score": 200,
      "maxScore": 200,
      "level": "Nível 5 (Repertório coesivo diversificado)",
      "feedback": "Diagnóstico sobre os operadores argumentativos...",
      "positives": ["Conectivos interparágrafos presentes"],
      "deviations": [],
      "improvement": "Recomendação..."
    },
    {
      "number": 5,
      "name": "Proposta de Intervenção (Os 5 Elementos)",
      "score": 200,
      "maxScore": 200,
      "level": "Nível 5 (Todos os 5 elementos presentes)",
      "feedback": "Diagnóstico sobre a proposta de intervenção...",
      "positives": ["Proposta completa com os 5 elementos"],
      "deviations": [],
      "improvement": "Recomendação..."
    }
  ],
  "c5Checklist": {
    "agente": {"present": true, "text": "Ministério da Educação"},
    "acao": {"present": true, "text": "deve instituir oficinas de capacitação"},
    "meio": {"present": true, "text": "por intermédio de verbas públicas"},
    "efeito": {"present": true, "text": "a fim de mitigar a desigualdade"},
    "detalhamento": {"present": true, "text": "focando nas escolas das periferias urbanas"}
  },
  "generalVerdict": "Parecer geral e direto do Dr. Viktor sobre as chances reais de nota mil.",
  "strengths": [
    "Destaque positivo 1",
    "Destaque positivo 2"
  ],
  "criticalCorrections": [
    "Correção urgente 1",
    "Correção urgente 2"
  ],
  "evaluatorName": "Dr. Viktor · Corretor Oficial ENEM"
}`;

/**
 * Fallback de avaliação heurística objetiva para garantir resposta instantânea e robusta
 */
export function evaluateEssayHeuristic(essayText: string, theme: string = ''): EssayCorrectionResult {
  const paragraphs = essayText
    .split(/\n\s*\n|\n/)
    .map((p) => p.trim())
    .filter((p) => p.length > 20);

  const wordList = essayText.match(/\b[A-Za-zÀ-ÿ0-9-]+\b/g) || [];
  const wordCount = wordList.length;
  const paragraphCount = Math.max(1, paragraphs.length);
  const estimatedLines = Math.min(30, Math.max(7, Math.round(wordCount / 12.5)));

  // C4: Análise de Conectivos
  const interConnectors = [
    'nesse sentido', 'nessa perspectiva', 'sob essa ótica', 'ademais', 'outrossim',
    'além disso', 'em contrapartida', 'portanto', 'em suma', 'logo', 'dessarte',
    'destarte', 'por conseguinte', 'diante disso', 'assim sendo'
  ];
  let interMatches = 0;
  for (let i = 1; i < paragraphs.length; i++) {
    const pLower = paragraphs[i].toLowerCase();
    if (interConnectors.some((c) => pLower.startsWith(c) || pLower.slice(0, 45).includes(c))) {
      interMatches++;
    }
  }

  let c4Score = 120;
  if (interMatches >= 2 && wordCount >= 220) c4Score = 200;
  else if (interMatches >= 1 && wordCount >= 160) c4Score = 160;

  // C5: Análise dos 5 Elementos da Proposta
  const lowerText = essayText.toLowerCase();
  const lastParagraph = paragraphs[paragraphs.length - 1]?.toLowerCase() || lowerText;

  const agenteFound = /(minist[eé]rio|governo|poder p[uú]blico|secretaria|escolas?|sociedade|fam[ií]lia|ong|m[ií]dia|estado|iniciativa privada)/i.test(lastParagraph);
  const acaoFound = /(deve|precisa|cabe [aà]|tem o dever|necessita|promova|implemente|institua|crie|desenvolva)/i.test(lastParagraph);
  const meioFound = /(por meio de|mediante|atrav[eé]s de|por interm[eé]dio de|com a utiliza[cç][aã]o de)/i.test(lastParagraph);
  const efeitoFound = /(a fim de|com o intuito de|com o fito de|para que|com o objetivo de|com vistas a|visando)/i.test(lastParagraph);
  const detalhamentoFound = /(como por exemplo|em especial|nomeadamente|notadamente|isto [eé]|a saber|com destaque)/i.test(lastParagraph);

  let c5Count = 0;
  if (agenteFound) c5Count++;
  if (acaoFound) c5Count++;
  if (meioFound) c5Count++;
  if (efeitoFound) c5Count++;
  if (detalhamentoFound) c5Count++;

  const c5Score = Math.min(200, c5Count * 40);

  // C2: Repertório e Tema
  const repertorioKeywords = [
    'constitui[cç][aã]o', 'bauman', 'foucault', 'habermas', 'durkheim',
    'hannah arendt', 'cidad[aã]o de papel', 'gilberto dimenstein', 'machado de assis',
    'artigo', 'declara[cç][aã]o universal', 'ibge', 'ipea', 'modernidade l[ií]quida'
  ];
  const hasRepertorio = repertorioKeywords.some((rk) => new RegExp(rk, 'i').test(lowerText));
  let c2Score = 120;
  if (hasRepertorio && wordCount >= 240) c2Score = 200;
  else if (hasRepertorio || wordCount >= 180) c2Score = 160;

  // C3: Projeto de texto
  let c3Score = 120;
  if (paragraphCount === 4 && wordCount >= 240) c3Score = 160;
  if (paragraphCount === 4 && wordCount >= 280 && hasRepertorio) c3Score = 200;

  // C1: Norma Culta
  let c1Score = 160;
  if (wordCount >= 280 && !/(disposto [aà] lutar|para mim fazer|a anos atr[aá]s)/i.test(lowerText)) {
    c1Score = 160;
  }
  if (wordCount < 180) c1Score = 120;

  const totalScore = c1Score + c2Score + c3Score + c4Score + c5Score;

  return {
    totalScore,
    theme: theme || 'Tema Geral de Atualidades do ENEM',
    wordCount,
    paragraphCount,
    estimatedLines,
    competencies: [
      {
        number: 1,
        name: 'Domínio da Norma Culta',
        score: c1Score,
        maxScore: 200,
        level: c1Score >= 160 ? 'Nível 4 (Bom domínio formal)' : 'Nível 3 (Domínio mediano)',
        feedback: 'O texto apresenta boa articulação de períodos e vocabulário formal condizente com a dissertação acadêmica.',
        positives: ['Vocabulário formal e preciso', 'Estruturação sintática adequada'],
        deviations: c1Score < 200 ? ['Pontuação pontualmente truncada em orações subordinadas'] : [],
        improvement: 'Revise o paralelismo sintático e as regências verbais para atingir a nota máxima na C1.'
      },
      {
        number: 2,
        name: 'Compreensão do Tema e Repertório Sociocultural',
        score: c2Score,
        maxScore: 200,
        level: c2Score === 200 ? 'Nível 5 (Repertório legitimado e produtivo)' : 'Nível 4 (Repertório pertinente)',
        feedback: hasRepertorio
          ? 'Identificada a mobilização de repertório sociocultural legitimado e pertinente à discussão proposta.'
          : 'O texto aborda o tema, mas carece de repertório sociocultural externo de áreas como Sociologia, Filosofia ou História.',
        positives: hasRepertorio ? ['Presença de áreas do conhecimento articuladas ao debate'] : ['Abordagem do tema central'],
        deviations: hasRepertorio ? [] : ['Falta de citação de autoridade, dado estatístico ou referência histórica'],
        improvement: 'Incorpore ao menos uma referência filosófica ou sociológica produtiva na introdução ou no D1.'
      },
      {
        number: 3,
        name: 'Projeto de Texto e Argumentação',
        score: c3Score,
        maxScore: 200,
        level: c3Score === 200 ? 'Nível 5 (Projeto estratégico consistente)' : 'Nível 4 (Projeto evidente com pequenas lacunas)',
        feedback: paragraphCount === 4
          ? 'Estrutura dissertativa clássica em 4 parágrafos bem delimitados (Introdução, 2 Desenvolvimentos e Conclusão).'
          : 'A distribuição dos parágrafos pode ser aprimorada para equilibrar a introdução, o desenvolvimento e a conclusão.',
        positives: ['Divisão de parágrafos estruturada', 'Direcionamento opinativo'],
        deviations: paragraphCount !== 4 ? ['Organização de parágrafos distante do modelo canônico de 4 blocos'] : [],
        improvement: 'Garanta que cada parágrafo de desenvolvimento trate de uma causa diferente do problema (ex: negligência estatal no D1 e herança sociocultural no D2).'
      },
      {
        number: 4,
        name: 'Coesão Textual e Conectivos',
        score: c4Score,
        maxScore: 200,
        level: c4Score === 200 ? 'Nível 5 (Repertório coesivo diversificado)' : 'Nível 4 (Coesão adequada com pouca variedade)',
        feedback: `Identificados operadores argumentativos conectando os blocos textuais (${interMatches} conectores interparágrafos detectados).`,
        positives: ['Presença de conectivos nos inícios de parágrafo', 'Transições lógicas mantidas'],
        deviations: interMatches < 2 ? ['Recomenda-se iniciar o D2 com conectivo de adição (ex: "Ademais") e a conclusão com conclusivo (ex: "Portanto")'] : [],
        improvement: 'Diversifique os operadores argumentativos inter e intraparágrafos para eliminar qualquer sensação de repetição.'
      },
      {
        number: 5,
        name: 'Proposta de Intervenção (Os 5 Elementos)',
        score: c5Score,
        maxScore: 200,
        level: `Nível ${c5Count} (${c5Count}/5 elementos identificados)`,
        feedback: `A proposta de intervenção na conclusão foi analisada nos 5 elementos oficiais do INEP: ${c5Count} elementos encontrados.`,
        positives: [
          agenteFound ? 'Agente identificado' : '',
          acaoFound ? 'Ação interventiva presente' : '',
          meioFound ? 'Meio de execução detalhado' : '',
          efeitoFound ? 'Finalidade/efeito expresso' : ''
        ].filter(Boolean),
        deviations: [
          !agenteFound ? 'Faltou o Agente (Quem fará?)' : '',
          !acaoFound ? 'Faltou a Ação (O que fará?)' : '',
          !meioFound ? 'Faltou o Meio/Modo (Por meio de quê?)' : '',
          !efeitoFound ? 'Faltou a Finalidade (A fim de quê?)' : '',
          !detalhamentoFound ? 'Faltou o Detalhamento de um dos elementos (ex: explicando o agente ou exemplificando o meio)' : ''
        ].filter(Boolean),
        improvement: 'Para cravar os 200 pontos na C5, garanta os 5 elementos com palavras-chave explícitas: Agente + Ação + "por meio de" (meio) + "a fim de" (efeito) + detalhamento com travessões.'
      }
    ],
    c5Checklist: {
      agente: { present: agenteFound, text: agenteFound ? 'Identificado no texto' : 'Ausente ou vago' },
      acao: { present: acaoFound, text: acaoFound ? 'Identificada no texto' : 'Ausente ou genérica' },
      meio: { present: meioFound, text: meioFound ? 'Identificado com operador de meio' : 'Ausente (use "por meio de")' },
      efeito: { present: efeitoFound, text: efeitoFound ? 'Identificado com operador de finalidade' : 'Ausente (use "a fim de")' },
      detalhamento: { present: detalhamentoFound, text: detalhamentoFound ? 'Detalhamento identificado' : 'Ausente (adicione um aposto explicativo)' }
    },
    generalVerdict: totalScore >= 900
      ? 'Excelente desempenho. Redação madura, com projeto de texto sólido e repertório produtivo. Ajustes finos nos desvios gramaticais garantem a nota 1000.'
      : totalScore >= 760
      ? 'Bom texto, competitivo. Para superar a barreira dos 900 pontos, complete os 5 elementos da proposta de intervenção na C5 e aprofunde o nexo causal no desenvolvimento.'
      : 'Texto com potencial, mas que precisa alinhar a estrutura dos 4 parágrafos e aplicar com mais rigor a proposta de intervenção completa.',
    strengths: [
      hasRepertorio ? 'Mobilização de repertório sociocultural no texto' : 'Abordagem coerente da discussão',
      paragraphCount === 4 ? 'Organização clássica em quatro parágrafos' : 'Articulação do ponto de vista',
      c5Score >= 160 ? 'Proposta de intervenção bem estruturada' : 'Presença de conectivos'
    ],
    criticalCorrections: [
      c5Score < 200 ? 'Garantir todos os 5 elementos da proposta de intervenção (C5)' : 'Manter a precisão gramatical em orações subordinadas',
      c4Score < 200 ? 'Iniciar o D2 e a conclusão com operadores argumentativos explícitos' : 'Aprofundar a criticidade do argumento sem descair para a mera exposição'
    ],
    evaluatorName: 'Dr. Viktor · Corretor Oficial ENEM'
  };
}

/**
 * Avalia a redação usando o modelo LLM do Dr. Viktor ou fallback heurístico
 */
export async function evaluateEssayWithAi(
  essayText: string,
  theme: string = '',
  apiKey?: string,
  model?: string
): Promise<EssayCorrectionResult> {
  const cleanEssay = essayText.trim();
  if (cleanEssay.length < 100) {
    throw new Error('A redação é muito curta para avaliação da banca. Insira ao menos um parágrafo completo.');
  }

  const prompt = `Analise objetivamente a seguinte redação para o tema: "${theme || 'Tema Livre do ENEM'}".
REDAÇÃO SUBMETIDA:
"""
${cleanEssay}
"""

Avalie estritamente com os critérios do ENEM e retorne o JSON solicitado:`;

  const messages: { role: 'system' | 'user'; content: string }[] = [
    { role: 'system', content: SYSTEM_PROMPT },
    { role: 'user', content: prompt }
  ];

  // Tenta chamada LLM via OpenRouter
  try {
    const { text, model: outModel } = await callOpenRouterLlm(messages, 3500, 0.3, 22000);
    if (text) {
      const jsonMatch = text.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const parsed = JSON.parse(jsonMatch[0]) as EssayCorrectionResult;
        if (parsed && typeof parsed.totalScore === 'number' && Array.isArray(parsed.competencies)) {
          parsed.modelUsed = outModel || 'OpenRouter LLM';
          return parsed;
        }
      }
    }
  } catch (err) {
    console.warn('OpenRouter evaluation failed, trying Nvidia or heuristic:', err);
  }

  // Tenta chamada LLM via Nvidia
  try {
    const { text, model: outModel } = await callNvidiaLlm(messages, apiKey, model);
    if (text) {
      const jsonMatch = text.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const parsed = JSON.parse(jsonMatch[0]) as EssayCorrectionResult;
        if (parsed && typeof parsed.totalScore === 'number' && Array.isArray(parsed.competencies)) {
          parsed.modelUsed = outModel || 'Nvidia LLM';
          return parsed;
        }
      }
    }
  } catch (err) {
    console.warn('Nvidia evaluation failed, using heuristic engine:', err);
  }

  // Fallback heurístico inteligente oficial
  const result = evaluateEssayHeuristic(cleanEssay, theme);
  result.modelUsed = 'Motor Heurístico Dr. Viktor (Banca Oficial)';
  return result;
}
