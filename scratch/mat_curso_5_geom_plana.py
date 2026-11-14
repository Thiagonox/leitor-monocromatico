# -*- coding: utf-8 -*-
"""Curso Completo de Matemática para o ENEM - Módulo 5: Geometria Plana (Capítulos 18 a 23)"""


def get_chapters():
    return [
        {
            "id": "mat-curso-18-angulos-paralelas-poligonos",
            "number": 18,
            "title": "Ângulos, Retas Paralelas e Polígonos: O Alfabeto da Geometria",
            "epigraph": {
                "text": "Antes de construir uma catedral, o arquiteto precisa dominar o encontro de duas retas. Em geometria, quem entende os ângulos lê qualquer figura como quem lê um livro aberto.",
                "author": "Aulas de Geometria ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas à Geometria Plana: O Que Realmente É um Ângulo?"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja bem-vindo ao nosso Módulo de Geometria Plana. Se você já olhou para uma questão cheia de linhas e letras gregas e pensou 'por onde começo?', respire fundo porque hoje tudo vai fazer sentido. A Geometria Plana mora na planta de uma casa, na tela do celular ou no campo de futebol. E o primeiro tijolo dela se chama ângulo."
                },
                {
                    "type": "paragraph",
                    "content": "Pense comigo: abra uma tesoura ou observe os ponteiros de um relógio. A abertura entre essas duas semirretas que partem do mesmo vértice é o ângulo — o comprimento das hastes não muda essa abertura. Os babilônios dividiram a volta completa em 360 graus (360°). Batizamos os ângulos assim: o ângulo reto mede exatos 90° (o canto da parede com o chão); o agudo é menor que 90°; o obtuso está entre 90° e 180°; e o raso mede 180° (meia-volta reta)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Pares de Ângulos Famosos: Complementares, Suplementares e OPV"
                },
                {
                    "type": "paragraph",
                    "content": "No ENEM, os ângulos costumam andar em duplas. Dois ângulos que somam 90° são complementares (o complemento de 35° é 55°). Já dois ângulos que somam 180° são suplementares (o suplemento de 110° é 70°). Guarde o truque: Complemento começa com C de Canto (90°) e Suplemento com S de Semicírculo (180°)."
                },
                {
                    "type": "paragraph",
                    "content": "Veja também os ângulos Opostos Pelo Vértice (OPV). Cruze duas canetas em X: os ângulos que ficam de frente um para o outro são imagens no espelho através do cruzamento. Sempre que você fecha um lado do X, o lado oposto fecha igual! Logo, ângulos OPV são sempre congruentes (têm exatamente a mesma medida)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Retas Paralelas Cortadas por uma Transversal: A Regra do Z"
                },
                {
                    "type": "paragraph",
                    "content": "Imagine duas ruas paralelas — Rua A e Rua B — cortadas por uma avenida transversal diagonal. Nascem oito ângulos: quatro em cima e quatro embaixo. Não tente decorar seis nomes complicados de uma vez; vamos simplificar."
                },
                {
                    "type": "paragraph",
                    "content": "Olhe para esses oito ângulos: só existem dois tamanhos ali! Todos os ângulos agudos têm exatamente a mesma medida alpha, e todos os obtusos têm a mesma medida beta, com alpha + beta = 180°. Guarde também a Regra do Z para alternos internos: desenhe a letra Z apoiada nas duas paralelas — os dois ângulos nas dobras internas do Z são sempre iguais."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: O Truque da Paralela Auxiliar",
                    "content": "O ENEM adora colocar uma linha quebrada em zigue-zague entre duas retas paralelas, formando um 'bico' no meio do caminho, como um M deitado ou um raio. Não entre em pânico! Basta passar com o lápis uma terceira reta paralela bem em cima da pontinha de cada dobra. Instantaneamente, o ângulo do bico se divide em dois pedaços que obedecem à Regra do Z lá de cima e cá de baixo. Esse traço invisível transforma questões difíceis em contas de somar."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Cruzamento de Ruas",
                    "content": "Suponha que duas avenidas paralelas são cortadas por uma ciclovia transversal. No cruzamento norte, o ângulo agudo formado mede (2x + 10)°. No cruzamento sul, o ângulo obtuso correspondente do outro lado mede (3x + 20)°. Quanto vale x? Pense comigo: um é agudo e o outro é obtuso em retas paralelas, logo eles são suplementares e somam 180°! Montamos a equação: (2x + 10) + (3x + 20) = 180. Somando os termos semelhantes, temos 5x + 30 = 180, logo 5x = 150, e portanto x = 30°. Substituindo de volta, o ângulo agudo vale 2(30) + 10 = 70°, e o obtuso vale 3(30) + 20 = 110°. Confira: 70° + 110° = 180°. Perfeito!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Polígonos: Soma dos Ângulos Internos, Externos e Diagonais"
                },
                {
                    "type": "paragraph",
                    "content": "Quando fechamos uma figura plana usando apenas segmentos de reta que não se cruzam, criamos um polígono — palavra grega que significa 'vários ângulos'. O mais simples é o triângulo, de 3 lados; depois vêm quadrilátero (4), pentágono (5), hexágono (6), heptágono (7), octógono (8), eneágono (9), decágono (10) e dodecágono (12). Mas quanto somam os ângulos internos de qualquer um deles?"
                },
                {
                    "type": "paragraph",
                    "content": "Em vez de decorar uma tabela gigante, faça comigo a dedução visual. Escolha um único vértice de um polígono de n lados e ligue-o a todos os outros vértices que não são vizinhos dele. Quantos triângulos você consegue fatiar ali dentro? Num quadrilátero (n = 4), nascem 2 triângulos. Num pentágono (n = 5), nascem 3 triângulos. Num hexágono (n = 6), nascem 4 triângulos. Percebeu o padrão? Sempre nascem (n - 2) triângulos! Como cada triângulo guarda 180° lá dentro, a soma dos ângulos internos é S_i = (n - 2) · 180°."
                },
                {
                    "type": "paragraph",
                    "content": "E a soma dos ângulos externos de qualquer polígono convexo? Imagine-se caminhando sobre as calçadas ao redor de uma praça pentagonal até voltar ao ponto de partida. Em cada esquina, você gira o seu corpo pelo ângulo externo da calçada. Ao terminar a volta completa ao redor da praça, quanto você girou no total? Exatos 360°! Não importa se a praça tem 3, 5, 10 ou 100 lados: a soma dos ângulos externos é sempre S_e = 360°. Além disso, em qualquer vértice, o ângulo interno e o externo formam uma linha reta, então a_i + a_e = 180°."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Ladrilhamento e Polígono Regular",
                    "content": "Em um projeto de calçamento com pisos regulares idênticos, sabe-se que cada ângulo interno do ladrilho mede 135°. Quantos lados tem esse ladrilho? Muita atenção aqui: em vez de jogar 135 = (n - 2)·180 / n e sofrer com álgebra, use o atalho do ângulo externo! Se o ângulo interno vale 135°, o externo vale 180° - 135° = 45°. Como o polígono é regular, todos os ângulos externos são iguais e somam 360°. Logo, n = 360° / 45° = 8 lados! Trata-se de um octógono regular. E quantas diagonais ele possui? De cada um dos 8 vértices partem diagonais para todos os outros, exceto para si mesmo e para os 2 vizinhos (logo, n - 3 = 5 diagonais por vértice). Multiplicando pelos 8 vértices e dividindo por 2 para não contar a mesma diagonal na ida e na volta, temos d = n(n - 3)/2 = 8 · 5 / 2 = 20 diagonais."
                },
                {
                    "type": "quote",
                    "content": "Não há estrada real para a geometria; o segredo é enxergar a simetria escondida antes de fazer a primeira conta.",
                    "author": "Adaptado de Euclides"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-19-triangulos-semelhanca",
            "number": 19,
            "title": "Triângulos e Semelhança de Triângulos: Medindo o Inalcançável",
            "epigraph": {
                "text": "Se quiser medir a altura de uma pirâmide sem subir até o topo, peça ajuda ao Sol e observe a sua própria sombra.",
                "author": "Inspirado em Tales de Mileto"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Por Que o Triângulo É o Rei da Engenharia?"
                },
                {
                    "type": "paragraph",
                    "content": "Pegue quatro palitos de picolé e prenda as pontas formando um quadrado. Se você empurrar um canto, ele entorta facilmente e vira um losango mole. Agora pegue três palitos e forme um triângulo. Tente entortá-lo sem quebrar os palitos: é impossível! O triângulo é a única figura poligonal naturalmente rígida. É exatamente por isso que pontes metálicas, torres de alta tensão, gruas de construção e tesouras de telhado são todas construídas à base de triângulos."
                },
                {
                    "type": "paragraph",
                    "content": "Podemos classificar um triângulo de duas maneiras. Quanto aos lados, ele é Equilátero quando tem os três lados iguais — e, por simetria, seus três ângulos internos valem sempre 60°; é Isósceles quando tem pelo menos dois lados iguais, o que garante que os dois ângulos apoiados na base também sejam idênticos; e é Escaleno quando os três lados têm medidas todas diferentes. Já quanto aos ângulos, ele é Acutângulo se os três ângulos forem agudos (menores que 90°), Retângulo se tiver um ângulo reto de 90°, e Obtusângulo se abrigar um ângulo obtuso maior que 90°."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Condição de Existência e Lei Angular de Tales"
                },
                {
                    "type": "paragraph",
                    "content": "Será que quaisquer três varetas formam um triângulo? Faça o teste mental comigo: tente montar um triângulo com uma barra de 10 metros e duas barrinhas curtas de 3 metros e 4 metros. Quando você tentar esticar as duas barras menores para elas se encontrarem sobre a barra de 10 metros, elas mal chegam a 3 + 4 = 7 metros e ficam curtas demais para fechar a ponta! Daí nasce a Condição de Existência (Desigualdade Triangular): o maior lado de um triângulo precisa ser sempre estritamente menor que a soma dos outros dois lados. Formalmente, qualquer lado 'a' satisfaz |b - c| < a < b + c."
                },
                {
                    "type": "paragraph",
                    "content": "Além disso, temos a sagrada Lei Angular de Tales: a soma dos três ângulos internos de qualquer triângulo plano é sempre igual a 180°. Quer uma prova instantânea sem fórmula? Desenhe um triângulo qualquer numa folha de papel, corte os três cantinhos e encoste os três bicos juntos sobre a borda da mesa: eles sempre formam exatamente uma meia-lua reta de 180°. E disso sai um coringa fantástico chamado Teorema do Ângulo Externo: se você prolongar um dos lados do triângulo para fora, o ângulo externo formado ali é sempre igual à soma dos dois ângulos internos que estão longe dele."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Teorema de Tales: Escadas, Lotes e Proporções"
                },
                {
                    "type": "paragraph",
                    "content": "Imagine três prateleiras paralelas na parede atravessadas por duas ripas inclinadas de madeira. O filósofo e matemático Tales de Mileto percebeu que os espaços cortados em uma ripa guardam exatamente a mesma proporção dos espaços correspondentes na outra ripa. Isso significa que, se um degrau tem o dobro da altura do outro de um lado, o correspondente do outro lado também terá o dobro! Esse é o Teorema de Tales, muito cobrado no ENEM em desenhos de lotes de terrenos entre duas ruas paralelas ou degraus de escadas inclinadas."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Semelhança de Triângulos (AA): O Poder do Zoom"
                },
                {
                    "type": "paragraph",
                    "content": "Agora entramos num dos assuntos campeões absolutos de cobrança no ENEM: Semelhança de Triângulos. Pense em uma foto no seu celular quando você faz o movimento de pinça para dar zoom. A foto cresce ou encolhe, mas não fica esticada nem deformada: os ângulos da imagem permanecem intactos e todas as distâncias são multiplicadas pelo mesmo fator de escala k."
                },
                {
                    "type": "paragraph",
                    "content": "Na geometria, dois triângulos são semelhantes pelo critério Ângulo-Ângulo (AA) quando possuem dois ângulos respectivamente iguais — porque se dois já são iguais, o terceiro obrigatoriamente completa os 180° igual também! Quando você enxergar dois triângulos com os mesmos ângulos, monte a proporção comparando sempre os lados opostos aos mesmos ângulos: lado grande sobre lado pequeno equivalente é sempre igual à razão k."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Medindo um Prédio pela Sombra",
                    "content": "Um estudante de 1,75 m de altura está em pé numa praça ensolarada às 15h, projetando no chão plano uma sombra de 1,40 m. No mesmo instante, um edifício vizinho projeta uma sombra de 24 m. Qual é a altura H do edifício? Pense comigo: como os raios solares chegam paralelos ao solo e tanto o estudante quanto o prédio estão na vertical (90°), formam-se dois triângulos retângulos com exatamente os mesmos ângulos! Eles são semelhantes pelo caso AA. Comparando altura com altura e sombra com sombra: H / 1,75 = 24 / 1,40. Vamos simplificar 24 / 1,40 multiplicando cima e baixo por 10: fica 240 / 14, que simplificando por 2 dá 120 / 7. Agora fazemos H = 1,75 · (120 / 7). Repare que 1,75 dividido por 7 dá exatos 0,25! E 0,25 · 120 é um quarto de 120, que vale 30 metros! Sem subir um único degrau, descobrimos que o prédio tem 30 metros."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Rampa com Pilar de Apoio",
                    "content": "Uma rampa de acessibilidade reta sobe suavemente até atingir 1,80 m de altura no final de uma projeção horizontal total de 12 m. Para reforçar a estrutura, o engenheiro instala um pilar vertical a 4 m do início da rampa. Qual deve ser a altura h desse pilar? Desenhe mentalmente o triângulo retângulo maior (base 12 m e altura 1,80 m) e, encaixado dentro dele na ponta esquerda, o triângulo retângulo menor formado até o pilar (base 4 m e altura h). Os dois compartilham o ângulo agudo da subida e ambos têm ângulo reto no chão — portanto, são semelhantes! Montamos a proporção: altura menor / base menor = altura maior / base maior, ou seja, h / 4 = 1,80 / 12. Como a base 4 é um terço da base 12, a altura h também precisa ser um terço de 1,80 m! Logo, h = 1,80 / 3 = 0,60 m (60 cm)."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Comprimento Cresce em k, Mas Área Cresce em k²!",
                    "content": "Atenção redobrada para questões nível 800+ no ENEM! Se você amplia os lados de um triângulo (ou de uma pizza, ou de um terreno) multiplicando tudo por k = 3, o perímetro multiplica por 3, a altura multiplica por 3, mas a ÁREA multiplica por k² = 3² = 9! Nunca cometa o erro clássico de achar que dobrar os lados de uma figura apenas dobra a sua área: dobrar as dimensões lineares quadruplica (2² = 4) a área."
                },
                {
                    "type": "quote",
                    "content": "A semelhança é a arte de resolver o gigante enxergando o mesmo desenho dentro do pequeno.",
                    "author": "Manual do Estudante ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-20-pitagoras-relacoes-metricas",
            "number": 20,
            "title": "Teorema de Pitágoras e Relações Métricas no Triângulo Retângulo",
            "epigraph": {
                "text": "Em todo triângulo retângulo, o quadrado construído sobre a hipotenusa equilibra exatamente a soma dos quadrados apoiados nos dois catetos.",
                "author": "Pitágoras de Samos"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Anatomia do Triângulo Retângulo e a Ideia de Pitágoras"
                },
                {
                    "type": "paragraph",
                    "content": "Se existe uma estrela absoluta da Geometria no ENEM, ela é o triângulo retângulo. Ele ganhou esse nome porque possui um ângulo reto de 90°, representado pelo quadradinho com um ponto no meio. Antes de fazer qualquer conta, identifique os personagens: o lado que fica bem na frente do ângulo de 90° — e que é sempre o maior lado do triângulo — chama-se hipotenusa (vamos chamá-la de 'a'). Os outros dois lados, que se abraçam formando o canto de 90°, são os catetos ('b' e 'c')."
                },
                {
                    "type": "paragraph",
                    "content": "Agora entenda o Teorema de Pitágoras de forma visual, sem magia. Imagine três pisos quadrados colados pelo lado de fora desse triângulo: um quadrado de lado 'a' na hipotenusa, um quadrado de lado 'b' em um cateto e um quadrado de lado 'c' no outro cateto. Pitágoras demonstrou que, se você enchesse de água os dois quadrados menores (b² e c²), a quantidade exata de água encheria perfeitamente até a borda o quadrado maior (a²)! Em linguagem algébrica: a² = b² + c²."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Trios Pitagóricos Mágicos: Ganhe 3 Minutos por Questão"
                },
                {
                    "type": "paragraph",
                    "content": "Na prova do ENEM, tempo é ouro. Quem conhece os trios pitagóricos resolve em cinco segundos uma conta em que o concorrente gasta dois minutos elevando números grandes ao quadrado e tirando raiz. O rei de todos é o trio 3 - 4 - 5 (note que 3² + 4² = 9 + 16 = 25 = 5²). E a grande sacada é que qualquer múltiplo dele também funciona! Se você multiplicar tudo por 2, tem 6 - 8 - 10; por 3, tem 9 - 12 - 15; por 4, tem 12 - 16 - 20; por 5, tem 15 - 20 - 25; por 10, tem 30 - 40 - 50."
                },
                {
                    "type": "paragraph",
                    "content": "Existem outros três trios que aparecem com muita frequência em provas bem elaboradas: o trio 5 - 12 - 13 (e seu dobro 10 - 24 - 26), o trio 8 - 15 - 17 e o trio 7 - 24 - 25. Sempre que olhar para um triângulo retângulo, antes de sair escrevendo a fórmula inteira, divida os lados conhecidos por um divisor comum para ver se algum desses trios mágicos está disfarçado ali!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Cabo de Aço na Antena",
                    "content": "Um técnico precisa esticar um cabo de aço do alto de uma torre vertical de 24 metros de altura até um ponto fixo no solo localizado a 18 metros da base da torre. Quantos metros de cabo são necessários? Olhe para os catetos: 18 e 24. Antes de calcular 18² + 24², simplifique mentalmente dividindo os dois por 6! Ora, 18 = 3 · 6 e 24 = 4 · 6! É o trio 3 - 4 - 5 multiplicado por 6! Portanto, a hipotenusa vale imediatamente 5 · 6 = 30 metros de cabo. Viu como economizamos conta e evitamos erro de multiplicação?"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Dois Atalhos Vitais: Diagonal do Quadrado e Altura do Equilátero"
                },
                {
                    "type": "paragraph",
                    "content": "Duas figuras aparecem tanto que vale a pena saber deduzir seus comprimentos em três segundos usando Pitágoras. A primeira é a diagonal de um quadrado de lado L. Ao cortar o quadrado ao meio pela diagonal 'd', nasce um triângulo retângulo de catetos L e L. Por Pitágoras, d² = L² + L² = 2L², logo d = L√2. Por exemplo, um terreno quadrado de 10 m de lado tem diagonal de 10√2 m (aproximadamente 14,1 m)."
                },
                {
                    "type": "paragraph",
                    "content": "A segunda é a altura 'h' de um triângulo equilátero de lado L. Quando você traça a altura vertical bem do topo até o meio da base, divide o triângulo em dois triângulos retângulos iguais de hipotenusa L e base L/2. Aplicando Pitágoras: L² = h² + (L/2)² = h² + L²/4. Isolando h², temos h² = 3L²/4, e tirando a raiz quadrada chegamos à famosa fórmula h = (L√3)/2. Assim, um triângulo equilátero de lado 8 cm tem altura imediata de 4√3 cm."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Relações Métricas no Triângulo Retângulo: Quando Traçamos a Altura"
                },
                {
                    "type": "paragraph",
                    "content": "Agora dê um passo para o nível 800+. Pegue o triângulo retângulo de hipotenusa 'a' e catetos 'b' e 'c', e derrube uma altura 'h' partindo do vértice de 90° em direção à hipotenusa. Essa altura 'h' divide a hipotenusa em dois pedaços chamados de projeções: 'm' (a sombra do cateto 'b') e 'n' (a sombra do cateto 'c'), de modo que m + n = a. Como essa altura cria dois triângulos retângulos menores lá dentro que são semelhantes ao grandão, nascem quatro relações métricas poderosíssimas."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: As 4 Relações Métricas (Sem Decoreba Cega)",
                    "content": "1. a · h = b · c  ->  Hipotenusa vezes altura é igual ao produto dos catetos! Por quê? Porque os dois lados calculam o dobro da área do triângulo! É a relação mais cobrada do ENEM.\n2. h² = m · n  ->  A altura ao quadrado é o produto das duas projeções na hipotenusa.\n3. b² = a · m  e  c² = a · n  ->  Cada cateto ao quadrado é igual à hipotenusa inteira multiplicada pela sua própria projeção (a sua própria 'sombra').\n4. a² = b² + c²  ->  O próprio Teorema de Pitágoras."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Passarela Sobre Cruzamento",
                    "content": "Um lote triangular retângulo tem catetos medindo 15 m e 20 m ao longo de duas ruas perpendiculares, e uma avenida passa ao longo da sua hipotenusa. A prefeitura deseja construir uma passarela reta saindo da esquina de 90° até a avenida, formando com ela o menor caminho possível (isto é, perpendicular à avenida). Qual será o comprimento dessa passarela? Primeiro, achamos a hipotenusa 'a' com o trio 3-4-5 multiplicado por 5: catetos 15 (3·5) e 20 (4·5) dão hipotenusa a = 25 m (5·5). Como o menor caminho é exatamente a altura 'h' relativa à hipotenusa, aplicamos a relação salva-vidas a · h = b · c! Substituindo: 25 · h = 15 · 20, ou seja, 25h = 300. Dividindo 300 por 25, encontramos h = 12 metros! E se a questão perguntasse onde a passarela encosta na avenida? Usamos b² = a · m: 15² = 25 · m => 225 = 25m => m = 9 m, e o outro trecho vale n = 25 - 9 = 16 m. Confira h² = m · n: 12² = 9 · 16 => 144 = 144!"
                },
                {
                    "type": "quote",
                    "content": "Quando você enxerga um trio 3-4-5 escondido numa planta arquitetônica, a matemática deixa de ser cálculo e vira visão de raio-X.",
                    "author": "Curso Preparatório ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-21-quadrilateros-notaveis",
            "number": 21,
            "title": "Quadriláteros Notáveis: Quadrado, Retângulo, Paralelogramo, Losango e Trapézio",
            "epigraph": {
                "text": "Todo quadrado é um retângulo e também é um losango, mas nem todo retângulo é quadrado. Conhecer essa árvore genealógica evita armadilhas teóricas preciosas.",
                "author": "Geometria das Formas"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Árvore Genealógica dos Quadriláteros"
                },
                {
                    "type": "paragraph",
                    "content": "Qualquer polígono de quatro lados é um quadrilátero, e como ele pode ser fatiado em dois triângulos, a soma dos seus quatro ângulos internos vale sempre 360°. Mas, na arquitetura, na engenharia e no dia a dia, cinco quadriláteros recebem tratamento VIP porque possuem lados paralelos organizados. Pense neles como duas grandes famílias: a família dos Paralelogramos (que têm dois pares de lados paralelos) e a família dos Trapézios (que têm apenas um par de lados paralelos)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Paralelogramo e Seus Três Filhos Famosos"
                },
                {
                    "type": "paragraph",
                    "content": "Comecemos pelo patriarca: o Paralelogramo. Imagine um retângulo de madeira que você empurrou de lado até inclinar. Ele continua tendo os lados opostos paralelos e de mesmo comprimento. Além disso, no paralelogramo, os ângulos opostos são sempre iguais, os ângulos vizinhos do mesmo lado somam 180° (são suplementares, pela regra das retas paralelas!), e as duas diagonais se cruzam exatamente no ponto médio uma da outra."
                },
                {
                    "type": "paragraph",
                    "content": "Agora olhe para os três filhos especiais que herdam tudo isso do paralelogramo e ganham superpoderes extras. O primeiro é o Retângulo: ele é um paralelogramo com os quatro ângulos retos de 90°. Por causa dessa simetria retinha, suas duas diagonais têm exatamente o mesmo comprimento! É exatamente assim que um pedreiro confere se o cômodo de uma casa está 'no esquadro': ele mede as duas diagonais do chão com a trena; se derem a mesma medida, os cantos são retos de 90°."
                },
                {
                    "type": "paragraph",
                    "content": "O segundo filho famoso é o Losango: pense no desenho clássico de uma pipa ou do centro amarelo da bandeira do Brasil. Ele é um paralelogramo cujos quatro lados têm o mesmo comprimento, mesmo que seus ângulos não sejam de 90°. E qual é o segredo de ouro do losango? Suas duas diagonais se cruzam formando um ângulo reto perfeito de 90° (são perpendiculares!) e dividem os ângulos dos cantos exatamente ao meio (são bissetrizes). Isso faz com que o losango inteiro seja dividido por suas diagonais em quatro triângulos retângulos idênticos!"
                },
                {
                    "type": "paragraph",
                    "content": "E o terceiro é o super-herói da família: o Quadrado. Ele junta os poderes do retângulo (quatro ângulos de 90° e diagonais iguais) com os poderes do losango (quatro lados iguais, diagonais perpendiculares a 90° e bissetrizes cortando os cantos em 45° e 45°). Por isso, afirmações como 'todo quadrado é um losango' e 'todo quadrado é um retângulo' são absolutamente verdadeiras!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: O Losango e o Teorema de Pitágoras",
                    "content": "Um portão de ferro decorativo tem um losango central cujas diagonais medem 16 cm e 12 cm. Qual é o perímetro desse losango? Lembre-se da propriedade mágica: as diagonais do losango se cortam ao meio e formam 90°! Portanto, as metades das diagonais medem 16 / 2 = 8 cm e 12 / 2 = 6 cm, servindo como os dois catetos de um dos quatro triângulos retângulos internos, cuja hipotenusa é justamente o lado L do losango! Olhe os catetos 6 e 8: eles formam o nosso velho amigo trio 3-4-5 multiplicado por 2! Logo, L = 5 · 2 = 10 cm (ou L² = 6² + 8² = 36 + 64 = 100 => L = 10 cm). Como o losango tem 4 lados iguais, o perímetro vale 4 · 10 = 40 cm."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Trapézios e a Base Média"
                },
                {
                    "type": "paragraph",
                    "content": "Diferente dos paralelogramos, o Trapézio possui apenas um par de lados paralelos, chamados de Base Maior (B) e Base Menor (b). Os outros dois lados não são paralelos. Quando esses dois lados laterais têm medidas diferentes, temos um trapézio escaleno. Quando o lado lateral faz 90° com as bases (como a parede reta de um galpão com telhado inclinado), temos um trapézio retângulo."
                },
                {
                    "type": "paragraph",
                    "content": "O mais cobrado no ENEM, porém, é o Trapézio Isósceles, aquele que parece uma saia simétrica ou a frente de um balde: seus dois lados não paralelos têm o mesmo comprimento, seus ângulos da base são iguais e suas duas diagonais também são iguais. Existe ainda um conceito elegante chamado Base Média (M) do trapézio, que é o segmento paralelo às bases ligado bem na metade da altura lateral. Como ela fica exatamente no meio do caminho entre B e b, seu comprimento é simplesmente a média aritmética das bases: M = (B + b) / 2. (E se você ligar os pontos médios das duas diagonais, acha a Mediana de Euler, que vale (B - b) / 2)."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Como Atacar Qualquer Trapézio",
                    "content": "Travou em um problema com trapézio isósceles ou escaleno? Trace duas alturas verticais saindo das duas pontas da base menor B_menor até encostar na base maior B_maior! Instantaneamente, o trapézio se desmonta em um retângulo central de largura b e dois triângulos retângulos nas pontas laterais. No trapézio isósceles, esses dois triângulos das pontas são idênticos, e a base de cada um deles vale exatamente (B - b) / 2. Daí em diante, Pitágoras resolve tudo!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Terreno em Formato de Trapézio Isósceles",
                    "content": "Um terreno tem formato de trapézio isósceles com frente (base menor) de 14 m, fundo (base maior) de 26 m e os dois muros laterais inclinados medindo 10 m cada. Qual é a altura (profundidade perpendicular) desse terreno e qual o comprimento da cerca de divisão instalada exatamente na base média? Primeiro, a base média é direta: M = (26 + 14) / 2 = 40 / 2 = 20 metros. Agora, para a altura h, baixamos as duas alturas das pontas da frente de 14 m até o fundo de 26 m. O meio retangular fica com 14 m, sobrando 26 - 14 = 12 m para dividir igualmente entre as duas abas triangulares laterais: cada aba fica com 12 / 2 = 6 m de base! Em cada triângulo retângulo da ponta, temos hipotenusa 10 m (o muro lateral) e cateto horizontal 6 m. Mais uma vez, trio 3-4-5 multiplicado por 2: 6, h, 10! Logo, a altura vale h = 8 metros."
                },
                {
                    "type": "quote",
                    "content": "Na geometria dos terrenos, fatiar um trapézio em um retângulo e dois triângulos é como abrir uma caixa de ferramentas: tudo o que você já sabe volta a funcionar.",
                    "author": "Aulas de Geometria ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-22-circunferencia-circulo",
            "number": 22,
            "title": "Circunferência e Círculo: Comprimento, Arcos e Setores",
            "epigraph": {
                "text": "Se você pegar qualquer objeto redondo — de uma moeda a uma roda de trator — e dividir o contorno pelo diâmetro, o universo responde sempre com o mesmo número mágico: pi.",
                "author": "Tradição Matemática"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Circunferência ou Círculo? A Diferença Que Evita Erros"
                },
                {
                    "type": "paragraph",
                    "content": "No bate-papo cotidiano usamos 'círculo' e 'circunferência' como sinônimos, mas na Matemática eles são coisas distintas. Pense em uma aliança de casamento ou no aro metálico de uma bicicleta: só a linha do contorno, oca por dentro. Isso é a Circunferência — uma linha curva fechada cujos pontos ficam todos à mesma distância de um ponto central. Como é só uma linha, a circunferência tem comprimento (medido em cm ou m). Já o Círculo é a moeda inteira, a pizza inteira, o disco preenchido por dentro junto com a borda! Como é uma superfície plana, o círculo tem área (medida em cm² ou m²)."
                },
                {
                    "type": "paragraph",
                    "content": "Vamos nomear as peças dessa engrenagem. A distância do centro até qualquer ponto da borda é o raio (R). Um segmento que atravessa o círculo ligando dois pontos da borda chama-se corda. Quando essa corda passa bem pelo centro, ela atinge seu tamanho máximo possível e ganha o nome de diâmetro (D), que vale exatamente dois raios: D = 2R. E quando uma reta apenas 'beija' a circunferência em um único pontinho de raspão (como a roda de um carro encostando no asfalto), ela é uma reta tangente, e faz sempre um ângulo reto de 90° com o raio naquele ponto de contato!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Número Pi e o Comprimento da Circunferência"
                },
                {
                    "type": "paragraph",
                    "content": "Faça um experimento imaginário: passe um barbante bem ajustado ao redor de uma lata de refrigerante e depois estique o barbante na régua. Agora meça o diâmetro da tampa da lata. Divida o tamanho do barbante pelo diâmetro. Vai dar aproximadamente 3,14! Faça o mesmo com o pneu de um caminhão ou com a linha do Equador: o resultado da divisão entre o contorno (C) e o diâmetro (D) é sempre a mesma constante irracional chamada pi (π ≈ 3,14159...). Da igualdade C / D = π, como D = 2R, nasce a fórmula imortal do comprimento da circunferência: C = 2 · π · R. Atenção às provas do ENEM: leia sempre o final do enunciado para conferir se ele manda usar π = 3,14, π = 3,1 ou π = 3!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Rodas Girando e Pistas de Atletismo: Clássicos do ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "Pense comigo no movimento de uma bicicleta. Cada vez que o pneu dá 1 volta completa sem derrapar no asfalto, qual distância a bicicleta anda para frente? Exatamente o comprimento da borda do pneu, ou seja, 2πR! Portanto, se uma roda der N voltas completas, a distância total percorrida será D_total = N · 2 · π · R. Cuidado apenas com as unidades: muitas questões dão o raio da roda em centímetros (por exemplo, R = 30 cm) e perguntam quantas voltas ela dá para percorrer 1,8 km! Converta tudo para a mesma unidade (1,8 km = 1.800 m = 180.000 cm) antes de dividir."
                },
                {
                    "type": "paragraph",
                    "content": "Outro cenário apaixonante do ENEM é a pista de atletismo em formato de cápsula: duas retas paralelas ligadas nas pontas por duas curvas em semicírculo. Quando você junta o semicírculo da esquerda com o semicírculo da direita, forma exatamente uma circunferência inteira! Assim, o comprimento de uma volta na pista é simplesmente a soma das duas retas mais 2πR. E se um corredor estiver na raia externa, a uma distância 'd' mais longe do centro, seu raio aumenta para (R + d), fazendo com que cada volta dele seja 2πd metros mais comprida — é por isso que nas Olimpíadas os corredores das raias de fora largam mais à frente!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: A Roda da Bicicleta",
                    "content": "Um ciclista usa uma bicicleta cujo pneu tem diâmetro de 70 cm (use π = 3,14). Quantas voltas completas cada roda dá em um trajeto reto de 1.099 metros? Passo 1: atenção às unidades! Vamos passar tudo para metros. O diâmetro é 70 cm = 0,70 m, logo o raio vale R = 0,35 m (ou podemos usar direto C = π · D!). Passo 2: calculamos o comprimento de 1 volta da roda: C = 3,14 · 0,70 = 2,198 metros. Passo 3: dividimos a distância total pelo tamanho de uma volta: N = 1.099 / 2,198. Olhe que beleza numérica típica do ENEM: 2,198 é exatamente o dobro de 1,099! Multiplicando cima e baixo por 1.000, fica 1.099.000 / 2.198 = 1.000 / 2 = 500 voltas completas!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Calculando Arcos, Setores e Ângulos na Circunferência"
                },
                {
                    "type": "paragraph",
                    "content": "E se quisermos calcular apenas um pedaço da borda da circunferência, chamado de arco, como a ponta que um limpador de para-brisa risca ou o caminho de um portão eletrônico girando? Não precisa decorar fórmula nenhuma em radianos se o ângulo vier em graus: use a regra de três mais intuitiva do mundo! A volta completa de 360° corresponde ao comprimento total 2πR. Logo, um ângulo central alpha corresponde a um arco L proporcional: L / (2πR) = alpha / 360°. Se o ângulo for 60°, por exemplo, 60° é um sexto de 360°, então o arco mede exatamente um sexto de 2πR."
                },
                {
                    "type": "paragraph",
                    "content": "Da mesma forma, se o ângulo estiver no centro da circunferência, chamamos de ângulo central, e ele tem a mesma medida em graus do arco que ele enxerga. Mas fique esperto com um detalhe que aparece em questões difíceis: se o vértice do ângulo estiver encostado lá na outra borda da circunferência (o chamado ângulo inscrito), ele enxerga o mesmo arco por um ângulo mais fechado, valendo exatamente a METADE do ângulo central correspondente! Em particular, todo triângulo inscrito em uma circunferência cujo maior lado seja o diâmetro (180°) tem obrigatoriamente um ângulo de 90° na borda."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: O Limpador de Para-brisa e a Pista",
                    "content": "Um aspersor de jardim gira formando um ângulo de 120° e joga água a até 6 metros de distância, sendo cercado por uma borda de proteção curva no limite do alcance. Qual é o comprimento dessa borda curva de proteção? (Adote π = 3). Passo 1: calculamos a circunferência completa de raio R = 6 m: C = 2 · 3 · 6 = 36 metros. Passo 2: comparamos o ângulo de 120° com a volta inteira de 360°. Ora, 120° / 360° = 1/3 da volta! Passo 3: logo, o comprimento do arco vale 1/3 de 36 = 12 metros."
                },
                {
                    "type": "quote",
                    "content": "Na roda que gira ou no arco de uma ponte, todo pedaço de círculo é apenas uma fração elegante dos 360 graus.",
                    "author": "Manual do Estudante ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-23-perimetro-area",
            "number": 23,
            "title": "Perímetro e Área das Figuras Planas: Decompondo Qualquer Terreno",
            "epigraph": {
                "text": "O perímetro compra o arame da cerca; a área compra a grama do jardim. Quem entende de onde vêm as fórmulas nunca esquece nenhuma delas.",
                "author": "Geometria Aplicada no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Perímetro vs. Área e a Armadilha das Unidades Quadradas"
                },
                {
                    "type": "paragraph",
                    "content": "Chegamos ao fechamento da Geometria Plana — um dos assuntos que mais rendem pontos no ENEM! Primeiro, nunca confunda perímetro com área. Perímetro é o contorno externo da figura (cercar um terreno com tela ou pôr rodapé na sala), medido em unidade linear (m, cm). Área é o preenchimento da superfície interna (grama ou lajotas para cobrir o chão), medida em unidade quadrada (m², cm²)."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Cuidado Mortal ao Converter Áreas!",
                    "content": "Se 1 m tem 100 cm, quantos cm² cabem em 1 m²? Muitos respondem 100 cm² no automático e erram! Num quadrado de 1 m por 1 m, cada lado mede 100 cm, logo a área vale 100 · 100 = 10.000 cm². Cada casa na escala de área varia por 100. E lembre que 1 hectare (ha) equivale a um quadrado de 100 m por 100 m = 10.000 m²."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Dedução Visual das Áreas: Do Retângulo ao Trapézio"
                },
                {
                    "type": "paragraph",
                    "content": "Veja como todas as fórmulas saem do retângulo! A área de um retângulo de base b e altura h é A = b · h (e no quadrado de lado L, A = L²). Num paralelogramo inclinado, corte o triângulo retângulo de uma ponta e encaixe na outra: vira um retângulo exato de área A = b · h — usando sempre a altura perpendicular, nunca o lado torto!"
                },
                {
                    "type": "paragraph",
                    "content": "Já o triângulo é exatamente metade de um paralelogramo, então A = (b · h) / 2. Se faltam alturas, mas você tem dois lados a e b com ângulo theta entre eles, use A = (a · b · sen(theta)) / 2; e no equilátero de lado L, A = (L²√3) / 4."
                },
                {
                    "type": "paragraph",
                    "content": "No losango de diagonais D e d, ele ocupa metade do retângulo que o envolve: A = (D · d) / 2. E no trapézio de bases B e b e altura h, basta multiplicar a base média pela altura: A = [(B + b) · h] / 2."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Área do Círculo, do Setor Circular e da Coroa Circular"
                },
                {
                    "type": "paragraph",
                    "content": "Como calcular a área de um círculo de raio R? Imagine cortar uma pizza redonda em 32 fatias bem fininhas e enfileirá-las alternando ponta para cima e ponta para baixo. Elas formam quase um retângulo perfeito cuja altura é o raio R e cuja base é metade da borda da pizza, isto é, πR! Multiplicando base vezes altura, nasce a famosa fórmula da área do círculo: A = π · R². Nunca confunda: comprimento é 2πR (o 2 fica na frente) e área é πR² (o 2 sobe como expoente porque área é bidimensional!)."
                },
                {
                    "type": "paragraph",
                    "content": "Se você quiser a área de apenas uma fatia da pizza — um Setor Circular de ângulo alpha —, faça a mesma regra de três do capítulo anterior: se 360° têm área πR², quanto tem um ângulo alpha? Basta calcular (alpha / 360°) · πR². E se você tiver um anel plano (uma Coroa Circular entre um círculo maior de raio R e um buraco concêntrico de raio r), subtraia a área do pequeno da área do grande: A_coroa = π(R² - r²)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Estratégias de Nível 800+: Decomposição e Subtração"
                },
                {
                    "type": "paragraph",
                    "content": "No ENEM, as plantas de casas, parques e peças metálicas raramente são um retângulo simples; elas têm formato em 'L', cantos arredondados ou regiões hachuradas (pintadas) estranhas. Ninguém decora fórmula para figura em L! Há duas táticas infalíveis. A primeira é a Decomposição: passe linhas tracejadas dividindo o terreno estranho em retângulos, triângulos e trapézios que você conhece, calcule cada pedaço e some tudo. A segunda é a Subtração (ou Completação): feche a figura por fora formando um retângulo ou quadrado perfeito e subtraia as áreas brancas que não pertencem à região pintada."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Sala em L e Revestimento",
                    "content": "Um arquiteto quer colocar piso cerâmico em uma sala em formato de 'L'. Olhando de cima, a largura total embaixo é 8 m e a altura total à esquerda é 6 m; no canto superior direito há um recorte retangular vazio (um terraço) de 3 m de largura por 2 m de altura. Quantos metros quadrados de piso são necessários e quantas caixas comprar se cada caixa cobre 2 m²? Vamos usar a estratégia da Subtração! Passo 1: fechamos o retângulo grandão completo de 8 m por 6 m, cuja área seria 8 · 6 = 48 m². Passo 2: calculamos a área do recorte vazio do terraço: 3 · 2 = 6 m². Passo 3: subtraímos o vazio do total: A_sala = 48 - 6 = 42 m². Passo 4: dividimos por 2 m² por caixa: 42 / 2 = 21 caixas de piso! E se a questão pedisse o perímetro para comprar rodapé? Note um truque genial: se você 'empurrar' para fora as duas paredes dobradas do recorte, verá que o contorno tem exatamente o mesmo perímetro do retângulo grandão: 2 · (8 + 6) = 28 metros!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Jardim com Canteiro Circular (Subtração Sombreada)",
                    "content": "Uma praça quadrada de 20 metros de lado terá todo o seu piso gramado, exceto um chafariz circular bem no centro de diâmetro 8 m e quatro canteiros triangulares idênticos nos quatro cantos, onde cada canteiro forma um triângulo retângulo de catetos 3 m e 4 m. Qual será a área de grama (região sombreada)? Use π = 3,1. Passo 1: área total do quadrado = 20 · 20 = 400 m². Passo 2: cuidado com a pegadinha do diâmetro! Se D = 8 m, então o raio vale R = 4 m. Área do chafariz = πR² = 3,1 · 4² = 3,1 · 16 = 49,6 m². Passo 3: área de 1 canteiro triangular = (3 · 4) / 2 = 6 m². Como são 4 canteiros iguais nos cantos, temos 4 · 6 = 24 m². Passo 4: subtraímos tudo o que não leva grama: A_grama = 400 - (49,6 + 24) = 400 - 73,6 = 326,4 m². Decompor e subtrair com calma transforma qualquer desenho assustador em aritmética simples e nota 800+ garantida!"
                },
                {
                    "type": "quote",
                    "content": "Toda forma complexa no papel é apenas uma coleção de peças simples esperando a linha certa que as separe.",
                    "author": "Curso Preparatório ENEM"
                }
            ],
            "quiz": []
        }
    ]
