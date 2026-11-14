# -*- coding: utf-8 -*-
"""Curso de Matemática ENEM - Módulo 2: Matemática Básica B (Capítulos 5 a 8)"""


def get_chapters():
    return [
        {
            "id": "mat-cap-05-mmc-mdc",
            "number": 5,
            "title": "5. Múltiplos, Divisores, MMC e MDC: O Segredo dos Ciclos e das Divisões Exatas",
            "epigraph": {
                "text": "Na natureza e na prova do ENEM, tudo o que se repete em ciclos se encontra no MMC; tudo o que se reparte no maior tamanho possível sem desperdício se resolve no MDC.",
                "author": "Aula Magna de Aritmética Aplicada"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas ao Mundo das Divisões Perfeitas e dos Encontros Marcados"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo a uma das aulas mais decisivas do seu curso. Pense comigo: quantas vezes você abriu uma questão falando de ônibus que saem juntos do terminal, remédios tomados em horários diferentes ou um marceneiro cortando tábuas sem desperdício e pensou: 'Professor, aqui é MMC ou MDC?'. Hoje essa dúvida acaba de vez, construindo o raciocínio do zero, passo a passo."
                },
                {
                    "type": "paragraph",
                    "content": "Antes disso, afiamos o olhar para divisões exatas com múltiplos, divisores e critérios de divisibilidade. Um número é múltiplo de outro quando nasce da multiplicação dele por um inteiro: os múltiplos positivos de 6 são 6, 12, 18, 24... até o infinito. Já os divisores são finitos e dividem o número com resto zero: os divisores positivos de 12 são 1, 2, 3, 4, 6 e 12."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Critérios de Divisibilidade: O Raio-X Instantâneo dos Números"
                },
                {
                    "type": "paragraph",
                    "content": "Na prova, você não precisa armar divisão para testar se 4.734 divide por 3 ou por 6. Um número divide por 2 se termina em algarismo par (0, 2, 4, 6 ou 8); por 5 se termina em 0 ou 5; e por 10 se termina em 0. Veja que sacada genial para o 3 e o 9: some todos os algarismos! Em 4.734, temos 4 + 7 + 3 + 4 = 18. Como 18 é múltiplo de 3 e de 9, garantimos na hora que 4.734 é divisível por 3 e por 9."
                },
                {
                    "type": "paragraph",
                    "content": "E os critérios do 4, 6, 8 e 11? Um número divide por 4 quando seus dois últimos algarismos formam um múltiplo de 4 (ou 00): 3.516 divide por 4 porque 16 divide por 4. Para o 8, olhamos os três últimos algarismos. O 6 é parceria do 2 com o 3: precisa ser par e ter soma dos algarismos divisível por 3. Já para o 11, some os algarismos de posição ímpar, some os de posição par e subtraia; dando 0 ou múltiplo de 11, divide! Em 2.728, (2 + 2) - (7 + 8) = -11, logo é divisível por 11."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Fatoração em Números Primos",
                    "content": "Todo inteiro maior que 1 se decompõe de forma única em fatores primos (2, 3, 5, 7, 11...). Quer contar quantos divisores positivos um número tem sem listar um por um? Fatore-o, some 1 a cada expoente e multiplique! Exemplo: 72 = 2³ × 3². Somando 1 aos expoentes: (3 + 1) × (2 + 1) = 4 × 3 = 12 divisores positivos."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "MMC na Veia: Quando a Questão Fala de Ciclos e Encontros"
                },
                {
                    "type": "paragraph",
                    "content": "Como bater o olho no enunciado e reconhecer o Mínimo Múltiplo Comum (MMC)? Pense comigo: múltiplos crescem para frente, saltando em intervalos regulares. Toda vez que eventos se repetem em ciclos periódicos e a questão pergunta quando eles voltarão a acontecer JUNTOS no futuro, o caminho é o MMC! Pense em ônibus partindo de um terminal, cometas passando perto da Terra, luzes piscando sincronizadas ou um paciente tomando dois remédios de 6 em 6 horas e de 8 em 8 horas."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: O Encontro dos Ônibus no Terminal",
                    "content": "Enunciado: Dois ônibus, A e B, saem juntos às 7h00. O ônibus A parte a cada 24 minutos e o B a cada 36 minutos. A que horas sairão juntos novamente?\n\nResolução passo a passo:\n1. Ciclo e encontro simultâneo futuro → MMC(24, 36).\n2. Fatoração simultânea: 24 e 36 por 2 → 12 e 18; por 2 → 6 e 9; por 2 → 3 e 9; por 3 → 1 e 3; por 3 → 1 e 1.\n3. Multiplicando os primos: 2 × 2 × 2 × 3 × 3 = 72 minutos.\n4. Convertendo: 72 min = 1 hora e 12 minutos.\n5. Somando a 7h00, eles partem juntos às 8h12!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "MDC na Veia: Quando a Questão Pede Partes Máximas e Sem Sobra"
                },
                {
                    "type": "paragraph",
                    "content": "E quando é Máximo Divisor Comum (MDC)? Dividir é repartir em pedaços menores! Sempre que a questão apresentar quantidades diferentes (ripas, rolos de fita, turmas, pacotes) e pedir para dividir tudo em partes iguais, do MAIOR tamanho possível e sem sobras, é MDC na certa! Muita atenção à pergunta final: muitas vezes o ENEM não pede o tamanho de cada pedaço (o MDC), e sim QUANTOS pedaços ou grupos serão formados no total."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: O Marceneiro e o Corte Perfeito",
                    "content": "Enunciado: Um marceneiro tem ripas de 120 cm, 180 cm e 240 cm e quer cortá-las em pedaços iguais, do maior tamanho possível, sem sobras. Quantos pedaços obterá?\n\nResolução passo a passo:\n1. Partes iguais máximas sem resto → MDC(120, 180, 240).\n2. Fatoramos juntos, marcando apenas os primos que dividem TODOS ao mesmo tempo:\n   • Por 2 → 60, 90, 120 (marca 2)\n   • Por 2 → 30, 45, 60 (marca 2)\n   • Por 2 → 15, 45, 30 (não marca)\n   • Por 3 → 5, 15, 10 (marca 3)\n   • Por 3 → 5, 5, 10; por 2 → 5, 5, 5 (não marca)\n   • Por 5 → 1, 1, 1 (marca 5)\n3. MDC = 2 × 2 × 3 × 5 = 60 cm por pedaço.\n4. Quantidade de pedaços: 120/60 = 2, 180/60 = 3 e 240/60 = 4. Total = 2 + 3 + 4 = 9 pedaços!"
                },
                {
                    "type": "heading",
                    "level": 3,
                    "content": "Pegadinha da TRI: O Resto Constante e a Propriedade Secreta"
                },
                {
                    "type": "paragraph",
                    "content": "Veja uma sacada de nível 800+: se ao dividir uma coleção de figurinhas em grupos de 8, 10 ou 12 sempre sobram 3 figurinhas, basta calcular MMC(8, 10, 12) = 120 e somar o resto 3, achando 123 (ou múltiplos de 120 mais 3). E guarde também uma propriedade preciosa para dois inteiros positivos A e B: A × B = MMC(A, B) × MDC(A, B)."
                },
                {
                    "type": "quote",
                    "content": "MMC olha para o futuro e pergunta: 'Quando nos encontraremos de novo?'. MDC olha para o material na mesa e pergunta: 'Qual é o maior corte igual que não deixa resto?'.",
                    "author": "Bússola de Prova do Professor"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-cap-06-razao-proporcao",
            "number": 6,
            "title": "6. Razão, Proporção e Divisão Proporcional: A Lógica da Justiça Matemática",
            "epigraph": {
                "text": "Proporção não é apenas multiplicar em cruz; é garantir que o esforço, o investimento e o resultado mantenham uma relação justa entre si.",
                "author": "Caderno de Estratégia ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Que É uma Razão de Verdade? Muito Além de Uma Simples Fração"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Vamos conversar hoje sobre a língua materna da prova de Matemática do ENEM: razão e proporção. Na matemática, razão é uma comparação por meio da divisão entre duas grandezas. Se numa sala existem 18 mulheres e 12 homens, a razão entre o número de mulheres e o de homens é 18 / 12, que simplificada por 6 vira 3 / 2. O que isso conta na prática? Que, para cada 3 mulheres presentes, existem exatamente 2 homens."
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque a maioria escorrega por pressa: na razão, A ORDEM IMPORTA! A razão de mulheres para homens é 3 / 2 (1,5), mas a de homens para mulheres é 2 / 3 (0,666...), e a de homens para o TOTAL da turma é 12 / 30 = 2 / 5 (40%). No ENEM, várias razões ganham nomes próprios: velocidade média (distância / tempo), densidade demográfica (população / área), densidade física (massa / volume) e consumo (km / litro). Enxergando a razão como comparação entre duas medidas, nenhuma fórmula parece decorada."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Proporção e a Constante k: O Coração da Igualdade"
                },
                {
                    "type": "paragraph",
                    "content": "Quando duas razões têm o mesmo valor, nasce uma proporção: a / b = c / d (com b e d não nulos). Você lembra da propriedade fundamental — 'produto dos meios igual ao produto dos extremos', ou seja, a × d = b × c (multiplicar em cruz). Mas quero te dar uma ferramenta ainda melhor para três ou mais partes: a constante de proporcionalidade k. Se x, y e z são proporcionais a 2, 3 e 5, escrevemos x / 2 = y / 3 = z / 5 = k, donde x = 2k, y = 3k e z = 5k. Em segundos, três letras viram uma só!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Grandezas Diretamente e Inversamente Proporcionais"
                },
                {
                    "type": "paragraph",
                    "content": "Pense comigo em duas situações do dia a dia. Primeira situação: você vai à padaria comprar pães. Se 10 pães custam 8 reais, 20 pães vão custar 16 reais. Quando você dobra uma grandeza, a outra dobra na mesma proporção; quando reduz pela metade, a outra cai pela metade. Chamamos essas grandezas de Diretamente Proporcionais (GDP). Matematicamente, a razão (divisão) entre elas é sempre constante: y / x = k. Se um gráfico mostra duas grandezas diretamente proporcionais, ele é obrigatoriamente uma reta passando pela origem (0, 0)!"
                },
                {
                    "type": "paragraph",
                    "content": "Segunda situação: você precisa viajar de carro por 300 km. A 60 km/h, leva 5 horas. Se dobrar a velocidade para 120 km/h, o tempo não dobra — ele cai pela metade, para 2,5 horas! Aqui, quando uma grandeza é multiplicada por um fator, a outra é dividida por esse mesmo fator. São as Grandezas Inversamente Proporcionais (GIP). Guarde isso no bolso: nas grandezas inversamente proporcionais, o que permanece constante não é a divisão, e sim a MULTIPLICAÇÃO entre elas: x × y = k. No nosso exemplo da viagem, 60 × 5 = 300 e 120 × 2,5 = 300. E no gráfico, elas formam uma curva suave descendente chamada hipérbole equilátera."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: A Diferença Fatal entre Direta e Inversa",
                    "content": "• Diretamente Proporcional (GDP): aumentou na mesma razão → DIVISÃO constante (A / B = k). Exemplo: lucro proporcional ao capital investido.\n• Inversamente Proporcional (GIP): aumentou uma, a outra diminuiu na razão inversa → PRODUTO constante (A × B = k). Exemplo: tempo de prova proporcional inversamente à velocidade, ou bônus inversamente proporcional ao número de faltas."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Divisão Diretamente Proporcional: O Lucro dos Sócios"
                },
                {
                    "type": "paragraph",
                    "content": "Esse é um clássico absoluto do ENEM. Imagine que três amigas — Ana, Beatriz e Carla — abriram uma confeitaria. Ana investiu R$ 20.000, Beatriz investiu R$ 30.000 e Carla investiu R$ 50.000. No final do primeiro ano, a confeitaria teve um lucro líquido de R$ 40.000 e elas combinaram de dividir esse lucro de forma diretamente proporcional ao valor que cada uma investiu. É justo, não é? Quem arriscou mais dinheiro recebe uma fatia maior do bolo."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Aplicando o Método da Constante k (As 'Partes')",
                    "content": "Vamos dividir R$ 40.000 em partes diretamente proporcionais a 20.000, 30.000 e 50.000.\n1. Dica de agilidade: simplifique os pesos antes de começar! Dividindo 20.000, 30.000 e 50.000 por 10.000, trabalhamos com 2, 3 e 5.\n2. Pela constante k: Ana recebe 2k, Beatriz recebe 3k e Carla recebe 5k.\n3. Somando todas as partes, precisamos completar o lucro total: 2k + 3k + 5k = 40.000 → 10k = 40.000 → k = 4.000.\n4. Agora basta multiplicar cada peso por k:\n   • Ana: 2 × 4.000 = R$ 8.000\n   • Beatriz: 3 × 4.000 = R$ 12.000\n   • Carla: 5 × 4.000 = R$ 20.000\nConferindo: 8.000 + 12.000 + 20.000 = R$ 40.000. Perfeito, limpo e sem frações feias!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Divisão Inversamente Proporcional: O Prêmio para Quem Faltou Menos"
                },
                {
                    "type": "paragraph",
                    "content": "Agora preste muita atenção, porque é aqui que muita gente boa trava na hora da prova. E se a divisão for INVERSAMENTE proporcional? Por exemplo, uma empresa quer dividir um prêmio de R$ 13.000 entre dois funcionários, Marcos e Paulo, de forma inversamente proporcional ao número de faltas de cada um no ano. Marcos faltou 2 vezes e Paulo faltou 3 vezes. Quem merece ganhar mais? Marcos, claro, porque faltou menos! Mas cuidado: erro clássico de iniciante é fazer 'Paulo tem 3, então dou 3 partes para Marcos e 2 para Paulo'. Com DOIS números isso até funciona por coincidência, mas com TRÊS números dá tudo errado! Vou te ensinar o jeito universal que funciona com dois, três, quatro ou dez números."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Divisão Inversamente Proporcional sem Erro",
                    "content": "Enunciado: Dividir R$ 15.600 entre três equipes (X, Y, Z) de forma inversamente proporcional aos seus tempos de erro: 2 h, 3 h e 4 h.\n\nResolução passo a passo:\n1. Inversamente proporcional a 2, 3 e 4 equivale a diretamente proporcional aos inversos: 1/2, 1/3 e 1/4.\n2. Com a constante k: X = k/2, Y = k/3 e Z = k/4.\n3. Somando ao total: k/2 + k/3 + k/4 = 15.600. Pelo MMC(2, 3, 4) = 12: (6k + 4k + 3k) / 12 = 15.600 → 13k / 12 = 15.600.\n4. Isolando k: k = (15.600 / 13) × 12 = 1.200 × 12 = 14.400.\n5. Calculamos cada prêmio: X = 14.400 / 2 = R$ 7.200; Y = 14.400 / 3 = R$ 4.800; Z = 14.400 / 4 = R$ 3.600.\nConferindo: 7.200 + 4.800 + 3.600 = R$ 15.600!"
                },
                {
                    "type": "quote",
                    "content": "Na divisão diretamente proporcional, multiplicamos os pesos por k. Na inversamente proporcional, dividimos k pelos pesos. Quem tem o menor peso fica com a maior fatia.",
                    "author": "Regra de Ouro da Proporcionalidade"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-cap-07-regra-de-tres",
            "number": 7,
            "title": "7. Regra de Três Simples e Composta: A Ferramenta Mais Rentável da Prova",
            "epigraph": {
                "text": "Se você pudesse levar apenas uma ferramenta matemática para o segundo dia do ENEM, levaria a Regra de Três analisada com lógica — nunca no piloto automático.",
                "author": "Manual do Candidato 800+"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Por Que Tanta Gente Erra Regra de Três se Ela Parece Tão Fácil?"
                },
                {
                    "type": "paragraph",
                    "content": "Seja muito bem-vindo à nossa sétima aula! Se você olhar as estatísticas dos últimos dez anos do ENEM, vai descobrir um segredo valioso: a Regra de Três é, disparada, a ferramenta com melhor retorno sobre o tempo investido na prova. Ela aparece disfarçada em questões de porcentagem, consumo de energia, dosagem de medicamentos, produtividade agrícola, vazão de torneiras e ritmo de obra. Mas então, por que tantos estudantes perdem pontos preciosos nela? A resposta é simples: porque foram treinados para 'multiplicar em cruz' no piloto automático, sem parar três segundos para perguntar se as grandezas são direta ou inversamente proporcionais."
                },
                {
                    "type": "paragraph",
                    "content": "Hoje nós vamos substituir o piloto automático por um método visual, limpo e infalível. A primeira regra sagrada antes de fazer qualquer conta é montar uma tabela organizada, onde cada coluna pertence a UMA única grandeza e, dentro da mesma coluna, todas as medidas precisam estar na MESMA unidade. Se em cima está em horas e embaixo está em minutos, converta tudo para minutos ou tudo para horas antes de prosseguir! Misturar unidades na mesma coluna é a armadilha número um dos distratores da banca."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Regra de Três Simples: O Método das Setas Inteligentes"
                },
                {
                    "type": "paragraph",
                    "content": "Na Regra de Três Simples, temos apenas duas grandezas variando. Suponha que 4 torneiras idênticas enchem um reservatório em 6 horas. Se abrirmos 6 dessas mesmas torneiras juntas, em quanto tempo o reservatório ficará cheio? Monte a tabela:\n• Coluna Torneiras: 4 em cima, 6 embaixo.\n• Coluna Tempo (h): 6 em cima, x embaixo.\nAgora faça a pergunta lógica com calma: 'Se eu AUMENTAR o número de torneiras jorrando água (seta para cima em Torneiras), o tempo para encher o tanque vai aumentar ou diminuir?' Vai DIMINUIR! Mais torneiras abertas enchem a caixa mais rápido! Logo, as setas apontam em sentidos contrários: são grandezas INVERSAMENTE proporcionais."
                },
                {
                    "type": "paragraph",
                    "content": "Quando as setas têm o mesmo sentido (direta), mantemos a fração como está e multiplicamos em cruz. Quando as setas têm sentidos opostos (inversa), nós INVERTEREMOS uma das frações — ou simplesmente multiplicamos EM LINHA RETA! Veja como fica fácil: 6 × x = 4 × 6 → 6x = 24 → x = 4 horas. Repare que, se você tivesse multiplicado em cruz sem pensar, acharia 9 horas: seis torneiras demorando MAIS que quatro torneiras! Sempre cheque o bom senso da resposta final; o ENEM cobra coerência com a realidade."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Cuidado com o 'A Mais' e com o 'Restante'",
                    "content": "Leia o enunciado como um detetive! Se uma obra tinha 10 operários e 'foram contratados mais 5 operários', na segunda linha da tabela não vai o número 5, vai 10 + 5 = 15 operários! Da mesma forma, se uma equipe deveria fazer um serviço em 20 dias, trabalhou 5 dias e depois recebeu reforço, a regra de três é montada apenas para os 15 dias RESTANTES do trabalho, e não para os 20 iniciais."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Regra de Três Composta: Comparando Tudo Sempre com o x"
                },
                {
                    "type": "paragraph",
                    "content": "Agora vamos subir um degrau e dominar a Regra de Três Composta, aquela que traz 3, 4 ou até 5 grandezas juntas (operários, máquinas, horas por dia, dias, metros construídos, rendimento). O erro fatal aqui é comparar uma coluna vizinha com a outra. NÃO FAÇA ISSO! A regra de ouro é: fixe uma seta (por exemplo, para baixo) na coluna do x e compare CADA uma das outras colunas INDIVIDUALMENTE com a coluna do x, fingindo que todas as demais ficaram congeladas."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: O Clássico das Máquinas, Horas e Peças",
                    "content": "Enunciado: Em uma gráfica, 4 impressoras idênticas, funcionando 6 horas por dia, imprimem 3.600 folhetos em 5 dias. Quantos dias serão necessários para que 6 dessas impressoras, trabalhando 8 horas por dia, imprimam 7.200 folhetos?\n\nPasso 1 — Montar a tabela com cuidado:\nImpressoras | Horas/dia | Folhetos | Dias\n     4      |     6     |  3.600   |  5\n     6      |     8     |  7.200   |  x\n\nPasso 2 — Fixar a coluna do x (Dias) e comparar cada grandeza com Dias:\n• Impressoras × Dias (mantendo horas/dia e folhetos fixos): mais impressoras trabalhando → preciso de MENOS dias → INVERSA (inverte 4/6 para 6/4).\n• Horas/dia × Dias (mantendo impressoras e folhetos fixos): mais horas por dia → preciso de MENOS dias → INVERSA (inverte 6/8 para 8/6).\n• Folhetos × Dias (mantendo impressoras e horas/dia fixos): mais folhetos para imprimir → preciso de MAIS dias → DIRETA (mantém 3.600/7.200).\n\nPasso 3 — Montar a equação isolando a razão do x de um lado e multiplicando as outras do outro:\n5 / x = (6 / 4) × (8 / 6) × (3.600 / 7.200)\nSimplificando antes de multiplicar (olha que delícia!): o 6 corta com o 6; 8/4 = 2; 3.600/7.200 = 1/2.\nFica: 5 / x = 2 × (1 / 2) = 1 → x = 5 dias!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Método Bônus: Causa e Efeito (Processo × Produto)"
                },
                {
                    "type": "paragraph",
                    "content": "Quer conhecer um segundo método que muitos professores guardam como carta na manga para conferir a resposta em dez segundos? É o método 'Processo × Produto' (ou Causa × Efeito). Pense assim: em quase todo problema de produção, existem recursos que trabalham juntos para gerar um resultado final. Quem trabalha, o tempo que trabalha e a eficiência são o PROCESSO (operários, máquinas, horas/dia, dias, rendimento). O que é produzido ou vencido é o PRODUTO (muro construído, peças fabricadas, litros bombeados, distância percorrida). A razão (Produto) / (Processo) é sempre constante — ou seja, multiplicamos todo o Processo da situação 1 pelo Produto da situação 2 e igualamos ao Processo da situação 2 pelo Produto da situação 1!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Resolvendo com 4 Grandezas pelo Método Processo × Produto",
                    "content": "Enunciado: 10 operários constroem 200 m de estrada em 12 dias, trabalhando 6 horas por dia. Quantos operários serão necessários para construir 300 m da mesma estrada em 9 dias, trabalhando 8 horas por dia?\n\nIdentificando os papéis:\n• Processo (quem trabalha e por quanto tempo): operários × dias × horas/dia.\n• Produto (o resultado construído): metros de estrada.\n\nMontando a igualdade direta (Processo 1 × Produto 2 = Processo 2 × Produto 1):\n(10 × 12 × 6) × 300 = (x × 9 × 8) × 200\nSimplificando os dois lados com elegância:\nCortamos dois zeros de 300 e 200: (10 × 12 × 6) × 3 = x × 9 × 8 × 2\nCalculando: 720 × 3 = x × 144 → 2.160 = 144x → x = 2.160 / 144 = 15 operários!\nZero dúvidas com setas e resultado 100% blindado."
                },
                {
                    "type": "quote",
                    "content": "Nunca compare grandezas vizinhas entre si na Regra de Três Composta: toda grandeza conversa exclusivamente com a coluna do x.",
                    "author": "Mandamento da Regra de Três"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-cap-08-escalas",
            "number": 8,
            "title": "8. Escalas Cartográficas, Lineares, Superficiais e Volumétricas",
            "epigraph": {
                "text": "Reduzir um mundo real para dentro de um mapa ou de uma maquete encolhe comprimentos por k, mas encolhe áreas por k² e volumes por k³.",
                "author": "Geometria Aplicada ao ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Bem-vindo ao Território Mais Previsível da Prova de Matemática"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos ao capítulo que fecha este nosso bloco de Matemática Básica, e eu posso te garantir com tranquilidade: não existe edição do ENEM sem pelo menos uma ou duas questões de Escala. Elas aparecem tanto na prova de Matemática quanto na prova de Geografia! E o melhor de tudo é que, depois de entender os detalhes que vamos destrinchar hoje, você vai olhar para uma questão de mapa, planta baixa ou maquete e sorrir, porque vai enxergar exatamente onde a banca colocou a armadilha para pegar o candidato apressado."
                },
                {
                    "type": "paragraph",
                    "content": "O conceito central é extremamente intuitivo. Escala é simplesmente uma razão entre uma medida no desenho (ou mapa, ou maquete) e a medida correspondente no objeto real, SEMPRE expressas na mesma unidade de comprimento. Escrevemos assim: Escala (E) = d / D, onde 'd' é o tamanho no desenho e 'D' é o tamanho real. Quando você vê num mapa a notação 1 : 50.000 (lê-se 'um para cinquenta mil'), isso significa que cada 1 centímetro medido com a régua no papel representa 50.000 centímetros no terreno real. Mas cuidado: ninguém sai por aí dizendo 'minha casa fica a 50.000 centímetros da escola'. É por isso que dominar a conversão de unidades é metade da questão!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Conversão Relâmpago entre cm, m e km Sem Decorar Escadinha"
                },
                {
                    "type": "paragraph",
                    "content": "Esqueça aquela escadinha confusa na hora do nervosismo e guarde apenas dois números mágicos que você já usa na vida: 1 metro tem 100 centímetros (2 zeros) e 1 quilômetro tem 1.000 metros (3 zeros). Agora junte os dois! Para ir de quilômetro para centímetro, você soma 3 zeros + 2 zeros = 5 zeros! Ou seja, 1 km = 100.000 cm. Pense na praticidade disso no ENEM: sempre que você vir uma escala cartográfica em centímetros, para transformar o lado direito em METROS, basta cortar 2 zeros; para transformar em QUILÔMETROS, basta cortar 5 zeros!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: O Corte Instantâneo de Zeros",
                    "content": "• Escala 1 : 200 (típica de planta baixa de apartamento): corte 2 zeros → 1 cm no papel vale 2 metros na obra.\n• Escala 1 : 500.000 (típica de mapa rodoviário): corte 5 zeros → 1 cm no mapa vale 5 km na estrada.\n• Escala 1 : 2.500.000: corte 5 zeros (ande 5 casas para a esquerda) → 1 cm no mapa vale 25 km reais.\n• E se precisar fazer o caminho inverso, de km para cm? Acrescente 5 zeros (multiplique por 100.000)!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Distância Real em Mapa Turístico",
                    "content": "Enunciado: Em um mapa na escala 1 : 400.000, a distância em linha reta entre duas cidades é de 6,5 cm. Qual é a distância real, em quilômetros, entre essas cidades?\n\nResolução passo a passo:\n1. Usando o corte de 5 zeros na escala 1 : 400.000, vemos que 1 cm no mapa equivale a 4 km no mundo real.\n2. Agora fazemos uma proporção direta instantânea:\n   1 cm → 4 km\n   6,5 cm → D\n3. D = 6,5 × 4 = 26 km! Veja como você resolveu em dez segundos e com zero risco de errar a vírgula."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Armadilha Mortal do ENEM: Escala de Área (k²) e de Volume (k³)"
                },
                {
                    "type": "paragraph",
                    "content": "Agora respire fundo e preste atenção máxima, porque este é o momento em que se separam os candidatos comuns dos candidatos acima de 800 pontos. Até aqui falamos de escala LINEAR — isto é, comprimento, largura, altura, distância entre cidades. Mas o que acontece quando a questão fala de ÁREA de um terreno numa planta baixa ou de VOLUME de água numa maquete de piscina? A maioria dos alunos pega a área do desenho e multiplica direto pelo fator da escala linear. E cai direto na alternativa A, feita especialmente para esse erro!"
                },
                {
                    "type": "paragraph",
                    "content": "Pense comigo geometricamente para nunca mais esquecer. Imagine um terreno quadrado de 10 m por 10 m: sua área real é 100 m². Na escala 1 : 100, cada lado do desenho fica 100 vezes menor, medindo 0,1 m (10 cm). Logo, a área no desenho é 0,1 m × 0,1 m = 0,01 m²! Compare 100 m² com 0,01 m²: a área NÃO diminuiu 100 vezes, e sim 100 × 100 = 10.000 vezes! Como reduzimos tanto a largura quanto o comprimento por k, a razão entre ÁREAS é k² = (Área do desenho) / (Área real). E no VOLUME, reduzindo largura, comprimento e altura juntos, a razão entre VOLUMES é k³ = (Volume do desenho) / (Volume real)!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: A Planta Baixa do Apartamento (Área = k²)",
                    "content": "Enunciado: Na planta baixa na escala 1 : 50, uma sala retangular tem área de 12 cm². Qual é a área real dessa sala em m²?\n\nResolução passo a passo:\n1. A escala linear 1 : 50 diz que 1 cm no papel = 50 cm = 0,5 m na realidade.\n2. Para ÁREA, elevamos ao quadrado: (1 cm)² → (0,5 m)², logo 1 cm² na planta → 0,25 m² reais.\n3. Multiplicamos pelos 12 cm² da planta: Área real = 12 × 0,25 = 3 m² (ou por k² = 1/2.500: 12 × 2.500 = 30.000 cm² = 3 m²!)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 3: A Maquete da Caixa-d'Água (Volume = k³)",
                    "content": "Enunciado: Um arquiteto construiu a maquete de um reservatório na escala 1 : 20. Ao testar a maquete com água, verificou que ela comporta exatamente 4 litros. Qual é a capacidade real desse reservatório, em litros?\n\nResolução passo a passo:\n1. A escala linear é E = 1 / 20 (cada dimensão real é 20 vezes maior que na maquete).\n2. Capacidade em litros mede VOLUME (três dimensões)! Logo, a razão volumétrica é (1 / 20)³ = 1 / 8.000.\n3. Montamos a proporção:\n   Volume_maquete / Volume_real = 1 / 8.000\n   4 / Volume_real = 1 / 8.000\n4. Multiplicando em cruz: Volume_real = 4 × 8.000 = 32.000 litros (ou 32 m³). Quem multiplicasse 4 por 20 marcaria 80 litros e perderia uma questão valiosíssima!"
                },
                {
                    "type": "heading",
                    "level": 3,
                    "content": "Checklist Final Antes de Marcar o Gabarito"
                },
                {
                    "type": "paragraph",
                    "content": "Sempre que pegar uma questão de escala na prova, siga três passos mentais rápidos: primeiro, confira se as duas medidas estão na mesma unidade antes de montar E = d / D; segundo, identifique se a pergunta trata de comprimento (use E), área (use E²) ou volume (use E³); terceiro, converta a resposta final para a unidade pedida no comando (lembrando que 1 m² = 10.000 cm² e 1 m³ = 1.000 litros). Dominando MMC/MDC, razão e proporção, regra de três e escalas, você acabou de blindar o coração da sua nota na Matemática Básica do ENEM!"
                },
                {
                    "type": "quote",
                    "content": "Na escala, comprimentos viajam na potência 1, áreas viajam ao quadrado e volumes viajam ao cubo. Quem respeita a dimensão da grandeza nunca cai na armadilha da banca.",
                    "author": "Síntese do Módulo de Matemática Básica"
                }
            ],
            "quiz": []
        }
    ]
