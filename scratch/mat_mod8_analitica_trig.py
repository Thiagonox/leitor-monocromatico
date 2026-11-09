# -*- coding: utf-8 -*-
"""Módulo 8: Geometria Analítica e Trigonometria (Capítulos 31 a 33)"""

def get_chapters():
    return [
        {
            "id": "mat-cap-31-geometria-analitica-reta",
            "number": 31,
            "title": "31. Geometria Analítica: Ponto, Distância, Ponto Médio e Equação da Reta",
            "epigraph": {
                "text": "A Geometria Analítica de Descartes une a álgebra e a geometria: cada ponto do plano é um par ordenado (x, y), e cada linha é uma equação.",
                "author": "Guia de Geometria Analítica ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Ponto no Plano, Distância e Ponto Médio"
                },
                {
                    "type": "paragraph",
                    "content": "Dados dois pontos A(xA, yA) e B(xB, yB) no plano cartesiano:\n• Ponto Médio (M): O ponto central equidistante de A e B tem coordenadas dadas pela média aritmética das coordenadas:\nxM = (xA + xB) / 2 e yM = (yA + yB) / 2.\n• Distância entre Dois Pontos (d_AB): É a aplicação direta do Teorema de Pitágoras no plano cartesiano:\nd_AB = raiz[ (xB - xA)² + (yB - yA)² ]."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Equações da Reta e Coeficiente Angular"
                },
                {
                    "type": "paragraph",
                    "content": "• Coeficiente Angular (m ou a): Mede a inclinação (tangente do ângulo theta formado com o semi-eixo positivo X):\nm = delta_y / delta_x = (yB - yA) / (xB - xA).\n• Equação Fundamental (Ponto-Inclinação): y - y0 = m * (x - x0).\n• Equação Reduzida: y = mx + n (onde m é o coeficiente angular e n é o coeficiente linear, ponto (0, n)).\n• Condição de Paralelismo: Duas retas r e s são paralelas se e somente se mr = ms.\n• Condição de Perpendicularismo: Duas retas r e s são perpendiculares se e somente se mr * ms = -1 (ou ms = -1 / mr)."
                }
            ],
            "quiz": [
                {
                    "question": "Em um sistema de coordenadas cartesianas onde as medidas estão em quilômetros, duas antenas transmissoras estão localizadas nos pontos A(1, 2) e B(7, 10). Qual é a distância em linha reta entre essas duas antenas?",
                    "options": [
                        "10 km",
                        "14 km",
                        "12 km",
                        "8 km"
                    ],
                    "correctAnswer": 0,
                    "explanation": "d = raiz[ (7 - 1)² + (10 - 2)² ] = raiz[ 6² + 8² ] = raiz[ 36 + 64 ] = raiz[ 100 ] = 10 km."
                }
            ]
        },
        {
            "id": "mat-cap-32-trigonometria-triangulo-retangulo",
            "number": 32,
            "title": "32. Trigonometria no Triângulo Retângulo: Seno, Cosseno e Tangente",
            "epigraph": {
                "text": "SOH-CAH-TOA: Seno = Oposto / Hipotenusa; Cosseno = Adjacente / Hipotenusa; Tangente = Oposto / Adjacente. Três razões que resolvem qualquer rampa, telhado ou ângulo visual no ENEM.",
                "author": "Mnemônica Clássica de Trigonometria"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Definições das Razões Trigonométricas"
                },
                {
                    "type": "paragraph",
                    "content": "Em um triângulo retângulo com um ângulo agudo theta:\n• sen(theta) = Cateto Oposto / Hipotenusa\n• cos(theta) = Cateto Adjacente / Hipotenusa\n• tg(theta) = Cateto Oposto / Cateto Adjacente = sen(theta) / cos(theta)\nRelação Fundamental da Trigonometria: sen²(theta) + cos²(theta) = 1 (válida para todo e qualquer ângulo!)."
                },
                {
                    "type": "callout",
                    "title": "Tabela de Ângulos Notáveis (30°, 45° e 60°) - Obrigatória!",
                    "content": "• Ângulo de 30°: sen = 1/2; cos = (raiz de 3)/2; tg = (raiz de 3)/3\n• Ângulo de 45°: sen = (raiz de 2)/2; cos = (raiz de 2)/2; tg = 1\n• Ângulo de 60°: sen = (raiz de 3)/2; cos = 1/2; tg = raiz de 3\nNote que sen(30°) = cos(60°) e sen(60°) = cos(30°), pois 30° e 60° são ângulos complementares (somam 90°)!"
                }
            ],
            "quiz": [
                {
                    "question": "Para acessar um hospital, constrói-se uma rampa reta de 20 metros de comprimento que forma um ângulo de 30° com o solo horizontal. A qual altura do solo a rampa conduz os pacientes?",
                    "options": [
                        "10 metros",
                        "17,3 metros",
                        "14,1 metros",
                        "8 metros"
                    ],
                    "correctAnswer": 0,
                    "explanation": "sen(30°) = Altura / Comprimento_da_rampa => 1/2 = h / 20 => h = 20 * (1/2) = 10 metros."
                }
            ]
        },
        {
            "id": "mat-cap-33-leis-senos-cossenos",
            "number": 33,
            "title": "33. Lei dos Senos e Lei dos Cossenos em Triângulos Quaisquer",
            "epigraph": {
                "text": "Quando o triângulo NÃO for retângulo, o Teorema de Pitágoras puro não se aplica. É o momento de convocar a Lei dos Senos ou a Lei dos Cossenos.",
                "author": "Trigonometria Avançada no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Quando Usar a Lei dos Senos vs Lei dos Cossenos"
                },
                {
                    "type": "paragraph",
                    "content": "O segredo de prova para escolher a lei certa sem perder tempo:\n• Use LEI DOS COSSENOS quando a questão fornecer (ou envolver) TRÊS LADOS e APENAS UM ÂNGULO:\na² = b² + c² - 2*b*c*cos(A).\nObserve que se o ângulo A fosse 90°, cos(90°) = 0 e a fórmula se transformaria no próprio Teorema de Pitágoras (a² = b² + c²)!\n• Use LEI DOS SENOS quando a questão fornecer DOIS ÂNGULOS e DOIS LADOS (ou o raio R da circunferência circunscrita):\na / sen(A) = b / sen(B) = c / sen(C) = 2R."
                }
            ],
            "quiz": [
                {
                    "question": "Em um triângulo qualquer, dois lados medem 5 cm e 8 cm, formando entre si um ângulo de 60°. Qual é a medida do terceiro lado desse triângulo?",
                    "options": [
                        "7 cm",
                        "6 cm",
                        "8 cm",
                        "9 cm"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Pela Lei dos Cossenos: a² = b² + c² - 2bc*cos(60°). a² = 5² + 8² - 2 * 5 * 8 * (1/2) = 25 + 64 - 40 = 89 - 40 = 49. Logo, a = raiz(49) = 7 cm."
                }
            ]
        }
    ]
