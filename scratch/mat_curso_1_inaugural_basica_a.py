# -*- coding: utf-8 -*-
"""Módulo 1A do Curso Completo de Matemática ENEM:
Aula Inaugural (TRI e Estratégia) e Fundamentos de Matemática Básica (Capítulos 1 a 4).
"""


def get_chapters():
    return [
        {
            "id": "mat-curso-cap-01-tri-rota-800",
            "number": 1,
            "title": "1. Aula Inaugural: Como Funciona a TRI e a Rota Estratégica dos 800+ em Matemática",
            "epigraph": {
                "text": "No ENEM, não vence quem decora a fórmula mais rara; vence quem não entrega de graça os pontos das questões fáceis e médias.",
                "author": "Lição Número Um da Nossa Sala de Aula"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas à Nossa Sala de Aula: Por Que Matemática Define Sua Aprovação"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo à nossa primeira aula. Puxe uma cadeira, pegue seu caderno e respire fundo, porque a partir de hoje você vai fazer as pazes definitivas com a Matemática. Muita gente chega aqui achando que exatas é um dom reservado para poucos, mas deixe-me contar um segredo logo na largada: o ENEM não quer saber se você é um gênio olímpico; ele quer saber se você resolve problemas do cotidiano com calma, método e atenção. Além disso, Matemática é disparada a área que mais puxa sua média geral no SISU: enquanto em Humanas ou Linguagens passar de 750 é raríssimo, em Matemática é perfeitamente possível romper 800, 850 e até 900 pontos sem gabaritar a prova."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Segredo da TRI: Consistência Vale Mais que Genialidade"
                },
                {
                    "type": "paragraph",
                    "content": "A nota do ENEM não nasce de uma simples contagem de acertos. O INEP usa a Teoria de Resposta ao Item (TRI). Pense comigo numa comparação bem clara: dois atletas tentam levantar pesos na academia. O atleta A ergue 10 kg, 20 kg e 40 kg com segurança, mas trava nos 80 kg. O atleta B derruba o peso de 10 kg no pé, sofre no de 20 kg e, de repente, aparece erguendo 80 kg quando ninguém olha. O treinador conclui na hora que o atleta B teve pura sorte!"
                },
                {
                    "type": "paragraph",
                    "content": "É exatamente assim que a TRI avalia as suas 45 questões, medindo dificuldade, poder de discriminação e chance de chute. Quando você acerta as questões fáceis e médias e erra as difíceis, seu desempenho é coerente e previsível: o algoritmo confia no seu resultado e premia você com uma nota alta. Já quando você erra uma questão fácil por pressa e acerta uma difícil no chute, o sistema detecta incoerência e reduz drasticamente o valor daquele acerto difícil."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: O Duelo dos Dois Candidatos com 25 Acertos",
                    "content": "Veja que sacada impressionante na prática. Imagine a Carla e o Bruno fazendo a mesma prova e terminando ambos com 25 acertos em 45 questões.\n• Perfil da Carla (Consistente): garantiu 17 fáceis, 7 médias e apenas 1 difícil, subindo a escada sem tropeços. Nota estimada na TRI: cerca de 765 pontos!\n• Perfil do Bruno (Incoerente): perdeu 6 fáceis por distração, acertou 11 médias e acertou 8 muito difíceis no chute. Nota estimada na TRI: cerca de 655 pontos!\nMesmo número de acertos (25/45), mas mais de 100 pontos de diferença! Por isso, blindar a base vale ouro."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Ranking de Prioridade do 2º Dia: Onde Moram 80% dos Pontos"
                },
                {
                    "type": "paragraph",
                    "content": "Para construir essa consistência, não faz sentido começar estudando assuntos raríssimos. Precisamos atacar a Matriz do ENEM seguindo uma ordem cirúrgica de retorno. Em 1º lugar absoluto está o trio de ouro: Matemática Básica, Porcentagem e Regra de Três (razão e proporção). Sozinho, esse bloco responde por cerca de 40% a 45% da prova e aparece como ferramenta dentro de quase todos os outros temas. Em 2º lugar vem Estatística e Leitura de Gráficos e Tabelas (média, mediana, moda e interpretação visual), questões geralmente rápidas e de altíssimo retorno na TRI."
                },
                {
                    "type": "paragraph",
                    "content": "Em 3º lugar surge a Geometria (Plana e Espacial) aplicada ao mundo real: áreas de terrenos, perímetros, volumes de caixas d'água, cilindros e conversão de litros. Em 4º lugar aparecem as Funções — Afim (1º grau), Quadrática (2º grau) e noções de crescimento exponencial e logarítmico ligadas a gráficos. Dominando esses quatro pilares com segurança, você já alcança a faixa dos 780 a 830 pontos; depois, Probabilidade e Análise Combinatória entram para levar você ao topo."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: A Escada Estratégica dos 800+",
                    "content": "1º Degrau (Obrigatório): Operações, Frações, Decimais, Potências, Razão, Proporção, Regra de Três e Porcentagem.\n2º Degrau (Alta Conversão): Gráficos, Tabelas, Média, Moda, Mediana e Desvio Padrão.\n3º Degrau (Visual e Prático): Áreas, Pitágoras, Semelhança, Prismas, Cilindros, Cones e Esferas.\n4º Degrau (Modelagem): Função do 1º Grau, Função do 2º Grau (vértice!), Exponencial e Logaritmo.\n5º Degrau (Diferencial): Probabilidade, Análise Combinatória e Trigonometria."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Técnica das Três Passadas: Como Vencer as 5 Horas do 2º Dia"
                },
                {
                    "type": "paragraph",
                    "content": "No domingo do 2º dia, são 5 horas para 90 questões (Natureza + Matemática) e cartão-resposta — cerca de 3 minutos por questão. Quem tenta resolver tudo na ordem rígida da 136 à 180 costuma travar numa questão gigante e chutar as últimas cinco, que muitas vezes são fáceis! Por isso, use a Técnica das Três Passadas: na 1ª Passada, leia o comando final e resolva imediatamente todas as questões rápidas e familiares (até 2 minutos cada), circulando as longas sem culpa. Na 2ª Passada, volte para as médias (geometria e equações). Na 3ª Passada, com a base garantida, encare as difíceis e faça chutes estratégicos no que faltar."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: O Perigo de Teimar com a Questão Monstro",
                    "content": "Muita atenção aqui porque é onde candidatos preparados perdem a vaga! Teimar por 12 minutos numa única questão difícil de Análise Combinatória significa sacrificar quatro questões fáceis lá na frente. Mesmo acertando a difícil, a perda das fáceis destrói sua coerência na TRI. Pular uma questão monstro no momento certo não é fraqueza: é inteligência de prova!"
                },
                {
                    "type": "quote",
                    "content": "Aprovações históricas não nascem de acertos milagrosos no chute; elas nascem da tranquilidade de resolver o básico com zero erro bobo.",
                    "author": "Professor Titular do Curso"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Nosso Pacto a Partir do Próximo Capítulo"
                },
                {
                    "type": "paragraph",
                    "content": "No Capítulo 2, começamos do alicerce absoluto. Mesmo que você já saiba somar ou dividir, acompanhe cada truque e exemplo resolvido comigo. É eliminando falhas invisíveis na base que colocamos você na rota segura dos 800+ pontos!"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-02-conjuntos-operacoes",
            "number": 2,
            "title": "2. Conjuntos Numéricos e as Quatro Operações Fundamentais na Prática",
            "epigraph": {
                "text": "Todo edifício capaz de tocar as nuvens apoia-se em fundações firmes. Na Matemática, essas fundações são os números e suas quatro operações.",
                "author": "Princípio da Construção Lógica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Conjuntos Numéricos Sem Decoreba: Do Elevador à Reta Real"
                },
                {
                    "type": "paragraph",
                    "content": "Quando o ENEM conta uma história — sobre o estoque de uma loja, a temperatura de uma câmara fria ou a medida de um terreno — cada situação mora em um tipo de número. Conhecer os conjuntos numéricos ajuda você a interpretar o comando e eliminar alternativas absurdas na hora da prova."
                },
                {
                    "type": "paragraph",
                    "content": "Os Números Naturais (ℕ = {0, 1, 2, 3, ...}) são os degraus de contagem: pessoas numa fila ou ônibus necessários numa excursão. Quando precisamos de valores abaixo de zero — como subsolos de um elevador, temperaturas negativas ou saldo bancário no vermelho — entram os Números Inteiros (ℤ = {..., -2, -1, 0, 1, 2, ...}). Todo Natural é Inteiro, mas nem todo Inteiro é Natural."
                },
                {
                    "type": "paragraph",
                    "content": "E quando dividimos uma pizza ou medimos 1,75 metro? Aí moram os Números Racionais (ℚ), todo número que pode ser escrito como fração a/b (com 'a' e 'b' inteiros e b ≠ 0), incluindo inteiros (5 = 5/1), decimais exatos (0,25 = 1/4) e dízimas periódicas (0,333... = 1/3). Já os números de infinitas casas decimais sem padrão repetitivo, como π ≈ 3,14159... e √2 ≈ 1,4142..., são os Irracionais. Juntando Racionais e Irracionais, formamos os Números Reais (ℝ), a avenida contínua da reta numérica."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: O Resto da Divisão no Mundo Real",
                    "content": "Muita atenção aqui porque cai todo ano! Uma escola precisa transportar 148 alunos em vans de 15 lugares. Dividindo 148 por 15, obtemos 9,866... (9 vans lotadas e sobram 13 alunos). Se o candidato arredonda para 9 vans, deixa 13 estudantes na calçada! Como o número de vans é Natural e todos precisam ir, a resposta certa é 10 vans. Sempre cheque se o contexto pede arredondamento para cima, para baixo ou valor decimal."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Quatro Operações com Agilidade Mental"
                },
                {
                    "type": "paragraph",
                    "content": "Sem calculadora no ENEM, truques limpos evitam erro bobo. Na adição, arredonde mentalmente: para somar 397 + 248, empreste 3 de 248 para transformar 397 em 400, fazendo 400 + 245 = 645. Na subtração, meça a distância: quanto falta de 187 até 500? De 187 a 200 faltam 13; de 200 a 500 faltam 300; logo, 500 - 187 = 313! Na multiplicação, quebre números: 36 × 15 = 36 × (10 + 5) = 360 + 180 = 540. E na divisão inteira, guarde a relação de Euclides: Dividendo = Divisor × Quociente + Resto (com 0 ≤ Resto < Divisor). Se um número dividido por 7 deu quociente 12 e resto 5, ele vale 7 × 12 + 5 = 89."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Jogo de Sinais Sem Confusão: Saldo Bancário vs. Multiplicação"
                },
                {
                    "type": "paragraph",
                    "content": "Aqui mora a confusão número um da Matemática básica: misturar regra de soma com regra de multiplicação! Na adição e subtração, pense em saldo bancário: sinais iguais juntam a dívida ou o crédito e mantêm o sinal (-15 - 8 = -23); sinais diferentes subtraem e vence o maior em módulo (-20 + 12 = -8). Nunca diga 'menos com menos dá mais' somando duas dívidas!"
                },
                {
                    "type": "paragraph",
                    "content": "A regra 'sinais iguais dão (+), sinais diferentes dão (-)' vale SOMENTE para multiplicação, divisão e eliminação de parênteses! Veja: (-4) × (-5) = +20; (-4) × (+5) = -20; (-36) ÷ (-9) = +4; (-36) ÷ (+9) = -4; e -(-7) = +7."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Prioridade nas Expressões Numéricas"
                },
                {
                    "type": "paragraph",
                    "content": "Expressões numéricas seguem uma hierarquia rígida. Primeiro resolva os sinais de associação de dentro para fora: parênteses ( ), depois colchetes [ ], depois chaves { }. Dentro de cada bloco, a ordem das operações é: 1º potências e raízes; 2º multiplicações e divisões (SEMPRE da esquerda para a direita!); 3º adições e subtrações."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: A Armadilha da Esquerda para a Direita",
                    "content": "Calcule 24 - 2 × (5 - 8)² + 18 ÷ 3 × 2.\n• Passo 1 (Parênteses): 5 - 8 = -3 -> 24 - 2 × (-3)² + 18 ÷ 3 × 2.\n• Passo 2 (Potência): (-3)² = +9 -> 24 - 2 × 9 + 18 ÷ 3 × 2.\n• Passo 3 (× e ÷ da esquerda para a direita): 2 × 9 = 18; e em 18 ÷ 3 × 2 fazemos primeiro 18 ÷ 3 = 6 e só depois 6 × 2 = 12 (jamais 3 × 2 antes!).\n• Passo 4 (+ e -): 24 - 18 + 12 = 6 + 12 = 18!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Problema Real Estilo ENEM Resolvido Passo a Passo"
                },
                {
                    "type": "paragraph",
                    "content": "Uma câmara fria de vacinas marcava -14 °C às 6h. Por queda de energia, a temperatura subiu 3 °C por hora durante 4 horas. Às 10h, o gerador ligou e resfriou a câmara em 2 °C por hora até as 15h. Qual a temperatura às 15h? Vamos passo a passo: das 6h às 10h (4 horas), subiu 4 × (+3) = +12 °C, chegando a -14 + 12 = -2 °C. Das 10h às 15h (5 horas), resfriou 5 × (-2) = -10 °C. Logo, às 15h a temperatura final foi -2 + (-10) = -12 °C."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Checklist das Quatro Operações",
                    "content": "• Soma/Subtração: sinais iguais somam mantendo o sinal; sinais diferentes subtraem e fica o sinal do maior.\n• Multiplicação/Divisão: sinais iguais = (+); sinais diferentes = (-).\n• Hierarquia: ( ) -> [ ] -> { }; Potência/Raiz -> × e ÷ (esquerda para direita) -> + e -.\n• Resto real: verifique se sobras exigem arredondar para cima."
                },
                {
                    "type": "quote",
                    "content": "Quem domina as quatro operações com tranquilidade guarda toda a energia mental para interpretar o texto do ENEM.",
                    "author": "Dica de Sala de Aula"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-03-fracoes-decimais",
            "number": 3,
            "title": "3. Desvendando Frações e Números Decimais Sem Trauma",
            "epigraph": {
                "text": "Fração e número decimal não são inimigos: são apenas dois idiomas diferentes falando exatamente da mesma quantidade.",
                "author": "Guia Prático de Aritmética"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Que é uma Fração? Parte de um Todo, Razão e Equivalência"
                },
                {
                    "type": "paragraph",
                    "content": "Se você sempre sentiu um frio na espinha ao ver uma fração numa prova, hoje esse trauma termina de vez! Em uma fração como 3/4, moram duas ideias muito naturais da nossa vida prática. A primeira é a de parte de um todo: o número de baixo, o denominador (4), diz em quantas fatias iguais o inteiro foi dividido; o número de cima, o numerador (3), conta quantas dessas fatias nós pegamos. A segunda ideia é a de razão ou divisão exata: 3/4 também significa literalmente 3 dividido por 4, que resulta em 0,75. E lembre-se das frações equivalentes: se você multiplica ou divide cima e baixo pelo mesmo número diferente de zero, o valor não muda nada — comer 1/2 pizza, 4/8 ou 50/100 é comer exatamente a mesma metade!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Soma e Subtração de Frações: MMC e Método da Borboleta"
                },
                {
                    "type": "paragraph",
                    "content": "Na soma e na subtração, só podemos juntar pedaços que tenham o mesmo tamanho, ou seja, o mesmo denominador! Em 2/7 + 3/7, mantemos o 7 e somamos em cima: 5/7. Mas quando os denominadores são diferentes, como em 2/3 + 1/4, jamais cometa o erro de somar em linha reta! Pelo MMC (ideal quando há três ou mais frações), o MMC(3, 4) = 12 transforma a conta em 8/12 + 3/12 = 11/12. Já para duas frações rápidas na prova, use o Método da Borboleta: multiplique os denominadores embaixo (3 × 4 = 12) e cruze as duas asas em cima (2×4 + 3×1 = 8 + 3 = 11), chegando direto a 11/12! Testando numa subtração: 5/6 - 1/4 = (5×4 - 6×1)/(6×4) = (20 - 6)/24 = 14/24, que simplificando por 2 vira 7/12."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Multiplicação com Simplificação Prévia e Divisão de Frações"
                },
                {
                    "type": "paragraph",
                    "content": "Multiplicar frações é direto: numerador × numerador, denominador × denominador. E lembre: no ENEM, 'de' significa multiplicação ('3/5 de 400' = (3/5) × 400 = 240). Veja que sacada genial: simplifique ANTES de multiplicar! Em (14/15) × (25/21), divida 14 e 21 por 7 (viram 2 e 3) e 25 e 15 por 5 (viram 5 e 3): fica (2/3) × (5/3) = 10/9 sem conta gigante!"
                },
                {
                    "type": "paragraph",
                    "content": "Já na divisão, conserva-se a primeira fração e multiplica-se pelo inverso da segunda: (a/b) ÷ (c/d) = (a/b) × (d/c). Pense por quê: 3 ÷ (1/2) pergunta quantas meias-pizzas cabem em 3 pizzas inteiras — cabem 3 × 2 = 6! Exemplo: (3/4) ÷ (9/8) = (3/4) × (8/9), simplificando 3 com 9 e 8 com 4, dá 2/3."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Dosagem de Medicamento com Frações",
                    "content": "Um frasco tem 240 mL de xarope. Na 1ª semana, um paciente toma 3/8 do frasco; na 2ª semana, toma 2/5 do restante. Quanto sobrou?\n• 1ª semana: (3/8) × 240 = 3 × (240 ÷ 8) = 3 × 30 = 90 mL.\n• Restante: 240 - 90 = 150 mL.\n• 2ª semana: (2/5) × 150 = 2 × (150 ÷ 5) = 2 × 30 = 60 mL.\n• Sobra final: 150 - 60 = 90 mL no frasco!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Números Decimais: Alinhamento de Vírgula, Multiplicação e Divisão"
                },
                {
                    "type": "paragraph",
                    "content": "Preços, medidas e doses vêm quase sempre em decimais (décimos 0,1; centésimos 0,01; milésimos 0,001). Na soma e subtração, a regra é sagrada: vírgula embaixo de vírgula, completando com zeros à direita (15,3 - 4,68 vira 15,30 - 4,68 = 10,62). Na multiplicação, ignore as vírgulas, multiplique os inteiros e devolva a soma total das casas decimais: em 0,25 × 0,04, fazemos 25 × 4 = 100 e voltamos 2 + 2 = 4 casas, achando 0,0100 = 0,01."
                },
                {
                    "type": "paragraph",
                    "content": "Na divisão com vírgula, elimine TODAS as vírgulas multiplicando dividendo e divisor pela mesma potência de 10 (10, 100, 1000...). Precisa calcular 4,8 ÷ 0,12? Multiplique ambos por 100: vira 480 ÷ 12 = 40! Quer 0,45 ÷ 1,5? Multiplique ambos por 100: vira 45 ÷ 150 = 0,3. Nunca divida mantendo vírgula no divisor!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Atalhos com 10, 100 e 0,5",
                    "content": "• Multiplicar por 10, 100, 1000 desloca a vírgula à direita; dividir desloca à esquerda.\n• Multiplicar por 0,5 é tirar a metade! Mas DIVIDIR por 0,5 é DOBRAR o número (18 ÷ 0,5 = 18 × 2 = 36), e dividir por 0,25 equivale a multiplicar por 4!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Dízimas Periódicas e Fração Geratriz"
                },
                {
                    "type": "paragraph",
                    "content": "Dízimas periódicas são decimais infinitos repetitivos com fração geratriz exata. Na dízima simples, cada algarismo do período ganha um '9' embaixo: 0,444... = 4/9; 0,3636... = 36/99 = 4/11; 2,333... = 2 + 1/3 = 7/3. Na dízima composta, como x = 0,2777..., temos um intruso (2) antes do período (7). Fazendo 100x = 27,777... menos 10x = 2,777..., obtemos 90x = 25, logo x = 25/90 = 5/18 (pelo atalho: (27 - 2) em cima; um 9 pelo período e um 0 pelo intruso embaixo)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Finanças e Combustível com Decimais",
                    "content": "Um motorista gastou R$ 176,40 por 29,4 litros de gasolina e reservou 1/3 do que sobrou do seu vale de R$ 240,00 para revisão. Qual o preço por litro e o valor da revisão?\n• Preço/litro: 176,40 ÷ 29,4 -> multiplique ambos por 10 -> 1764 ÷ 294 = R$ 6,00/litro.\n• Saldo no vale: 240,00 - 176,40 = R$ 63,60.\n• Revisão (1/3 de 63,60): 63,60 ÷ 3 = R$ 21,20."
                },
                {
                    "type": "quote",
                    "content": "Simplificar frações antes de multiplicar e eliminar vírgulas antes de dividir economiza minutos preciosos em quase metade da prova.",
                    "author": "Professor Titular do Curso"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-04-potencias-raizes-notacao",
            "number": 4,
            "title": "4. Potenciação, Radiciação e Notação Científica no Dia a Dia e na Ciência",
            "epigraph": {
                "text": "Do diâmetro de um vírus invisível à distância entre galáxias, as potências de 10 são a língua oficial em que a Ciência e o ENEM conversam.",
                "author": "Matriz de Ciências e Matemática"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Potenciação: A Máquina de Multiplicar em Escala"
                },
                {
                    "type": "paragraph",
                    "content": "Pense comigo em uma bactéria que se divide em duas a cada hora. Depois de 1 hora temos 2; depois de 2 horas temos 4; depois de 10 horas temos 2 × 2 × ... × 2 dez vezes seguidas, que escrevemos de forma compacta como 2¹⁰ = 1024! Na potenciação aⁿ, 'a' é a base (o fator que se repete) e 'n' é o expoente (quantas vezes ela multiplica). Mas muita atenção aqui a dois detalhes clássicos onde o ENEM derruba gente apressada: primeiro, (-3)² = (-3) × (-3) = +9, enquanto -3² = -(3 × 3) = -9, porque sem parênteses o expoente só atinge o 3 e o sinal de menos espera do lado de fora! Segundo, todo número diferente de zero elevado a zero vale 1 (a⁰ = 1). Quer enxergar a lógica? Desça a escada da base 2: 2³ = 8, 2² = 4, 2¹ = 2. Cada vez que o expoente cai 1 unidade, dividimos o resultado por 2 — logo, 2⁰ = 2 ÷ 2 = 1!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Propriedades das Potências Que Destravam a Álgebra"
                },
                {
                    "type": "paragraph",
                    "content": "Agora guarde as cinco ferramentas que resolvem metade da álgebra e da física no 2º dia. (1) Produto de mesma base conserva a base e soma os expoentes: aᵐ × aⁿ = a^(m+n), como em 10⁴ × 10⁵ = 10⁹. (2) Divisão de mesma base conserva a base e subtrai os expoentes (sempre o de cima menos o de baixo!): aᵐ ÷ aⁿ = a^(m-n). Cuidado redobrado quando o denominador tem expoente negativo: 10⁴ ÷ 10⁻² = 10^(4 - (-2)) = 10^(4 + 2) = 10⁶! (3) Potência de potência multiplica os expoentes: (aᵐ)ⁿ = a^(m×n), logo (2³)⁴ = 2¹². (4) A potência se distribui sobre multiplicações e divisões: (a × b)ⁿ = aⁿ × bⁿ e (a / b)ⁿ = aⁿ / bⁿ. Só nunca cometa o pecado de distribuir potência numa soma: (3 + 4)² é 7² = 49, e jamais 3² + 4² = 9 + 16 = 25!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Expoente Negativo e Fracionário (A Regra do Sol e Sombra)"
                },
                {
                    "type": "paragraph",
                    "content": "E quando aparece um expoente negativo, como 2⁻³? Muita gente acha que o resultado fica negativo — erro clássico! Expoente negativo apenas manda inverter a base e trocar o sinal do expoente: 2⁻³ = 1 / 2³ = 1/8, e com fração fica ainda mais simples, pois (2/3)⁻² = (3/2)² = 9/4. Já o expoente fracionário faz a ponte direta com as raízes por meio da famosa Regra do Sol e Sombra: a^(m/n) = ⁿ√(aᵐ). Olhe para a fração m/n: quem está em cima tomando sol ('m') vai para a sombra debaixo do teto da raiz; quem está embaixo na sombra ('n') vai para o sol lá fora no índice! Teste comigo: 8^(2/3) = ³√(8²). Dica de ouro: tire a raiz antes de elevar ao quadrado! Como ³√8 = 2, fazemos 2² = 4 em segundos. E em 25^(-1/2), o sinal negativo inverte para 1 / 25^(1/2) = 1 / √25 = 1/5."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Radiciação, Simplificação de Raízes e Racionalização"
                },
                {
                    "type": "paragraph",
                    "content": "Na prova de Geometria ou Física, sua conta frequentemente termina numa raiz não exata, como √72 ou √12 + √27. Para simplificar sem calculadora, fatore em números primos: como 72 = 36 × 2 = 6² × 2, o 6² paga a fiança e sai da raiz quadrada, deixando o 2 preso lá dentro: √72 = 6√2. Para somar ou subtrair raízes, só juntamos termos com o mesmo radicando: em √12 + √27, simplificamos √12 = 2√3 e √27 = 3√3, somando 2√3 + 3√3 = 5√3! Na multiplicação e divisão de mesmo índice, podemos unir tudo sob a mesma raiz: √2 × √8 = √16 = 4. E se surgir uma raiz no denominador, como 6 / √3, racionalize multiplicando cima e baixo por √3: (6 × √3) / (√3 × √3) = 6√3 / 3 = 2√3."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: A Soma Proibida Dentro da Raiz",
                    "content": "Atenção absoluta ao erro mais comum no Teorema de Pitágoras! Se aparecer √(9 + 16), NUNCA separe em √9 + √16! Resolvendo certo (somando antes): √25 = 5. Separando errado daria 3 + 4 = 7, completamente falso. A raiz só pode ser separada na multiplicação e na divisão, jamais na soma ou subtração."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Notação Científica: Domando Números Gigantes e Microscópicos"
                },
                {
                    "type": "paragraph",
                    "content": "O ENEM adora números astronômicos e microscópicos — distância entre planetas, tamanho de células ou toneladas de grãos. Para não perder zeros pelo caminho, usamos a notação científica: N = a × 10^k, com a exigência obrigatória de 1 ≤ |a| < 10 e k inteiro (ou seja, exatamente um algarismo diferente de zero antes da vírgula!). Para nunca errar o sinal de k, aplique a Lei da Gangorra: se o número 'a' diminui (vírgula anda para a esquerda), o expoente k aumenta; se 'a' aumenta (vírgula anda para a direita), k diminui! Veja: 450.000.000 anda 8 casas à esquerda até virar 4,5, então vira 4,5 × 10^8. Já 0,000032 anda 5 casas à direita até virar 3,2, logo cai para 3,2 × 10^(-5). E se uma conta der 45 × 10^(-9)? Diminuímos 45 para 4,5 (1 casa) e aumentamos -9 em +1: 4,5 × 10^(-8)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Ordem de Grandeza e o Teste da Raiz de 10"
                },
                {
                    "type": "paragraph",
                    "content": "Ordem de Grandeza é a potência de 10 mais próxima daquele valor. Muita gente erra achando que a metade entre 10⁰ (1) e 10¹ (10) é 5 — cuidado! Numa escala de potências, o ponto exatamente no meio é 10^(0,5) = √10 ≈ 3,16! Então o roteiro é infalível: coloque em notação científica N = a × 10^k e compare 'a' com 3,16. Se a < 3,16, a ordem de grandeza é 10^k; se a ≥ 3,16, ela sobe para 10^(k+1)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Vírus, Células e Ordem de Grandeza no ENEM",
                    "content": "Uma célula tem diâmetro de 8,4 × 10^(-5) m e um vírus mede 2 × 10^(-8) m. Quantos vírus enfileirados cabem no diâmetro dessa célula e qual é a ordem de grandeza desse número?\n• Passo 1 (Divisão em notação científica): dividimos os coeficientes e subtraímos os expoentes da base 10! (8,4 ÷ 2) × 10^(-5 - (-8)) = 4,2 × 10^(-5 + 8) = 4,2 × 10³ = 4.200 vírus.\n• Passo 2 (Ordem de Grandeza): o coeficiente é a = 4,2. Comparando com √10 ≈ 3,16, vemos que 4,2 ≥ 3,16. Logo, o expoente sobe uma unidade: 10^(3+1) = 10⁴!"
                },
                {
                    "type": "quote",
                    "content": "Dominar potências, raízes e notação científica dá superpoderes para Matemática, Física, Química e Biologia no mesmo domingo.",
                    "author": "Professor Titular do Curso"
                }
            ],
            "quiz": []
        }
    ]
