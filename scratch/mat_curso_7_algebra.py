# -*- coding: utf-8 -*-
"""Curso Completo de Matemática ENEM - Módulo 7: Álgebra (Capítulos 29 a 32)"""


def get_chapters():
    return [
        {
            "id": "cap-29-expressoes-produtos-notaveis-fatoracao",
            "number": 29,
            "title": "Expressões Algébricas, Produtos Notáveis e Fatoração Inteligente",
            "epigraph": {
                "text": "A Álgebra é generosa: ela transforma contas particulares em leis universais.",
                "author": "Jean le Rond d'Alembert"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas à Álgebra: por que as letras entraram na Matemática?"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao nosso módulo de Álgebra! Se você já olhou para letras misturadas com números e pensou 'por que complicar?', venha comigo fazer as pazes com o famoso x. A Álgebra nasceu para simplificar a vida. Imagine que você trabalha com entregas e cobra R$ 6,00 fixos pela saída mais R$ 2,50 por quilômetro rodado. Para 4 km, a conta é 6 + 2,5 × 4; para 10 km, 6 + 2,5 × 10. Percebeu que a regra nunca muda, só muda a distância? Em vez de listar infinitos exemplos, criamos uma 'caixinha fechada' chamada d e escrevemos 6 + 2,5d. A letra é apenas um apelido prático para um número variável ou desconhecido."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Dicionário Mágico: traduzindo do português para o matematiquês"
                },
                {
                    "type": "paragraph",
                    "content": "No ENEM, a equação quase nunca vem pronta: o desafio é traduzir o enunciado sem cair em armadilhas de parênteses. Veja como uma vírgula ou preposição muda tudo. 'O dobro de um número somado com 5' significa dobrar primeiro e somar depois: 2x + 5. Já 'o dobro da soma de um número com 5' exige parênteses antes de multiplicar: 2(x + 5). Para x = 3, a primeira vale 11 e a segunda vale 16!"
                },
                {
                    "type": "paragraph",
                    "content": "Guarde outras traduções campeãs de prova: 'a diferença entre o quadrado de um número e sua terça parte' é x² - x/3, enquanto 'o quadrado da diferença entre um número e sua terça parte' fica (x - x/3)². Três números inteiros consecutivos são x, x + 1 e x + 2, somando 3x + 3. Um número par qualquer escreve-se 2n, e um ímpar qualquer, 2n + 1."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: A Ordem na Subtração Importa!",
                    "content": "Se o texto disser 'João tem 5 anos a menos que Maria' (idade m), a idade de João é m - 5, e NÃO 5 - m! E 'x excede y em 12 unidades' significa x - y = 12 (ou x = y + 12). Sempre teste com números fáceis para conferir o sentido da frase."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Valor Numérico: abrindo a caixinha com segurança"
                },
                {
                    "type": "paragraph",
                    "content": "Calcular o valor numérico é abrir a caixinha da letra, colocar o número dado e resolver as operações. O maior perigo mora nos negativos! Regra de ouro: sempre coloque o número negativo entre parênteses ao substituir. Vamos calcular V = x² - 3xy + y² para x = -2 e y = 3: temos V = (-2)² - 3 · (-2) · (3) + (3)². Note que (-2)² dá +4 (sem parênteses, -2² daria -4!). Depois, -3 · (-2) · 3 = +18, e 3² = 9. Somando tudo: V = 4 + 18 + 9 = 31."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Três Produtos Notáveis que Salvam sua Prova"
                },
                {
                    "type": "paragraph",
                    "content": "Três multiplicações aparecem tanto que ganharam atalhos próprios. O primeiro é o Quadrado da Soma: (a + b)² = a² + 2ab + b². Pense em um quadrado de lado (a + b) dividido internamente em quatro peças: um quadrado a², um quadrado b² e dois retângulos ab. Juntando tudo, aparecem exatamente os três termos!"
                },
                {
                    "type": "paragraph",
                    "content": "O segundo é o Quadrado da Diferença: (a - b)² = a² - 2ab + b² (só o termo do meio fica negativo). O terceiro — queridinho do ENEM — é o Produto da Soma pela Diferença: (a + b)(a - b) = a² - b², pois +ab e -ab se cancelam. Olhe a magia no cálculo mental: 53² = (50 + 3)² = 2500 + 300 + 9 = 2809; 98² = (100 - 2)² = 10000 - 400 + 4 = 9604; e 104 × 96 = (100 + 4)(100 - 4) = 10000 - 16 = 9984!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: O Erro Mortal da Álgebra",
                    "content": "Nunca escreva que (x + 3)² = x² + 9! Faltaram os dois retângulos do meio (2ab). O quadrado da soma sempre tem três termos: (x + 3)² = x² + 6x + 9."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fatoração Inteligente: fazendo o caminho de volta"
                },
                {
                    "type": "paragraph",
                    "content": "Fatorar é transformar uma soma ou subtração em multiplicação, permitindo simplificar frações algébricas. Domine três técnicas essenciais. Primeiro, Fator Comum em Evidência: em 6x² + 9x, ambos os termos dividem por 3x, resultando em 3x(2x + 3). Segundo, Agrupamento em duplas: em ax + ay + 2x + 2y, colocamos 'a' nos dois primeiros e '2' nos últimos: a(x + y) + 2(x + y) = (x + y)(a + 2). Terceiro, Diferença de Quadrados: sempre que vir a² - b², escreva (a + b)(a - b), como em x² - 49 = (x + 7)(x - 7)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido — Nível 800+",
                    "content": "Uma chapa metálica quadrada de 105 cm de lado recebeu um furo quadrado de 95 cm de lado. Qual a área restante? E qual o valor de (x² - 9) / (x² + 6x + 9) para x = 97?\nResolução:\n1) Área restante = 105² - 95² = (105 + 95)(105 - 95) = 200 × 10 = 2.000 cm².\n2) Fatorando a fração: (x + 3)(x - 3) / (x + 3)². Cortando um (x + 3) em cima e embaixo (para x ≠ -3), sobra (x - 3) / (x + 3). Para x = 97, temos (97 - 3) / (97 + 3) = 94 / 100 = 0,94!"
                },
                {
                    "type": "quote",
                    "content": "Fatorar uma expressão difícil é como encontrar o zíper oculto de uma jaqueta: um único movimento abre tudo diante dos seus olhos.",
                    "author": "Curso ENEM de Matemática"
                }
            ],
            "quiz": []
        },
        {
            "id": "cap-30-equacoes-1-grau-inequacoes",
            "number": 30,
            "title": "Equações do 1º Grau e Inequações: O Princípio da Balança e das Restrições",
            "epigraph": {
                "text": "Na igualdade da balança e nos limites das desigualdades, a matemática traduz o equilíbrio e as restrições do mundo real.",
                "author": "Curso ENEM de Matemática"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Balança de Dois Pratos: o segredo por trás de toda equação"
                },
                {
                    "type": "paragraph",
                    "content": "Olá, meu caro estudante! Chegou a hora de resolver igualdades e restrições reais. Imagine uma balança de dois pratos equilibrada na horizontal. À esquerda há três caixinhas idênticas de peso x e um peso de 2 kg; à direita, um peso total de 14 kg. Escrevemos 3x + 2 = 14. Se você tirar 2 kg só da esquerda, a balança tomba! Para manter o equilíbrio, qualquer operação feita de um lado deve ser repetida do outro. Por isso 'passar trocando o sinal' funciona: subtraímos 2 dos dois lados, ficando 3x = 14 - 2 = 12. Depois dividimos os dois lados por 3 e descobrimos x = 4 kg!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Isolando a Incógnita Passo a Passo (Sem Errar Sinais!)"
                },
                {
                    "type": "paragraph",
                    "content": "Siga este roteiro infalível em quatro passos: 1) elimine parênteses com a distributiva; 2) se houver frações numéricas, multiplique toda a equação pelo MMC dos denominadores; 3) junte termos com x de um lado e números do outro; 4) isole o x dividindo pelo seu coeficiente."
                },
                {
                    "type": "paragraph",
                    "content": "Vamos treinar com dois exemplos. Primeiro: 3(x - 2) - 2(x - 5) = 14 - 4x. Abrindo os parênteses: 3x - 6 - 2x + 10 = 14 - 4x → x + 4 = 14 - 4x → x + 4x = 14 - 4 → 5x = 10 → x = 2! Segundo, com frações: x/2 + (x - 1)/3 = 4. O MMC entre 2 e 3 é 6. Multiplicando TODOS os termos por 6 (inclusive o 4!): 3x + 2(x - 1) = 24 → 3x + 2x - 2 = 24 → 5x = 26 → x = 26/5 = 5,2."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: O Sinal Negativo na Frente dos Parênteses",
                    "content": "Em expressões como 10 - (2x - 5) = 3, o sinal de menos antes dos parênteses funciona como um -1 multiplicando TODOS os termos internos! Logo, -(2x - 5) vira -2x + 5, jamais -2x - 5."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Entrando nas Inequações: quando o mundo tem limites e metas"
                },
                {
                    "type": "paragraph",
                    "content": "Na vida real, quase tudo trabalha com limites. Com R$ 150,00 no bolso, sua compra deve ser menor ou igual a 150 (≤ 150). Um elevador com placa 'máximo 600 kg' exige peso ≤ 600. Uma meta de 'pelo menos 20 vendas' pede ≥ 20, e uma empresa lucra quando a receita é maior que o custo (>). Sentenças com <, >, ≤ e ≥ são chamadas de inequações."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Regra Sagrada: por que o sinal vira de cabeça para baixo?"
                },
                {
                    "type": "paragraph",
                    "content": "Resolvemos a inequação quase igual à equação, mas com uma regra sagrada: ao multiplicar ou dividir os dois lados por um número NEGATIVO, invertemos o sentido da desigualdade! Por quê? Pense nos números 2 e 5: todo mundo concorda que 2 < 5. Multiplique ambos por -1 e obtemos -2 e -5. Na conta bancária, quem está melhor, quem deve 2 reais (-2) ou quem deve 5 reais (-5)? Quem deve 2! Logo, -2 > -5: o sinal virou!"
                },
                {
                    "type": "paragraph",
                    "content": "Exemplo resolvido: 10 - 3x ≥ 22. Passando 10 para a direita: -3x ≥ 12. Dividindo os dois lados por -3 (negativo!), invertemos ≥ para ≤: x ≤ 12 / (-3) → x ≤ -4. Quer um truque para nunca precisar inverter? Sempre passe o x para o lado onde ele fique positivo! Em 10 - 3x ≥ 22, fazemos 10 - 22 ≥ 3x → -12 ≥ 3x → -4 ≥ x, que lido ao contrário é exatamente x ≤ -4."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Traduzindo Restrições do ENEM",
                    "content": "• 'No máximo', 'até', 'não ultrapassa': ≤\n• 'No mínimo', 'pelo menos', 'a partir de': ≥\n• 'Supera', 'maior que', 'acima de': >\n• 'Inferior a', 'abaixo de', 'menor que': <"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Modelagem Prática 1: Comparando Locadoras de Carros"
                },
                {
                    "type": "paragraph",
                    "content": "A locadora A cobra diária de R$ 120,00 mais R$ 1,50 por km rodado. A locadora B cobra R$ 180,00 mais R$ 0,90 por km. A partir de quantos quilômetros inteiros a locadora B fica mais barata que a A? Seja x a distância em km. Queremos Custo(B) < Custo(A): 180 + 0,90x < 120 + 1,50x. Isolando x no lado positivo: 180 - 120 < 1,50x - 0,90x → 60 < 0,60x → x > 100. Em 100 km os preços empatam em R$ 270,00; portanto, B fica mais barata a partir de 101 km!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Modelagem Prática 2: Capacidade Máxima de Carga"
                },
                {
                    "type": "paragraph",
                    "content": "Um caminhão suporta carga máxima de 3.200 kg. Já transporta o motorista (80 kg) e uma máquina (450 kg), e vai carregar n caixas de 35 kg cada. Qual o máximo de caixas por viagem? Montamos: 80 + 450 + 35n ≤ 3200 → 530 + 35n ≤ 3200 → 35n ≤ 2670 → n ≤ 76,285... Como não há fração de caixa e 77 caixas estourariam o limite, o máximo inteiro é 76 caixas (3.190 kg)."
                },
                {
                    "type": "quote",
                    "content": "Resolver uma inequação é descobrir a fronteira exata entre o que cabe no orçamento e o que ultrapassa o limite permitido.",
                    "author": "Curso ENEM de Matemática"
                }
            ],
            "quiz": []
        },
        {
            "id": "cap-31-equacoes-2-grau-bhaskara-soma-produto",
            "number": 31,
            "title": "Equações do 2º Grau: Bhaskara, Soma e Produto e Análise do Delta",
            "epigraph": {
                "text": "Quem entende o discriminante e domina Soma e Produto enxerga a estrutura da equação antes mesmo de fazer contas.",
                "author": "Curso ENEM de Matemática"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Salto para o 2º Grau: reconhecendo a forma geral"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Quando calculamos áreas de terrenos, trajetórias de lançamento ou descontos progressivos, a incógnita aparece elevada ao quadrado: é a equação do 2º grau, ax² + bx + c = 0, com a ≠ 0. Antes de aplicar qualquer fórmula, iguale tudo a zero e identifique a, b e c pelos expoentes, nunca pela ordem de escrita! Em 5 - 3x + 2x² = 0, temos a = 2 (junto de x²), b = -3 (junto de x) e c = 5 (termo independente)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Equações Incompletas: resolva em 5 segundos sem Bhaskara!"
                },
                {
                    "type": "paragraph",
                    "content": "Não use canhão para matar formiga! Se faltar b ou c, resolva em segundos. Caso 1 (c = 0): coloque x em evidência! Em x² - 7x = 0, temos x(x - 7) = 0. Se um produto dá zero, um dos fatores é zero: logo x1 = 0 ou x - 7 = 0 (x2 = 7). Caso 2 (b = 0): isole o x²! Em 2x² - 50 = 0, fazemos 2x² = 50 → x² = 25 → x = ±√25 = ±5. E se aparecer x² + 9 = 0? Como x² = -9 é impossível nos reais, não há raízes reais!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Nunca 'Corte o x' Dos Dois Lados!",
                    "content": "Em x² = 5x, jamais divida os dois lados por x achando só x = 5! Ao cortar o x, você joga fora a raiz x = 0. Passe tudo para um lado: x² - 5x = 0 → x(x - 5) = 0 → raízes 0 e 5."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fórmula de Bhaskara: entendendo a ferramenta completa"
                },
                {
                    "type": "paragraph",
                    "content": "Quando os três coeficientes a, b e c são diferentes de zero, entra em cena a famosa Fórmula de Bhaskara. Primeiro calculamos o discriminante, a letra grega Delta: Δ = b² - 4ac. Depois encontramos as raízes por x = (-b ± √Δ) / (2a). Para essa fórmula fazer sentido na sua cabeça, perceba o significado geométrico de cada pedaço: o termo -b/(2a) representa exatamente o ponto central de simetria da parábola, enquanto ±√Δ/(2a) mostra o quanto cada raiz se afasta desse centro para a esquerda e para a direita."
                },
                {
                    "type": "paragraph",
                    "content": "Vamos resolver juntos 2x² - 5x - 3 = 0 passo a passo, sem tropeçar nos sinais (aqui a = 2, b = -5, c = -3). Calculando Δ sempre usando parênteses nos negativos: Δ = (-5)² - 4 · (2) · (-3). Lembre-se de que (-5)² vale +25 e que -4 · 2 · (-3) vale +24. Somando os dois, obtemos Δ = 25 + 24 = 49, cuja raiz exata é √49 = 7! Agora aplicamos a segunda parte da fórmula, prestando muita atenção ao sinal duplo de -b: x = (-(-5) ± 7) / (2 · 2) = (5 ± 7) / 4. Abrindo os dois caminhos possíveis: usando o sinal de mais, x1 = (5 + 7)/4 = 12/4 = 3; usando o sinal de menos, x2 = (5 - 7)/4 = -2/4 = -1/2 (ou -0,5). Fazendo a prova real rápida para x = 3: 2(9) - 5(3) - 3 = 18 - 15 - 3 = 0!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Termômetro da Equação: interpretando o Delta"
                },
                {
                    "type": "paragraph",
                    "content": "O ENEM adora perguntar quantas soluções um problema possui apenas analisando o sinal de Δ, sem exigir que você calcule as raízes! Pense no Δ como o termômetro da equação: se Δ > 0, existe √Δ positiva, então o 'mais ou menos' produz duas raízes reais distintas. Se Δ = 0, como √0 = 0, somar ou subtrair zero dá o mesmo resultado, gerando uma única raiz real dupla (a parábola apenas toca o eixo x). Se Δ < 0, não existe raiz quadrada real de número negativo, logo não existem raízes reais. Exemplo clássico de prova: para qual valor de k a equação x² - 6x + k = 0 tem raiz única? Exigimos Δ = 0: (-6)² - 4(1)(k) = 0 → 36 - 4k = 0 → k = 9!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Atalho Ninja: Soma e Produto (Relações de Girard)"
                },
                {
                    "type": "paragraph",
                    "content": "Para ganhar velocidade máxima, use Soma (S = x1 + x2 = -b/a) e Produto (P = x1 · x2 = c/a). Quando a = 1, basta achar de cabeça dois números que multiplicam c e somam o oposto de b! Em x² - 9x + 20 = 0, buscamos produto 20 e soma 9 → 4 e 5! E em x² + 2x - 15 = 0? Produto -15 e soma -2: como o produto é negativo, os sinais são opostos; testando 3 e 5, achamos -5 e +3, pois (-5)·3 = -15 e -5 + 3 = -2! Além disso, quando o ENEM pede diretamente a soma ou o produto das raízes de uma equação grande, essas fórmulas resolvem tudo sem precisar achar cada raiz."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Soma, Produto e Quadrados",
                    "content": "Se uma questão pedir x1² + x2² em uma equação com raízes feias, não use Bhaskara! Lembre de (x1 + x2)² = x1² + 2·x1·x2 + x2², logo x1² + x2² = S² - 2P. É só substituir S = -b/a e P = c/a!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Problema Real do ENEM: Terreno Retangular e Descarte de Raiz"
                },
                {
                    "type": "paragraph",
                    "content": "Um paisagista quer um canteiro retangular cujo comprimento tenha 5 m a mais que a largura, com área total de 84 m². Chamando a largura de x, o comprimento é x + 5, logo x(x + 5) = 84 → x² + 5x - 84 = 0. Por Soma e Produto: S = -5 e P = -84. Como 7 × 12 = 84, as raízes são 7 e -12. Como largura não pode ser negativa, descartamos -12! Resposta: largura 7 m e comprimento 12 m."
                },
                {
                    "type": "quote",
                    "content": "Em problemas reais, a álgebra entrega todas as raízes possíveis, mas é a sua leitura do contexto que escolhe a solução verdadeira.",
                    "author": "Curso ENEM de Matemática"
                }
            ],
            "quiz": []
        },
        {
            "id": "cap-32-sistemas-equacoes-problemas-enem",
            "number": 32,
            "title": "Sistemas de Equações e Resolução de Problemas Algébricos do ENEM",
            "epigraph": {
                "text": "Uma incógnita sozinha admite infinitos caminhos; duas pistas independentes revelam a resposta exata.",
                "author": "Curso ENEM de Matemática"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Duas Incógnitas, Duas Pistas: bem-vindo aos Sistemas Lineares"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Fechamos nosso módulo de Álgebra com um dos assuntos mais rentáveis de toda a prova do ENEM: sistemas de equações! Pense comigo: se eu disser que comprei um café e um pão de queijo por R$ 14,00 (c + p = 14), existem infinitos preços possíveis (6 e 8, 5 e 9, 4 e 10...). Mas se eu acrescentar uma segunda pista independente — que o pão de queijo custou R$ 2,00 a mais que o café (p = c + 2) — as duas condições travam uma única resposta verdadeira! Primeiro mandamento antes de começar qualquer conta: sempre batize as variáveis com letras intuitivas (como c e p) para nunca trocar os valores na hora do gabarito."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Método da Substituição vs. Método da Adição"
                },
                {
                    "type": "paragraph",
                    "content": "Na Substituição, imbatível quando uma letra já está isolada ou tem coeficiente 1, você isola essa letra numa equação e a encaixa dentro da outra. No nosso exemplo da padaria: trocando p por (c + 2) em c + p = 14, temos c + (c + 2) = 14 → 2c = 12 → c = 6 reais e p = 8 reais."
                },
                {
                    "type": "paragraph",
                    "content": "Na Adição, ideal quando as letras aparecem alinhadas com números na frente, somamos as duas equações termo a termo para cancelar uma incógnita na hora. Se tivermos 3x + 2y = 23 e x - y = 1, basta multiplicar a segunda equação inteira por +2, obtendo 2x - 2y = 2. Somando com a primeira equação, +2y e -2y se anulam perfeitamente, sobrando 5x = 25 → x = 5 e, voltando na segunda equação, y = 4."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Não Trabalhe Dobrado!",
                    "content": "Antes de resolver o sistema inteiro, leia a pergunta final do ENEM! Às vezes a questão pede apenas (x + y) ou (2x + 3y), e somar ou subtrair as equações originais entrega a resposta direta em uma linha."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Clássico 1 do ENEM: Ingressos, Cédulas e 'Cabeças e Pés'"
                },
                {
                    "type": "paragraph",
                    "content": "Em um estacionamento há carros (4 rodas) e motos (2 rodas), totalizando 35 veículos e 116 rodas. Quantos veículos há de cada tipo? Definimos c + m = 35 e 4c + 2m = 116. Multiplicando a primeira equação inteira por -2, ficamos com -2c - 2m = -70. Somando com 4c + 2m = 116, os termos com m desaparecem e obtemos 2c = 46 → c = 23 carros e m = 35 - 23 = 12 motos! Conferindo rapidamente: 23 × 4 + 12 × 2 = 92 + 24 = 116 rodas. Esse mesmo esqueleto algébrico resolve ingressos (inteira e meia-entrada), notas de dinheiro e mesas de restaurante!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Clássico 2 do ENEM: Misturas de Cafés, Sucos e Ligas Metálicas"
                },
                {
                    "type": "paragraph",
                    "content": "Receita fixa para problemas de misturas: uma equação soma as quantidades totais e a outra equação soma o valor financeiro (ou concentração) total! Um comerciante mistura café tipo A (R$ 20/kg) com café tipo B (R$ 32/kg) para obter 60 kg de um lote especial a R$ 25/kg. Montamos a + b = 60 e 20a + 32b = 60 × 25 = 1500. Substituindo b = 60 - a na segunda equação: 20a + 32(60 - a) = 1500 → 20a + 1920 - 32a = 1500 → -12a = -420 → a = 35 kg de café A e b = 25 kg de café B. Faz todo sentido: como R$ 25 está mais perto de R$ 20, vai mais café tipo A!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Clássico 3 do ENEM: Problemas de Idades (O Tempo Passa para Todos!)"
                },
                {
                    "type": "paragraph",
                    "content": "Hoje, Marina tem o triplo da idade de seu filho Lucas (m = 3l). Daqui a 10 anos, ela terá o dobro da idade dele. Como o tempo passa igualmente para os dois, ambos ganham 10 anos: m + 10 = 2(l + 10) → m + 10 = 2l + 20. Substituindo m = 3l: 3l + 10 = 2l + 20 → l = 10 anos e m = 30 anos! Conferindo: hoje 30 é o triplo de 10; daqui a 10 anos terão 40 e 20 anos, e 40 é exatamente o dobro de 20."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Esquecer de Envelhecer a Outra Pessoa",
                    "content": "Um erro clássico é escrever m + 10 = 2l em vez de m + 10 = 2(l + 10). Sempre adicione (ou subtraia) o tempo passado na idade de TODAS as pessoas da frase, usando parênteses!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Clássico 4 do ENEM: Combos e Estoque com Três Variáveis"
                },
                {
                    "type": "paragraph",
                    "content": "Veja um truque nível 800+ para três variáveis em estoque ou lanchonete: Combo 1 (su + sa + do = 22), Combo 2 (2su + 2sa + do = 37) e Combo 3 (su + 2sa + 2do = 39). Quanto custa 1 salgado (sa)? Em vez de se perder em contas longas, subtraia Combo 1 de Combo 2: (2su + 2sa + do) - (su + sa + do) = 37 - 22 → su + sa = 15. Como su + sa + do = 22, descobrimos na hora que o doce custa do = 7 reais! Agora subtraia Combo 1 de Combo 3: sa + do = 39 - 22 = 17. Logo, sa + 7 = 17 → 1 salgado custa R$ 10,00 (e o suco, R$ 5,00)!"
                },
                {
                    "type": "quote",
                    "content": "A força da Álgebra no ENEM está em enxergar relações escondidas entre quantidades e transformá-las em atalhos até a resposta.",
                    "author": "Curso ENEM de Matemática"
                }
            ],
            "quiz": []
        }
    ]
