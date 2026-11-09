# -*- coding: utf-8 -*-
"""Módulo 2: Porcentagem e Matemática Financeira (Capítulos 7 a 11)"""

def get_chapters():
    return [
        {
            "id": "mat-cap-07-porcentagem-aumentos",
            "number": 7,
            "title": "7. Porcentagem, Aumentos e Descontos Sucessivos",
            "epigraph": {
                "text": "Quem soma porcentagens de aumentos sucessivos erra na hora. Aprender o Fator de Multiplicação é a arma mais rápida do candidato 800+.",
                "author": "Matemática Financeira Estratégica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Conceito e o Poder do Fator Multiplicativo"
                },
                {
                    "type": "paragraph",
                    "content": "Porcentagem nada mais é do que uma fração de denominador 100: p% = p / 100. Em vez de calcular a porcentagem e depois somar ou subtrair do valor original, utilize diretamente o Fator Multiplicativo (FM):\n• Aumento de i%: FM = 1 + (i / 100). Exemplo: Aumento de 15% -> multiplica por 1,15. Aumento de 8% -> multiplica por 1,08. Aumento de 120% -> multiplica por 2,20.\n• Desconto de i%: FM = 1 - (i / 100). Exemplo: Desconto de 20% -> multiplica por 0,80. Desconto de 5% -> multiplica por 0,95."
                },
                {
                    "type": "callout",
                    "title": "O Erro que 90% dos Candidatos Cometem em Aumentos e Descontos",
                    "content": "Se um produto sofre um aumento de 10% e depois outro aumento de 20%, o aumento acumulado NÃO É 30%!\nO cálculo real é o produto dos fatores:\nValor Final = V0 * 1,10 * 1,20 = V0 * 1,32 -> Aumento real de 32%!\nDa mesma forma, um aumento de 25% seguido de um desconto de 20% retorna exatamente ao valor original, pois 1,25 * 0,80 = 1,00!"
                }
            ],
            "quiz": [
                {
                    "question": "Uma mercadoria que custava R$ 200,00 sofreu um aumento de 20% em janeiro e, em seguida, uma liquidação com desconto de 15% em fevereiro. Qual é o preço final do produto?",
                    "options": [
                        "R$ 204,00",
                        "R$ 210,00",
                        "R$ 200,00",
                        "R$ 205,00"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Preço final = 200 * 1,20 * 0,85 = 240 * 0,85 = R$ 204,00."
                }
            ]
        },
        {
            "id": "mat-cap-08-variacao-percentual",
            "number": 8,
            "title": "8. Variação Percentual e Análise Crítica de Índices",
            "epigraph": {
                "text": "Variação percentual mede o quanto uma grandeza mudou em relação ao seu valor inicial de referência. No ENEM, identificar a base de comparação correta evita o distrator mais frequente.",
                "author": "Estatística Econômica no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Fórmula Universal da Variação Percentual (Delta %)"
                },
                {
                    "type": "paragraph",
                    "content": "A variação percentual mede a mudança relativa de um valor inicial (Vi) para um valor final (Vf):\nDelta % = [(Vf - Vi) / Vi] * 100%.\nSe o resultado for positivo, houve crescimento percentual; se for negativo, houve redução percentual. O ponto crítico é SEMPRE dividir pelo valor INICIAL (a base de comparação), nunca pelo final."
                },
                {
                    "type": "callout",
                    "title": "Diferença Vital: 'Pontos Percentuais' vs 'Variação Percentual'",
                    "content": "Se a taxa de desemprego passa de 10% para 12%:\n• Ela subiu 2 PONTOS PERCENTUAIS (12% - 10% = 2 p.p.).\n• Ela teve uma VARIAÇÃO PERCENTUAL de 20% (pois (12 - 10) / 10 = 2 / 10 = 0,20 = 20%). O ENEM adora explorar essa confusão em gráficos da imprensa!"
                }
            ],
            "quiz": [
                {
                    "question": "As vendas de uma livraria passaram de 400 exemplares em março para 500 exemplares em abril. Qual foi a taxa percentual de aumento nas vendas?",
                    "options": [
                        "25%",
                        "20%",
                        "30%",
                        "15%"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Delta % = (500 - 400) / 400 = 100 / 400 = 0,25 = 25%."
                }
            ]
        },
        {
            "id": "mat-cap-09-juros-simples-compostos",
            "number": 9,
            "title": "9. Juros Simples versus Juros Compostos: Curvas de Crescimento",
            "epigraph": {
                "text": "Juros simples crescem em linha reta (progressão aritmética). Juros compostos crescem em curva exponencial acelerada (progressão geométrica). O ENEM cobra a comparação direta entre as duas modalidades.",
                "author": "Guia de Matemática Financeira"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Mecânica dos Juros Simples"
                },
                {
                    "type": "paragraph",
                    "content": "Nos juros simples, a taxa de juros (i) incide SEMPRE e exclusivamente sobre o Capital Inicial (C), durante todo o tempo de aplicação (t):\n• Juros: J = C * i * t\n• Montante final: M = C + J = C * (1 + i * t)\nImportante: a taxa 'i' e o tempo 't' precisam estar rigorosamente na mesma unidade de tempo (se a taxa for ao mês, o tempo deve estar em meses; se a taxa for ao ano, o tempo em anos)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Mecânica dos Juros Compostos (Juros sobre Juros)"
                },
                {
                    "type": "paragraph",
                    "content": "Nos juros compostos, a taxa incide sobre o saldo acumulado do período anterior (capital + juros passados):\n• Montante final: M = C * (1 + i)^t\n• Juros acumulados: J = M - C = C * [(1 + i)^t - 1]\nEsse é o regime utilizado universalmente no sistema financeiro real: cartões de crédito, cheque especial, poupança, tesouro direto e empréstimos bancários."
                },
                {
                    "type": "callout",
                    "title": "Comparativo Visual no Gráfico do ENEM",
                    "content": "• No período t = 0: Ambos partem do Capital C.\n• No período t = 1: Juros simples e compostos rendem exatamente o MESMO montante!\n• Para t > 1: Os juros compostos superam exponencialmente os juros simples, formando uma curva côncava para cima, enquanto os juros simples formam uma reta."
                }
            ],
            "quiz": [
                {
                    "question": "Um capital de R$ 1.000,00 foi aplicado a juros compostos à taxa de 10% ao mês durante 2 meses. Qual o montante gerado ao final do período?",
                    "options": [
                        "R$ 1.210,00",
                        "R$ 1.200,00",
                        "R$ 1.220,00",
                        "R$ 1.150,00"
                    ],
                    "correctAnswer": 0,
                    "explanation": "M = C * (1 + i)^t = 1000 * (1 + 0,10)^2 = 1000 * (1,10)^2 = 1000 * 1,21 = R$ 1.210,00."
                }
            ]
        },
        {
            "id": "mat-cap-10-inflacao-financiamentos",
            "number": 10,
            "title": "10. Inflação, Financiamentos, Parcelamentos e Investimentos",
            "epigraph": {
                "text": "Comprar à vista com desconto ou a prazo em parcelas sem juros aparentes? A resposta está no cálculo do custo de oportunidade e da taxa implícita de juros.",
                "author": "Educação Financeira no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Ilusão das 'Parcelas Sem Juros' no Comércio"
                },
                {
                    "type": "paragraph",
                    "content": "Uma questão clássica do ENEM traz um produto anunciado por R$ 100,00 à vista ou em 2 vezes de R$ 50,00 (uma entrada de R$ 50,00 no ato e outra parcela de R$ 50,00 após 30 dias). Parece que não há juros, mas se a loja oferece 10% de desconto à vista (R$ 90,00):\n• Se você optar pelo parcelamento: você dá R$ 50,00 de entrada.\n• O valor que você realmente está financiando é 90 - 50 = R$ 40,00.\n• Ao pagar R$ 50,00 após um mês, você está pagando R$ 10,00 de juros sobre uma dívida de R$ 40,00!\n• Taxa real de juros da operação: 10 / 40 = 0,25 = 25% ao mês! Uma taxa absurda disfarçada de 'sem juros'."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Inflação e Poder de Compra: Taxa Real vs Taxa Nominal"
                },
                {
                    "type": "paragraph",
                    "content": "A inflação mede a perda do poder de compra da moeda. Se um investimento rende 10% ao ano (taxa nominal) e a inflação do período foi de 6%, o rendimento real NÃO é 10 - 6 = 4%. Pela Equação de Fisher:\n(1 + i_nominal) = (1 + i_real) * (1 + inflação)\nLogo, (1 + i_real) = 1,10 / 1,06 ~= 1,0377 -> rendimento real de aproximadamente 3,77%."
                }
            ],
            "quiz": [
                {
                    "question": "Um eletrodoméstico custa R$ 500,00 à vista. A loja oferece a opção de pagar em duas parcelas de R$ 260,00: a primeira como entrada no ato da compra e a segunda após 30 dias. Qual é a taxa de juros mensal cobrada nesse parcelamento?",
                    "options": [
                        "8,33%",
                        "4,00%",
                        "10,00%",
                        "5,50%"
                    ],
                    "correctAnswer": 0,
                    "explanation": "À vista: R$ 500,00. Dando R$ 260,00 de entrada, a dívida financiada fica em 500 - 260 = R$ 240,00. Após 30 dias, paga-se R$ 260,00, gerando juros de 260 - 240 = R$ 20,00. Taxa de juros = 20 / 240 = 1 / 12 ~= 0,0833 = 8,33% ao mês."
                }
            ]
        },
        {
            "id": "mat-cap-11-custo-receita-lucro",
            "number": 11,
            "title": "11. Custo, Receita, Lucro e Ponto de Equilíbrio",
            "epigraph": {
                "text": "Lucro = Receita - Custo Total. O Ponto de Equilíbrio (Break-Even Point) é o instante exato em que a empresa não tem lucro nem prejuízo: o faturamento cobre exatamente todos os custos.",
                "author": "Matemática Aplicada aos Negócios"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Modelagem Algébrica da Produção Empresarial"
                },
                {
                    "type": "paragraph",
                    "content": "Toda atividade produtiva é descrita por três funções essenciais em função da quantidade produzida e vendida (x):\n1. Custo Total: C(x) = Custo Fixo + (Custo Variável Unitário * x). O custo fixo independe da produção (aluguel, salários administrativos); o custo variável varia diretamente com x (matéria-prima, energia de maquinário).\n2. Receita Total: R(x) = Preço de Venda Unitário * x.\n3. Lucro Total: L(x) = R(x) - C(x).\nNo Ponto de Equilíbrio: L(x) = 0 => R(x) = C(x)."
                },
                {
                    "type": "callout",
                    "title": "Conexão com Funções Afins e Quadráticas no ENEM",
                    "content": "Se o preço de venda é constante, a Receita e o Custo são funções afins (retas). Mas quando o preço de venda cai conforme a quantidade aumenta (demanda elástica), a Receita vira uma parábola com concavidade para baixo, e o Lucro Máximo é atingido no VÉRTICE da parábola!"
                }
            ],
            "quiz": [
                {
                    "question": "Uma microempresa tem custo fixo mensal de R$ 3.000,00 e custo variável de R$ 20,00 por camiseta produzida. Cada camiseta é vendida por R$ 50,00. Quantas camisetas a empresa precisa vender mensalmente para atingir o ponto de equilíbrio?",
                    "options": [
                        "100 camisetas",
                        "150 camisetas",
                        "60 camisetas",
                        "120 camisetas"
                    ],
                    "correctAnswer": 0,
                    "explanation": "C(x) = 3000 + 20x. R(x) = 50x. Ponto de equilíbrio: R(x) = C(x) => 50x = 3000 + 20x => 30x = 3000 => x = 100 camisetas."
                }
            ]
        }
    ]
