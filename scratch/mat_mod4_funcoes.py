# -*- coding: utf-8 -*-
"""Módulo 4: Funções (Capítulos 15 a 19)"""

def get_chapters():
    return [
        {
            "id": "mat-cap-15-conceito-funcao-graficos",
            "number": 15,
            "title": "15. Conceito de Função, Domínio, Imagem e Interpretação de Gráficos",
            "epigraph": {
                "text": "Uma função é uma relação de dependência unívoca: para cada valor de entrada (x), existe um único valor de saída correspondente (y). Saber ler gráficos cartesianos garante pelo menos 5 questões no ENEM.",
                "author": "Matriz de Habilidades do ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Domínio, Contradomínio e Imagem"
                },
                {
                    "type": "paragraph",
                    "content": "Seja uma função f: A -> B:\n• Domínio (D): Conjunto de partida A. São todos os valores possíveis da variável independente x.\n• Contradomínio (CD): Conjunto de chegada B.\n• Conjunto Imagem (Im): Subconjunto de B formado pelos valores efetivamente atingidos por f(x).\nNo teste da reta vertical: um gráfico no plano cartesiano representa uma função se e somente se qualquer reta vertical imaginária intercepta a curva em no máximo UM único ponto."
                },
                {
                    "type": "callout",
                    "title": "Leitura de Gráficos no ENEM: Os Quatro Pontos Vitais",
                    "content": "Ao analisar qualquer gráfico cartesiano na prova:\n1. Intercepto com o eixo Y: Ocorre quando x = 0 (valor inicial, custo fixo, ponto de partida).\n2. Interceptos com o eixo X (Raízes ou Zeros da função): Ocorrem quando y = f(x) = 0.\n3. Pontos de Máximo e Mínimo: Onde a curva muda de direção (crescente para decrescente ou vice-versa).\n4. Intervalos de Crescimento e Decrescimento: Onde a inclinação da reta tangente é positiva ou negativa."
                }
            ],
            "quiz": [
                {
                    "question": "Um reservatório de água tem sua capacidade modelada por V(t) = 500 - 25t, onde V é o volume em litros e t é o tempo em horas. Qual é o tempo necessário para o reservatório esvaziar completamente?",
                    "options": [
                        "20 horas",
                        "25 horas",
                        "15 horas",
                        "10 horas"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Reservatório vazio significa V(t) = 0. Logo, 500 - 25t = 0 => 25t = 500 => t = 20 horas."
                }
            ]
        },
        {
            "id": "mat-cap-16-funcao-afim",
            "number": 16,
            "title": "16. Função Afim (1º Grau): Taxa de Variação, Coeficientes e Aplicações",
            "epigraph": {
                "text": "f(x) = ax + b. A função afim é a representação matemática do crescimento linear a uma taxa constante.",
                "author": "Álgebra Linear no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Significado Físico e Geométrico dos Coeficientes 'a' e 'b'"
                },
                {
                    "type": "paragraph",
                    "content": "Na função afim f(x) = ax + b:\n• Coeficiente Angular (a): É a TAXA DE VARIAÇÃO da função: a = delta_y / delta_x = (y2 - y1) / (x2 - x1). Se a > 0, a função é estritamente crescente; se a < 0, a função é decrescente; se a = 0, a função é constante.\n• Coeficiente Linear (b): É o ponto onde a reta cruza o eixo vertical Y, correspondendo às coordenadas (0, b). No cotidiano, 'b' representa o valor inicial, a bandeirada do táxi ou o custo fixo de uma conta de energia."
                },
                {
                    "type": "callout",
                    "title": "Como Montar a Equação da Reta Direto do Gráfico",
                    "content": "1. Identifique onde a reta corta o eixo vertical: esse valor é o 'b'.\n2. Escolha outro ponto conhecido (x, y) da reta e calcule a inclinação: a = (y - b) / x.\nExemplo clássico: Táxi cobra bandeirada de R$ 5,00 e R$ 2,50 por km rodado. A função do preço P em relação aos quilômetros x é: P(x) = 2,50x + 5,00."
                }
            ],
            "quiz": [
                {
                    "question": "Um plano de telefonia cobra uma taxa fixa mensal de R$ 35,00 mais R$ 0,50 por gigabyte adicional consumido além da franquia. Se um cliente consumiu 18 GB adicionais em um mês, qual foi o valor total da sua fatura?",
                    "options": [
                        "R$ 44,00",
                        "R$ 42,00",
                        "R$ 40,00",
                        "R$ 48,00"
                    ],
                    "correctAnswer": 0,
                    "explanation": "P(x) = 35 + 0,50 * x. Para x = 18 GB: P(18) = 35 + 0,50 * 18 = 35 + 9 = R$ 44,00."
                }
            ]
        },
        {
            "id": "mat-cap-17-funcao-quadratica",
            "number": 17,
            "title": "17. Função Quadrática (2º Grau): Vértice, Máximos, Mínimos e Trajetórias",
            "epigraph": {
                "text": "Toda vez que uma questão do ENEM falar em 'lucro máximo', 'altura máxima atingida por um projétil' ou 'custo mínimo de produção': você DEVE calcular o VÉRTICE da parábola.",
                "author": "Gatilho de Resolução Imediata"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Parábola e a Concavidade"
                },
                {
                    "type": "paragraph",
                    "content": "A função quadrática é dada por f(x) = ax² + bx + c (com a != 0):\n• Se a > 0: a parábola tem concavidade voltada para CIMA ('sorriso'). Ela possui um ponto de MÍNIMO absoluto.\n• Se a < 0: a parábola tem concavidade voltada para BAIXO ('tristeza'). Ela possui um ponto de MÁXIMO absoluto.\n• O coeficiente 'c' é o ponto exato onde a curva corta o eixo Y (x = 0, y = c)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Coordenadas do Vértice V(Xv, Yv)"
                },
                {
                    "type": "paragraph",
                    "content": "O vértice é o ponto de virada da parábola:\n• X do Vértice: Xv = -b / (2a). Ele indica 'QUANDO' ou 'QUAL QUANTIDADE' gera o máximo ou o mínimo.\n• Y do Vértice: Yv = -Delta / (4a) = f(Xv). Ele indica 'QUAL É' o valor máximo ou mínimo em si (o valor do lucro máximo, a altura máxima em metros)."
                },
                {
                    "type": "callout",
                    "title": "Atenção ao Enunciado: O ENEM Pede Xv ou Yv?",
                    "content": "• Se perguntar: 'Quantas peças devem ser produzidas para maximizar o lucro?': a resposta é o Xv!\n• Se perguntar: 'Qual é o lucro máximo obtido?': a resposta é o Yv!"
                }
            ],
            "quiz": [
                {
                    "question": "O lucro mensal de uma confecção é modelado por L(x) = -2x² + 120x - 1000, onde x é a quantidade de vestidos fabricados. Quantos vestidos devem ser produzidos para se obter o lucro máximo?",
                    "options": [
                        "30 vestidos",
                        "60 vestidos",
                        "25 vestidos",
                        "40 vestidos"
                    ],
                    "correctAnswer": 0,
                    "explanation": "A pergunta quer saber 'quantos vestidos' (variável x), logo calculamos Xv = -b / (2a) = -120 / (2 * (-2)) = -120 / -4 = 30 vestidos."
                }
            ]
        },
        {
            "id": "mat-cap-18-funcao-exponencial",
            "number": 18,
            "title": "18. Função Exponencial: Fenômenos de Multiplicação Acelerada",
            "epigraph": {
                "text": "Enquanto a função afim soma uma quantia fixa a cada passo, a função exponencial multiplica por um fator fixo a cada passo. É a matemática dos vírus, bactérias e juros compostos.",
                "author": "Modelagem Biológica e Financeira"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Forma Geral e Comportamento da Função Exponencial"
                },
                {
                    "type": "paragraph",
                    "content": "Uma função exponencial tem a forma f(x) = c * a^x (com a > 0 e a != 1):\n• Se a > 1: a função é estritamente crescente, com crescimento vertiginoso (ex: duplicação de bactérias a(t) = N0 * 2^t).\n• Se 0 < a < 1: a função é estritamente decrescente, aproximando-se assintoticamente de zero mas nunca tocando o zero (ex: decaimento radioativo e meia-vida N(t) = N0 * (1/2)^(t/T))."
                },
                {
                    "type": "callout",
                    "title": "Técnica de Resolução de Equações Exponenciais no ENEM",
                    "content": "O método principal consiste em igualar as bases dos dois lados da equação:\na^f(x) = a^g(x) <=> f(x) = g(x).\nExemplo: 4^(x + 1) = 32 => (2²)^(x + 1) = 2^5 => 2^(2x + 2) = 2^5 => 2x + 2 = 5 => 2x = 3 => x = 1,5."
                }
            ],
            "quiz": [
                {
                    "question": "Uma colônia de bactérias dobra de tamanho a cada 3 horas. Inicialmente há 500 bactérias. Qual será a população após 12 horas?",
                    "options": [
                        "8.000 bactérias",
                        "4.000 bactérias",
                        "16.000 bactérias",
                        "6.000 bactérias"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Em 12 horas, ocorrem 12 / 3 = 4 ciclos de duplicação. População = 500 * 2^4 = 500 * 16 = 8.000 bactérias."
                }
            ]
        },
        {
            "id": "mat-cap-19-funcao-logaritmica",
            "number": 19,
            "title": "19. Função Logarítmica: Descoberta de Tempo, Escalas Richter, pH e Decibéis",
            "epigraph": {
                "text": "O logaritmo é o inverso da exponencial: ele responde à pergunta 'a qual expoente devo elevar a base para obter este resultado?'. No ENEM, os dados de logaritmo sempre vêm no enunciado.",
                "author": "Guia de Logaritmos no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Definição e Propriedades Operatórias Fundamentais"
                },
                {
                    "type": "paragraph",
                    "content": "log_b(a) = x <=> b^x = a (com a > 0, b > 0 e b != 1).\nAs propriedades que você precisa dominar para o ENEM são:\n1. Logaritmo do Produto: log(a * b) = log(a) + log(b)\n2. Logaritmo do Quociente: log(a / b) = log(a) - log(b)\n3. Regra do Tombo (Potência): log(a^k) = k * log(a)\n4. Mudança de Base: log_b(a) = log_c(a) / log_c(b)."
                },
                {
                    "type": "callout",
                    "title": "Como o ENEM Cobra Logaritmos: Escalas Científicas",
                    "content": "O ENEM quase nunca cobra equações logarítmicas puras. Ele fornece uma fórmula da física ou química:\n• Escala Richter de terremotos: M = (2/3) * log(E / E0)\n• Potencial Hidrogeniônico (pH): pH = -log[H+]\n• Nível de intensidade sonora em decibéis: beta = 10 * log(I / I0)\nVocê só precisa aplicar as propriedades operatórias aos dados informados (como log 2 = 0,30 e log 3 = 0,48)!"
                }
            ],
            "quiz": [
                {
                    "question": "Sabendo que log 2 = 0,301 e log 3 = 0,477, qual é o valor aproximado de log 6?",
                    "options": [
                        "0,778",
                        "0,825",
                        "0,650",
                        "0,720"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Como 6 = 2 * 3, pela propriedade do produto: log 6 = log(2 * 3) = log 2 + log 3 = 0,301 + 0,477 = 0,778."
                }
            ]
        }
    ]
