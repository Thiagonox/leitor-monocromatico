# -*- coding: utf-8 -*-
"""Curso Completo de Matemática ENEM - Módulo 8: Funções (Capítulos 33 a 38)."""


def get_chapters():
    return [
        {
            "id": "mat-curso-cap-33-conceito-funcao-leitura-grafica",
            "number": 33,
            "title": "Conceito de Função, Domínio, Imagem e Leitura Gráfica",
            "epigraph": {
                "text": "Uma função é a linguagem com que a matemática descreve como uma grandeza reage às mudanças de outra; quem lê bem um gráfico já tem meio caminho andado na prova do ENEM.",
                "author": "Sala de Aula — Matemática ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Metáfora da Máquina Transformadora"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao módulo de Funções, um dos corações da prova de Matemática do ENEM. Se você quer bater os 800 pontos, precisa dominar este assunto com naturalidade, porque funções aparecem puras ou disfarçadas em problemas de economia, biologia, física e leitura de gráficos. A melhor notícia é que você já usa funções todo dia! Quando entra em um aplicativo de transporte e vê o preço mudar conforme a distância, ou olha para a conta de luz e vê o valor depender dos quilowatts-hora consumidos, você está diante de uma função."
                },
                {
                    "type": "paragraph",
                    "content": "Pense comigo em uma máquina transformadora organizada. Você coloca um ingrediente na entrada — a variável independente x —, a máquina aplica uma regra fixa e entrega um resultado na saída — a variável dependente y, ou f(x). Mas existe uma regra de ouro para essa máquina ser uma função: para CADA valor permitido que entra, pode sair APENAS UM único resultado! Imagine uma cafeteira onde você aperta 'expresso' e ora sai café, ora sai suco. Ela estaria quebrada, certo? Na matemática é igual: um mesmo x nunca gera dois y diferentes."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Domínio, Contradomínio e Conjunto Imagem"
                },
                {
                    "type": "paragraph",
                    "content": "Agora vamos dar os nomes oficiais às peças dessa máquina. Imagine dois conjuntos em um diagrama de flechas: o conjunto de partida A e o conjunto de chegada B. O Domínio (D) é o conjunto A inteiro, ou seja, todos os valores de entrada x que a máquina aceita processar. Todo elemento do domínio precisa disparar exatamente uma flecha para o outro lado; ninguém no domínio pode ficar sem saída, nem disparar duas flechas ao mesmo tempo."
                },
                {
                    "type": "paragraph",
                    "content": "Já o conjunto de chegada B é o Contradomínio (CD): ele funciona como o cardápio de saídas possíveis que a máquina poderia, em tese, produzir. Porém, nem todo prato do cardápio precisa ser escolhido! O Conjunto Imagem (Im) é formado apenas pelos elementos de B que realmente receberam alguma flecha, isto é, os valores de y que efetivamente saíram da máquina. Por exemplo, considere a regra f(x) = x², com domínio A = {-2, -1, 0, 1, 2} e contradomínio B = {0, 1, 2, 3, 4, 5}. Calculando as saídas: f(-2) = 4, f(-1) = 1, f(0) = 0, f(1) = 1 e f(2) = 4. Perceba que os números 2, 3 e 5 estão no contradomínio B, mas não receberam flecha alguma! Logo, o conjunto Imagem é Im = {0, 1, 4}."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Restrições de Domínio",
                    "content": "Quando o ENEM não diz quem é o domínio, assumimos que é o maior conjunto real possível. Só tome cuidado com duas proibições clássicas dos números reais: (1) Nunca divida por zero! Em f(x) = 10 / (x - 3), devemos exigir x - 3 != 0, logo x != 3. (2) Nunca tire raiz quadrada (ou de índice par) de número negativo! Em g(x) = raiz(x - 5), exigimos x - 5 >= 0, portanto x >= 5."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Como Ler Domínio, Imagem e o Teste da Reta Vertical no Gráfico"
                },
                {
                    "type": "paragraph",
                    "content": "No plano cartesiano, as flechas dão lugar a pontos (x, y). Como saber olhando para um desenho no plano se aquela curva representa uma função? Use o infalível Teste da Reta Vertical! Passe uma régua imaginária na posição vertical e deslize-a da esquerda para a direita. Se, em algum lugar, essa reta vertical cortar a curva em DOIS ou mais pontos ao mesmo tempo, significa que um mesmo x tem mais de um y — logo, NÃO é função! Uma circunferência fechada ou uma parábola deitada, por exemplo, falham nesse teste."
                },
                {
                    "type": "paragraph",
                    "content": "Para encontrar o Domínio direto no gráfico, imagine esmagar a curva inteira contra o eixo horizontal X (como se uma luz viesse de cima e de baixo projetando a sombra da curva sobre o eixo X). O trecho coberto no eixo X é o Domínio. Para encontrar a Imagem, faça o contrário: projete a sombra da curva na horizontal contra o eixo vertical Y. A altura ocupada, do ponto mais baixo ao ponto mais alto que a curva alcança, é o Conjunto Imagem."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Lendo f(x), Raízes e Sinais no Plano Cartesiano"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque é onde o ENEM pesca pontos fáceis de quem tem pressa. Se o gráfico traz o ponto (4, 7), lembre-se da tradução imediata: quando x = 4, temos f(4) = 7. E se a questão perguntar: 'Para qual valor de x temos f(x) = 7?', ela está te dando a altura y = 7 e pedindo que você olhe para baixo até encontrar x = 4 no eixo horizontal."
                },
                {
                    "type": "paragraph",
                    "content": "Outros dois elementos vitais na leitura gráfica são os interceptos e os sinais. Onde a curva corta o eixo vertical Y, o valor de x é sempre zero; esse ponto (0, f(0)) costuma representar o valor inicial do fenômeno. Já onde a curva toca ou cruza o eixo horizontal X, a altura y vale zero — esses valores de x são chamados de Zeros ou Raízes da função! E quanto aos sinais? É pura geografia visual: sempre que o desenho da curva estiver ACIMA do eixo X, a função é positiva (f(x) > 0); sempre que estiver ABAIXO do eixo X, a função é negativa (f(x) < 0)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido — Lendo um Gráfico na Prática",
                    "content": "Suponha que o gráfico de lucro mensal L(t), em milhares de reais, de uma cafeteria nos primeiros 12 meses (0 <= t <= 12) comece no ponto (0, -6), suba em linha curva cruzando o eixo horizontal em t = 3, atinja o pico máximo no ponto (8, 10) e termine no ponto (12, 4).\n\nPasso 1 (Domínio e Imagem): No eixo horizontal t, a curva vai de 0 até 12, então D = [0, 12]. No eixo vertical L, o ponto mais baixo é -6 e o mais alto é 10, então Im = [-6, 10].\nPasso 2 (Valor inicial e valor específico): Em t = 0, L(0) = -6 (prejuízo inicial de R$ 6 mil). No pico, L(8) = 10 (lucro de R$ 10 mil no oitavo mês).\nPasso 3 (Raiz e sinais): A curva corta o eixo horizontal em t = 3, que é a raiz (mês em que a cafeteria empatou, L(3) = 0). Para 0 <= t < 3, o gráfico está abaixo do eixo, logo L(t) < 0 (prejuízo). Para 3 < t <= 12, está acima, logo L(t) > 0 (lucro)."
                },
                {
                    "type": "quote",
                    "content": "Antes de sair fazendo contas em uma questão de gráfico no ENEM, passe o dedo sobre os eixos: descubra o que o eixo X representa, o que o eixo Y mede e em quais unidades eles estão.",
                    "author": "Regra de Ouro da Leitura Cartesiana"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-34-funcao-afim-primeiro-grau",
            "number": 34,
            "title": "Função Afim (1º Grau): Taxa de Variação, Gráficos e Tarifas",
            "epigraph": {
                "text": "Se a variação é sempre a mesma a cada passo igual, não há mistério: você está diante de uma reta e da função mais cobrada de toda a prova do ENEM.",
                "author": "Sala de Aula — Matemática ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Anatomia de f(x) = ax + b"
                },
                {
                    "type": "paragraph",
                    "content": "Se existe um assunto que é garantia absoluta de aparecer todo ano no ENEM, é a Função Afim, também conhecida como função do 1º grau. Sua fórmula geral é elegante e enxuta: f(x) = ax + b, em que 'a' e 'b' são números reais constantes. Sempre que 'a' for diferente de zero, o gráfico dessa função no plano cartesiano será uma reta inclinada."
                },
                {
                    "type": "paragraph",
                    "content": "Mas o que separa o aluno de 600 pontos do aluno de 800+ não é apenas decorar a fórmula f(x) = ax + b — é enxergar o significado físico e financeiro escondido por trás das letras 'a' e 'b'. Pense comigo em uma corrida de táxi: assim que você entra no carro e o taxímetro é ligado, antes mesmo de rodar um único metro, já aparece uma cobrança inicial chamada bandeirada, digamos R$ 5,00. Depois, a cada quilômetro rodado, o valor sobe exatamente R$ 3,00. Se você rodar x quilômetros, o preço P(x) será P(x) = 3x + 5."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Papel de 'a' (Taxa de Variação) e de 'b' (Valor Fixo)"
                },
                {
                    "type": "paragraph",
                    "content": "Veja que sacada genial: na equação P(x) = 3x + 5, o número 5 (que é o coeficiente linear 'b') representa o valor fixo, o ponto de partida! Graficamente, quando substituímos x = 0, sobra f(0) = a·0 + b = b. Isso significa que 'b' é SEMPRE a altura exata onde a reta corta o eixo vertical Y, no ponto (0, b)."
                },
                {
                    "type": "paragraph",
                    "content": "Já o número 3 (que é o coeficiente angular 'a') é o verdadeiro motor da reta: ele representa a TAXA DE VARIAÇÃO constante! Ele te diz quanto o y muda toda vez que o x aumenta 1 unidade. Como essa taxa é constante, podemos calculá-la a partir de quaisquer dois pontos (x1, y1) e (x2, y2) da reta usando a fórmula a = (y2 - y1) / (x2 - x1), ou simplesmente variação de y dividida pela variação de x (Delta y / Delta x)."
                },
                {
                    "type": "paragraph",
                    "content": "O sinal de 'a' comanda a direção da reta da esquerda para a direita: se a > 0, a função é crescente (a reta sobe); se a < 0, a função é decrescente (a reta desce, como um reservatório esvaziando ou um carro consumindo combustível); e se a = 0, temos uma função constante f(x) = b (uma reta horizontal paralela ao eixo X, como um plano de internet ilimitado onde você paga o mesmo preço qualquer que seja o uso)."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Função Afim x Função Linear",
                    "content": "Cuidado com a nomenclatura em enunciados! Toda função do tipo f(x) = ax + b é afim. Quando o valor fixo 'b' é igual a zero, ela fica f(x) = ax e ganha o nome especial de Função Linear. Só na função linear (b = 0), cujo gráfico passa exatamente pela origem (0, 0), as grandezas x e y são diretamente proporcionais e você pode resolver por regra de três simples! Se b != 0 (como na conta de água com taxa mínima), regra de três direta dá resposta errada."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Zero da Função e a Montagem da Reta em Tabelas e Gráficos"
                },
                {
                    "type": "paragraph",
                    "content": "E onde a reta cruza o eixo horizontal X? Esse ponto é o Zero ou Raiz da função afim. Para encontrá-lo, igualamos a saída a zero: ax + b = 0, o que nos dá x = -b/a. Na prática, esse valor responde perguntas como 'após quantas horas a bateria chega a 0%?' ou 'quantas unidades preciso vender para o lucro deixar de ser negativo e zerar?'."
                },
                {
                    "type": "paragraph",
                    "content": "No ENEM, quase sempre a questão te entrega uma tabela ou um gráfico com dois pontos e pede um terceiro valor ou a própria fórmula. Não faça sistemas demorados se puder usar a taxa de variação! Olhe primeiro quanto y variou, divida por quanto x variou para achar 'a', e depois substitua um dos pontos em f(x) = ax + b para descobrir 'b' — ou leia 'b' direto no eixo Y se o gráfico mostrar o corte em x = 0."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido — Montando a Equação a partir de uma Tabela",
                    "content": "Um técnico de informática cobra uma taxa fixa de visita mais um valor por hora trabalhada. Em um serviço de 2 horas, cobrou R$ 170,00. Em outro de 5 horas, cobrou R$ 320,00. Quanto ele cobrará por um serviço de 8 horas e qual é sua taxa fixa de visita?\n\nPasso 1 (Calcular a taxa de variação 'a'): De 2 horas para 5 horas, o tempo aumentou Delta x = 5 - 2 = 3 horas. O preço aumentou Delta y = 320 - 170 = 150 reais. Logo, a = 150 / 3 = 50 reais por hora!\nPasso 2 (Calcular o valor fixo 'b'): Usando o ponto (2, 170) na fórmula P(x) = 50x + b, temos: 170 = 50·2 + b => 170 = 100 + b => b = 70 reais de taxa fixa. Assim, a função é P(x) = 50x + 70.\nPasso 3 (Responder ao pedido): Para x = 8 horas, P(8) = 50·8 + 70 = 400 + 70 = R$ 470,00. Perceba também um atalho mental lindo: de 5h para 8h são mais 3 horas, então bastava somar mais R$ 150 aos R$ 320, chegando direto aos R$ 470!"
                },
                {
                    "type": "heading",
                    "level": 3,
                    "content": "Quando o Gráfico Corta o Eixo X e o Eixo Y"
                },
                {
                    "type": "paragraph",
                    "content": "Imagine agora um gráfico decrescente clássico do ENEM: um tanque cheio marca 600 litros no instante t = 0, ou seja, passa por (0, 600), e esvazia completamente após 12 horas, passando por (12, 0). Em segundos você monta a função: o corte no eixo Y já te deu b = 600. E a taxa de variação 'a' é (0 - 600) / (12 - 0) = -600 / 12 = -50 litros por hora. Pronto! V(t) = -50t + 600. Com isso você descobre o volume em qualquer instante com segurança absoluta."
                },
                {
                    "type": "quote",
                    "content": "Na função do 1º grau, 'b' é onde você começa e 'a' é o tamanho de cada passo que você dá.",
                    "author": "Resumo de Sala de Aula"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-35-funcao-quadratica-segundo-grau",
            "number": 35,
            "title": "Função Quadrática (2º Grau): Parábolas, Vértice e Otimização Máximo/Mínimo",
            "epigraph": {
                "text": "Quando o problema pedir o maior lucro, a maior área cercada ou a altura máxima de um lançamento, o seu alarme mental deve soar imediatamente: é hora do vértice da parábola!",
                "author": "Sala de Aula — Matemática ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Parábola e o Significado de a, b e c"
                },
                {
                    "type": "paragraph",
                    "content": "Bem-vindo ao capítulo das curvas mais famosas e rentáveis da prova do ENEM: a Função Quadrática, ou função do 2º grau! Sua lei de formação é f(x) = ax² + bx + c, com 'a', 'b' e 'c' reais e uma condição obrigatória: 'a' nunca pode ser zero, pois se a = 0 o termo x² some e voltamos para uma reta do 1º grau. Quando 'a' é diferente de zero, o gráfico é uma curva simétrica maravilhosa chamada Parábola."
                },
                {
                    "type": "paragraph",
                    "content": "Cada coeficiente cumpre um papel visual claríssimo no gráfico. O coeficiente 'a' determina a concavidade (a boca da parábola): se a > 0, a concavidade é voltada para cima — costumo dizer que a parábola está 'sorrindo' — e possui um ponto de MÍNIMO lá embaixo. Se a < 0, a concavidade é voltada para baixo — a parábola está 'triste' — e possui um ponto de MÁXIMO lá no alto. Já o coeficiente 'c' funciona exatamente como o 'b' da função afim: fazendo x = 0, obtemos f(0) = c, logo 'c' é o ponto exato onde a parábola corta o eixo vertical Y, nas coordenadas (0, c)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Raízes e o Discriminante Delta"
                },
                {
                    "type": "paragraph",
                    "content": "As raízes (ou zeros) da função quadrática são os valores de x onde a parábola corta o eixo horizontal X, ou seja, onde ax² + bx + c = 0. Para encontrá-las, usamos a famosa fórmula de Bhaskara, calculando primeiro o discriminante Delta = b² - 4ac e depois x = (-b ± raiz(Delta)) / (2a), ou ainda as relações de soma e produto quando 'a' vale 1 (a soma das raízes é -b/a e o produto é c/a)."
                },
                {
                    "type": "paragraph",
                    "content": "O sinal de Delta conta quantas vezes a parábola encontra o eixo X: se Delta > 0, a curva atravessa o eixo X em dois pontos distintos (duas raízes reais diferentes); se Delta = 0, a curva apenas encosta, tangenciando o eixo X em um único ponto (que é o próprio vértice!); e se Delta < 0, a parábola flutua inteira acima ou inteira abaixo do eixo X, sem jamais encostar nele (não há raízes reais)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Vértice (Xv e Yv): O Segredo da Otimização no ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque este é o ponto exato onde nascem as questões de nível 750 a 850+ no ENEM! Toda parábola tem um ponto de virada chamado Vértice, de coordenadas V = (Xv, Yv). É exatamente no vértice que a curva deixa de descer e passa a subir (ponto de mínimo, quando a > 0) ou deixa de subir e passa a descer (ponto de máximo, quando a < 0)."
                },
                {
                    "type": "paragraph",
                    "content": "As fórmulas do vértice são:\n• Xv = -b / (2a) — que também é sempre o ponto médio exato entre as duas raízes, ou seja, Xv = (x1 + x2) / 2, graças à simetria perfeita da parábola!\n• Yv = -Delta / (4a) — ou, o que quase sempre é muito mais rápido e seguro na hora da prova: basta calcular Xv e jogar esse valor dentro da própria função f(x), pois Yv = f(Xv)!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Não Confunda Xv com Yv!",
                    "content": "Na hora da prova, o comando da questão decide qual coordenada do vértice é a resposta final:\n• Se o texto perguntar 'QUANDO ocorre o máximo', 'QUAL o preço que maximiza o lucro' ou 'QUAL a largura que gera a maior área', ele está perguntando a variável de entrada: calcule Xv!\n• Se o texto perguntar 'QUAL é o lucro máximo', 'QUAL a altura máxima atingida' ou 'QUAL a maior área possível', ele está perguntando o valor de saída: calcule Yv (de preferência fazendo f(Xv))!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Três Problemas Clássicos de Otimização Resolvidos"
                },
                {
                    "type": "paragraph",
                    "content": "Primeiro clássico — Altura Máxima de Projéteis: Suponha que uma bola chutada do chão siga a trajetória h(t) = -5t² + 20t, onde h é a altura em metros e t é o tempo em segundos. Como a = -5 < 0, há um ponto de máximo. Em que instante ela atinge a altura máxima? Calculamos tv = -b / (2a) = -20 / (2 · (-5)) = -20 / -10 = 2 segundos. E qual é essa altura máxima? Substituímos t = 2 na função: h(2) = -5·(2)² + 20·2 = -20 + 40 = 20 metros!"
                },
                {
                    "type": "paragraph",
                    "content": "Segundo clássico — Área Cercada Máxima: Um fazendeiro tem 80 metros de tela para cercar um canteiro retangular aproveitando um muro já existente em um dos lados (ou seja, ele só cerca 3 lados: duas larguras x e um comprimento y). Como o total de tela é 80 m, temos 2x + y = 80, logo y = 80 - 2x. A área do retângulo será A(x) = x · y = x · (80 - 2x) = -2x² + 80x. Veja que surgiu uma função do 2º grau com a = -2 e b = 80! A largura que maximiza a área é Xv = -80 / (2 · (-2)) = 20 metros. E a área máxima é A(20) = -2·(20)² + 80·20 = -800 + 1600 = 800 m²."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido — O Clássico do Lucro Máximo (Preço x Quantidade)",
                    "content": "Um cinema cobra R$ 20,00 pelo ingresso e vende 300 ingressos por sessão. O gerente descobre que, a cada R$ 1,00 de desconto dado no preço, o público aumenta em 30 pessoas. Qual valor de ingresso gera a arrecadação máxima e qual é essa arrecadação?\n\nPasso 1 (Criar a variável x): Seja x o número de descontos de R$ 1,00 aplicados. O novo preço será (20 - x) e a nova quantidade de público será (300 + 30x).\nPasso 2 (Montar a Receita): R(x) = (20 - x) · (300 + 30x) = 6000 + 600x - 300x - 30x² = -30x² + 300x + 6000.\nPasso 3 (Achar o vértice sem sofrer!): Em vez de decorar fórmulas gigantes, olhe para os fatores originais: as raízes de (20 - x)(300 + 30x) = 0 são x1 = 20 e x2 = -10! Pela simetria da parábola, Xv = (20 + (-10)) / 2 = 5 descontos! (Conferindo por -b/2a: -300 / -60 = 5).\nPasso 4 (Responder com precisão): Com x = 5 descontos de R$ 1,00, o preço ótimo do ingresso é 20 - 5 = R$ 15,00, atraindo 300 + 30·5 = 450 pessoas, e a arrecadação máxima será 15 · 450 = R$ 6.750,00!"
                },
                {
                    "type": "quote",
                    "content": "Toda parábola é perfeitamente simétrica: seu vértice mora exatamente no meio do caminho entre as duas raízes.",
                    "author": "Atalho Ninja do Vértice"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-36-funcao-exponencial",
            "number": 36,
            "title": "Função Exponencial: O Poder do Crescimento e Decaimento Explosivo",
            "epigraph": {
                "text": "Na função afim você soma um valor fixo a cada passo; na função exponencial você multiplica por um fator fixo — e é essa multiplicação repetida que faz o gráfico decolar ou despencar rapidamente.",
                "author": "Sala de Aula — Matemática ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Onde Mora a Variável? A Marca Registrada da Exponencial"
                },
                {
                    "type": "paragraph",
                    "content": "Cuidado para não confundir x² com 2^x! Na função quadrática, a variável x fica embaixo, na base, e o número 2 fica no expoente. Na Função Exponencial, o jogo vira completamente: a variável x sobe para o EXPOENTE! A forma geral mais cobrada nos problemas contextualizados do ENEM é f(x) = b · a^x, onde 'b' é o valor inicial (quando x = 0, pois a^0 = 1, logo f(0) = b) e 'a' é a base da potência — também chamada de fator de crescimento ou decrescimento."
                },
                {
                    "type": "paragraph",
                    "content": "Para que essa função exista bem comportada no conjunto dos números reais, a base 'a' precisa obedecer a duas condições: a > 0 e a != 1. Por quê? Se a = 1, teríamos 1^x = 1 sempre, o que vira uma reta constante sem graça. E se 'a' fosse negativo, como (-2)^x, valores fracionários como x = 1/2 gerariam raiz quadrada de número negativo, quebrando o gráfico real."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Crescimento (a > 1) vs Decrescimento (0 < a < 1)"
                },
                {
                    "type": "paragraph",
                    "content": "O comportamento visual do gráfico depende inteiramente do tamanho da base 'a' (considerando b > 0). Quando a > 1 (por exemplo, a = 2, a = 3 ou a = 1,15), a função é estritamente CRESCENTE: a cada passo no eixo X, multiplicamos o resultado anterior por um número maior que 1, então a curva começa baixinha à esquerda e dispara para o alto como um foguete à direita."
                },
                {
                    "type": "paragraph",
                    "content": "Por outro lado, quando 0 < a < 1 (por exemplo, a = 1/2, a = 0,8 ou a = 2^(-1)), a função é estritamente DECRESCENTE: a cada passo multiplicamos o valor por uma fração própria, fazendo a quantidade encolher rapidamente no começo e depois ir suavizando rumo a zero. Note um detalhe lindo e super cobrado em leitura de gráficos: quando b > 0, a função exponencial b · a^x é SEMPRE positiva! Ela se aproxima cada vez mais do eixo X sem nunca tocá-lo ou cruzá-lo — dizemos que o eixo X é uma assíntota horizontal."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso — Como Identificar a Base 'a' em Problemas de Porcentagem",
                    "content": "Se uma grandeza cresce 20% a cada período, você multiplica por 1 + 0,20 = 1,20. Logo a base é a = 1,20 (maior que 1, crescimento).\nSe uma grandeza sofre desvalorização ou perda de 15% por ano, você multiplica por 1 - 0,15 = 0,85. Logo a base é a = 0,85 (entre 0 e 1, decrescimento).\nSe uma população dobra a cada hora, a = 2. Se cai pela metade a cada ciclo, a = 1/2 = 0,5."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Modelagem Passo a Passo: Bactérias, Juros Compostos e Meia-Vida"
                },
                {
                    "type": "paragraph",
                    "content": "O ENEM adora três cenários reais para a função exponencial. O primeiro é a multiplicação de bactérias ou vírus em biologia. Imagine uma cultura que começa com 500 bactérias e triplica a cada 2 horas. Quantas bactérias existirão após t horas? Primeiro, observe quantos ciclos de triplicação cabem em t horas: é t / 2. Então nossa lei de formação é N(t) = 500 · 3^(t/2). Vamos testar! Em t = 0, N(0) = 500 · 3^0 = 500. Em t = 2 horas, N(2) = 500 · 3^1 = 1.500. Em t = 6 horas, temos 3 ciclos de 2 horas, logo N(6) = 500 · 3^3 = 500 · 27 = 13.500 bactérias!"
                },
                {
                    "type": "paragraph",
                    "content": "O segundo cenário são os Juros Compostos da matemática financeira, que nada mais são do que uma função exponencial do tempo: M(t) = C · (1 + i)^t, onde C é o capital inicial (o nosso 'b') e (1 + i) é o fator de aumento (a nossa base 'a'). Se você aplica R$ 2.000,00 a 10% ao ano, em t anos terá M(t) = 2000 · (1,1)^t."
                },
                {
                    "type": "paragraph",
                    "content": "O terceiro cenário — queridinho das provas de Ciências da Natureza e Matemática juntas — é a Meia-Vida Radioativa ou eliminação de medicamentos no sangue! Meia-vida (T) é o tempo necessário para a massa de um material cair exatamente pela metade. A fórmula natural é M(t) = M0 · (1/2)^(t / T). Por exemplo, se um paciente toma 800 mg de um remédio cuja meia-vida no organismo é de 4 horas, após 12 horas terão passado 12 / 4 = 3 meias-vidas. Então restarão M(12) = 800 · (1/2)^3 = 800 · (1/8) = 100 mg no sangue!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Equações Exponenciais por Igualdade de Bases"
                },
                {
                    "type": "paragraph",
                    "content": "Como resolver quando o ENEM te dá o valor final e pede o tempo x que está lá no expoente? O primeiro método — antes de recorrer aos logaritmos do próximo capítulo — é a Igualdade de Bases! A lógica é cristalina: se b^x = b^y (com b > 0 e b != 1), então obrigatoriamente os expoentes são iguais: x = y. Para fazer as bases ficarem idênticas, fatoramos os números grandes e lembramos de duas propriedades preciosas de potenciação: a^(-n) = 1 / a^n (expoente negativo inverte a base) e a^(m/n) = raiz_n(a^m) (expoente fracionário vira raiz)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido — Equação Exponencial Estilo ENEM",
                    "content": "Uma amostra radioativa inicia com 640 gramas e tem meia-vida de 5 dias. Depois de quantos dias restarão apenas 20 gramas dessa amostra?\n\nPasso 1 (Montar a função): M(t) = 640 · (1/2)^(t/5).\nPasso 2 (Substituir o valor desejado): Queremos M(t) = 20, logo 640 · (1/2)^(t/5) = 20.\nPasso 3 (Isolar a potência antes de mexer nas bases!): Dividindo os dois lados por 640, temos: (1/2)^(t/5) = 20 / 640 = 1 / 32.\nPasso 4 (Igualar as bases): Sabemos que 32 = 2^5, portanto 1 / 32 = (1/2)^5. Ficamos com (1/2)^(t/5) = (1/2)^5.\nPasso 5 (Igualar os expoentes): t / 5 = 5 => t = 25 dias! Simples, limpo e sem precisar de calculadora."
                },
                {
                    "type": "quote",
                    "content": "Em qualquer equação exponencial, sua primeira missão antes de fatorar é deixar a potência a^x completamente sozinha de um lado da igualdade.",
                    "author": "Dica de Sala de Aula"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-37-funcao-logaritmica",
            "number": 37,
            "title": "Função Logarítmica: Domando Escalas Gigantes na Natureza",
            "epigraph": {
                "text": "Se a função exponencial faz os números explodirem para bilhões, o logaritmo é a lente de redução inteligente que traz esses números gigantes de volta para uma escala humana de 1 a 14.",
                "author": "Sala de Aula — Matemática ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Desmistificando o Logaritmo: O Expoente que Faltava"
                },
                {
                    "type": "paragraph",
                    "content": "Chegamos ao tópico que costuma assustar os candidatos só pelo nome, mas que depois desta aula vai virar ponto garantido para você no ENEM: os Logaritmos! Respire fundo e pense comigo: se eu te perguntar '2 elevado a quanto dá 8?', você responde na hora '3', porque 2³ = 8. E se eu perguntar '10 elevado a quanto dá 10.000?', você responde '4', porque 10^4 = 10.000. Parabéns! Você acabou de resolver dois logaritmos de cabeça."
                },
                {
                    "type": "paragraph",
                    "content": "O logaritmo nada mais é do que a operação inversa da exponenciação: ele existe exatamente para descobrir 'qual é o expoente que faltava'. A definição formal diz que log_b(a) = x equivale a b^x = a. Aqui, 'a' é o logaritmando (precisa ser estritamente positivo, a > 0) e 'b' é a base (precisa ser positiva e diferente de 1: b > 0 e b != 1). Quando a base não aparece escrita, como em log(100), está subentendido que é o logaritmo decimal, de base 10! Logo, log(100) = 2 porque 10² = 100. E lembre-se sempre de dois resultados imediatos: log_b(1) = 0 (pois b^0 = 1) e log_b(b) = 1 (pois b^1 = b)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Quatro Propriedades Operatórias que Salvam sua Prova"
                },
                {
                    "type": "paragraph",
                    "content": "Por que o ENEM quase sempre te dá valores como log 2 = 0,30 e log 3 = 0,48 no enunciado? Porque você não precisa decorar tabela de logaritmos; você só precisa saber quebrar números grandes usando as quatro propriedades operatórias — que são reflexo direto das propriedades de potências!"
                },
                {
                    "type": "paragraph",
                    "content": "1) Logaritmo do Produto vira Soma: log_b(M · N) = log_b(M) + log_b(N). Quer calcular log(6) sabendo log(2) = 0,30 e log(3) = 0,48? Escreva 6 = 2 · 3, logo log(6) = log(2) + log(3) = 0,30 + 0,48 = 0,78!\n2) Logaritmo do Quociente vira Subtração: log_b(M / N) = log_b(M) - log_b(N). Veja que truque fantástico para achar log(5): escreva 5 como 10 / 2! Então log(5) = log(10) - log(2) = 1 - 0,30 = 0,70!\n3) Regra do Tombo (Potência): log_b(M^k) = k · log_b(M). O expoente 'cai' multiplicando na frente do log! Por exemplo, log(8) = log(2³) = 3 · log(2) = 3 · 0,30 = 0,90. É essa regra que permite tirar a incógnita t lá de cima do expoente em equações como 2^t = 10 (aplicamos log dos dois lados: t · log 2 = log 10 => t · 0,30 = 1 => t ≈ 3,33).\n4) Mudança de Base: se precisar trocar a base 'b' para uma nova base 'c' (geralmente base 10), faça log_b(a) = log_c(a) / log_c(b). Ou seja, log de quem está em cima dividido pelo log da base que estava embaixo!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: O Erro Fatal da Soma dentro do Log",
                    "content": "Atenção redobrada! log(A + B) NÃO é igual a log(A) + log(B)! O logaritmo transforma MULTIPLICAÇÃO em soma, e DIVISÃO em subtração. Se você vir log(2 + 3), é log(5), jamais log(2) + log(3). E também nunca se esqueça da restrição de domínio na função f(x) = log_b(x): o logaritmando precisa ser sempre > 0, por isso a curva do gráfico logarítmico mora inteira à direita do eixo Y, passando sempre pelo ponto (1, 0)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Três Aplicações Clássicas do ENEM: Richter, pH e Decibéis"
                },
                {
                    "type": "paragraph",
                    "content": "No ENEM, quase toda questão de logaritmo vem vestida com uma aplicação real onde grandezas variam de 10 em 10, 100 em 100 ou milhões de vezes. A primeira é a Escala Richter de terremotos, frequentemente modelada por M = (2/3) · log(E / E0) para energia ou M = log(A / A0) para amplitude. Olhe o que isso significa na prática: se a magnitude M sobe apenas 1 ponto (de 5 para 6 na escala de amplitude), a amplitude das ondas sísmicas não aumentou 20% — ela foi multiplicada por 10! Se subiu 2 pontos (de 5 para 7), a amplitude multiplicou por 10² = 100 vezes!"
                },
                {
                    "type": "paragraph",
                    "content": "A segunda aplicação famosa une Matemática e Química: a escala de pH, definida por pH = -log[H+], onde [H+] é a concentração de íons hidrogênio em mol/L. Imagine uma solução com [H+] = 10^(-4) mol/L. Aplicando a fórmula: pH = -log(10^(-4)) = -(-4) · log(10) = 4. Se essa solução ficar 100 vezes menos ácida, sua concentração [H+] cai para 10^(-6), e o pH sobe de 4 para 6!"
                },
                {
                    "type": "paragraph",
                    "content": "A terceira aplicação é a intensidade sonora em Decibéis (dB): Beta = 10 · log(I / I0), onde I é a intensidade sonora medida e I0 = 10^(-12) W/m² é o limiar da audição humana. Se um show de rock tem intensidade sonora de 10^(-2) W/m², a razão I / I0 vale 10^(-2) / 10^(-12) = 10^10. Logo, o nível sonoro é Beta = 10 · log(10^10) = 10 · 10 = 100 decibéis!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido — Comparando Terremotos (Nível 800+)",
                    "content": "Em uma região, a magnitude de um terremoto é dada por M = (2/3) · log(E / E0). Um terremoto A teve magnitude 6,0 e um terremoto B teve magnitude 4,0. Quantas vezes a energia liberada no terremoto A foi maior do que no terremoto B?\n\nPasso 1 (Escrever as duas equações): Para A, 6,0 = (2/3) · log(EA / E0). Para B, 4,0 = (2/3) · log(EB / E0).\nPasso 2 (O atalho elegante da subtração!): Em vez de isolar cada energia separadamente, subtraia as duas equações: MA - MB = (2/3) · [log(EA / E0) - log(EB / E0)]. Pela propriedade do quociente, log(EA / E0) - log(EB / E0) = log(EA / EB), eliminando E0 imediatamente!\nPasso 3 (Resolver para a razão EA / EB): 6,0 - 4,0 = (2/3) · log(EA / EB) => 2,0 = (2/3) · log(EA / EB) => log(EA / EB) = 3.\nPasso 4 (Aplicar a definição de logaritmo decimal): Como a base é 10, temos EA / EB = 10³ = 1.000! Portanto, um aumento de apenas 2 pontos na escala Richter representou uma energia liberada 1.000 vezes maior."
                },
                {
                    "type": "quote",
                    "content": "Cada unidade a mais no logaritmo decimal significa que a grandeza real foi multiplicada por 10.",
                    "author": "Chave de Leitura das Escalas Logarítmicas"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-38-interpretacao-avancada-graficos",
            "number": 38,
            "title": "Crescimento, Decrescimento e Interpretação Avançada de Gráficos",
            "epigraph": {
                "text": "Mais de um terço da prova de Matemática do ENEM testa se você sabe comparar cenários, ler intervalos e enxergar decisões reais escondidas dentro de um plano cartesiano.",
                "author": "Sala de Aula — Matemática ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Intervalos Crescentes, Decrescentes e Constantes"
                },
                {
                    "type": "paragraph",
                    "content": "Para fechar nosso módulo de funções com chave de ouro e blindar sua nota contra as pegadinhas clássicas do ENEM, vamos treinar a interpretação avançada de gráficos. A primeira regra de sobrevivência ao analisar intervalos de crescimento e decrescimento é ler o gráfico SEMPRE da esquerda para a direita, acompanhando o crescimento do eixo X — exatamente como lemos um livro em português."
                },
                {
                    "type": "paragraph",
                    "content": "Se, ao caminhar para a direita, a linha do gráfico sobe, a função é crescente naquele intervalo. Se a linha desce, a função é decrescente. Se a linha forma um patamar perfeitamente horizontal, a função é constante naquele trecho. E aqui mora uma armadilha campeã de erros: os intervalos de crescimento e decrescimento são SEMPRE respondidos olhando para os valores do eixo X, nunca do eixo Y! Por exemplo, se uma curva sobe do ponto (2, 10) até o ponto (7, 50), dizemos que ela é crescente no intervalo [2, 7] (valores de x), e não [10, 50]."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Comparando Múltiplas Curvas e o Ponto de Equilíbrio"
                },
                {
                    "type": "paragraph",
                    "content": "Outro formato adorado pela banca do ENEM coloca duas ou três funções diferentes desenhadas no mesmo plano cartesiano — por exemplo, a receita R(x) e o custo C(x) de uma fábrica, ou dois planos de telefonia móvel, A e B. Como saber qual opção é melhor em cada situação? Basta comparar quem está geometricamente mais alto na vertical naquela faixa de x!"
                },
                {
                    "type": "paragraph",
                    "content": "Se estamos comparando planos de serviço (onde o eixo Y é o preço a pagar), o plano mais econômico para o cliente é a curva que está MAIS ABAIXO. Se estamos comparando receitas ou desempenhos (onde mais alto é melhor), vence a curva que está MAIS ACIMA. E o que significa o ponto exato onde duas curvas se cruzam? É o Ponto de Interseção ou Ponto de Equilíbrio (break-even): ali f(x) = g(x), ou seja, os dois planos custam exatamente o mesmo valor, ou a receita empata com o custo (lucro zero). A partir desse ponto de cruzamento, ocorre a inversão de vantagem!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido — Escolhendo entre Planos de Impressão",
                    "content": "Uma gráfica oferece dois pacotes mensais para empresas. No Plano Básico, paga-se R$ 40,00 fixos mais R$ 0,50 por cópia impressa. No Plano Corporativo, paga-se R$ 100,00 fixos mais R$ 0,20 por cópia. A partir de quantas cópias o Plano Corporativo se torna mais vantajoso?\n\nPasso 1 (Equacionar as duas retas): C_Basico(x) = 0,50x + 40 e C_Corp(x) = 0,20x + 100.\nPasso 2 (Achar o ponto de interseção): Igualamos os dois custos para descobrir o empate: 0,50x + 40 = 0,20x + 100 => 0,30x = 60 => x = 60 / 0,30 = 200 cópias! Nesse ponto, ambos custam R$ 140,00.\nPasso 3 (Interpretar os lados do gráfico): Antes de 200 cópias (0 <= x < 200), a reta do Plano Básico está abaixo, pois começa em 40 enquanto a outra começa em 100 — logo o Básico é mais barato. Após o cruzamento (x > 200), a reta do Corporativo cresce mais devagar (inclinação 0,20 contra 0,50) e passa a ficar por baixo! Portanto, a partir de 201 cópias, o Plano Corporativo é mais vantajoso."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Funções Definidas por Partes: Água, Energia e Imposto de Renda"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção agora a um tema de ouro para garantir 800+: as Funções Definidas por Partes (ou por várias sentenças). Na vida real, tarifas públicas e impostos raramente usam uma única fórmula para todo mundo; eles mudam de regra conforme você muda de faixa de consumo ou de renda. No gráfico, isso aparece como segmentos de reta emendados com inclinações diferentes (ficando mais íngremes a cada nova faixa), ou até com degraus horizontais (como tarifas de estacionamento por hora cheia)."
                },
                {
                    "type": "paragraph",
                    "content": "Vamos entender o erro número 1 dos estudantes em contas progressivas de água, luz ou Imposto de Renda: achar que a alíquota mais alta incide sobre o valor TOTAL! Não funciona assim na maioria das tabelas progressivas do ENEM. Cada faixa de consumo ou salário paga apenas a sua respectiva fatia dentro daquela faixa."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Como Calcular Contas por Faixas sem Errar",
                    "content": "Imagine uma conta de água com três faixas:\n• De 0 a 10 m³: taxa mínima fixa de R$ 30,00 (segmento horizontal no gráfico!).\n• De 11 a 20 m³: paga R$ 4,00 por cada m³ que exceder 10 m³.\n• Acima de 20 m³: paga R$ 7,00 por cada m³ que exceder 20 m³.\n\nSe uma família consumiu 25 m³, quanto ela paga?\nNão multiplique 25 por 7! Fatie o consumo:\n1ª fatia (primeiros 10 m³): R$ 30,00.\n2ª fatia (os 10 m³ seguintes, do 10 ao 20): 10 · R$ 4,00 = R$ 40,00.\n3ª fatia (os 5 m³ restantes, do 20 ao 25): 5 · R$ 7,00 = R$ 35,00.\nTotal da conta = 30 + 40 + 35 = R$ 105,00!\nPercebeu como o gráfico dessa conta é uma linha horizontal de 0 a 10 (altura 30), depois uma reta subindo com inclinação 4 de 10 a 20 (chegando à altura 70), e depois uma reta mais inclinada subindo com inclinação 7 a partir de 20?"
                },
                {
                    "type": "heading",
                    "level": 3,
                    "content": "Velocidade de Crescimento e Taxas no Gráfico"
                },
                {
                    "type": "paragraph",
                    "content": "Para encerrar, lembre-se de olhar sempre para a inclinação quando o gráfico comparar velocidades de variação. Se uma curva representa a quantidade de água em um reservatório ao longo do tempo, os trechos onde a reta é mais íngreme indicam maior vazão (enchendo ou esvaziando mais rápido), enquanto um trecho horizontal indica que o nível parou de variar (vazão líquida zero). Dominando essa leitura intuitiva junto com as funções afim, quadrática, exponencial e logarítmica, você está pronto para gabaritar qualquer questão de funções do ENEM!"
                },
                {
                    "type": "quote",
                    "content": "Em gráficos de funções por partes, cada mudança de inclinação conta a história de uma nova regra entrando em vigor.",
                    "author": "Encerramento do Módulo de Funções"
                }
            ],
            "quiz": []
        }
    ]
