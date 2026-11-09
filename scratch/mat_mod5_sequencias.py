# -*- coding: utf-8 -*-
"""Módulo 5: Sequências Numéricas, PA e PG (Capítulos 20 e 21)"""

def get_chapters():
    return [
        {
            "id": "mat-cap-20-progressao-aritmetica",
            "number": 20,
            "title": "20. Progressão Aritmética (PA): Padrões Lineares e Soma dos Termos",
            "epigraph": {
                "text": "Na Progressão Aritmética, a diferença entre qualquer termo e seu antecessor é uma constante chamada razão (r). A PA é a versão discreta (em passos inteiros) da função afim.",
                "author": "Guia de Sequências no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Termo Geral da PA: Onde Chegar em n Passos"
                },
                {
                    "type": "paragraph",
                    "content": "Para chegar ao termo de ordem n partindo do primeiro termo (a1), precisamos somar a razão (n - 1) vezes:\nan = a1 + (n - 1) * r.\nGeneralização útil para o ENEM: an = ak + (n - k) * r. Exemplo: se conhecemos o a5 e queremos o a12, basta somar 7 razões (12 - 5 = 7): a12 = a5 + 7r."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Soma dos Termos de uma PA Finita (Fórmula de Gauss)"
                },
                {
                    "type": "paragraph",
                    "content": "A soma dos n primeiros termos de uma PA é dada por:\nSn = [(a1 + an) * n] / 2.\nO jovem Gauss descobriu essa relação ao perceber que a soma dos termos equidistantes dos extremos é sempre constante: (a1 + an) = (a2 + a(n-1)) = (a3 + a(n-2))."
                },
                {
                    "type": "callout",
                    "title": "Aplicações Típicas no ENEM",
                    "content": "• Fileiras de cadeiras em um teatro ou estádio onde cada fileira tem 2 ou 4 assentos a mais que a anterior.\n• Poupança progressiva (guardar R$ 5,00 na 1ª semana, R$ 10,00 na 2ª, R$ 15,00 na 3ª...).\n• Empilhamento de latas ou canos formando triângulos simétricos."
                }
            ],
            "quiz": [
                {
                    "question": "Um teatro tem 20 fileiras de poltronas. A primeira fileira tem 14 poltronas e cada fileira seguinte tem 2 poltronas a mais que a fileira imediatamente anterior. Qual é a capacidade total de poltronas do teatro?",
                    "options": [
                        "660 poltronas",
                        "640 poltronas",
                        "680 poltronas",
                        "620 poltronas"
                    ],
                    "correctAnswer": 0,
                    "explanation": "a1 = 14, r = 2, n = 20. O último termo é a20 = 14 + (20 - 1) * 2 = 14 + 38 = 52. A soma total é S20 = [(a1 + a20) * 20] / 2 = [(14 + 52) * 20] / 2 = 66 * 10 = 660 poltronas."
                }
            ]
        },
        {
            "id": "mat-cap-21-progressao-geometrica",
            "number": 21,
            "title": "21. Progressão Geométrica (PG): Crescimento Exponencial e Decaimento",
            "epigraph": {
                "text": "Na Progressão Geométrica, a razão entre qualquer termo e seu antecessor é uma constante multiplicativa (q). A PG é a versão discreta da função exponencial.",
                "author": "Guia de Sequências no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Termo Geral da PG"
                },
                {
                    "type": "paragraph",
                    "content": "Para encontrar o termo an a partir do primeiro termo a1, multiplicamos pela razão q elevada a (n - 1):\nan = a1 * q^(n - 1).\nSe q > 1 e a1 > 0: a PG é crescente.\nSe 0 < q < 1 e a1 > 0: a PG é decrescente (exemplo: decaimento de remédio na corrente sanguínea ou desvalorização anual de um carro).\nSe q < 0: a PG é oscilante (alterna sinais positivos e negativos)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Soma dos Termos da PG: Finita e Infinita"
                },
                {
                    "type": "paragraph",
                    "content": "• Soma da PG Finita: Sn = a1 * (q^n - 1) / (q - 1) [para q != 1].\n• Soma da PG Infinita (Série Geométrica Convergente, válida apenas para |q| < 1):\nS_infinito = a1 / (1 - q).\nEssa fórmula resolve problemas de fractais geométricos (como o floco de neve de Koch) e dízimas periódicas."
                }
            ],
            "quiz": [
                {
                    "question": "Uma bola de borracha é solta de uma altura de 16 metros. A cada quique no solo, ela atinge 1/2 da altura anterior. Qual a distância total vertical percorrida por essa bola até parar completamente?",
                    "options": [
                        "48 metros",
                        "32 metros",
                        "64 metros",
                        "16 metros"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Na 1ª queda: 16 m. Depois, cada quique sobe e desce a mesma altura: sobe 8 e desce 8 (16); sobe 4 e desce 4 (8); sobe 2 e desce 2 (4)... As subidas e descidas após o 1º impacto formam uma PG infinita com a1 = 2 * 8 = 16 e razão q = 1/2. Soma dos quiques = a1 / (1 - q) = 16 / (1 - 1/2) = 16 / 0,5 = 32 m. Distância total = 16 (queda inicial) + 32 = 48 metros."
                }
            ]
        }
    ]
