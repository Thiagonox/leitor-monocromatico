# -*- coding: utf-8 -*-
"""Curso Completo de Matemática ENEM - Módulo 10: Probabilidade e Análise Combinatória (Capítulos 47 a 50)."""


def get_chapters():
    return [
        {
            "id": "mat-cap-47-probabilidade-simples",
            "number": 47,
            "title": "47. Probabilidade Simples, Espaço Amostral, Eventos e a Lógica do E / OU",
            "epigraph": {
                "text": "A probabilidade é, na sua essência, apenas o bom senso reduzido a cálculo.",
                "author": "Pierre-Simon Laplace"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas à arte de medir o acaso"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo a um dos módulos mais deliciosos e estratégicos de toda a Matemática do ENEM. Se você já olhou para a previsão do tempo e viu que há 70% de chance de chuva, ou já pegou um saco de balas tentando adivinhar se vai tirar uma de morango sem olhar, parabéns: você já pensa em probabilidade no cotidiano. Pense comigo: o que significa dizer que algo tem muita ou pouca chance de acontecer? Na Matemática, medir a chance nada mais é do que comparar o tamanho daquilo que queremos que aconteça com o tamanho de tudo o que pode acontecer naquela situação."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Espaço Amostral e Evento Favorável: a base de tudo"
                },
                {
                    "type": "paragraph",
                    "content": "Antes de fazer qualquer conta, precisamos dar nome a dois personagens principais. O primeiro é o Espaço Amostral, representado pela letra grega ômega (Ω) ou por S. Ele é a lista completa de TODOS os resultados possíveis de um experimento aleatório, desde que todos tenham a mesma chance de ocorrer (experimento equiprovável). Ao lançar um dado comum de seis faces, nosso espaço amostral tem 6 elementos: {1, 2, 3, 4, 5, 6}."
                },
                {
                    "type": "paragraph",
                    "content": "O segundo personagem é o Evento Favorável, que representa exatamente o que a questão pede. Se o enunciado pergunta: 'Qual a probabilidade de sair um número par no lançamento de um dado?', o evento favorável é o conjunto {2, 4, 6}, com 3 elementos. Então, quantas chances em quantas você tem? Você tem 3 casos favoráveis em 6 casos possíveis. Dividindo 3 por 6, encontramos 1/2, igual a 0,5 ou 50%."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: A Fórmula Mãe da Probabilidade",
                    "content": "P(E) = (Número de casos favoráveis) / (Número total de casos possíveis)\n\nFique atento aos extremos da régua probabilística:\n• Evento Impossível: nunca acontece (0 casos favoráveis). Ex.: tirar o número 9 num dado comum de 6 faces -> P = 0/6 = 0 (0%).\n• Evento Certo: acontece sempre (todos os casos são favoráveis). Ex.: tirar número menor que 10 num dado comum -> P = 6/6 = 1 (100%).\nToda probabilidade mora entre 0 e 1 (0% a 100%). Se der 1,4 ou -0,2, revise sua conta!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O atalho mágico da Probabilidade Complementar ('pelo menos um')"
                },
                {
                    "type": "paragraph",
                    "content": "Veja que sacada genial economiza minutos preciosos na prova. Imagine que uma família terá 3 filhos e queremos saber a probabilidade de nascer PELO MENOS UMA menina. Tentar contar caso por caso — 1 menina, ou 2 meninas, ou 3 meninas — dá trabalho. Agora pense ao contrário: o que precisa acontecer para NÃO termos pelo menos uma menina? Só existe um único jeito de falhar: nascerem 3 meninos seguidos!"
                },
                {
                    "type": "paragraph",
                    "content": "Como acontecer e NÃO acontecer somam juntos 100% (ou 1 inteiro), chamamos esses dois cenários de eventos complementares. Para 3 filhos, cada nascimento tem 2 opções (Menino ou Menina), gerando 2 × 2 × 2 = 8 combinações possíveis. Apenas 1 combinação é formada só por meninos (M-M-M), com chance 1/8. Logo, a probabilidade de haver pelo menos uma menina é 1 - 1/8 = 7/8 (87,5%). Leu 'pelo menos um'? Acenda o alerta do complemento!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Lógica do OU: Regra da Adição e contagem dupla"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque é aqui que a maioria escorrega! Quando a questão pede a chance de acontecer A OU B, somamos as probabilidades: P(A) + P(B). Isso funciona direto quando os eventos não ocorrem juntos, como tirar uma carta de copas OU de espadas num baralho de 52 cartas: 13/52 + 13/52 = 26/52 = 50%."
                },
                {
                    "type": "paragraph",
                    "content": "Mas o que acontece se houver sobreposição? Suponha que sorteamos uma carta e queremos que ela seja de COPAS OU um REI. Há 13 cartas de copas e 4 reis. Se você somar 13 + 4 = 17, cometeu um erro clássico: o Rei de Copas está nos dois grupos e foi contado duas vezes! Para corrigir, subtraímos uma vez a interseção (os elementos em comum): 13/52 + 4/52 - 1/52 = 16/52 = 4/13."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Fórmula Completa do OU",
                    "content": "P(A ou B) = P(A) + P(B) - P(A e B)\n\nSe A e B não tiverem nada em comum (mutuamente exclusivos), P(A e B) vale zero e você apenas soma. Se existir algum elemento que cumpra as duas condições ao mesmo tempo, subtraia a interseção uma vez."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Lógica do E: Eventos Independentes e Regra do Produto"
                },
                {
                    "type": "paragraph",
                    "content": "E quando queremos que duas coisas aconteçam juntas ou em sequência? É o conectivo E. Acertar duas vezes seguidas é mais difícil que acertar uma vez — a chance diminui! Como multiplicar frações menores que 1 reduz o resultado, o conectivo E em eventos independentes manda MULTIPLICAR: P(A e B) = P(A) × P(B). Dois eventos são independentes quando o primeiro não afeta o segundo. Lançar uma moeda e depois um dado: chance de 'Cara' (1/2) E 'número 6' (1/6) é 1/2 × 1/6 = 1/12."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Estilo ENEM: O Semáforo Duplo",
                    "content": "Enunciado: No trajeto ao trabalho, Helena passa por dois semáforos independentes. A probabilidade de o 1º estar aberto é 0,6, e a do 2º estar aberto é 0,8. Qual a chance de encontrar EXATAMENTE UM semáforo aberto?\n\nResolução passo a passo:\n1. Complementos (fechados): 1º fechado = 1 - 0,6 = 0,4; 2º fechado = 1 - 0,8 = 0,2.\n2. Cenários possíveis para 'exatamente um aberto':\n   • Cenário I (1º aberto E 2º fechado): 0,6 × 0,2 = 0,12.\n   • Cenário II (1º fechado E 2º aberto): 0,4 × 0,8 = 0,32.\n3. Como serve o Cenário I OU o Cenário II, somamos:\n   P = 0,12 + 0,32 = 0,44 (44%)."
                },
                {
                    "type": "quote",
                    "content": "Na prova do ENEM, 'E' indica exigência simultânea e multiplica as chances; 'OU' indica alternativas que nos servem e soma as chances, sempre vigiando a interseção.",
                    "author": "Regra de Ouro da Sala de Aula"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-cap-48-probabilidade-condicional",
            "number": 48,
            "title": "48. Probabilidade Condicional e Análise de Possibilidades em Tabelas",
            "epigraph": {
                "text": "Quando recebemos uma informação nova sobre o mundo, o conjunto do que ainda é possível encolhe — e as probabilidades se transformam.",
                "author": "Raciocínio Bayesiano Intuitivo"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O poder oculto do 'sabendo que...' e do 'dado que...'"
                },
                {
                    "type": "paragraph",
                    "content": "Olá novamente! Prepare o café porque hoje vamos desvendar um dos tópicos que mais separam os alunos de nota 650 daqueles que passam dos 850 no ENEM: a Probabilidade Condicional. Imagine que escolhi um aluno aleatório de uma escola com 500 estudantes, onde 20% usam óculos. Mas e se eu sussurrar uma pista valiosa: 'O aluno sorteado é do 3º B, que só tem 30 alunos, e lá 15 usam óculos'? Na hora, a chance salta para 15 em 30 (50%)!"
                },
                {
                    "type": "paragraph",
                    "content": "Percebeu a mágica? Quando recebemos uma informação prévia — introduzida por expressões como 'sabendo que', 'dado que', 'dentre os que' ou 'escolhido ao acaso entre aqueles que' —, jogamos fora o resto do universo que não satisfaz essa condição. A Probabilidade Condicional nada mais é do que uma REDUÇÃO DO ESPAÇO AMOSTRAL!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Entendendo a fórmula antes de decorá-la"
                },
                {
                    "type": "paragraph",
                    "content": "Nos livros, vemos a notação P(A | B), lida como 'probabilidade de A, dado que B já aconteceu'. A barra vertical funciona como uma tesoura que corta o espaço amostral antigo e deixa vivo apenas o conjunto B no denominador. No numerador colocamos apenas os casos de A que moram dentro desse novo mundo chamado B, isto é, a interseção entre A e B."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: A Fórmula da Condicional sem Mistério",
                    "content": "P(A | B) = P(A e B) / P(B)   ou, direto com quantidades:   P(A | B) = n(A e B) / n(B)\n\nTruque infalível de leitura: tudo o que vem DEPOIS de 'sabendo que...', 'dado que...' ou 'dentre os...' vira o novo DENOMINADOR da sua fração!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Tabelas de Contingência: o formato favorito do ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "O ENEM adora colocar probabilidade condicional dentro de tabelas de dupla entrada. Vamos treinar juntos com uma pesquisa feita com 200 estudantes sobre turno de estudo e prática de esportes:"
                },
                {
                    "type": "callout",
                    "title": "Tabela da Pesquisa Escolar (Total = 200 alunos)",
                    "content": "                  | Pratica Esporte | Não Pratica | TOTAL\nTurno da Manhã    |       60        |      40     |  100\nTurno da Noite    |       30        |      70     |  100\nTOTAL             |       90        |     110     |  200"
                },
                {
                    "type": "paragraph",
                    "content": "Compare três perguntas que parecem gêmeas, mas têm respostas distintas. Pergunta 1: 'Sorteando um estudante dentre os 200, qual a chance de estudar de manhã E praticar esporte?' Aqui o universo é a escola inteira (200), e o cruzamento 'Manhã' com 'Pratica' tem 60 alunos: 60/200 = 30%. Agora veja a Pergunta 2: 'Sorteando um estudante que PRATICA ESPORTE, qual a chance de estudar de manhã?' A condição reduz nosso universo à primeira coluna (90 atletas), onde 60 são da manhã: 60/90 = 2/3 (66,7%)."
                },
                {
                    "type": "paragraph",
                    "content": "Veja a Pergunta 3: 'Sabendo que o estudante escolhido estuda à NOITE, qual a chance de NÃO praticar esporte?' A tesoura recortou apenas a linha do Turno da Noite, cujo total é 100. Dentro dessa linha, 70 não praticam esporte: 70/100 = 70%. Bastou tapar com a mão o resto da tabela e olhar só para a linha ou coluna da condição!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sorteios sucessivos sem reposição: espaço amostral em movimento"
                },
                {
                    "type": "paragraph",
                    "content": "A condicional também aparece nos sorteios em sequência SEM reposição. Imagine uma urna com 5 bolas azuis e 3 vermelhas (8 no total). Queremos retirar duas bolas sem devolver a primeira, e saber a chance de ambas serem azuis. Na 1ª retirada, temos 5/8. Se a primeira saiu azul e não voltou, a urna encolheu! Para a 2ª retirada, restam 7 bolas no total e apenas 4 azuis, logo a chance condicional é 4/7. Pelo conectivo E, multiplicamos: (5/8) × (4/7) = 20/56 = 5/14."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O problema clássico dos exames médicos e falsos positivos"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque este problema derruba até candidatos bem preparados. Suponha que uma doença rara afete 2% da população. Um teste identifica corretamente 90% dos doentes (verdadeiro positivo), mas dá alarme falso em 10% das pessoas sadias (falso positivo). Se uma pessoa faz o teste e dá POSITIVO, qual a probabilidade real de ela estar doente? Se você pensou '90%', caiu na armadilha! Resolva criando uma cidade imaginária com 1.000 habitantes:"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: A Cidade dos 1.000 Habitantes",
                    "content": "1. População total: 1.000 pessoas -> Doentes (2%): 20 pessoas; Sadias (98%): 980 pessoas.\n2. Aplicando o teste:\n   • Entre os 20 doentes, 90% testam positivo = 18 positivos reais.\n   • Entre os 980 sadios, 10% têm falso positivo = 98 falsos positivos.\n3. Total de testes POSITIVOS = 18 + 98 = 116 pessoas.\n4. Condicional ('dado que deu positivo, qual a chance de estar doente?'):\n   Nosso novo universo são os 116 positivos; apenas 18 estão doentes.\n   P(Doente | Positivo) = 18 / 116 ≈ 15,5%!"
                },
                {
                    "type": "paragraph",
                    "content": "Que resultado surpreendente! Como a doença é rara, 10% de falso positivo sobre a multidão sadia gera muito mais positivos do que os doentes reais. Sempre que vir teste médico no ENEM, crie uma população fictícia de 1.000 pessoas e nunca mais erre!"
                },
                {
                    "type": "quote",
                    "content": "Inventar uma população de 1.000 pessoas transforma porcentagens abstratas de falsos positivos em contas de padaria impossíveis de errar.",
                    "author": "Estratégia 800+ do Professor"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-cap-49-combinatoria-pfc-permutacao",
            "number": 49,
            "title": "49. Análise Combinatória I: Princípio Multiplicativo (PFC) e Permutações",
            "epigraph": {
                "text": "Contar não é enumerar um por um até cansar; contar é enxergar a estrutura escondida por trás das escolhas.",
                "author": "Espírito da Combinatória"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Bem-vindo à Análise Combinatória sem trauma!"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos ao tema que costuma dar frio na barriga em muita gente: Análise Combinatória. Por que tantos alunos travam aqui? Porque tentam começar decorando um monte de fórmulas com letras estranhas antes de entender a ferramenta mais natural de todas: contar usando decisões simples. Hoje vamos jogar o medo pela janela e construir tudo passo a passo."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Da Árvore de Possibilidades às Caixinhas de Decisão (PFC)"
                },
                {
                    "type": "paragraph",
                    "content": "Imagine que você abriu uma lanchonete com 3 tipos de pão (francês, brioche, integral) e 4 tipos de recheio (queijo, frango, carne, vegetariano). Quantos sanduíches de um pão E um recheio existem? Poderíamos desenhar uma Árvore de Possibilidades: de cada pão saem 4 galhos de recheio, somando 4 + 4 + 4 = 12 sanduíches. Mas com 10 pães, 15 recheios e 8 molhos, ninguém teria papel para a árvore! Aí entra o Princípio Fundamental da Contagem (PFC)."
                },
                {
                    "type": "paragraph",
                    "content": "No método das caixinhas de decisão, desenhamos uma caixinha para cada escolha em sequência, colocamos dentro quantas opções existem naquele passo e multiplicamos tudo: [ 3 opções de pão ] × [ 4 opções de recheio ] = 12 combinações. Simples, visual e poderoso!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Regra de Ouro do PFC: Restrições Primeiro!"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque é onde a maioria cai no ENEM! Sempre que houver restrições em alguma posição — 'tem que ser par', 'não pode começar com zero', 'primeira letra é vogal' — preencha PRIMEIRO as caixinhas restritas! Se começar pelas casas livres, você pode gastar justamente os elementos que faziam falta na casa exigente."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Quantos números pares de 3 algarismos distintos?",
                    "content": "Enunciado: Usando {0, 1, 2, 3, 4, 5}, quantos números PARES de 3 algarismos DISTINTOS podemos formar?\n\nO 0 no final altera as opções do começo, então dividimos em dois casos:\n• Caso A (termina em 0): Fixamos 0 na última casa (1 opção). Como o 0 já foi usado, sobram 5 algarismos {1,2,3,4,5} para a 1ª casa e 4 para o meio. Total A = 5 × 4 × 1 = 20.\n• Caso B (termina em 2 ou 4): 2 opções no final. Para a 1ª casa, 1 dígito foi para o fim e o 0 não pode entrar no início -> sobram 4 opções! Para o meio, o 0 volta a valer -> 4 opções (6 - 2 usados). Total B = 4 × 4 × 2 = 32.\n• Resposta final (Caso A OU Caso B): 20 + 32 = 52 números."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Permutação Simples (n!): trocando todo mundo de lugar"
                },
                {
                    "type": "paragraph",
                    "content": "Quando usamos TODOS os elementos disponíveis apenas para colocá-los em fila, mudando sua ordem, temos uma Permutação. Suponha que 4 amigos — Ana, Bruno, Carla e Diego — vão tirar uma foto lado a lado. Pelas caixinhas: 4 opções no 1º lugar, 3 no 2º, 2 no 3º e 1 no 4º, dando 4 × 3 × 2 × 1 = 24 modos. Na Matemática, esse produto decrescente até 1 ganha o símbolo fatorial: 4! = 24. Para n elementos distintos, Pn = n! (e por convenção, 0! = 1)."
                },
                {
                    "type": "paragraph",
                    "content": "Mas cuidado com uma pegadinha clássica de fila: e se o enunciado disser que Ana e Bruno são namorados e exigem ficar SEMPRE JUNTOS na foto? Veja que truque fantástico usamos em sala de aula: colocamos Ana e Bruno dentro de um 'bloco' amarrado com corda, como se fossem uma pessoa só! Agora temos 3 blocos para permutar: [Ana+Bruno], Carla e Diego, o que dá 3! = 6 ordens. Mas atenção: dentro do bloco, Ana pode estar à esquerda ou à direita de Bruno, isto é, 2! = 2 jeitos. Multiplicando os dois passos: 3! × 2! = 6 × 2 = 12 fotos possíveis!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Permutação com Repetição: domando anagramas e senhas"
                },
                {
                    "type": "paragraph",
                    "content": "E ao calcular os anagramas de uma palavra com letras repetidas, como BANANA? Se pintássemos os três 'A's com cores diferentes, teríamos 6! = 720 anagramas. Mas apagando as cores, trocar dois 'A's idênticos de lugar NÃO cria palavra nova! As 3 letras A podem trocar entre si de 3! = 6 jeitos e os 2 N's de 2! = 2 jeitos sem mudar nada. Para limpar a repetição, DIVIDIMOS pelo fatorial de cada repetido: P6^(3,2) = 6! / (3! × 2!) = 720 / 12 = 60 anagramas!"
                },
                {
                    "type": "callout",
                    "title": "Aplicação Secreta: Caminhos na Grade (Estilo ENEM!)",
                    "content": "Sabe questões de mapa quadriculado onde alguém vai de A até B dando 5 passos para a Direita (D) e 3 para Cima (C)? Qualquer trajeto mínimo é um anagrama de 'DDDDDCCC'! São 8 passos com 5 D's e 3 C's repetidos:\nTotal = 8! / (5! × 3!) = (8 × 7 × 6) / (3 × 2 × 1) = 56 caminhos!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Permutação Circular: a mesa redonda e a roda de amigos"
                },
                {
                    "type": "paragraph",
                    "content": "Para fechar, imagine 5 pessoas sentando-se em uma mesa redonda sem cadeiras numeradas. Se todos derem um passo para a direita, quem está ao lado de quem continua idêntico — rodar a roda não cria nova disposição! Como resolvemos? Fixamos UMA pessoa como referência para travar a roda e permutamos as outras (n - 1) pessoas em relação a ela: PCn = (n - 1)!. Para 5 amigos: (5 - 1)! = 4! = 24 disposições."
                },
                {
                    "type": "quote",
                    "content": "Antes de sair multiplicando números em combinatória, pergunte sempre: qual é a casa mais exigente? Resolva a restrição primeiro e o resto flui naturalmente.",
                    "author": "Lição de Sala de Aula"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-cap-50-combinatoria-arranjo-combinacao",
            "number": 50,
            "title": "50. Análise Combinatória II: Arranjo versus Combinação — O Teste Definitivo da Ordem",
            "epigraph": {
                "text": "A diferença entre o caos e a clareza em combinatória cabe numa única pergunta: se eu trocar dois escolhidos de lugar, nasce um novo resultado?",
                "author": "O Teste da Ordem"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O grande dilema: Arranjo ou Combinação?"
                },
                {
                    "type": "paragraph",
                    "content": "Seja muito bem-vindo ao capítulo que encerra com chave de ouro nossa jornada pela Análise Combinatória! Se você já travou pensando 'Aqui é Arranjo ou Combinação?', essa dúvida termina hoje. Não vamos adivinhar por palavras mágicas: você vai aprender um teste mental infalível. Quando escolhemos apenas uma parte 'p' de um total de 'n' elementos disponíveis, existem dois mundos possíveis: o do Arranjo e o da Combinação."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Teste Infalível da Inversão: troque dois elementos!"
                },
                {
                    "type": "paragraph",
                    "content": "Simule UMA escolha e troque a ordem de dois elementos selecionados. O resultado mudou ou continuou igual? Teste em dois cenários. Cenário 1: escolher 2 alunos entre 10 para PRESIDENTE e VICE-PRESIDENTE. Se João é presidente e Maria é vice, e depois invertemos para Maria presidente e João vice, a chapa mudou? SIM! Quando a ordem IMPORTA, temos um ARRANJO."
                },
                {
                    "type": "paragraph",
                    "content": "Cenário 2: escolher 2 alunos entre 10 para uma COMISSÃO sem cargos diferentes. Escolher João e Maria é idêntico a escolher Maria e João — é a mesma dupla! Quando trocar a ordem NÃO muda o grupo (a ordem NÃO importa), temos uma COMBINAÇÃO."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Radar do Arranjo vs. Combinação",
                    "content": "• A ordem IMPORTA -> ARRANJO (Pódios, cargos distintos, senhas sem repetição, filas).\n  Dica libertadora: Não decore A(n,p) = n!/(n-p)! Use as caixinhas do PFC! Para Presidente e Vice entre 10 alunos: [10] × [9] = 90 chapas.\n\n• A ordem NÃO importa -> COMBINAÇÃO (Comissões, equipes, salada de frutas, apertos de mão, cartas na mão, loterias, triângulos entre pontos)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Por que dividimos por p! e como calcular em 5 segundos"
                },
                {
                    "type": "paragraph",
                    "content": "Veja que sacada maravilhosa: na comissão de 2 alunos entre 10, fazer 10 × 9 = 90 conta 'João e Maria' e 'Maria e João' como se fossem diferentes — cada dupla aparece repetida 2! = 2 vezes. Numa comissão de 3 pessoas, cada trio apareceria contado 3! = 6 vezes! Para apagar essas ordens repetidas, dividimos o Arranjo por p!."
                },
                {
                    "type": "paragraph",
                    "content": "Por isso você nunca precisa escrever fatoriais gigantes como C(10, 3) = 10! / (3! × 7!). Use o Método da Simplificação Rápida: abra apenas 3 números decrescentes em cima começando do 10 (10 × 9 × 8) e divida por 3! embaixo (3 × 2 × 1). Simplificando antes de multiplicar: 9 ÷ 3 = 3 e 8 ÷ 2 = 4. Sobra 10 × 3 × 4 = 120 comissões! Sem contas gigantes!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Clássicos do ENEM: Aperta-mão, Diagonais e Mega-Sena"
                },
                {
                    "type": "paragraph",
                    "content": "Dominando a Combinação, você começa a enxergá-la em problemas que à primeira vista nem parecem de escolha de grupos! Primeiro clássico: numa reunião com 12 executivos, todos se cumprimentam com um único aperto de mão. Quantos apertos ocorrem ao todo? Cada aperto envolve 2 pessoas sem importar quem estendeu a mão primeiro, logo C(12, 2) = (12 × 11) / 2 = 66 apertos."
                },
                {
                    "type": "paragraph",
                    "content": "Segundo clássico: quantas diagonais tem um octógono (8 vértices)? Para traçar um segmento ligando dois vértices quaisquer, a ordem dos vértices não muda o segmento: são C(8, 2) = (8 × 7) / 2 = 28 segmentos ao todo. Desses 28 segmentos, 8 são os lados externos da figura, então sobram 28 - 8 = 20 diagonais! Terceiro clássico: na Mega-Sena você marca 6 dezenas entre 60 números sem importar a ordem em que as bolas caem no globo. O total de jogos possíveis é C(60, 6) = (60 × 59 × 58 × 57 × 56 × 55) / (6 × 5 × 4 × 3 × 2 × 1) = 50.063.860 apostas diferentes!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Comissões com Restrição: juntando E, OU e Complemento"
                },
                {
                    "type": "paragraph",
                    "content": "Agora vamos ao nível 850+ do ENEM, juntando tudo o que você aprendeu neste módulo: Combinação, conectivo E, conectivo OU e probabilidade complementar. Veja como o mesmo problema pode ser resolvido por dois caminhos diferentes — e como o atalho do complemento economiza um tempo precioso na hora da prova."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Nível 850+: A Comissão Médica",
                    "content": "Enunciado: Um hospital tem 6 médicos e 4 enfermeiros para montar uma equipe de 4 profissionais contendo PELO MENOS UM médico. Quantas equipes existem?\n\nCaminho 1 (Somando casos com OU):\n• 1 médico E 3 enfermeiros: C(6,1) × C(4,3) = 6 × 4 = 24.\n• 2 médicos E 2 enfermeiros: C(6,2) × C(4,2) = 15 × 6 = 90.\n• 3 médicos E 1 enfermeiro: C(6,3) × C(4,1) = 20 × 4 = 80.\n• 4 médicos E 0 enfermeiros: C(6,4) × C(4,0) = 15 × 1 = 15.\nTotal = 24 + 90 + 80 + 15 = 209 equipes.\n\nCaminho 2 (Complemento — muito mais rápido!):\nTodas as equipes sem restrição: C(10, 4) = (10 × 9 × 8 × 7) / (4 × 3 × 2 × 1) = 210.\nSubtraímos as equipes proibidas (zero médicos, só os 4 enfermeiros): C(4, 4) = 1.\nTotal válido = 210 - 1 = 209 equipes!"
                },
                {
                    "type": "paragraph",
                    "content": "Veja que perfeição: tudo o que estudamos ao longo destes quatro capítulos se encaixa como engrenagens de um relógio. Agora você mede chances, recorta tabelas na condicional, monta caixinhas com restrições e separa Arranjo de Combinação com total segurança!"
                },
                {
                    "type": "quote",
                    "content": "Na Combinação, invertemos os escolhidos e nada muda; por isso dividimos pela permutação interna p! e multiplicamos apenas o que realmente importa.",
                    "author": "Fechamento do Módulo 10"
                }
            ],
            "quiz": []
        }
    ]
