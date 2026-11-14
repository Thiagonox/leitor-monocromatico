# -*- coding: utf-8 -*-
"""Curso Completo de Matemática ENEM - Módulo 3: Matemática Financeira e Negócios (Capítulos 9 a 13)."""


def get_chapters():
    return [
        {
            "id": "mat-curso-cap-09-porcentagem-fatores",
            "number": 9,
            "title": "Porcentagem na Ponta da Língua: Fatores Multiplicativos e Cálculo Mental",
            "epigraph": {
                "text": "Quem domina porcentagem não faz contas longas no rascunho; enxerga proporções de cabeça e ganha minutos preciosos no segundo dia do ENEM.",
                "author": "Aula Inaugural de Matemática Financeira"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas ao Coração da Matemática do Dia a Dia"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo a este módulo que transforma sua nota no ENEM e a forma como você enxerga o seu bolso. Depois de razão e proporção, o assunto que mais aparece na prova está em toda vitrine: porcentagem. Ela surge em gráficos de desmatamento, tabelas de vacinação, reajustes salariais, contas de luz e promoções. Hoje, vamos colocá-la na ponta da língua para você resolver questões com velocidade de candidato 800+."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Que Significa 'Por Cento' de Verdade?"
                },
                {
                    "type": "paragraph",
                    "content": "Pense na palavra: por cento vem do latim per centum, literalmente 'a cada cem'. Quando você ouve que 35% das pessoas preferem café sem açúcar, significa que, em um grupo de 100 pessoas, exatamente 35 tomam café amargo. Matematicamente, 35% é a razão centesimal 35/100, escrita em decimal como 0,35. Essa trinca — percentual (35%), fracionária (35/100) e decimal (0,35) — representa exatamente o mesmo valor."
                },
                {
                    "type": "paragraph",
                    "content": "Veja que sacada importante: muita gente erra ao converter porcentagens menores que 10% em decimal. Dividir por 100 significa andar com a vírgula duas casas para a esquerda. Assim, 8% vira 8/100 = 0,08, e não 0,8 (que vale 80%)! Da mesma forma, 2,5% vira 0,025, e 0,4% vira 0,004. Já quando passa de 100%, o decimal passa de 1: 150% equivale a 150/100 = 1,50, ou uma vez e meia o valor original."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Porcentagens Clássicas em Fração",
                    "content": "Memorizar equivalências acelera suas contas no ENEM: 50% = 1/2 (metade); 25% = 1/4 (dividir por 4); 20% = 1/5 (dividir por 5); 10% = 1/10 (dividir por 10); 5% = 1/20 (metade de 10%); 75% = 3/4; e 1% = 1/100. Pediu 25% de 480 litros? Não monte regra de três: divida 480 por 4 e crave 120 litros em dois segundos."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Técnica Mental dos 10%, 1%, 5% e 50%"
                },
                {
                    "type": "paragraph",
                    "content": "Agora vamos ao truque de cálculo mental mais útil da matemática básica. Todo valor inteiro representa 100% dele mesmo, e daí tiramos quatro âncoras sem calculadora: 50% é a metade do número; 10% surge andando com a vírgula uma casa para a esquerda; 5% é exatamente a metade de 10%; e 1% surge andando com a vírgula duas casas para a esquerda."
                },
                {
                    "type": "paragraph",
                    "content": "Vamos testar em um aluguel de R$ 1.800,00. De cabeça: 50% é a metade, R$ 900,00; 10% anda uma casa, R$ 180,00; 5% é metade de 180, R$ 90,00; e 1% anda duas casas, R$ 18,00. Agora veja a mágica: se o reajuste for de 17%, não multiplique 1.800 por 17 no papel! Decomponha 17% em 10% + 5% + 1% + 1%. Somando nossas peças: 180 + 90 + 18 + 18 = R$ 306,00! Leve e à prova de erros."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Cálculo Mental em Conta de Restaurante",
                    "content": "Um grupo jantou e a conta fechou em R$ 240,00. O garçom sugeriu taxa de serviço de 15%, mas um amigo tinha cupom de desconto de 2% sobre a conta. Qual a diferença, em reais, entre a taxa e o desconto?\nPasso 1: 10% de R$ 240,00 = R$ 24,00.\nPasso 2: 5% é metade de 10% -> R$ 12,00. Logo, 15% = 24 + 12 = R$ 36,00.\nPasso 3: 1% de R$ 240,00 = R$ 2,40. Logo, 2% = 2 x 2,40 = R$ 4,80.\nPasso 4: Subtraímos: 36,00 - 4,80 = R$ 31,20. Resolvido de forma limpa!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Poder do Fator Multiplicativo para Ir Direto à Resposta"
                },
                {
                    "type": "paragraph",
                    "content": "Se a técnica dos 10% e 1% é maravilhosa para contas rápidas de cabeça, o Fator Multiplicativo é a ferramenta definitiva para resolver problemas com múltiplos passos, equações e aumentos ou descontos diretos. Pense comigo: quando você calcula um aumento de 20% pelo método tradicional, faz duas etapas — primeiro acha 20% do valor e depois soma ao valor inicial. Mas existe uma forma de fazer tudo em uma única multiplicação! Como o valor original representa 100% (ou 1 inteiro), aumentar i% significa passar a ter (100% + i%)."
                },
                {
                    "type": "paragraph",
                    "content": "Assim, para calcular um aumento de 20%, em vez de achar 20% e somar, você multiplica diretamente por 1 + 0,20 = 1,20! Quer dar um aumento de 8%? Multiplique por 1 + 0,08 = 1,08. Quer dar um aumento de 3,5%? Multiplique por 1,035. E nos descontos? A lógica é idêntica, só que subtraindo de 100% (ou de 1). Se uma jaqueta tem 30% de desconto, você não vai pagar 30%, vai pagar o que sobrou: 100% - 30% = 70%. Logo, basta multiplicar o preço original por 1 - 0,30 = 0,70! Um desconto de 12% significa pagar 88%, então multiplique por 0,88. Um desconto de 5% significa multiplicar por 0,95."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: O Caminho de Volta!",
                    "content": "Muita atenção aqui porque é aqui que a maioria cai no ENEM! Suponha que uma loja anunciou um tênis já com 20% de desconto por R$ 240,00, e a questão pergunta qual era o preço ORIGINAL antes da promoção. O erro fatal é calcular 20% de 240 (que dá 48) e somar, achando R$ 288,00. Isso está ERRADO porque os 20% foram descontados do preço antigo, e não de 240! Usando o fator multiplicativo, você monta a equação perfeita: Preço_Original x 0,80 = 240. Passando 0,80 dividindo: Preço_Original = 240 / 0,80 = R$ 300,00. Percebeu a diferença? Com fator multiplicativo, ir e voltar nunca dá erro!"
                },
                {
                    "type": "quote",
                    "content": "Na matemática financeira, multiplicar pelo fator certo economiza metade das contas e elimina cem por cento das dúvidas sobre qual é a base do cálculo.",
                    "author": "Manual do Candidato 800+"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Questão Comentada Passo a Passo"
                },
                {
                    "type": "paragraph",
                    "content": "Vamos fechar este capítulo com uma situação completa de prova. Imagine que um reservatório agrícola possuía uma certa quantidade de água e, após uma reforma com ampliação, sua capacidade cresceu 35%, passando a comportar 54.000 litros. Qual era a capacidade inicial antes da reforma? Veja como o fator multiplicativo resolve em duas linhas: um aumento de 35% corresponde ao fator 1 + 0,35 = 1,35. Chamando a capacidade inicial de C, escrevemos C x 1,35 = 54.000. Isolando C, temos C = 54.000 / 1,35. Para dividir sem vírgula, multiplicamos em cima e em baixo por 100: 5.400.000 / 135. Como 540 dividido por 135 dá exatamente 4, encontramos C = 40.000 litros! Simples, elegante e à prova de pegadinhas."
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-10-aumentos-descontos-variacao",
            "number": 10,
            "title": "Aumentos, Descontos Sucessivos e Variação Percentual Real",
            "epigraph": {
                "text": "Porcentagens não se somam; fatores se multiplicam. Quem entende essa regra nunca mais cai na armadilha do 'sobe 20% e cai 20%'.",
                "author": "Aula de Estratégia Financeira"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Grande Mito: Por Que +20% e -20% Não Volta ao Início?"
                },
                {
                    "type": "paragraph",
                    "content": "Seja muito bem-vindo ao nosso décimo encontro! Hoje vamos desmascarar uma pegadinha clássica do ENEM e das vitrines. Imagine que um celular custa R$ 1.000,00. Na semana passada, sofreu um aumento de 20%. Hoje, o gerente anuncia: 'Queima de estoque! Baixei 20% para voltar ao preço antigo!'. O celular voltou a custar R$ 1.000,00? Se o seu instinto disse sim, acompanhe comigo a conta real."
                },
                {
                    "type": "paragraph",
                    "content": "Quando o celular de R$ 1.000,00 subiu 20%, foi para 1.000 x 1,20 = R$ 1.200,00. Agora, o desconto de 20% não incide mais sobre R$ 1.000,00, mas sobre a nova base de R$ 1.200,00! Como 20% de 1.200 vale R$ 240,00, subtraindo 240 de 1.200 chegamos a R$ 960,00! Houve uma redução líquida de 4%, e não de 0%. Usando os fatores multiplicativos, fica cristalino: 1,20 x 0,80 = 0,96, isto é, 96% do valor inicial — uma queda real de 4%."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: A Ordem dos Fatores Não Altera o Produto!",
                    "content": "Uma dúvida muito comum dos alunos é: 'Professor, e se o celular primeiro caísse 20% e depois subisse 20%, daria diferente?'. Vamos testar! Como a multiplicação é comutativa, 0,80 x 1,20 também dá exatamente 0,96! Primeiro cai para R$ 800,00, e depois 20% de 800 é 160, somando R$ 960,00 do mesmo jeito. Guarde isso: em variações percentuais sucessivas, você SEMPRE multiplica os fatores, nunca soma nem subtrai as taxas diretamente."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Aumentos em Cascata e Descontos Compostos"
                },
                {
                    "type": "paragraph",
                    "content": "Agora que o fator multiplicativo já é seu melhor amigo, vamos ver o que acontece quando uma mercadoria ou um imposto sofre vários aumentos seguidos — o famoso efeito cascata. Suponha que a passagem de ônibus subiu 10% em janeiro e depois subiu mais 10% em julho. Quem não estudou com a gente marca na hora que o aumento acumulado no ano foi de 20%. Mas nós sabemos que o primeiro aumento multiplica o preço por 1,10, e o segundo aumento multiplica esse novo valor por 1,10 novamente. Multiplicando os fatores: 1,10 x 1,10 = 1,21. Como 1,21 significa 1 + 0,21, o aumento real acumulado foi de 21%!"
                },
                {
                    "type": "paragraph",
                    "content": "E nos descontos sucessivos das liquidações? Sabe aquela placa famosa na vitrine: '50% + 20% de desconto na boca do caixa'? Muita gente desavisada acha que vai ganhar 70% de desconto e pagar apenas 30% do produto. Vamos fazer a conta justa? O primeiro desconto de 50% reduz o preço à metade, aplicando o fator 0,50. Sobre essa metade restante, aplica-se o segundo desconto de 20%, cujo fator é 0,80. Multiplicando os dois fatores: 0,50 x 0,80 = 0,40! Ou seja, o cliente vai pagar 40% do preço original. Se ele paga 40%, o desconto total real foi de 100% - 40% = 60%, e não 70%!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Promoção Black Friday com Três Etapas",
                    "content": "Um notebook custava R$ 4.000,00. Na véspera da promoção, a loja aumentou o preço em 25%. No dia seguinte, anunciou 'Super desconto de 20%' e, para pagamento no PIX, ofereceu mais 10% sobre o valor promocional. Qual foi o preço final no PIX e qual foi a variação percentual total em relação aos R$ 4.000,00 iniciais?\nPasso 1: Convertemos cada variação em fator multiplicativo: +25% -> 1,25; -20% -> 0,80; -10% -> 0,90.\nPasso 2: Multiplicamos os fatores em cadeia: 1,25 x 0,80 x 0,90. Note que 1,25 x 0,80 = 1,00 (voltou ao valor inicial!). Depois 1,00 x 0,90 = 0,90.\nPasso 3: Preço final = 4.000 x 0,90 = R$ 3.600,00. Como o fator acumulado foi 0,90 (90% do inicial), houve um desconto real efetivo de apenas 10% em relação ao preço antes da maquiagem!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Como Calcular a Variação Percentual Entre Dois Valores"
                },
                {
                    "type": "paragraph",
                    "content": "Outra cobrança que despenca nos gráficos e tabelas do ENEM é a seguinte: a prova te mostra um valor antigo (Inicial) e um valor novo (Final) e pergunta de quanto por cento foi o aumento ou a queda. Existe uma fórmula simples e infalível que você precisa gravar na alma: Variação Percentual = (Valor Final - Valor Inicial) / Valor Inicial. Veja por que o denominador é SEMPRE o Valor Inicial: porque toda mudança percentual é medida tomando como referência o ponto de partida, de onde você saiu."
                },
                {
                    "type": "paragraph",
                    "content": "Vamos praticar com dois exemplos bem claros. Primeiro, um caso de aumento: a produção de soja de uma fazenda saltou de 800 toneladas em 2024 para 1.000 toneladas em 2025. Aplicando a fórmula: (1.000 - 800) / 800 = 200 / 800 = 1/4 = 0,25, que equivale a +25%. Agora, um caso de queda: o número de focos de incêndio caiu de 1.000 para 800. Aplicando a mesma fórmula: (800 - 1.000) / 1.000 = -200 / 1.000 = -0,20, ou seja, uma redução de 20%. Reparou na maravilha desse exemplo? Ir de 800 para 1.000 é um aumento de 25%, mas voltar de 1.000 para 800 é uma queda de 20%! As porcentagens são diferentes justamente porque o ponto de partida (o denominador) mudou."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: O Atalho da Razão Direta",
                    "content": "Quer descobrir a variação percentual ainda mais rápido? Basta dividir diretamente o Valor Final pelo Valor Inicial! Esse quociente já é o próprio Fator Multiplicativo. Exemplo: o litro do combustível foi de R$ 5,00 para R$ 5,60. Divida 5,60 / 5,00 = 1,12. Se o fator deu 1,12, você já lê imediatamente: aumento de 12%! Outro exemplo: uma ação na bolsa caiu de R$ 40,00 para R$ 34,00. Divida 34 / 40 = 0,85. Quanto falta para chegar a 1,00? Falta 0,15. Logo, queda de 15%! Esse atalho poupa preciosos segundos na prova."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Que Fazer Para Compensar Uma Queda Percentual?"
                },
                {
                    "type": "paragraph",
                    "content": "Para fechar com chave de ouro, pense neste desafio clássico de nível 800+: se um produto sofreu uma redução de 20% em seu preço, de quantos por cento deve ser o aumento seguinte para que ele retorne exatamente ao preço original? Já sabemos que não é 20%! Vamos usar nossa razão direta: após cair 20%, o preço virou 0,80 do original. Para sair de 0,80 e voltar a 1,00, qual deve ser o fator de aumento? Fazemos Final / Inicial = 1,00 / 0,80 = 10 / 8 = 1,25! Um fator de 1,25 significa um aumento de 25%! Ou seja, sempre que algo cai 20%, precisa subir 25% para recuperar o patamar inicial. Guarde essa lógica do fator multiplicativo e nenhuma questão de variação percentual derrubará você!"
                },
                {
                    "type": "quote",
                    "content": "Subir 25% e cair 20% devolve exatamente ao ponto de partida, porque cinco quartos vezes quatro quintos é igual a um.",
                    "author": "Aritmética das Proporções"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-11-juros-simples-compostos",
            "number": 11,
            "title": "Juros Simples, Juros Compostos e Taxas de Juros: Linear vs. Exponencial",
            "epigraph": {
                "text": "Os juros compostos são a oitava maravilha do mundo: quem os entende, ganha; quem não os entende, paga.",
                "author": "Atribuído a Albert Einstein"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Aluguel do Dinheiro e os Quatro Personagens da História"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos ao capítulo que separa quem apenas decora fórmulas de quem realmente entende como o dinheiro cresce ou vira bola de neve ao longo do tempo. Pense comigo: quando você aluga um apartamento, você paga um valor mensal pelo direito de usar o imóvel de outra pessoa, certo? Com dinheiro é exatamente igual: o juro (J) é o aluguel que se paga — ou se recebe — pelo uso de uma quantia durante certo tempo. Quem empresta dinheiro ao banco (investidor) recebe juros; quem pega dinheiro emprestado (tomador) paga juros."
                },
                {
                    "type": "paragraph",
                    "content": "Para conversar a mesma língua que os bancos e a banca do ENEM, precisamos dominar quatro símbolos fundamentais. O Capital (C) é a quantia inicial aplicada ou emprestada, o dinheiro na data zero. A Taxa de Juros (i) é o percentual cobrado em cada período, geralmente escrito em forma decimal nas fórmulas (por exemplo, 5% ao mês entra como 0,05). O Tempo (t ou n) é o número de períodos em que o dinheiro fica rendendo. E o Montante (M) é a soma final: o capital inicial mais todos os juros acumulados, ou seja, M = C + J."
                },
                {
                    "type": "callout",
                    "title": "Regra de Ouro: Taxa e Tempo na Mesma Unidade!",
                    "content": "Antes de colocar qualquer número na fórmula, faça uma checagem obrigatória: a taxa (i) e o tempo (t) estão falando a mesma língua? Se a taxa estiver ao mês (a.m.) e o tempo em anos, você DEVE converter um dos dois para que ambos fiquem em meses ou ambos em anos. Ignorar essa regra é a causa número um de erros em questões fáceis e médias de Matemática Financeira no ENEM."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Juros Simples vs. Juros Compostos: Duelo Mês a Mês"
                },
                {
                    "type": "paragraph",
                    "content": "Vamos entender a diferença prática entre os dois regimes de capitalização acompanhando o mesmo investimento de R$ 1.000,00 a uma taxa de 10% ao mês durante 3 meses. No regime de Juros Simples, os juros de cada mês são calculados SEMPRE sobre o capital inicial (C). Como 10% de R$ 1.000,00 são R$ 100,00, todo santo mês o investimento ganha exatamente os mesmos R$ 100,00. No mês 1 vai para R$ 1.100,00; no mês 2 vai para R$ 1.200,00; no mês 3 chega a R$ 1.300,00. Perceba que os valores crescem somando uma constante (+100), formando uma Progressão Aritmética (PA). As fórmulas são diretas: J = C . i . t e M = C . (1 + i . t)."
                },
                {
                    "type": "paragraph",
                    "content": "Agora observe o que acontece com os mesmos R$ 1.000,00 a 10% ao mês nos Juros Compostos — o famoso 'juros sobre juros'. Aqui, a taxa incide sempre sobre o montante do mês imediatamente anterior! No mês 1, calculamos 10% de R$ 1.000,00 (+100) e chegamos a R$ 1.100,00 — igualzinho ao simples até aqui! Mas no mês 2, calculamos 10% sobre R$ 1.100,00, o que dá R$ 110,00 de juros, levando o montante a R$ 1.210,00. No mês 3, calculamos 10% sobre R$ 1.210,00, rendendo R$ 121,00 e alcançando R$ 1.331,00! Repare que a cada mês multiplicamos o montante anterior pelo fator 1,10. Isso forma uma Progressão Geométrica (PG), cuja fórmula é M = C . (1 + i)^t."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Representação Gráfica: A Reta Contra a Curva Exponencial"
                },
                {
                    "type": "paragraph",
                    "content": "O ENEM adora pedir para você identificar qual gráfico representa juros simples e qual representa juros compostos. Visualize o plano cartesiano com o Tempo no eixo horizontal e o Montante no eixo vertical. Como nos juros simples o montante cresce em quantias fixas a cada período, sua função M(t) = C + (C.i).t é uma função afim do 1º grau: o gráfico é uma LINHA RETA crescente partindo do ponto (0, C). Já nos juros compostos, como M(t) = C . (1 + i)^t tem a variável t no expoente, trata-se de uma função exponencial: o gráfico também parte de (0, C), mas forma uma CURVA ascendente que fica cada vez mais inclinada com o passar do tempo."
                },
                {
                    "type": "paragraph",
                    "content": "Um detalhe genial que já foi questão de prova: para t = 0, os dois montantes são iguais a C; para t = 1 período, os dois montantes TAMBÉM são exatamente iguais (M = C.(1+i))! Entre t = 0 e t = 1, inclusive, matematicamente a reta dos juros simples fica ligeiramente acima da curva exponencial. Mas, a partir de t > 1 período, a curva exponencial dos juros compostos ultrapassa a reta e dispara para cima, abrindo uma distância gigantesca em prazos longos."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Comparando Investimentos em Longo Prazo",
                    "content": "Um jovem investidor aplicou R$ 5.000,00 por 2 anos em um título de juros compostos com taxa de 10% ao ano. Qual foi o montante final e quanto ele teria perdido se o contrato fosse de juros simples na mesma taxa?\nPasso 1 (Compostos): M = 5.000 . (1 + 0,10)^2 = 5.000 . (1,10)^2 = 5.000 . 1,21 = R$ 6.050,00.\nPasso 2 (Simples): M = 5.000 . (1 + 0,10 . 2) = 5.000 . 1,20 = R$ 6.000,00.\nPasso 3 (Diferença): 6.050 - 6.000 = R$ 50,00 a mais nos compostos em apenas 2 anos! Se fosse por 20 anos, os juros simples triplicariam o dinheiro (R$ 15.000,00), enquanto os compostos fariam 5.000 . (1,1)^20, passando de R$ 33.637,00!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Taxas Nominais, Proporcionais e Equivalentes"
                },
                {
                    "type": "paragraph",
                    "content": "Para fechar este capítulo no nível máximo da prova, vamos esclarecer três nomes que assustam muita gente, mas têm ideias bem diretas: taxa proporcional, taxa equivalente e taxa nominal. Nos juros simples, converter períodos é moleza: usamos Taxas Proporcionais. Se a taxa é 2% ao mês, em 12 meses será 2% x 12 = 24% ao ano. Basta multiplicar ou dividir proporcionalmente pelo tempo."
                },
                {
                    "type": "paragraph",
                    "content": "Já nos juros compostos, 2% ao mês NÃO equivale a 24% ao ano! Por quê? Porque há juros sobre juros! Para achar a Taxa Equivalente anual nos juros compostos, multiplicamos os fatores mensais: (1 + i_anual) = (1 + i_mensal)^12. Por exemplo, uma taxa de 10% ao mês em 2 meses equivale a (1,10)^2 - 1 = 1,21 - 1 = 0,21, ou seja, 21% ao bimestre (e não 20%). Por fim, a chamada Taxa Nominal aparece em contratos bancários quando a taxa declarada está em um período (por exemplo, '12% ao ano'), mas a capitalização acontece em outro menor ('capitalizado mensalmente'). Nesse caso, divide-se proporcionalmente para achar a taxa efetiva de cada mês (12% / 12 = 1% ao mês), e a taxa efetiva real do ano será (1,01)^12 - 1, aproximadamente 12,68% ao ano!"
                },
                {
                    "type": "quote",
                    "content": "Nos juros simples, o tempo soma; nos juros compostos, o tempo multiplica no expoente.",
                    "author": "Princípio da Capitalização"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-12-matematica-do-bolso",
            "number": 12,
            "title": "Matemática do Bolso: Inflação, Financiamentos, Parcelamentos e Investimentos",
            "epigraph": {
                "text": "Ganhar dez por cento no banco quando os preços subiram doze por cento no supermercado não é lucro: é perder dinheiro em câmera lenta.",
                "author": "Lição de Educação Financeira"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Como a Inflação Corrói o Poder de Compra"
                },
                {
                    "type": "paragraph",
                    "content": "Bem-vindo ao capítulo mais prático de toda a sua preparação! Tudo o que envolve cartão de crédito, carnê de loja, inflação e aplicações financeiras mora aqui. Comecemos por um conceito que aparece nos noticiários todo mês: a inflação. Inflação é o aumento contínuo e generalizado dos preços de bens e serviços. Quando dizemos que a inflação foi de 10% em um ano, significa que uma cesta de compras que custava R$ 100,00 passou a custar R$ 110,00. O dinheiro no seu bolso continua tendo o mesmo valor impresso na nota, mas compra menos produtos: é isso que chamamos de perda do poder de compra."
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção à armadilha clássica: se os preços subiram 25%, de quantos por cento caiu o seu poder de compra? Cuidado para não responder 25%! Pense comigo em um exemplo numérico delicioso: antes, com R$ 100,00 você comprava 10 quilos de café a R$ 10,00 cada. Se o café sofre inflação de 25%, cada quilo passa a custar R$ 12,50. Com os mesmos R$ 100,00, quantos quilos você compra agora? Dividindo 100 por 12,50, você só leva 8 quilos! Ora, sair de 10 quilos para 8 quilos é uma redução de 20% na quantidade comprada! Em termos gerais, se os preços multiplicam por (1 + I), a quantidade que o dinheiro compra multiplica por 1 / (1 + I)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Taxa Real vs. Taxa Aparente: A Equação de Fisher"
                },
                {
                    "type": "paragraph",
                    "content": "Agora que entendemos a inflação, imagine que você aplicou seu dinheiro em um investimento que prometeu rendimento nominal — chamado de Taxa Aparente (i_a) — de 15% no ano. Porém, nesse mesmo ano, a inflação (I) foi de 10%. Será que o seu poder de compra cresceu 5% (15% - 10%)? Quase, mas não exatamente! Para calcular o ganho verdadeiro acima da inflação, chamado de Taxa Real (r), usamos a famosa Equação de Fisher, que nada mais é do que a velha regra dos fatores multiplicativos!"
                },
                {
                    "type": "paragraph",
                    "content": "Veja como ela é intuitiva e você nem precisa decorar como mágica: o fator de crescimento do seu dinheiro (1 + i_a) é igual ao fator da inflação (1 + I) multiplicado pelo fator de ganho real (1 + r). Escrevendo como equação: (1 + i_a) = (1 + I) . (1 + r). Vamos testar com nossos números: 1,15 = 1,10 . (1 + r). Isolando o fator real: (1 + r) = 1,15 / 1,10 = 1,04545... Subtraindo 1, encontramos r = 0,04545, ou seja, uma taxa real de aproximadamente 4,55%, e não 5%! Percebeu por que na hora da prova você nunca deve simplesmente subtrair a inflação da taxa aparente quando as alternativas têm valores próximos?"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Salário vs. Inflação",
                    "content": "Durante um ano, a inflação acumulada foi de 8%, e uma categoria profissional recebeu um reajuste salarial de 13,4%. Qual foi o aumento real do poder de compra desses trabalhadores?\nPasso 1: Aplicamos a Equação de Fisher: (1 + i_a) = (1 + I) . (1 + r).\nPasso 2: Substituímos os fatores: 1,134 = 1,08 . (1 + r).\nPasso 3: Dividimos 1,134 por 1,08 -> 113,4 / 108 = 1,05.\nPasso 4: Como 1 + r = 1,05, temos r = 0,05 = 5% de ganho real! Note que uma conta simples de subtração daria 13,4% - 8% = 5,4%, levando o candidato distraído ao distrator da prova."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "À Vista com Desconto vs. Parcelado: O Valor do Dinheiro no Tempo"
                },
                {
                    "type": "paragraph",
                    "content": "Vamos a uma questão clássica do ENEM que também salva suas finanças pessoais! Uma loja vende uma televisão por R$ 2.000,00 em duas parcelas iguais de R$ 1.000,00 — sendo a primeira paga na hora (entrada) e a segunda após 30 dias —, dizendo que é 'sem juros'. Porém, se o cliente pagar à vista, ganha 10% de desconto, levando a TV por R$ 1.800,00. Pergunta de ouro: qual é a taxa de juros embutida nesse parcelamento?"
                },
                {
                    "type": "paragraph",
                    "content": "Muita gente olha os R$ 200,00 de diferença sobre R$ 1.800,00 e responde 200 / 1.800 = 11,1%. ERRADO! Pense comigo com calma de sala de aula: se você tem R$ 1.800,00 na mão para comprar à vista e escolhe parcelar dando R$ 1.000,00 de entrada na boca do caixa, quanto dinheiro você REALMENTE financiou, isto é, ficou devendo para a loja naquele instante? Se o preço justo à vista era R$ 1.800,00 e você já entregou R$ 1.000,00 no ato, sua dívida restante na data zero é de apenas R$ 800,00! Um mês depois, para quitar esses R$ 800,00 de dívida, você terá que pagar R$ 1.000,00. Ora, pagar R$ 1.000,00 por uma dívida de R$ 800,00 significa pagar R$ 200,00 de juros sobre R$ 800,00! Dividindo 200 / 800 = 0,25, descobrimos que a taxa de juros embutida é de absurdos 25% ao mês! Essa sacada de abater a entrada do preço à vista é o segredo absoluto desse tipo de questão."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sistemas de Amortização e Comparação de Investimentos"
                },
                {
                    "type": "paragraph",
                    "content": "Quando você financia um imóvel ou carro em muitas parcelas, dois sistemas dominam as tabelas do ENEM: o SAC (Sistema de Amortização Constante) e a Tabela Price. Toda parcela mensal é formada por duas partes: a Amortização (o pedaço que realmente abate o saldo da dívida) e os Juros (calculados sempre sobre o saldo devedor restante). No sistema SAC, a amortização é fixa todo mês! Como a dívida vai diminuindo em parcelas iguais, os juros também diminuem a cada mês, fazendo com que a prestação comece mais alta e vá ficando mais barata ao longo do tempo."
                },
                {
                    "type": "paragraph",
                    "content": "Já na Tabela Price (sistema francês), todas as prestações mensais têm o MESMO valor do início ao fim. No começo, a maior parte da parcela paga juros e amortiza pouco a dívida; no final, quase toda a parcela amortiza a dívida e sobra pouco de juros. E quando o assunto é escolher o melhor investimento entre duas opções no ENEM? Compare sempre a rentabilidade líquida no mesmo prazo e descontando impostos ou taxas administrativas quando houver! Lembre-se: se uma aplicação rende 10% brutos ao ano, mas cobra 15% de Imposto de Renda sobre o lucro, o rendimento líquido será de 85% de 10%, ou seja, 8,5% líquidos. Quem compara tudo na mesma base temporal e líquida acerta de olhos fechados."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: SAC vs. Tabela Price no ENEM",
                    "content": "Bateu o olho na tabela de financiamento da questão? Olhe a coluna da PRESTAÇÃO: se o valor da prestação cai de mês para mês em degraus iguais, é SAC (Amortização Constante, prestações decrescentes). Se a prestação é idêntica em todos os meses, é Tabela Price (Prestações Fixas, amortização crescente). E lembre-se: em qualquer sistema, Juros do mês = taxa x Saldo Devedor do mês anterior!"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-13-custo-receita-lucro",
            "number": 13,
            "title": "Custo, Receita e Lucro: A Engenharia das Empresas no ENEM",
            "epigraph": {
                "text": "Faturamento alto não garante empresa saudável; quem define a sobrevivência de um negócio é o equilíbrio entre custos, preço e margem.",
                "author": "Aula de Modelagem Empresarial"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Por Dentro de Uma Empresa: O Que Sai e O Que Entra"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos ao último capítulo deste módulo, e ele faz uma ponte espetacular entre a Matemática Financeira e as Funções que o ENEM tanto ama cobrar em problemas contextualizados de fábricas, padarias, startups e vendedores ambulantes. Para modelar qualquer negócio matematicamente, precisamos enxergar duas grandes forças opostas: de um lado, o Custo Total (o dinheiro que sai para produzir ou operar); do outro, a Receita Total (o dinheiro que entra pelas vendas). A diferença entre o que entra e o que sai é o famoso Lucro."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Custo Fixo vs. Custo Variável: Construindo a Função Custo"
                },
                {
                    "type": "paragraph",
                    "content": "Imagine que você decidiu abrir uma pequena fábrica artesanal de bolos de pote. Antes mesmo de assar o primeiro bolo do mês, há contas que chegam faça chuva ou faça sol: o aluguel do ponto comercial, a internet, o salário do atendente e a taxa fixa da contabilidade. Vamos supor que tudo isso some R$ 2.400,00 por mês. Mesmo se você vender zero bolos, terá que pagar esses R$ 2.400,00. É por isso que chamamos esse valor de Custo Fixo (CF): ele não depende da quantidade produzida x."
                },
                {
                    "type": "paragraph",
                    "content": "Agora, para cada bolo de pote que você realmente produz, você gasta com farinha, chocolate, leite condensado, embalagem e colherzinha. Suponha que os ingredientes e a embalagem custem R$ 4,00 por unidade. Se você fizer 100 bolos, gasta R$ 400,00; se fizer 500 bolos, gasta R$ 2.000,00. Esse gasto que cresce proporcionalmente ao número de unidades x é o Custo Variável (CV). Juntando os dois, escrevemos a função Custo Total para x unidades produzidas: C(x) = CF + cv . x. No nosso exemplo da doceria, C(x) = 2.400 + 4x. Repare que essa é uma função do 1º grau!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Receita Total, Formação de Preço e Função Lucro"
                },
                {
                    "type": "paragraph",
                    "content": "Agora vamos colocar dinheiro no caixa! A Receita Total R(x), também chamada de faturamento bruto, é simplesmente o preço unitário de venda (p) multiplicado pela quantidade vendida (x): R(x) = p . x. Se você vende cada bolo de pote por R$ 12,00, sua função receita será R(x) = 12x. Atenção à diferença de vocabulário que derruba muita gente: faturamento (receita) NÃO é lucro! Se você vendeu 300 bolos a R$ 12,00, sua receita foi de R$ 3.600,00, mas ainda precisamos pagar os custos!"
                },
                {
                    "type": "paragraph",
                    "content": "O Lucro Líquido L(x) é dado pela equação fundamental dos negócios: Lucro = Receita - Custo, ou seja, L(x) = R(x) - C(x). Cuidado máximo com os parênteses ao subtrair o custo! Vamos montar o lucro da nossa fábrica de bolos: L(x) = 12x - (2.400 + 4x). Aplicando o sinal negativo aos dois termos dentro dos parênteses, temos L(x) = 12x - 2.400 - 4x, o que simplifica para L(x) = 8x - 2.400. Olha que leitura linda essa expressão permite: cada bolo vendido gera R$ 8,00 de contribuição (12 de venda menos 4 de custo variável) para primeiro pagar o custo fixo de R$ 2.400,00 e depois virar lucro no bolso!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: O Sinal Negativo nos Parênteses!",
                    "content": "Quando montar L(x) = R(x) - C(x), JAMAIS escreva L(x) = 12x - 2.400 + 4x! Esse erro de esquecer os parênteses faz somar o custo variável em vez de subtrair e destrói toda a questão. Sempre abra os parênteses ao escrever a função Custo após o sinal de menos: L(x) = R(x) - (CF + cv.x)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Ponto de Equilíbrio (Break-Even) e Análise de Margem"
                },
                {
                    "type": "paragraph",
                    "content": "Todo empresário faz a mesma pergunta quando abre um negócio: 'Quantas unidades eu preciso vender no mês para não ficar no prejuízo?'. Esse número mágico tem nome na matemática e na administração: Ponto de Equilíbrio, ou Break-Even Point. No ponto de equilíbrio, a empresa empata suas contas: o Lucro é exatamente zero, o que é o mesmo que dizer que a Receita se iguala ao Custo Total: L(x) = 0, ou R(x) = C(x)."
                },
                {
                    "type": "paragraph",
                    "content": "Na nossa fábrica de bolos, igualamos L(x) = 0: 8x - 2.400 = 0 -> 8x = 2.400 -> x = 300 bolos! Isso significa que, vendendo exatamente 300 bolos, o faturamento é de R$ 3.600,00 e o custo total também é de R$ 3.600,00 (2.400 fixo + 1.200 variável). Abaixo de 300 bolos, a empresa tem prejuízo (L(x) < 0); a partir de 301 bolos, a empresa começa a ter lucro positivo (L(x) > 0)! E se uma questão pedir o Break-Even em gráfico? Ele é exatamente o ponto de intersecção (cruzamento) entre a reta da Receita e a reta do Custo Total!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Formação de Preço e Margem de Lucro",
                    "content": "Um comerciante compra camisetas de um fornecedor por R$ 40,00 cada e deseja vendê-las obtendo um lucro correspondente a 20% sobre o PREÇO DE VENDA (margem sobre a venda), e não sobre o custo. Por quanto ele deve vender cada camiseta?\nPasso 1: Cuidado redobrado! Se fosse 20% sobre o custo, bastaria fazer 40 x 1,20 = R$ 48,00. Mas o enunciado pediu 20% sobre o preço de venda (P)!\nPasso 2: Montamos a relação: Preço de Venda = Custo + Lucro -> P = 40 + 0,20.P.\nPasso 3: Passamos 0,20.P para o outro lado: P - 0,20.P = 40 -> 0,80.P = 40.\nPasso 4: Dividimos: P = 40 / 0,80 = R$ 50,00! Confira a prova real: vendendo por R$ 50,00, o lucro é de R$ 10,00. E R$ 10,00 dividido pelo preço de venda (R$ 50,00) dá exatamente 20%! Essa distinção entre margem sobre o custo (markup) e margem sobre a venda vale ouro no ENEM."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Lucro Máximo Quando o Preço Varia (Conexão com Função Quadrática)"
                },
                {
                    "type": "paragraph",
                    "content": "Para fechar no nível mais alto da prova, lembre-se de uma situação que o ENEM ama: quando o preço de venda não é fixo, mas varia conforme o número de clientes! Por exemplo: um teatro tem 200 lugares e cobra R$ 50,00 pelo ingresso, mas a cada R$ 5,00 de aumento no ingresso, perde 10 espectadores. Nesse caso, após x aumentos de R$ 5,00, o preço vira (50 + 5x) e o público vira (200 - 10x). Ao multiplicar preço pela quantidade para achar a Receita R(x) = (50 + 5x).(200 - 10x), nasce uma função do 2º grau com concavidade para baixo! Aí basta achar o vértice da parábola (x_v = -b / 2a ou a média das raízes) para descobrir o preço que gera a receita máxima ou o lucro máximo. Dominar essa transição entre matemática financeira e funções garante que você resolva com tranquilidade qualquer problema empresarial da prova!"
                },
                {
                    "type": "quote",
                    "content": "Na matemática das empresas, o ponto de equilíbrio separa a sobrevivência do prejuízo, e a margem bem calculada transforma faturamento em lucro real.",
                    "author": "Fechamento do Módulo Financeiro"
                }
            ],
            "quiz": []
        }
    ]
