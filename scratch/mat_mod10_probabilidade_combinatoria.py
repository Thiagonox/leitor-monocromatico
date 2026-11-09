# -*- coding: utf-8 -*-
"""Módulo 10: Análise Combinatória e Probabilidade (Capítulos 38 a 41)"""

def get_chapters():
    return [
        {
            "id": "mat-cap-38-combinatoria-multiplicativo",
            "number": 38,
            "title": "38. Análise Combinatória: Princípio Multiplicativo e Fatorial",
            "epigraph": {
                "text": "Se uma decisão pode ser tomada de 'm' maneiras e, em seguida, uma segunda decisão pode ser tomada de 'n' maneiras, o número total de possibilidades conjuntas é m * n.",
                "author": "Princípio Fundamental da Contagem"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Princípio Fundamental da Contagem (PFC)"
                },
                {
                    "type": "paragraph",
                    "content": "O Princípio Multiplicativo é o pilar de toda a análise combinatória. Em vez de listar uma por uma centenas de opções (como senhas bancárias, placas de veículos ou cardápios), multiplicamos o número de opções disponíveis para cada etapa independente da decisão.\nExemplo clássico: Uma pessoa tem 4 camisas, 3 calças e 2 pares de tênis. O número de trajes completos distintos que ela pode formar é 4 * 3 * 2 = 24 trajes."
                },
                {
                    "type": "callout",
                    "title": "Regra do Conectivo: 'E' Multiplica, 'OU' Soma",
                    "content": "• Conectivo 'E' (eventos sucessivos ou simultâneos): Multiplicam-se as possibilidades (vestir camisa E calça E tênis = 4 * 3 * 2).\n• Conectivo 'OU' (opções mutuamente exclusivas): Somam-se as possibilidades (viajar de avião OU de ônibus = 3 voos + 5 linhas de ônibus = 8 opções)."
                }
            ],
            "quiz": [
                {
                    "question": "Um sistema de senhas bancárias exige que cada cliente crie um código formado por 3 letras distintas seguidas de 2 algarismos também distintos. Quantas senhas diferentes podem ser geradas considerando o alfabeto de 26 letras e os 10 algarismos (0 a 9)?",
                    "options": [
                        "1.404.000 senhas",
                        "1.757.600 senhas",
                        "1.560.000 senhas",
                        "1.200.000 senhas"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Letras distintas: 26 opções para a 1ª, 25 para a 2ª e 24 para a 3ª (26 * 25 * 24 = 15.600). Algarismos distintos: 10 opções para o 1º e 9 para o 2º (10 * 9 = 90). Total de senhas = 15.600 * 90 = 1.404.000 senhas."
                }
            ]
        },
        {
            "id": "mat-cap-39-permutacao-arranjo-combinacao",
            "number": 39,
            "title": "39. Permutação, Arranjo e Combinação: O Algoritmo da Decisão",
            "epigraph": {
                "text": "A pergunta que decide a sua questão: 'A ordem dos elementos importa?'. Se a ordem importar, é Arranjo ou Permutação. Se a ordem não fizer a menor diferença, é Combinação.",
                "author": "O Dilema Central da Combinatória"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Algoritmo de Escolha da Fórmula Correta"
                },
                {
                    "type": "paragraph",
                    "content": "Faça a si mesmo este teste mental: troque a posição de dois elementos escolhidos. O grupo resultante mudou ou continuou exatamente o mesmo?\n• Caso 1: A ordem IMPORTA (Ordem = Cargo, Pódio, Posição, Sequência de Fila):\n   - Se você usa TODOS os n elementos: PERMUTAÇÃO SIMPLES -> Pn = n! (Se houver repetição de letras/elementos: Pn^(a,b) = n! / (a! * b!)).\n   - Se você escolhe p elementos de um total n (com p < n): ARRANJO SIMPLES -> A(n, p) = n! / (n - p)!.\n• Caso 2: A ordem NÃO IMPORTA (Ordem = Grupo, Equipe, Comissão, Salada de Frutas, Sorteio de Duplas):\n   - COMBINAÇÃO SIMPLES -> C(n, p) = n! / [p! * (n - p)!]."
                },
                {
                    "type": "callout",
                    "title": "Atalho de Cálculo Rápido de Combinação sem Fatorial Gigante",
                    "content": "Para calcular C(10, 3): no numerador, comece em 10 e decresça 3 números (10 * 9 * 8). No denominador, fatorial de 3 (3 * 2 * 1):\nC(10, 3) = (10 * 9 * 8) / (3 * 2 * 1) = 720 / 6 = 120. Simples e direto, sem armar fórmulas gigantes!"
                }
            ],
            "quiz": [
                {
                    "question": "Um comitê científico composto por 4 médicos deve ser formado a partir de um grupo de 10 médicos voluntários. De quantas maneiras diferentes esse comitê pode ser escolhido?",
                    "options": [
                        "210 maneiras",
                        "5.040 maneiras",
                        "120 maneiras",
                        "240 maneiras"
                    ],
                    "correctAnswer": 0,
                    "explanation": "A ordem de escolha dos médicos não altera o comitê (escolher João e Maria é o mesmo comitê que Maria e João). Logo, é Combinação Simples: C(10, 4) = (10 * 9 * 8 * 7) / (4 * 3 * 2 * 1) = 5.040 / 24 = 210 maneiras."
                }
            ]
        },
        {
            "id": "mat-cap-40-probabilidade-simples",
            "number": 40,
            "title": "40. Probabilidade Simples, Espaço Amostral e Eventos Equiprováveis",
            "epigraph": {
                "text": "Probabilidade = (Casos Favoráveis) / (Casos Possíveis Totais). Um valor sempre entre 0 (evento impossível) e 1 (evento certo), ou de 0% a 100%.",
                "author": "Definição Clássica de Laplace"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Conceitos Fundamentais da Teoria das Probabilidades"
                },
                {
                    "type": "paragraph",
                    "content": "• Espaço Amostral (Omega): É o conjunto de todos os resultados possíveis de um experimento aleatório. Exemplo: lançamento de um dado honesto de 6 faces: Omega = {1, 2, 3, 4, 5, 6}, com n(Omega) = 6.\n• Evento (E): É qualquer subconjunto do espaço amostral. Exemplo: sair um número primo: E = {2, 3, 5}, com n(E) = 3.\n• Probabilidade Laplaciana: P(E) = n(E) / n(Omega) = 3 / 6 = 1/2 = 50%.\n• Evento Complementar (E'): P(E') = 1 - P(E). Técnica vital para o ENEM: quando a questão pedir 'a probabilidade de pelo menos um...', calcule 1 MENOS a probabilidade de NENHUM acontecer!"
                }
            ],
            "quiz": [
                {
                    "question": "Em uma urna há 12 bolas verdes, 8 azuis e 10 amarelas, todas idênticas ao tato. Retirando-se uma bola ao acaso, qual é a probabilidade de ela NÃO ser azul?",
                    "options": [
                        "11/15 (73,3%)",
                        "4/15 (26,7%)",
                        "2/5 (40%)",
                        "3/5 (60%)"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Total de bolas = 12 + 8 + 10 = 30 bolas. Bolas que NÃO são azuis = 12 verdes + 10 amarelas = 22 bolas. Probabilidade = 22 / 30 = 11 / 15 (aproximadamente 73,3%)."
                }
            ]
        },
        {
            "id": "mat-cap-41-probabilidade-uniao-condicional",
            "number": 41,
            "title": "41. Probabilidade da União, Condicional e Árvore de Decisão",
            "epigraph": {
                "text": "A probabilidade condicional P(A|B) é a probabilidade de o evento A acontecer SABENDO que o evento B já ocorreu. O efeito direto é a redução do espaço amostral.",
                "author": "Probabilidade Bayesiana no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Probabilidade da União de Dois Eventos: P(A ou B)"
                },
                {
                    "type": "paragraph",
                    "content": "Ao calcular a probabilidade de A OU B ocorrer:\nP(A união B) = P(A) + P(B) - P(A intersecção B).\nA subtração de P(A intersecção B) é necessária porque os elementos que pertencem simultaneamente a A e a B foram somados duas vezes! Se os eventos forem mutuamente exclusivos (não podem ocorrer juntos), P(A intersecção B) = 0."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Probabilidade Condicional: P(A | B)"
                },
                {
                    "type": "paragraph",
                    "content": "A notação P(A | B) lê-se 'probabilidade de A dado B':\nP(A | B) = P(A intersecção B) / P(B).\nNo ENEM, você resolve 99% das questões de probabilidade condicional sem fórmula: basta restringir a tabela ou o espaço amostral apenas à linha ou coluna do evento B que já ocorreu, e contar quantos casos favoráveis de A existem dentro dessa linha reduzida!"
                }
            ],
            "quiz": [
                {
                    "question": "Dois dados honestos de 6 faces são lançados. Sabendo que a soma das faces obtidas foi igual a 8, qual é a probabilidade de o primeiro dado ter mostrado o número 5?",
                    "options": [
                        "1/5",
                        "1/6",
                        "1/36",
                        "2/5"
                    ],
                    "correctAnswer": 0,
                    "explanation": "O espaço amostral fica reduzido aos pares cuja soma é 8: (2,6), (3,5), (4,4), (5,3), (6,2). São 5 casos possíveis no novo espaço amostral. Desses 5, apenas o par (5,3) tem o primeiro dado igual a 5 (1 caso favorável). Logo, P = 1/5."
                }
            ]
        }
    ]
