# -*- coding: utf-8 -*-
"""Módulo 6: Geometria Plana (Capítulos 22 a 26)"""

def get_chapters():
    return [
        {
            "id": "mat-cap-22-angulos-triangulos-pitagoras",
            "number": 22,
            "title": "22. Ângulos, Triângulos e o Teorema de Pitágoras",
            "epigraph": {
                "text": "A soma dos ângulos internos de qualquer triângulo no plano euclidiano é sempre 180°. O Teorema de Pitágoras é a relação métrica mais testada da história dos exames vestibulares.",
                "author": "Geometria Euclidiana no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Classificação e Condição de Existência de Triângulos"
                },
                {
                    "type": "paragraph",
                    "content": "Condição de Existência (Desigualdade Triangular): Para que três segmentos a, b e c formem um triângulo, o comprimento de qualquer lado deve ser estritamente menor que a soma dos outros dois e maior que o módulo da diferença: |b - c| < a < b + c.\nClassificação quanto aos lados: Equilátero (3 lados iguais e 3 ângulos de 60°), Isósceles (2 lados iguais e ângulos da base congruentes) e Escaleno (3 lados distintos).\nClassificação quanto aos ângulos: Acutângulo (3 ângulos < 90°), Retângulo (um ângulo de 90°) e Obtusângulo (um ângulo > 90°)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Teorema de Pitágoras e os Triângulos Notáveis"
                },
                {
                    "type": "paragraph",
                    "content": "Em todo triângulo retângulo de hipotenusa 'a' e catetos 'b' e 'c':\na² = b² + c².\nTriângulos Pitagóricos que você deve memorizar para poupar tempo de prova:\n• 3 - 4 - 5 (e seus múltiplos: 6-8-10, 9-12-15, 15-20-25, 30-40-50...)\n• 5 - 12 - 13\n• 8 - 15 - 17\n• 7 - 24 - 25."
                }
            ],
            "quiz": [
                {
                    "question": "Um poste de 12 metros de altura está perpendicular ao solo. Um cabo de sustentação deve ser fixado do topo do poste até um ponto no solo a 9 metros de distância da base do poste. Qual é o comprimento mínimo desse cabo?",
                    "options": [
                        "15 metros",
                        "14 metros",
                        "16 metros",
                        "13 metros"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Triângulo retângulo de catetos 12 e 9. Note que 9 = 3 * 3 e 12 = 4 * 3. Trata-se do triângulo pitagórico 3-4-5 multiplicado por 3: Hipotenusa = 5 * 3 = 15 metros (ou h² = 12² + 9² = 144 + 81 = 225 => h = 15 m)."
                }
            ]
        },
        {
            "id": "mat-cap-23-semelhanca-triangulos",
            "number": 23,
            "title": "23. Semelhança de Triângulos e Relações Métricas",
            "epigraph": {
                "text": "Se dois triângulos possuem os mesmos ângulos internos, seus lados homólogos (opostos aos mesmos ângulos) são proporcionais. É a base do cálculo de alturas inalcançáveis e sombras projetadas.",
                "author": "Teorema de Tales e Semelhança"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Critérios de Semelhança e Proporcionalidade de Tales"
                },
                {
                    "type": "paragraph",
                    "content": "Dois triângulos ABC e DEF são semelhantes (ABC ~ DEF) principalmente pelo caso Ângulo-Ângulo (AA): se dois ângulos de um triângulo são iguais a dois ângulos do outro, o terceiro é obrigatoriamente igual e os triângulos são semelhantes. A razão de semelhança k vale:\na / d = b / e = c / f = k.\nAtenção crucial: se os comprimentos lineares variam na razão k, as ÁREAS variam na razão k²!"
                },
                {
                    "type": "callout",
                    "title": "Relações Métricas no Triângulo Retângulo",
                    "content": "Seja a hipotenusa 'a', catetos 'b' e 'c', altura relativa à hipotenusa 'h', e projeções dos catetos 'm' e 'n':\n1. b² = a * m\n2. c² = a * n\n3. h² = m * n\n4. a * h = b * c (Hipotenusa vezes altura = cateto vezes cateto - fórmula salva-vidas no ENEM!)."
                }
            ],
            "quiz": [
                {
                    "question": "Uma pessoa de 1,80 m de altura projeta uma sombra de 1,20 m no solo no mesmo instante em que um edifício projeta uma sombra de 30 m. Qual é a altura desse edifício?",
                    "options": [
                        "45 metros",
                        "40 metros",
                        "50 metros",
                        "36 metros"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Por semelhança de triângulos retângulos: Altura_edificio / Sombra_edificio = Altura_pessoa / Sombra_pessoa => H / 30 = 1,80 / 1,20 = 1,5. Logo, H = 30 * 1,5 = 45 metros."
                }
            ]
        },
        {
            "id": "mat-cap-24-quadrilateros-poligonos",
            "number": 24,
            "title": "24. Quadriláteros e Polígonos Regulares",
            "epigraph": {
                "text": "Polígonos regulares possuem todos os lados e todos os ângulos congruentes. O hexágono regular, em especial, é formado por seis triângulos equiláteros perfeitos.",
                "author": "Mosaicos e Pavimentações no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Quadriláteros Notáveis: Propriedades e Hierarquia"
                },
                {
                    "type": "paragraph",
                    "content": "• Trapézio: Possui pelo menos um par de lados paralelos (base maior B e base menor b). Trapézio isósceles tem lados não paralelos iguais e diagonais iguais.\n• Paralelogramo: Lados opostos paralelos e congruentes. Ângulos opostos congruentes. As diagonais interceptam-se nos seus pontos médios.\n• Retângulo: Paralelogramo equiângulo (quatro ângulos de 90°). Suas diagonais são iguais.\n• Losango: Paralelogramo equilátero (quatro lados iguais). Suas diagonais são PERPENDICULARES entre si.\n• Quadrado: É simultaneamente retângulo e losango (quatro ângulos retos e quatro lados iguais)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Ângulos em Polígonos de n Lados"
                },
                {
                    "type": "paragraph",
                    "content": "• Soma dos Ângulos Internos: Si = (n - 2) * 180°\n• Soma dos Ângulos Externos: Se = 360° (para QUALQUER polígono convexo, não importa o número de lados!)\n• Ângulo Interno de polígono regular: ai = Si / n = [(n - 2) * 180°] / n\n• Número de Diagonais: d = [n * (n - 3)] / 2."
                }
            ],
            "quiz": [
                {
                    "question": "Qual é a medida do ângulo interno de um hexágono regular?",
                    "options": [
                        "120°",
                        "108°",
                        "135°",
                        "140°"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Para n = 6: Si = (6 - 2) * 180° = 4 * 180° = 720°. Como é regular, ai = 720° / 6 = 120°."
                }
            ]
        },
        {
            "id": "mat-cap-25-circunferencia-circulo",
            "number": 25,
            "title": "25. Circunferência, Círculo e Setores Circulares",
            "epigraph": {
                "text": "Circunferência é o contorno (comprimento C = 2*pi*R); círculo é a região interna preenchida (área A = pi*R²). Não confunda as duas grandezas.",
                "author": "Geometria Circular no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Comprimento e Área do Círculo"
                },
                {
                    "type": "paragraph",
                    "content": "• Raio (R) e Diâmetro (D): D = 2R.\n• Comprimento da Circunferência: C = 2 * pi * R = pi * D (onde pi ~= 3,14, ou frequentemente adotado como 3 ou 3,1 no ENEM para facilitar contas).\n• Área do Círculo: A = pi * R².\n• Aplicação clássica no ENEM: Número de voltas de uma roda ou esteira = Distância total / Comprimento da roda (C = 2*pi*R)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Setor Circular e Coroa Circular"
                },
                {
                    "type": "paragraph",
                    "content": "• Setor Circular (fatia de pizza com ângulo central theta em graus):\nÁrea do Setor = (theta / 360°) * pi * R²\nComprimento do Arco = (theta / 360°) * 2 * pi * R\n• Coroa Circular (espaço entre dois círculos concêntricos de raios R e r):\nÁrea da Coroa = pi * (R² - r²)."
                }
            ],
            "quiz": [
                {
                    "question": "Uma pista de atletismo circular tem raio de 50 metros. Um corredor completa 6 voltas completas nessa pista. Considerando pi = 3,14, qual a distância aproximada percorrida pelo atleta?",
                    "options": [
                        "1.884 metros",
                        "1.570 metros",
                        "942 metros",
                        "2.100 metros"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Comprimento de uma volta: C = 2 * pi * R = 2 * 3,14 * 50 = 314 metros. Para 6 voltas: Distância = 6 * 314 = 1.884 metros."
                }
            ]
        },
        {
            "id": "mat-cap-26-areas-perimetros-planas",
            "number": 26,
            "title": "26. Áreas e Perímetros de Figuras Planas: Decomposição e Otimização",
            "epigraph": {
                "text": "O ENEM quase nunca cobra uma figura geométrica isolada simples. Ele apresenta uma planta baixa irregular e exige que você decomponha a figura em retângulos, triângulos e semicírculos.",
                "author": "Competência 2 do ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Tabela Definitiva de Fórmulas de Área"
                },
                {
                    "type": "paragraph",
                    "content": "• Retângulo: A = base * altura = b * h\n• Quadrado: A = lado² = L² (e diagonal d = L * raiz de 2)\n• Triângulo qualquer: A = (base * altura) / 2\n• Triângulo equilátero de lado L: A = (L² * raiz de 3) / 4 (altura h = L * raiz de 3 / 2)\n• Paralelogramo: A = base * altura\n• Losango: A = (Diagonal maior * Diagonal menor) / 2 = (D * d) / 2\n• Trapézio: A = [(Base maior + Base menor) * altura] / 2 = [(B + b) * h] / 2\n• Hexágono regular de lado L: A = 6 * (L² * raiz de 3) / 4 = 3 * L² * raiz de 3 / 2."
                },
                {
                    "type": "callout",
                    "title": "Estratégia da Decomposição e Subtração de Áreas",
                    "content": "Ao encarar uma área hachurada (sombreada) irregular:\n1. Calcule a área da figura envolvente total (retângulo ou círculo maior).\n2. Subtraia as áreas 'vazias' que não fazem parte da região hachurada.\nEsse método é muito mais rápido e imune a erros do que tentar somar dezenas de pequenos pedaços irregulares!"
                }
            ],
            "quiz": [
                {
                    "question": "Deseja-se gramar um terreno retangular de 20 m por 15 m, exceto por uma piscina circular instalada no centro com raio de 3 m. Adotando pi = 3, qual é a área de grama necessária para cobrir o restante do terreno?",
                    "options": [
                        "273 m²",
                        "280 m²",
                        "255 m²",
                        "291 m²"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Área do retângulo: 20 * 15 = 300 m². Área da piscina circular: pi * R² = 3 * 3² = 3 * 9 = 27 m². Área gramada = 300 - 27 = 273 m²."
                }
            ]
        }
    ]
