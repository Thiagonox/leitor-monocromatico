import { CatalogItem } from './types.js';

export const DEFAULT_CATALOG: CatalogItem[] = [
  {
    id: "linguagens-enem-essencial",
    title: "Linguagens e Códigos ENEM: O Guia Essencial de 2 Horas",
    subtitle: "Revisão Rápida e Direta de Alto Rendimento por Ordem de Peso na TRI: O Que Realmente Cai em Cada Tópico",
    author: "Prof. Antigravity & Estudos Vivos da Linguagem",
    category: "Revisão Express ENEM · Linguagens & Códigos",
    chaptersCount: 17,
    estimatedTime: "Aprox. 2 horas (Sprint Estratégico)",
    file: "/data/linguagens-enem-essencial.json",
    description: "A versão condensada, veloz e de alto impacto de todo o currículo de Linguagens para o ENEM. Rigorosamente organizada na ordem de maior valor na TRI para o menor: da interpretação cirúrgica e gêneros aos conectivos de inglês/espanhol, gramática aplicada ao sentido, dossiês dos autores canônicos (Machado, Alencar, Drummond, Graciliano, Clarice, Guimarães Rosa e Conceição Evaristo), história da arte e cultura corporal. Sem enrolação: conceitos mastigados, fórmulas práticas, alertas de pegadinhas e questões comentadas para revisar em 120 minutos.",
    isPriority: true
  },
  {
    id: "linguagens-enem-completo",
    title: "Manual Supremo de Linguagens, Códigos e suas Tecnologias",
    subtitle: "O Curso Definitivo do ENEM por Ordem de Relevância e Peso na TRI: Da Interpretação Máxima às Artes, Literatura e Línguas Estrangeiras",
    author: "Prof. Antigravity & Estudos Vivos da Linguagem",
    category: "Curso Completo ENEM · Linguagens & Códigos",
    chaptersCount: 68,
    estimatedTime: "Aprox. 8 horas de imersão completa (68 Capítulos)",
    file: "/data/linguagens-enem-completo.json",
    description: "O mais completo curso de Linguagens, Códigos e suas Tecnologias já estruturado para o ENEM e vestibulares. Reúne todo o currículo em 68 capítulos ordenados rigorosamente do maior peso e retorno na TRI para o menor: 1. Interpretação de Texto e Estratégias Argumentativas (~35-40% dos pontos), 2. Gêneros Textuais e Multimodalidade (~25%), 3. Língua Estrangeira Instrumental (Inglês e Espanhol - Questões 1 a 5), 4. Gramática Aplicada ao Sentido e Coesão (~15%), 5. Literatura e Dossiês de Autores Canônicos (~15%), 6. História da Arte, Cultura Visual e Patrimônio (~7%) e 7. Linguagem Corporal e Cultura do Movimento (~3%). Cada capítulo traz conceitos mastigados, quadros comparativos, exemplos reais de prova e questões formativas comentadas.",
    isPriority: true
  },
  {
    id: "redacao-enem",
    title: "Manual Vivo de Redação e Argumentação Nota 1000",
    subtitle: "Como Interpretar Qualquer Tema, Construir uma Tese Inabalável, Dominar os Quatro Parágrafos e Aplicar Repertórios Socioculturais com Fluidez",
    author: "Prof. Antigravity & Estudos Vivos da Linguagem",
    category: "Redação ENEM & Produção Textual",
    chaptersCount: 9,
    estimatedTime: "Aprox. 78 min de aula",
    file: "/data/redacao-enem.json",
    description: "Uma imersão completa, fluida e conversada em toda a engenharia da redação nota 1000 do ENEM: visão panorâmica da estrutura dissertativo-argumentativa, leitura cirúrgica do tema, construção da tese, introdução passo a passo, desenvolvimento 1 e 2, conclusão com os 5 elementos da proposta de intervenção, as cinco competências e um arsenal completo com os 11 eixos de repertório sociocultural explicados e aplicados em parágrafos reais.",
    isPriority: true
  },
  {
    id: "elogio-da-tinta",
    title: "O Elogio da Tinta e do Silêncio",
    subtitle: "Um Tratado sobre a Leitura Imersiva em Preto e Branco",
    author: "Antigravity Editorial",
    category: "Ensaio & Estética",
    chaptersCount: 3,
    estimatedTime: "15 min",
    file: "/data/elogio-da-tinta.json",
    description: "Um manifesto e experiência demonstrativa projetada para demonstrar a pureza do contraste, a eliminação de ruídos visuais e o retorno à palavra impressa no ambiente digital.",
    isPriority: false
  }
];

export const THEMES = [
  { id: 'eink', label: 'E-Ink (Papel Digital)', desc: 'Preto & Branco puro de alto contraste' },
  { id: 'dark', label: 'Noite (OLED Escuro)', desc: 'Fundo negro absoluto e tipografia clara' },
  { id: 'white', label: 'Papel Alvo', desc: 'Fundo branco puro editorial' },
  { id: 'sepia', label: 'Papiro / Sépia', desc: 'Tom suave de papel antigo' }
] as const;

export const FONTS = [
  { id: 'serif', label: 'Serifada (Editorial)', family: 'var(--font-serif), Newsreader, Georgia, serif' },
  { id: 'sans', label: 'Linear (Moderna)', family: 'var(--font-sans), Inter, system-ui, sans-serif' },
  { id: 'mono', label: 'Monoespaçada (Foco)', family: 'var(--font-mono), JetBrains Mono, monospace' }
] as const;
