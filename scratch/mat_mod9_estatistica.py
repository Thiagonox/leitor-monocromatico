# -*- coding: utf-8 -*-
"""Módulo 9: Estatística Descritiva (Capítulos 34 a 37)"""

def get_chapters():
    return [
        {
            "id": "mat-cap-34-tabelas-graficos-estatistica",
            "number": 34,
            "title": "34. Leitura Crítica de Tabelas e Gráficos no ENEM",
            "epigraph": {
                "text": "Estatística representa em média 6 a 8 questões por edição no ENEM. A prova testa a sua capacidade de interpretar dados de pesquisas demográficas, econômicas, ambientais e de saúde.",
                "author": "Matriz de Estatística do INEP"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Tipos Fundamentais de Gráficos e Suas Armadilhas"
                },
                {
                    "type": "paragraph",
                    "content": "1. Gráficos de Colunas ou Barras: Ideais para comparar categorias discretas (produção por estado, vendas por marca). Cuidado com o truncamento do eixo vertical (quando o eixo não começa no zero, distorcendo visualmente as diferenças).\n2. Gráficos de Linhas: Perfeitos para mostrar evolução temporal contínua (séries temporais: PIB ao longo dos anos, variação diária de casos de gripe).\n3. Gráficos de Setores (Pizza): Indicam partes de um todo (composição percentual). Lembre-se da conversão angular: 100% = 360°, logo 10% = 36°, 25% = 90°, 50% = 180°.\n4. Histogramas: Gráficos de colunas contíguas (sem espaço entre elas) representando intervalos de classes de dados contínuos (faixas etárias, faixas salariais)."
                }
            ],
            "quiz": [
                {
                    "question": "Em um gráfico de setores representando as fontes de energia de uma cidade, o setor correspondente à energia solar possui um ângulo central de 72°. Qual é a porcentagem correspondente da energia solar na matriz dessa cidade?",
                    "options": [
                        "20%",
                        "25%",
                        "15%",
                        "18%"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Como a circunferência completa tem 360° correspondendo a 100%: Porcentagem = (72° / 360°) * 100% = (1/5) * 100% = 20%."
                }
            ]
        },
        {
            "id": "mat-cap-35-medias-aritmetica-ponderada",
            "number": 35,
            "title": "35. Médias: Aritmética Simples e Ponderada",
            "epigraph": {
                "text": "Média é o valor que sintetiza um conjunto de dados equilibrando as discrepâncias. A média ponderada atribui importâncias (pesos) diferenciados a cada valor.",
                "author": "Guia de Estatística do ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Média Aritmética Simples vs Ponderada"
                },
                {
                    "type": "paragraph",
                    "content": "• Média Aritmética Simples (X_barra): É a soma de todos os n valores dividida pelo número total de valores:\nX_barra = (x1 + x2 + ... + xn) / n.\nAtalho vital do ENEM: Soma Total = n * X_barra. Se a média de idade de 10 pessoas é 25 anos, a soma das idades de todas elas juntas é 10 * 25 = 250 anos!\n• Média Ponderada (Xp): Cada elemento xi possui um peso associado pi:\nXp = (x1*p1 + x2*p2 + ... + xn*pn) / (p1 + p2 + ... + pn).\nAtenção fatal: O denominador é SEMPRE a soma dos pesos, nunca a quantidade de disciplinas ou notas!"
                }
            ],
            "quiz": [
                {
                    "question": "Em um concurso, a prova de Matemática tem peso 3, Redação tem peso 2 e Conhecimentos Gerais tem peso 1. Um candidato obteve notas 8,0 em Matemática, 9,0 em Redação e 6,0 em Conhecimentos Gerais. Qual foi a sua média final ponderada?",
                    "options": [
                        "8,0",
                        "7,8",
                        "8,2",
                        "7,6"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Soma dos pesos = 3 + 2 + 1 = 6. Média ponderada = (8*3 + 9*2 + 6*1) / 6 = (24 + 18 + 6) / 6 = 48 / 6 = 8,0."
                }
            ]
        },
        {
            "id": "mat-cap-36-moda-mediana",
            "number": 36,
            "title": "36. Moda e Mediana: Medidas de Tendência Central",
            "epigraph": {
                "text": "Ao contrário da média, a mediana não é distorcida por valores discrepantes extremos. É o número que ocupa exatamente o centro do conjunto quando os dados estão em ordem crescente.",
                "author": "Estatística Não Paramétrica no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Moda (Mo): O Valor Mais Frequente"
                },
                {
                    "type": "paragraph",
                    "content": "A Moda é simplesmente o valor que aparece com maior frequência no conjunto de dados:\n• Conjunto Unimodal: Possui apenas uma moda única.\n• Bimodal: Dois valores empatam com a frequência máxima.\n• Amodal: Todos os valores aparecem com a mesma frequência (nenhum se destaca)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Mediana (Md): O Ponto Médio do Rol"
                },
                {
                    "type": "paragraph",
                    "content": "PASSO OBRIGATÓRIO: Colocar TODOS os dados em ordem crescente ou decrescente (construir o ROL)!\n• Se a quantidade n de elementos for ÍMPAR: a mediana é exatamente o elemento central de posição (n + 1) / 2.\n• Se a quantidade n de elementos for PAR: existem dois elementos centrais nas posições (n/2) e (n/2 + 1). A mediana é a MÉDIA ARITMÉTICA desses dois valores centrais."
                }
            ],
            "quiz": [
                {
                    "question": "Considere o conjunto de notas de 8 alunos em um simulado: 4, 7, 5, 9, 7, 6, 8, 8. Qual é a mediana dessas notas?",
                    "options": [
                        "7,0",
                        "6,5",
                        "7,5",
                        "6,8"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Colocando os 8 valores em ordem crescente (Rol): 4, 5, 6, 7, 7, 8, 8, 9. Como n = 8 (par), os termos centrais são o 4º e o 5º termos: 7 e 7. Mediana = (7 + 7) / 2 = 7,0."
                }
            ]
        },
        {
            "id": "mat-cap-37-variancia-desvio-padrao",
            "number": 37,
            "title": "37. Medidas de Dispersão: Amplitude, Variância e Desvio Padrão",
            "epigraph": {
                "text": "Dois alunos podem ter a mesma média 7,0. Mas aquele com notas 7, 7 e 7 é muito mais 'regular' e 'homogêneo' do que o aluno com notas 10, 7 e 4. O desvio padrão mede essa regularidade.",
                "author": "Conceito Fundamental de Regularidade no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Amplitude, Variância e Desvio Padrão"
                },
                {
                    "type": "paragraph",
                    "content": "• Amplitude (A): É a diferença entre o maior e o menor valor do conjunto: A = X_max - X_min.\n• Variância (Var ou sigma²): É a média aritmética dos quadrados das distâncias de cada dado em relação à média geral:\nVar = sum[(xi - X_barra)²] / n.\n• Desvio Padrão (DP ou sigma): É a raiz quadrada da variância: DP = raiz(Var). Tem a mesma unidade de medida dos dados originais."
                },
                {
                    "type": "callout",
                    "title": "A Pergunta Clássica do ENEM: Quem é o Mais Regular?",
                    "content": "O ENEM quase nunca pede para você calcular a fórmula completa da variância à mão com dezenas de números. O enunciado dá uma tabela com a média e o desvio padrão de cinco atletas ou máquinas e pergunta: 'Qual atleta teve o desempenho mais regular/homogêneo/confiável?'.\nResposta: Aquele que tiver o MENOR DESVIO PADRÃO (ou seja, cujos resultados ficaram mais próximos e concentrados em torno da média)!"
                }
            ],
            "quiz": [
                {
                    "question": "Cinco atiradores obtiveram a mesma pontuação média de 80 pontos em 10 disparos. Seus desvios padrão foram: Atirador I (DP = 4,2); Atirador II (DP = 1,8); Atirador III (DP = 5,6); Atirador IV (DP = 3,1); Atirador V (DP = 2,5). Qual atirador foi o mais regular?",
                    "options": [
                        "Atirador II",
                        "Atirador I",
                        "Atirador V",
                        "Atirador IV"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Maior regularidade (ou homogeneidade) corresponde rigorosamente ao MENOR desvio padrão. O Atirador II possui o menor DP (1,8)."
                }
            ]
        }
    ]
