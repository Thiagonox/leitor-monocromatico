# -*- coding: utf-8 -*-
"""Módulo 7: Geometria Espacial (Capítulos 27 a 30)"""

def get_chapters():
    return [
        {
            "id": "mat-cap-27-prismas-cilindros-volume",
            "number": 27,
            "title": "27. Prismas e Cilindros: Volume e Capacidade em Litros",
            "epigraph": {
                "text": "Volume de sólidos com bases paralelas e retas (prismas e cilindros): Área da Base vezes a Altura. E lembre-se: 1 metro cúbico equivale a exatamente 1.000 litros.",
                "author": "Regra de Conversão Essencial ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Regra Mestra: V = Ab * h"
                },
                {
                    "type": "paragraph",
                    "content": "Para qualquer prisma (reto ou oblíquo) e para qualquer cilindro:\nVolume = Área da Base * Altura (V = Ab * h).\n• Paralelepípedo retângulo (bloco retangular de dimensões a, b e c):\nVolume: V = a * b * c\nÁrea Total: At = 2(ab + ac + bc)\nDiagonal interna: D = raiz(a² + b² + c²)\n• Cubo de aresta a: V = a³, At = 6a², Diagonal D = a * raiz de 3.\n• Cilindro reto de raio R e altura h:\nVolume: V = pi * R² * h\nÁrea Lateral: Al = 2 * pi * R * h (quando planificada, é um retângulo de base 2*pi*R e altura h!)\nÁrea Total: At = 2 * pi * R * h + 2 * (pi * R²)."
                },
                {
                    "type": "callout",
                    "title": "Tabela de Conversão de Volumes e Capacidades (Cai em Toda Prova!)",
                    "content": "• 1 m³ = 1.000 dm³ = 1.000 Litros\n• 1 dm³ = 1 Litro\n• 1 cm³ = 1 mL\n• 1 Litro = 1.000 mL = 1.000 cm³.\nO ENEM adora dar as medidas em metros ou centímetros e pedir a resposta final em litros ou metros cúbicos!"
                }
            ],
            "quiz": [
                {
                    "question": "Uma caixa d'água cilíndrica tem raio da base medindo 2 metros e altura de 3 metros. Considerando pi = 3,1, qual é a capacidade máxima dessa caixa em litros?",
                    "options": [
                        "37.200 litros",
                        "31.000 litros",
                        "372.000 litros",
                        "12.400 litros"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Volume = pi * R² * h = 3,1 * 2² * 3 = 3,1 * 4 * 3 = 37,2 m³. Como 1 m³ = 1.000 L, a capacidade é 37,2 * 1.000 = 37.200 litros."
                }
            ]
        },
        {
            "id": "mat-cap-28-piramides-cones-troncos",
            "number": 28,
            "title": "28. Pirâmides e Cones: Vértices, Troncos e Proporções Cúbicas",
            "epigraph": {
                "text": "Sólidos que afunilam até um único vértice (pirâmides e cones): o volume é sempre 1/3 da área da base vezes a altura. Quando cortados por um plano paralelo à base, geram troncos e relações cúbicas de semelhança.",
                "author": "Geometria Espacial no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Volume de Sólidos com Bico: V = (1/3) * Ab * h"
                },
                {
                    "type": "paragraph",
                    "content": "• Pirâmide qualquer: V = (Ab * h) / 3. Se a base for um quadrado de lado L, Ab = L² e V = (L² * h) / 3.\n• Cone reto de raio R e altura h:\nVolume: V = (pi * R² * h) / 3\nGeratriz (g): hipotenusa do triângulo retângulo formado pela altura e pelo raio da base: g² = h² + R².\nÁrea Lateral do cone: Al = pi * R * g (setor circular quando planificado)."
                },
                {
                    "type": "callout",
                    "title": "Semelhança Espacial e Troncos de Pirâmide/Cone",
                    "content": "Ao seccionar um cone ou pirâmide a uma altura h' paralela à base:\n• Razão das alturas: k = h' / H\n• Razão das áreas das bases: Ab' / Ab = k²\n• Razão dos volumes dos sólidos: V' / V = k³!\nPara achar o volume do TRONCO que sobra embaixo, basta subtrair: V_tronco = V_total - V_topo!"
                }
            ],
            "quiz": [
                {
                    "question": "Um recipiente cônico tem altura total de 12 cm e está preenchido com líquido até a altura de 6 cm (metade da altura total). Se o volume total do cone é de 240 mL, qual é o volume do líquido contido no recipiente?",
                    "options": [
                        "30 mL",
                        "120 mL",
                        "60 mL",
                        "40 mL"
                    ],
                    "correctAnswer": 0,
                    "explanation": "A razão entre as alturas é k = h' / H = 6 / 12 = 1/2. Como o volume varia com o cubo da razão de semelhança: V_liquido / V_total = k³ = (1/2)³ = 1/8. Logo, V_liquido = 240 / 8 = 30 mL."
                }
            ]
        },
        {
            "id": "mat-cap-29-esferas-geometria",
            "number": 29,
            "title": "29. Esferas: Área Superficial e Volume",
            "epigraph": {
                "text": "A esfera é o sólido perfeitamente simétrico. Todo ponto de sua superfície está à mesma distância R do centro.",
                "author": "Geometria Espacial no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Área da Superfície Esférica e Volume da Esfera"
                },
                {
                    "type": "paragraph",
                    "content": "• Área da Superfície Esférica: A = 4 * pi * R² (curiosamente, equivale exatamente a quatro vezes a área do círculo máximo da esfera).\n• Volume da Esfera: V = (4/3) * pi * R³.\n• Hemisfério (semiesfera): Volume = (2/3) * pi * R³; Área total do hemisfério fechado = 2*pi*R² (casca) + pi*R² (tampa plana) = 3*pi*R²."
                },
                {
                    "type": "callout",
                    "title": "Problemas de Derretimento e Moldagem no ENEM",
                    "content": "Questões clássicas trazem barras de metal ou esferas de chumbo que são derretidas para formar outros sólidos. O princípio físico e geométrico imutável é a CONSERVAÇÃO DO VOLUME: V_inicial_total = V_final_total!"
                }
            ],
            "quiz": [
                {
                    "question": "Uma esfera metálica maciça de raio 3 cm é derretida e remodelada em pequenos cilindros retos de raio 1 cm e altura 3 cm. Considerando pi = 3, quantos cilindros completos podem ser obtidos?",
                    "options": [
                        "12 cilindros",
                        "9 cilindros",
                        "15 cilindros",
                        "8 cilindros"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Volume da esfera = (4/3) * pi * R³ = (4/3) * 3 * 3³ = 4 * 27 = 108 cm³. Volume de cada cilindro = pi * r² * h = 3 * 1² * 3 = 9 cm³. Quantidade de cilindros = 108 / 9 = 12 cilindros."
                }
            ]
        },
        {
            "id": "mat-cap-30-planificacao-visao-espacial",
            "number": 30,
            "title": "30. Planificação de Sólidos e Visão Espacial Tridimensional",
            "epigraph": {
                "text": "Planificar é 'desdobrar' um sólido 3D em uma superfície plana 2D sem rasgar nem sobrepor faces. O ENEM tem pelo menos duas questões visuais puras de planificação e projeção ortogonal a cada ano.",
                "author": "Competência de Habilidade Espacial ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Planificações Clássicas que Caem no ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "• Cubo: Possui 11 planificações possíveis formadas por 6 quadrados conectados. O padrão mais comum é o formato em cruz latina (4 quadrados em linha e 2 laterais).\n• Tetraedro Regular: 4 triângulos equiláteros.\n• Octaedro Regular: 8 triângulos equiláteros.\n• Cilindro Reto: Um retângulo (superfície lateral) conectado a dois círculos congruentes (as bases superior e inferior).\n• Cone Reto: Um setor circular (superfície lateral) conectado a um círculo (a base)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Projeção Ortogonal e Vistas (Frontal, Lateral e Superior)"
                },
                {
                    "type": "paragraph",
                    "content": "A projeção ortogonal de uma figura sobre um plano é a 'sombra' geométrica perpendicular produzida por raios de luz paralelos que atingem o plano formando 90°:\n• A projeção de um segmento oblíquo é sempre menor ou igual ao comprimento real do segmento.\n• A projeção de uma hélice cilíndrica (formato de mola) sobre o plano perpendicular ao seu eixo é uma CIRCUNFERÊNCIA.\n• A projeção de um cone iluminado de cima (vista superior) é um círculo com um ponto central representando o vértice."
                }
            ],
            "quiz": [
                {
                    "question": "Um cubo tem suas faces numeradas de 1 a 6 de modo que a soma das faces opostas seja sempre 7. Em sua planificação em cruz com 4 quadrados alinhados verticalmente (1, 2, 3, 4) e duas abas laterais ligadas ao quadrado 2, qual face fica oposta à face 1 após montar o cubo?",
                    "options": [
                        "Face 3",
                        "Face 6",
                        "Face 4",
                        "Face 5"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Na fita vertical com quatro quadrados alinhados (1, 2, 3, 4), ao dobrar em 90°, as faces que se alternam com um quadrado de intervalo tornam-se opostas: a face 1 opõe-se à face 3, e a face 2 opõe-se à face 4."
                }
            ]
        }
    ]
