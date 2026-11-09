# -*- coding: utf-8 -*-
"""Módulo 3: Álgebra Elementar e Equacionamento (Capítulos 12 a 14)"""

def get_chapters():
    return [
        {
            "id": "mat-cap-12-produtos-notaveis-fatoracao",
            "number": 12,
            "title": "12. Expressões Algébricas, Produtos Notáveis e Fatoração",
            "epigraph": {
                "text": "Produtos notáveis e fatoração são atalhos mentais que transformam cálculos gigantescos em simplificações instantâneas na prova de Matemática.",
                "author": "Guia de Álgebra do ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Três Produtos Notáveis Sagrados"
                },
                {
                    "type": "paragraph",
                    "content": "Você precisa saber estes três produtos de forma automática:\n1. Quadrado da Soma: (a + b)² = a² + 2ab + b² (nunca escreva a² + b²; o termo do meio '2ab' é indispensável).\n2. Quadrado da Diferença: (a - b)² = a² - 2ab + b².\n3. Produto da Soma pela Diferença (Diferença de Quadrados): (a + b)(a - b) = a² - b²."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Técnicas de Fatoração Algébrica"
                },
                {
                    "type": "paragraph",
                    "content": "Fatorar significa transformar uma soma ou subtração em uma multiplicação. As quatro técnicas mais cobradas são:\n• Fator Comum em Evidência: ax + ay = a(x + y).\n• Agrupamento: ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y).\n• Trinômio Quadrado Perfeito: a² +- 2ab + b² = (a +- b)².\n• Diferença de Dois Quadrados: a² - b² = (a + b)(a - b). Dica mágica de cálculo mental: quanto vale 102² - 98²? Em vez de calcular os quadrados, faça (102 + 98)(102 - 98) = 200 * 4 = 800!"
                }
            ],
            "quiz": [
                {
                    "question": "Qual é o valor numérico da expressão (2025² - 2024²)?",
                    "options": [
                        "4.049",
                        "1",
                        "4.050",
                        "2.025"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Pela diferença de quadrados: a² - b² = (a + b)(a - b). Logo, 2025² - 2024² = (2025 + 2024)(2025 - 2024) = 4049 * 1 = 4.049."
                }
            ]
        },
        {
            "id": "mat-cap-13-equacoes-1-2-grau",
            "number": 13,
            "title": "13. Equações do 1º e 2º Grau: Modelagem de Problemas Reais",
            "epigraph": {
                "text": "No ENEM, a equação não vem pronta. O desafio é traduzir o texto em português para a linguagem matemática sem cometer erros de interpretação.",
                "author": "Matriz de Competências do ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Dicionário de Tradução: Português para Matemática"
                },
                {
                    "type": "paragraph",
                    "content": "• 'O dobro de um número aumentado de 5': 2x + 5\n• 'O dobro da soma de um número com 5': 2(x + 5) [Atenção aos parênteses!]\n• 'A terça parte do quadrado de x': (x²) / 3\n• 'O quadrado da terça parte de x': (x / 3)² = x² / 9\n• 'x excede y em 8 unidades': x - y = 8 ou x = y + 8\n• 'A soma de três números consecutivos': x + (x + 1) + (x + 2) = 3x + 3."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Resolução de Equações do 2º Grau e Relações de Girard (Soma e Produto)"
                },
                {
                    "type": "paragraph",
                    "content": "A forma canônica da equação do 2º grau é ax² + bx + c = 0 (com a != 0). Pela fórmula de Bhaskara:\nDelta = b² - 4ac\nx = (-b +- raiz de Delta) / (2a)\n• Se Delta > 0: duas raízes reais e distintas.\n• Se Delta = 0: duas raízes reais e iguais (uma raiz dupla).\n• Se Delta < 0: não possui raízes reais.\nAtalho rápido: Relações de Girard (Soma e Produto):\nS = x1 + x2 = -b / a\nP = x1 * x2 = c / a. Exemplo: Para x² - 7x + 12 = 0, procuramos dois números que somam 7 e multiplicam 12 -> as raízes são 3 e 4!"
                }
            ],
            "quiz": [
                {
                    "question": "O produto da idade de João pela idade que ele terá daqui a 4 anos é igual a 96. Qual é a idade atual de João?",
                    "options": [
                        "8 anos",
                        "10 anos",
                        "12 anos",
                        "6 anos"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Seja x a idade atual: x * (x + 4) = 96 => x² + 4x - 96 = 0. Procuramos dois números cuja soma é -4 e produto é -96: 8 e -12. Como a idade é positiva, x = 8 anos."
                }
            ]
        },
        {
            "id": "mat-cap-14-sistemas-inequacoes",
            "number": 14,
            "title": "14. Inequações e Sistemas de Equações Lineares no ENEM",
            "epigraph": {
                "text": "Sistemas de equações resolvem problemas de misturas, compras no supermercado, estacionamento de veículos com motos e carros e balanço financeiro.",
                "author": "Guia de Resolução Prática"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Métodos de Solução de Sistemas Lineares: Adição vs Substituição"
                },
                {
                    "type": "paragraph",
                    "content": "1. Método da Adição: Multiplique uma ou ambas as equações por números convenientes para que os coeficientes de uma das incógnitas fiquem opostos (ex: +3y e -3y). Ao somar as duas equações membro a membro, essa incógnita é eliminada de imediato.\n2. Método da Substituição: Isole uma incógnita que tenha coeficiente 1 em uma das equações e substitua sua expressão na outra equação."
                },
                {
                    "type": "callout",
                    "title": "Cuidado Crítico com Inequações: A Inversão do Sinal",
                    "content": "Ao resolver uma inequação (ex: -3x <= 12), ao multiplicar ou dividir ambos os membros por um número NEGATIVO, o sentido da desigualdade DEVE OBRIGATORIAMENTE INVERTER:\n-3x <= 12 => x >= 12 / (-3) => x >= -4. Esquecer de inverter o sinal é o distrator número 1 em inequações no ENEM!"
                }
            ],
            "quiz": [
                {
                    "question": "Em um estacionamento há 40 veículos entre carros e motos, totalizando 130 rodas. Quantos carros estão no estacionamento?",
                    "options": [
                        "25 carros",
                        "20 carros",
                        "15 carros",
                        "30 carros"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Seja c o número de carros e m o de motos: c + m = 40 (I) e 4c + 2m = 130 (II). Multiplicando (I) por -2: -2c - 2m = -80. Somando com (II): 2c = 50 => c = 25 carros."
                }
            ]
        }
    ]
