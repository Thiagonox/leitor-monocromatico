"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FONTS = exports.THEMES = exports.DEFAULT_CATALOG = void 0;
exports.DEFAULT_CATALOG = [
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
        id: "interpretacao-de-texto",
        title: "Manual Vivo de Interpretação e Compreensão Textual",
        subtitle: "Como Ler nas Entrelinhas, Dominar a Argumentação e Destravar Qualquer Texto sem Mistério",
        author: "Prof. Antigravity & Estudos Vivos da Linguagem",
        category: "Língua Portuguesa & Prática de Leitura",
        chaptersCount: 13,
        estimatedTime: "Aprox. 86 min de aula",
        file: "/data/interpretacao-de-texto.json",
        description: "Uma verdadeira imersão didática em forma de conversa viva: aprenda compreensão vs interpretação, tese, inferência, gêneros, multimodalidade, variação linguística, implícitos, estratégias persuasivas e conectivos com dezenas de exemplos cotidianos, notícias, redações e questões práticas explicadas passo a passo.",
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
exports.THEMES = [
    { id: 'eink', label: 'E-Ink (Papel Digital)', desc: 'Preto & Branco puro de alto contraste' },
    { id: 'dark', label: 'Noite (OLED Escuro)', desc: 'Fundo negro absoluto e tipografia clara' },
    { id: 'white', label: 'Papel Alvo', desc: 'Fundo branco puro editorial' },
    { id: 'sepia', label: 'Papiro / Sépia', desc: 'Tom suave de papel antigo' }
];
exports.FONTS = [
    { id: 'serif', label: 'Serifada (Editorial)', family: 'var(--font-serif), Newsreader, Georgia, serif' },
    { id: 'sans', label: 'Linear (Moderna)', family: 'var(--font-sans), Inter, system-ui, sans-serif' },
    { id: 'mono', label: 'Monoespaçada (Foco)', family: 'var(--font-mono), JetBrains Mono, monospace' }
];
