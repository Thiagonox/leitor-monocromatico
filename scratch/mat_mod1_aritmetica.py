# -*- coding: utf-8 -*-
"""Módulo 1: Matemática Básica e Aritmética (Capítulos 1 a 6)"""

def get_chapters():
    return [
        {
            "id": "mat-cap-01-operacoes-conjuntos",
            "number": 1,
            "title": "1. Operações Fundamentais, Frações e Decimais no ENEM",
            "epigraph": {
                "text": "A Matemática básica responde por mais de 40% das questões do ENEM. Dominar o cálculo ágil e seguro é o passaporte direto para superar os 800 pontos na TRI.",
                "author": "Guia de Estratégia de Prova ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Base da Pirâmide da TRI: Por Onde os Pontos Realmente Escorrem"
                },
                {
                    "type": "paragraph",
                    "content": "Na Teoria de Resposta ao Item (TRI) adotada pelo ENEM, as questões são calibradas em três níveis: fáceis, médias e difíceis. Uma questão de trigonometria complexa ou logaritmo vale quase nada se você errar uma questão de divisão de frações ou leitura de números decimais. O algoritmo interpreta o acerto na questão difícil e o erro na fácil como 'chute' (acerto ao acaso), derrubando a sua nota. Por isso, a aritmética básica não é apenas um pré-requisito técnico: ela é a fundação da sua nota máxima."
                },
                {
                    "type": "paragraph",
                    "content": "Os conjuntos numéricos estruturam todo o raciocínio quantitativo: os Números Naturais (N = {0, 1, 2, ...}) modelam contagens inteiras; os Inteiros (Z = {..., -2, -1, 0, 1, 2, ...}) introduzem saldos negativos, fusos horários e variações de temperatura; os Racionais (Q = {a/b, com b != 0}) representam frações e decimais finitos ou dízimas periódicas; e os Reais (R) englobam também os irracionais como pi e raiz de 2."
                },
                {
                    "type": "callout",
                    "title": "Regra de Ouro no ENEM: Operações com Frações sem Perder Tempo",
                    "content": "• Soma e Subtração: frações com denominadores diferentes exigem MMC ou o método da borboleta cruzada (a/b + c/d = (a*d + b*c)/(b*d)).\n• Multiplicação: direto numerador com numerador e denominador com denominador ((a/b)*(c/d) = (a*c)/(b*d)). Simplifique SEMPRE antes de multiplicar.\n• Divisão: conserva a primeira e multiplica pelo inverso da segunda ((a/b) / (c/d) = (a/b) * (d/c))."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Números Decimais e Transformação Fracionária"
                },
                {
                    "type": "paragraph",
                    "content": "No ENEM, quase todas as situações cotidianas (preço por litro de combustível, massa de medicamentos em miligramas, dosagens de adubos por hectare) vêm expressas em números decimais. O erro mais recorrente é o alinhamento da vírgula na adição e na subtração, ou a contagem errônea de casas decimais na multiplicação (por exemplo, 0,2 * 0,03 = 0,006, pois somamos 1 casa com 2 casas decimais = 3 casas decimais)."
                },
                {
                    "type": "quote",
                    "content": "Nunca divida números com vírgula direto: multiplique dividendo e divisor por potências de 10 até eliminar todas as vírgulas. Dividir 4,8 por 0,12 é exatamente o mesmo que dividir 480 por 12 = 40.",
                    "author": "Gatilho de Prova de Matemática"
                }
            ],
            "quiz": [
                {
                    "question": "Um atleta consome 3/5 de uma garrafa de 750 mL de isotônico no primeiro tempo de uma partida e 1/3 do restante no intervalo. Quantos mililitros de isotônico restaram na garrafa?",
                    "options": [
                        "200 mL",
                        "150 mL",
                        "100 mL",
                        "250 mL"
                    ],
                    "correctAnswer": 0,
                    "explanation": "No 1º tempo, ele consome (3/5) * 750 = 450 mL. Sobram 750 - 450 = 300 mL. No intervalo, consome 1/3 de 300 mL = 100 mL. Portanto, restam 300 - 100 = 200 mL."
                }
            ]
        },
        {
            "id": "mat-cap-02-potencias-notacao",
            "number": 2,
            "title": "2. Potenciação, Radiciação e Notação Científica no ENEM",
            "epigraph": {
                "text": "O ENEM adora grandezas microscópicas (como o diâmetro do vírus ou a massa do elétron) e grandezas astronômicas (como a distância da Terra ao Sol ou o orçamento federal). A notação científica é a linguagem oficial dessas questões.",
                "author": "Matriz de Competências do INEP"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Propriedades Fundamentais de Potenciação"
                },
                {
                    "type": "paragraph",
                    "content": "A potenciação sintetiza produtos de fatores iguais: a^n = a * a * ... * a (n vezes). As propriedades que você precisa executar de olhos fechados na prova são:\n1. Produto de mesma base: a^m * a^n = a^(m+n)\n2. Divisão de mesma base: a^m / a^n = a^(m-n)\n3. Potência de potência: (a^m)^n = a^(m*n)\n4. Potência de produto ou quociente: (a*b)^n = a^n * b^n e (a/b)^n = a^n / b^n\n5. Expoente negativo: a^(-n) = 1 / (a^n)\n6. Expoente fracionário (ponte com radiciação): a^(m/n) = raiz n-ésima de a^m ('o que está no sol vai para a sombra, o que está na sombra vai para o sol')."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Notação Científica e Ordem de Grandeza"
                },
                {
                    "type": "paragraph",
                    "content": "A forma canônica de um número em notação científica é dada por: N = a * 10^k, onde 1 <= a < 10 (o coeficiente 'a' deve ser estritamente maior ou igual a 1 e estritamente menor que 10) e k é um número inteiro. Para números muito grandes, deslocamos a vírgula para a esquerda e o expoente k fica positivo. Para números minúsculos (menores que 1), deslocamos a vírgula para a direita e o expoente k fica negativo."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha Clássica do Distrator no ENEM: Ordem de Grandeza",
                    "content": "Para encontrar a ordem de grandeza de N = a * 10^k:\n• Se a < raiz de 10 (~3,16), a ordem de grandeza é 10^k.\n• Se a >= raiz de 10 (~3,16), a ordem de grandeza é 10^(k+1).\nExemplo: 4 * 10^6 tem ordem de grandeza 10^7, porque 4 >= 3,16!"
                }
            ],
            "quiz": [
                {
                    "question": "Um nanômetro equivale a 10^(-9) metros. Uma molécula tem comprimento médio de 45 nanômetros. Como esse valor é expresso corretamente em notação científica em metros?",
                    "options": [
                        "4,5 * 10^(-8) m",
                        "45 * 10^(-9) m",
                        "4,5 * 10^(-10) m",
                        "0,45 * 10^(-7) m"
                    ],
                    "correctAnswer": 0,
                    "explanation": "45 nm = 45 * 10^(-9) m = (4,5 * 10^1) * 10^(-9) = 4,5 * 10^(1 - 9) = 4,5 * 10^(-8) m."
                }
            ]
        },
        {
            "id": "mat-cap-03-mmc-mdc",
            "number": 3,
            "title": "3. Múltiplos, Divisores, MMC e MDC em Situações Cotidianas",
            "epigraph": {
                "text": "Quando dois ou mais eventos periódicos se repetem e você precisa descobrir quando eles vão coincidir de novo: pense em MMC. Quando você precisa dividir ou repartir recursos em partes iguais e máximas: pense em MDC.",
                "author": "Gatilho de Identificação de Enunciado"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Como Reconhecer se a Questão Pede MMC ou MDC"
                },
                {
                    "type": "paragraph",
                    "content": "O ENEM quase nunca escreve as palavras 'calcule o MMC' ou 'calcule o MDC'. A prova traz historinhas do cotidiano. Você precisa decodificar o gatilho semântico do enunciado:\n• Gatilhos de MMC: 'De quanto em quanto tempo se encontram novamente?', 'Quando as luzes piscam juntas de novo?', 'Três remédios tomados em horários diferentes que serão ingeridos juntos no mesmo horário'.\n• Gatilhos de MDC: 'Dividir em lotes com o maior tamanho possível', 'Cortar tecidos ou tábuas sem sobras no maior comprimento comum', 'Agrupar pessoas em equipes com o mesmo número de integrantes sem misturar categorias'."
                },
                {
                    "type": "callout",
                    "title": "Técnica de Fatoração Simultânea Ágil",
                    "content": "Para calcular MMC e MDC ao mesmo tempo: fature os números por fatores primos simultaneamente. O MMC é o produto de TODOS os fatores primos até que todos os números cheguem a 1. O MDC é o produto APENAS daqueles fatores primos que dividiram todos os números ao mesmo tempo naquela linha!"
                }
            ],
            "quiz": [
                {
                    "question": "Três linhas de ônibus A, B e C passam em um mesmo terminal a cada 12, 15 e 20 minutos, respectivamente. Se às 8h00 os três ônibus partiram simultaneamente, qual será o próximo horário em que eles partirão juntos de novo?",
                    "options": [
                        "9h00",
                        "9h15",
                        "8h45",
                        "9h30"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Calculamos o MMC(12, 15, 20): 12 = 2^2 * 3; 15 = 3 * 5; 20 = 2^2 * 5. MMC = 2^2 * 3 * 5 = 60 minutos (1 hora). 8h00 + 1h = 9h00."
                }
            ]
        },
        {
            "id": "mat-cap-04-razao-proporcao",
            "number": 4,
            "title": "4. Razão, Proporção e Divisão Proporcional",
            "epigraph": {
                "text": "Razão é a comparação entre duas grandezas por meio de uma divisão. Proporção é a igualdade entre duas razões. Essa ferramenta simples resolve cerca de 8 a 10 questões por prova no ENEM.",
                "author": "Estatística da Matriz do ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Razões Especiais que o ENEM Adora"
                },
                {
                    "type": "paragraph",
                    "content": "No mundo real e nas questões interdisciplinares do ENEM, certas razões recebem nomes consagrados pela ciência e pela economia:\n1. Velocidade Média: Razão entre o deslocamento e o intervalo de tempo (v = delta_s / delta_t).\n2. Densidade Demográfica: Razão entre o número de habitantes e a área territorial em km² (Hab/km²).\n3. Massa Específica / Densidade: Razão entre a massa de um corpo e seu volume (d = m / V).\n4. Concentração Comum: Razão entre a massa de soluto e o volume da solução (C = m / V em g/L).\n5. Consumo de Combustível: Razão entre a distância percorrida e o volume de combustível gasto (km/L)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Divisão em Partes Diretamente e Inversamente Proporcionais"
                },
                {
                    "type": "paragraph",
                    "content": "Dividir uma quantia Q em partes proporcionais aos números a, b e c significa encontrar x, y e z tais que x/a = y/b = z/c = k (onde k é a constante de proporcionalidade). Logo, x = a*k, y = b*k, z = c*k, e a soma x + y + z = Q.\nQuando a divisão é INVERSAMENTE proporcional a a, b e c, ela equivale a ser DIRETAMENTE proporcional aos inversos (1/a, 1/b, 1/c). Exemplo clássico do ENEM: bônus financeiro dividido inversamente ao número de faltas dos funcionários!"
                }
            ],
            "quiz": [
                {
                    "question": "Um prêmio de R$ 60.000,00 deve ser dividido entre dois funcionários de forma diretamente proporcional ao tempo de serviço de cada um na empresa. O funcionário A trabalha há 3 anos e o funcionário B há 7 anos. Quanto receberá o funcionário B?",
                    "options": [
                        "R$ 42.000,00",
                        "R$ 18.000,00",
                        "R$ 35.000,00",
                        "R$ 40.000,00"
                    ],
                    "correctAnswer": 0,
                    "explanation": "A soma das partes é 3 + 7 = 10 partes. Cada parte k vale 60.000 / 10 = R$ 6.000,00. O funcionário B tem 7 partes: 7 * 6.000 = R$ 42.000,00."
                }
            ]
        },
        {
            "id": "mat-cap-05-regra-de-tres",
            "number": 5,
            "title": "5. Regra de Três Simples e Composta: O Método das Grandezas",
            "epigraph": {
                "text": "O segredo da regra de três não é cruzar em 'X' automaticamente. O segredo é identificar se as grandezas são diretamente ou inversamente proporcionais antes de armar a proporção.",
                "author": "Mestre de Questões ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Grandezas Diretamente vs Inversamente Proporcionais"
                },
                {
                    "type": "paragraph",
                    "content": "Duas grandezas são DIRETAMENTE proporcionais quando o aumento de uma acarreta o aumento da outra na mesma proporção (se uma dobra, a outra dobra). Exemplo: quantidade de combustível e distância percorrida; massa de farinha e quantidade de pães produzidos.\nDuas grandezas são INVERSAMENTE proporcionais quando o aumento de uma provoca a redução proporcional da outra (se uma dobra, a outra cai pela metade). Exemplo: velocidade de um carro e tempo de viagem; número de operários trabalhando no mesmo ritmo e dias necessários para concluir uma obra."
                },
                {
                    "type": "callout",
                    "title": "Método Infalível para Regra de Três Composta",
                    "content": "1. Isole a grandeza que contém a incógnita 'x' no lado esquerdo da igualdade.\n2. Compare cada uma das outras grandezas isoladamente com a grandeza de 'x':\n   - Se for diretamente proporcional, mantenha a fração original no produto do lado direito.\n   - Se for inversamente proporcional, inverta a fração no produto do lado direito.\n3. Isole o 'x' e simplifique antes de multiplicar os números grandes!"
                }
            ],
            "quiz": [
                {
                    "question": "Se 6 operários constroem um muro de 120 metros em 8 dias, quantos operários de mesma capacidade seriam necessários para construir um muro de 180 metros em 6 dias?",
                    "options": [
                        "12 operários",
                        "10 operários",
                        "9 operários",
                        "15 operários"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Incógnita: Operários (6/x). Muro maior -> mais operários (direta: 120/180). Menos dias -> mais operários (inversa: 6/8). Equação: 6/x = (120/180) * (6/8) = (2/3) * (3/4) = 2/4 = 1/2. Logo, 6/x = 1/2 => x = 12 operários."
                }
            ]
        },
        {
            "id": "mat-cap-06-escalas",
            "number": 6,
            "title": "6. Escalas Cartográficas, Lineares, Superficiais e Volumétricas",
            "epigraph": {
                "text": "Escala linear cai todo ano no ENEM sem exceção. O grande distrator é esquecer que área varia com o quadrado da escala e volume varia com o cubo da escala.",
                "author": "Alerta de Distrator ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Definição de Escala Linear (E)"
                },
                {
                    "type": "paragraph",
                    "content": "A escala linear é a razão constante entre a medida no mapa, desenho ou maquete (d) e a medida real correspondente (D), ambas expressas rigorosamente na MESMA unidade de medida:\nE = d / D.\nSe a escala de uma planta é 1 : 50, significa que 1 cm no papel equivale a 50 cm no mundo real (0,5 metros)."
                },
                {
                    "type": "callout",
                    "title": "A Armadilha Fatal do ENEM: Escalas de Área e Volume",
                    "content": "Se a escala linear de comprimento é E = d / D:\n• Escala de Área (superfície): Razão entre as áreas = E² = (d / D)².\n• Escala de Volume (capacidade): Razão entre os volumes = E³ = (d / D)³.\nExemplo: Se um mapa tem escala 1 : 100, uma sala de 2 cm² no papel tem área real de 2 * (100)² = 2 * 10.000 = 20.000 cm² = 2 m²!"
                }
            ],
            "quiz": [
                {
                    "question": "Em um mapa construído na escala 1 : 250.000, a distância em linha reta entre duas cidades é de 8 cm. Qual é a distância real entre essas duas cidades em quilômetros?",
                    "options": [
                        "20 km",
                        "2 km",
                        "200 km",
                        "25 km"
                    ],
                    "correctAnswer": 0,
                    "explanation": "D = d / E = 8 cm * 250.000 = 2.000.000 cm. Como 1 m = 100 cm, 2.000.000 cm = 20.000 m. Como 1 km = 1.000 m, 20.000 m = 20 km."
                }
            ]
        }
    ]
