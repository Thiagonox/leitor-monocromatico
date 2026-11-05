# Leitor Monocromático — Monorepo

Sistema editorial focado em leitura imersiva e cognitiva de alto contraste, estruturado como **Monorepo** com separação completa entre Frontend (Next.js) e Backend (API REST).

---

## 🏛️ Arquitetura do Monorepo

```
leitor-monocromatico/
├── apps/
│   ├── web/                    # Frontend em Next.js 15 (App Router, React 19, Tailwind CSS)
│   │   ├── src/
│   │   │   ├── app/            # Rotas: Biblioteca (/), Leitor (/reader/[id]), Camadas (/reader/[id]/camadas)
│   │   │   ├── components/     # Componentes: AiStudio, BookCard, ThemeToggle, TocDrawer, QuizBlock...
│   │   │   └── lib/            # Cliente de API e gerenciador de estado local
│   │   └── public/data/        # Acervo estático de fallback
│   │
│   └── api/                    # Backend REST em Node.js / TypeScript (Express)
│       ├── src/
│       │   ├── routes/         # Endpoints: /api/catalog, /api/books/:id, /api/ai/*
│       │   ├── services/       # Conectores OpenRouter, NVIDIA NIM, síntese em camadas
│       │   └── server.ts       # Servidor HTTP com CORS (Porta 3001)
│       └── server.py           # Runner Python alternativo legado mantido
│
├── packages/
│   └── shared/                 # Modelos, tipos TypeScript e catálogo padrão compartilhado
│       └── src/
│           ├── types.ts        # BookDoc, Chapter, Section, QuizItem, LayeredChapterData...
│           └── constants.ts    # DEFAULT_CATALOG, Temas, Fontes
│
├── data/                       # Arquivos canônicos de livros (JSON)
│   ├── redacao-enem.json       # Manual Vivo de Redação Nota 1000 (Obra Oficial)
│   ├── interpretacao-de-texto.json
│   ├── elogio-da-tinta.json
│   └── library.json
│
├── legacy/                     # Cópia integral de segurança dos arquivos legados
├── pnpm-workspace.yaml         # Configuração de workspaces pnpm
└── package.json                # Scripts centralizados de orquestração
```

---

## 🚀 Como Executar

### 1. Pré-requisitos
- Node.js >= 20
- pnpm >= 9 (ou npm)

### 2. Instalação de Dependências
Na raiz do projeto:
```bash
pnpm install
```

### 3. Modo de Desenvolvimento (Frontend + Backend juntos)
```bash
pnpm dev
```
Inicia simultaneamente:
- **Frontend (Next.js)**: `http://localhost:3000`
- **Backend (API)**: `http://localhost:3001`

### 4. Modo de Produção
```bash
# Compilar todos os pacotes:
pnpm build

# Iniciar ambos os servidores:
pnpm start
```

---

## 🔌 Endpoints da API (`apps/api`)

- `GET /health` — Verificação de status do serviço
- `GET /api/catalog` — Catálogo de obras disponíveis
- `GET /api/books/:id` — Retorna o documento completo da obra
- `POST /api/books` — Registra/salva nova obra
- `POST /api/ai/generate-layered` — Motor de geração de conteúdo em camadas (resumo rápido, progressive disclosure e texto completo sem resíduos de minutos)
- `POST /api/ai/deepen` — Aprofundamento conceitual via IA
- `POST /api/ai/tts` — Audiodescrição e leitura por voz

---

## 🎨 Temas e Tipografia

- **Temas**: E-Ink (Papel Monocromático Quente), Dark (OLED Preto Puro) e Light (Branco Editorial).
- **Tipografia**: Newsreader (Serifada), Inter (Linear Sans) e JetBrains Mono (Monoespaçada).
