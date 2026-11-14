# -*- coding: utf-8 -*-
"""
Curso Completo de Matemática para o ENEM
Módulo 9: Sequências Numéricas, Trigonometria e Geometria Analítica (Capítulos 39 a 46)
"""


def get_chapters():
    return [
        # =====================================================================
        # CAPÍTULO 39
        # =====================================================================
        {
            "id": "mat-curso-cap-39-pa",
            "number": 39,
            "title": "Sequências Numéricas e Progressão Aritmética (PA): O Ritmo Somado",
            "epigraph": {
                "text": "A matemática é a arte de dar o mesmo nome a coisas diferentes, reconhecendo o padrão oculto por trás da aparência.",
                "author": "Henri Poincaré"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas ao mundo dos padrões: onde tudo tem ritmo"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo a um dos assuntos mais previsíveis da prova do ENEM. Quando observamos o calendário, os degraus de uma escada, as poltronas de um cinema ou as parcelas de um crediário, percebemos que o mundo se organiza em padrões. Uma sequência numérica nada mais é do que uma lista ordenada de números guiada por uma regra. Nesta aula, vamos dominar a Progressão Aritmética (PA): a sequência do ritmo somado."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sequências figurais e numéricas: enxergando a lei por trás do desenho"
                },
                {
                    "type": "paragraph",
                    "content": "Antes das fórmulas, pense comigo em um desafio clássico. Imagine montar um quadrado com 4 palitos de fósforo. Para colar um segundo quadrado ao lado, aproveitando um lado existente, você acrescenta apenas 3 palitos, chegando a 7. Para o terceiro quadrado, soma mais 3 e chega a 10; para o quarto, chega a 13."
                },
                {
                    "type": "paragraph",
                    "content": "Olhe para os números gerados: (4, 7, 10, 13, ...). Da figura 1 para a 2 somamos 3; da 2 para a 3 somamos 3; da 3 para a 4 somamos 3. Quando uma sequência avança sempre somando uma mesma quantidade fixa, chamamos de Progressão Aritmética (PA). Essa constante é a razão r. Se r > 0, a PA cresce; se r < 0, decresce; e se r = 0, é constante."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor",
                    "content": "Para descobrir a razão r de qualquer PA sem medo de errar sinal, pegue um termo da frente e subtraia o termo imediatamente anterior: r = a2 - a1 = a3 - a2. Na sequência (20, 14, 8, 2, ...), por exemplo, temos r = 14 - 20 = -6. Nunca faça o primeiro menos o segundo!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Fórmula do Termo Geral: viajando para o futuro sem contar no dedo"
                },
                {
                    "type": "paragraph",
                    "content": "Para descobrir quantos palitos formam 50 quadrados na fila (4, 7, 10, 13, ...), não precisamos contar no dedo. Raciocine comigo: de a1 para a2 damos 1 salto de tamanho r; de a1 para a3 damos 2 saltos; de a1 para a4 damos 3 saltos."
                },
                {
                    "type": "paragraph",
                    "content": "Veja que sacada genial: o número de saltos é sempre uma unidade menor que a posição desejada! Assim nasce o termo geral: an = a1 + (n - 1) * r. Para 50 quadrados (a1 = 4, r = 3): a50 = 4 + (50 - 1) * 3 = 4 + 147 = 151 palitos. E se você já tiver o a5 e quiser o a20? De 5 para 20 faltam 15 saltos, logo a20 = a5 + 15 * r."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Propriedade do Termo Médio: o segredo da simetria"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque essa propriedade resolve questões inteiras em três linhas! Em qualquer PA, escolha três termos vizinhos, como (5, 11, 17). Note que o termo do meio, o 11, é exatamente a média aritmética dos seus dois vizinhos: (5 + 17) / 2 = 22 / 2 = 11. Isso funciona porque o anterior é (x - r) e o posterior é (x + r); quando somamos os dois, o -r cancela o +r e sobra 2x, cuja metade é x."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido — Achando o x na PA",
                    "content": "Se os números (x + 1, 2x + 3, 17) formam, nessa ordem, uma PA, qual é o valor de x?\nPasso 1: Aplicamos a propriedade do termo médio: o do meio vale a média dos extremos. Logo, 2x + 3 = (x + 1 + 17) / 2.\nPasso 2: Multiplicamos os dois lados por 2 para eliminar a fração: 4x + 6 = x + 18.\nPasso 3: Isolamos x: 4x - x = 18 - 6, logo 3x = 12 e x = 4.\nConferindo: os termos ficam (4+1, 8+3, 17) = (5, 11, 17), uma PA lindíssima de razão 6!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Soma dos Termos de Gauss: somando centenas de termos num piscar de olhos"
                },
                {
                    "type": "paragraph",
                    "content": "Conta a história que o pequeno Carl Friedrich Gauss, ainda criança na escola primária, recebeu do professor a tarefa castigante de somar todos os números inteiros de 1 a 100. Em poucos segundos, ele entregou a resposta correta: 5.050. Como ele fez? Gauss percebeu que a soma dos extremos é sempre a mesma! Veja: 1 + 100 = 101; 2 + 99 = 101; 3 + 98 = 101; e assim por diante até 50 + 51 = 101. Ora, de 1 a 100 existem 100 números, o que forma exatamente 50 pares cuja soma é 101. Então 50 * 101 = 5.050!"
                },
                {
                    "type": "paragraph",
                    "content": "Generalizando essa genialidade para qualquer PA finita de n termos, a soma dos n primeiros termos é dada por: Sn = [(a1 + an) * n] / 2. Leia em voz alta para gravar no coração: soma do primeiro com o último, vezes a quantidade de termos, dividido por dois. Vamos aplicar isso agora em dois cenários clássicos do ENEM: poltronas de teatro e economia mensal."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1 — Poltronas do Teatro",
                    "content": "Um teatro foi projetado com 15 fileiras de poltronas. A primeira fileira, próxima ao palco, possui 18 poltronas, e cada fileira seguinte possui 3 poltronas a mais que a anterior. Qual é a capacidade total desse teatro?\nPasso 1: Identificamos os dados: a1 = 18, r = 3 e n = 15.\nPasso 2: Para usar a fórmula de Gauss, precisamos saber quantas poltronas há na última fileira (a15). Usamos o termo geral: a15 = 18 + (15 - 1) * 3 = 18 + 14 * 3 = 18 + 42 = 60 poltronas.\nPasso 3: Agora somamos tudo com Gauss: S15 = [(18 + 60) * 15] / 2 = (78 * 15) / 2 = 39 * 15 = 585 poltronas no teatro inteiro."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2 — Economia Mensal",
                    "content": "Marina decidiu poupar dinheiro durante os 12 meses do ano. No 1º mês, guardou R$ 40,00; no 2º mês, R$ 55,00; no 3º mês, R$ 70,00, mantendo esse aumento mensal de R$ 15,00 até dezembro. Quanto ela terá juntado ao final do 12º mês?\nPasso 1: Temos uma PA com a1 = 40, r = 15 e n = 12.\nPasso 2: Calculamos quanto ela depositou no último mês: a12 = 40 + (12 - 1) * 15 = 40 + 11 * 15 = 40 + 165 = R$ 205,00.\nPasso 3: Aplicamos a soma: S12 = [(40 + 205) * 12] / 2 = 245 * 6 = R$ 1.470,00 acumulados ao final do ano."
                },
                {
                    "type": "quote",
                    "content": "Não basta contar passos; na PA, quem entende o tamanho do salto e a simetria dos extremos domina o caminho inteiro antes mesmo de percorrê-lo.",
                    "author": "Aula de Sequências — Curso ENEM"
                }
            ],
            "quiz": []
        },

        # =====================================================================
        # CAPÍTULO 40
        # =====================================================================
        {
            "id": "mat-curso-cap-40-pg",
            "number": 40,
            "title": "Progressão Geométrica (PG): O Ritmo Multiplicado e a Soma Infinita",
            "epigraph": {
                "text": "O juro composto e o crescimento exponencial são forças silenciosas: no início parecem lentas, depois superam qualquer imaginação linear.",
                "author": "Adaptado de Leonhard Euler"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Da soma à multiplicação: o salto exponencial da PG"
                },
                {
                    "type": "paragraph",
                    "content": "Olá novamente! Na aula anterior, vimos a PA caminhando por somas constantes. Mas muitos fenômenos reais multiplicam o valor anterior: a divisão celular, a viralização de um vídeo ou os juros compostos. Quando uma sequência avança multiplicando sempre pelo mesmo fator fixo, estamos diante de uma Progressão Geométrica (PG)."
                },
                {
                    "type": "paragraph",
                    "content": "Esse fator multiplicador chama-se razão q e é obtido dividindo um termo pelo seu antecessor imediato: q = a2 / a1 = a3 / a2. Em (3, 6, 12, 24, ...), temos q = 6 / 3 = 2. Em (100, 50, 25, ...), temos q = 50 / 100 = 0,5. Se q < 0, como em (2, -6, 18, -54, ...), os sinais se alternam formando uma PG oscilante."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fórmula do Termo Geral da PG e a armadilha do tempo"
                },
                {
                    "type": "paragraph",
                    "content": "Vamos deduzir o termo geral da PG com a mesma intuição que usamos na PA. Para ir de a1 até a2, multiplicamos por q uma vez. Para ir de a1 até a3, multiplicamos por q duas vezes (q²). Para chegar ao enésimo termo (an), partindo de a1, precisamos multiplicar por q exatamente (n - 1) vezes! Daí surge a fórmula: an = a1 * q^(n - 1). Simples, limpa e direta."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI — O Termo Inicial vs. Tempo Zero",
                    "content": "Muita atenção aqui porque é onde a maioria escorrega! Se uma colônia começa com 500 bactérias no instante inicial (t = 0) e triplica a cada hora (q = 3), quantas bactérias haverá após 4 horas? Cuidado! No instante 0 temos 500; após 1 hora temos 1.500; após 2 horas temos 4.500; após 3 horas temos 13.500; após 4 horas temos 40.500! Perceba que 'após 4 horas' equivale a 4 multiplicações por 3 (500 * 3^4 = 500 * 81 = 40.500), que seria o 5º termo se você chamar t=0 de a1. Sempre confira quantas multiplicações de fato aconteceram!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Média Geométrica e Produto dos Equidistantes"
                },
                {
                    "type": "paragraph",
                    "content": "Assim como na PA o termo central era a média aritmética dos vizinhos, na PG o termo central (em termos positivos) é a média geométrica dos vizinhos! Observe a sequência (4, 12, 36). Multiplique os extremos: 4 * 36 = 144. Agora eleve o termo do meio ao quadrado: 12² = 144. Isso sempre acontece: em três termos consecutivos (a, b, c) de uma PG, vale que b² = a * c. E mais: em qualquer PG finita, o produto dos termos equidistantes dos extremos é constante. Em (2, 4, 8, 16, 32, 64), note que 2 * 64 = 128, 4 * 32 = 128 e 8 * 16 = 128."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Soma dos Termos de uma PG Finita"
                },
                {
                    "type": "paragraph",
                    "content": "Imagine que uma notícia começa com 2 pessoas compartilhando no primeiro minuto. No segundo minuto, cada uma manda para mais 2 (4 novas pessoas). No terceiro minuto, 8 novas pessoas, e assim por diante até o 6º minuto. Quantas pessoas ao todo ficaram sabendo? Precisamos somar S6 = 2 + 4 + 8 + 16 + 32 + 64. Para não somar tudo na mão quando n for grande, usamos a fórmula da soma finita (válida para q ≠ 1): Sn = a1 * (q^n - 1) / (q - 1)."
                },
                {
                    "type": "paragraph",
                    "content": "Aplicando no nosso exemplo com a1 = 2, q = 2 e n = 6, fazemos: S6 = 2 * (2^6 - 1) / (2 - 1) = 2 * (64 - 1) / 1 = 2 * 63 = 126 pessoas. Se o enunciado trouxer uma razão fracionária menor que 1, você pode inverter a ordem da subtração em cima e embaixo para evitar sinais negativos: Sn = a1 * (1 - q^n) / (1 - q). É exatamente a mesma conta, só mais confortável de fazer."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A mágica da Soma Infinita Convergente (|q| < 1)"
                },
                {
                    "type": "paragraph",
                    "content": "Agora prepare-se para uma das ideias mais lindas da matemática. É possível somar infinitos números positivos e obter um resultado finito? Sim! Pense numa pizza inteira que você come metade hoje (1/2), metade do que sobrou amanhã (1/4), metade do restante depois de amanhã (1/8), depois 1/16, 1/32... Mesmo somando para sempre, você nunca vai comer mais do que 1 pizza inteira! Na fórmula Sn = a1 * (1 - q^n) / (1 - q), quando o módulo da razão é menor que 1 (ou seja, -1 < q < 1) e o número de termos n vai para o infinito, a potência q^n encolhe tanto que tende a zero! Sobra então a fórmula da PG infinita: S_inf = a1 / (1 - q)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1 — Os Quiques da Bola (Clássico do ENEM!)",
                    "content": "Uma bola de borracha é abandonada de uma altura de 12 metros. Toda vez que bate no chão, ela sobe exatamente 2/3 da altura anterior. Qual é a distância total vertical percorrida pela bola até parar completamente?\nPasso 1: Cuidado com a pegadinha! Na primeira queda, a bola apenas DESCE 12 metros. Depois disso, cada quique tem uma SUBIDA e uma DESCIDA iguais!\nPasso 2: As alturas dos quiques formam uma PG infinita de razão q = 2/3: primeiro quique sobe 12 * (2/3) = 8 m (e desce 8 m); segundo quique sobe 16/3 m (e desce 16/3 m), e assim por diante.\nPasso 3: Calculamos a soma infinita das alturas dos quiques (com a1 = 8 e q = 2/3): S_inf = 8 / (1 - 2/3) = 8 / (1/3) = 8 * 3 = 24 metros.\nPasso 4: Como cada quique após a primeira queda é percorrido duas vezes (sobe e desce), temos: Distância total = 12 + 2 * 24 = 12 + 48 = 60 metros!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2 — Fractais e Quadrados Encaixados",
                    "content": "Considere um quadrado de lado 8 cm (área de 64 cm²). Ligando os pontos médios de seus lados, construímos um segundo quadrado inscrito, cuja área vale metade do primeiro (32 cm²). Repetimos esse processo infinitas vezes. Qual é a soma das áreas de todos esses infinitos quadrados?\nPasso 1: A sequência das áreas é (64, 32, 16, 8, ...), uma PG infinita com a1 = 64 e q = 1/2.\nPasso 2: Como |q| = 1/2 < 1, aplicamos S_inf = a1 / (1 - q) = 64 / (1 - 1/2) = 64 / (1/2) = 128 cm²."
                },
                {
                    "type": "quote",
                    "content": "Na PA o tempo caminha a passos iguais; na PG, cada passo multiplica o alcance do anterior — e, quando encolhe, até o infinito cabe dentro de uma fração.",
                    "author": "Aula de Sequências — Curso ENEM"
                }
            ],
            "quiz": []
        },

        # =====================================================================
        # CAPÍTULO 41
        # =====================================================================
        {
            "id": "mat-curso-cap-41-trig-retangulo",
            "number": 41,
            "title": "Trigonometria no Triângulo Retângulo: Seno, Cosseno e Tangente Sem Mistério",
            "epigraph": {
                "text": "A trigonometria nasceu da necessidade humana de medir o inacessível: a altura das pirâmides, a largura dos rios e a distância das estrelas.",
                "author": "História da Matemática"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Medindo o que não dá para alcançar com trena"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo à Trigonometria! Muita gente treme quando ouve as palavras seno, cosseno e tangente, mas hoje você vai perceber que isso nada mais é do que comparar o tamanho dos lados de um triângulo retângulo. Pense comigo: se você construir dois triângulos retângulos de tamanhos diferentes — um pequenininho no caderno e outro gigante num terreno —, mas ambos tiverem o mesmo ângulo agudo de 30°, eles serão semelhantes! Isso significa que, nos dois triângulos, a razão entre o lado da frente do ângulo de 30° e o maior lado será sempre exatamente igual a 0,5. É essa razão constante que recebe nome especial."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Quem é quem no triângulo retângulo: identificando sem errar"
                },
                {
                    "type": "paragraph",
                    "content": "Antes de fazer qualquer conta, precisamos batizar os três lados do triângulo retângulo em relação ao ângulo agudo de interesse, que chamaremos de θ (teta). Primeiro passo: ache o quadradinho de 90°. O lado que está bem na frente do ângulo de 90° — sempre o maior lado do triângulo — é a Hipotenusa (H). Ela nunca muda de lugar, não importa qual ângulo você escolha!"
                },
                {
                    "type": "paragraph",
                    "content": "Os outros dois lados são os catetos, e o apelido deles depende de onde você colocou seu olhar (o ângulo θ). Imagine-se em pé bem no vértice do ângulo θ olhando para dentro do triângulo: o cateto que está lá do outro lado, bem na sua frente, é o Cateto Oposto (O). Já o cateto que encosta no seu ombro, ajudando a formar o ângulo θ junto com a hipotenusa, é o Cateto Adjacente (A) — lembre que 'adjacente' significa 'vizinho, ao lado'."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O famoso SOH-CAH-TOA e a relação entre eles"
                },
                {
                    "type": "paragraph",
                    "content": "Agora vem o mnemônico mais famoso e salvador da matemática escolar: SOH-CAH-TOA! Repita comigo devagar: SOH (Seno = Oposto sobre Hipotenusa), CAH (Cosseno = Adjacente sobre Hipotenusa) e TOA (Tangente = Oposto sobre Adjacente). Note que a tangente também pode ser vista como a razão entre o seno e o cosseno do mesmo ângulo: tg(θ) = sen(θ) / cos(θ), e vale sempre a relação fundamental sen²(θ) + cos²(θ) = 1, que vem direto do Teorema de Pitágoras dividido pela hipotenusa ao quadrado."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso — Como construir a tabela dos ângulos notáveis",
                    "content": "O ENEM adora os ângulos de 30°, 45° e 60° (muitas vezes sem dar os valores!). Construa a tabela em 10 segundos na margem da prova:\n1. Escreva as colunas 30°, 45°, 60°.\n2. Na linha do SENO, coloque 1, 2, 3; na do COSSENO, coloque 3, 2, 1.\n3. Divida tudo por 2 e coloque raiz quadrada nos numeradores (lembrando que raiz de 1 é 1).\nResultado do Seno: 1/2, √2/2, √3/2.\nResultado do Cosseno: √3/2, √2/2, 1/2.\n4. Para a TANGENTE, divida seno por cosseno: tg 30° = √3/3, tg 45° = 1, tg 60° = √3.\nDica de aproximação rápida para contas do ENEM: √2 ≈ 1,41 e √3 ≈ 1,73."
                },
                {
                    "type": "paragraph",
                    "content": "Quer saber por que sen 30° = 1/2? Basta cortar um triângulo equilátero ao meio! A base se parte em duas metades iguais, logo o cateto oposto a 30° mede exatamente metade da hipotenusa. E por que tg 45° = 1? Porque num triângulo retângulo com um ângulo de 45°, o outro ângulo também vale 45°, tornando os dois catetos exatamente iguais — dividir um número por ele mesmo dá 1!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Aplicando na prática: rampas de acessibilidade, escadas e elevações"
                },
                {
                    "type": "paragraph",
                    "content": "Na prova do ENEM, trigonometria quase sempre aparece vestida de problema prático de engenharia, acessibilidade ou topografia. O segredo é sempre desenhar o triângulo retângulo, marcar o ângulo dado, circular o lado que você TEM e o lado que você QUER descobrir, e escolher no SOH-CAH-TOA qual fórmula conecta exatamente esses dois lados."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1 — Rampa de Acessibilidade",
                    "content": "Para vencer um degrau de 1,5 metro de altura, construiu-se uma rampa plana com inclinação de 30° em relação ao piso horizontal. Qual deve ser o comprimento L da rampa e qual a distância horizontal d ocupada no chão? (Use √3 ≈ 1,7).\nPasso 1: Desenhamos o triângulo retângulo. A altura (1,5 m) está na frente do ângulo de 30°: é o Cateto Oposto (O). O comprimento da rampa L é a Hipotenusa (H).\nPasso 2: Quem relaciona O e H? É o Seno (SOH)! Logo: sen 30° = 1,5 / L. Como sen 30° = 1/2, temos 1/2 = 1,5 / L, portanto L = 3,0 metros!\nPasso 3: Para achar a distância horizontal d (Cateto Adjacente, A) usando O = 1,5 m, usamos a Tangente (TOA): tg 30° = 1,5 / d. Como tg 30° = √3/3, vem √3/3 = 1,5 / d -> d = 4,5 / √3 = (4,5√3)/3 = 1,5 * √3 ≈ 1,5 * 1,7 = 2,55 metros."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2 — Dois Ângulos de Elevação (Nível 800+)",
                    "content": "Um topógrafo observa o topo de uma torre vertical sob um ângulo de elevação de 30°. Ele caminha 40 metros em linha reta em direção à torre e passa a observar o mesmo topo sob um ângulo de 60°. Desprezando a altura do aparelho, qual é a altura h da torre? (Use √3 ≈ 1,73).\nPasso 1: Chame de x a distância que ainda falta até a base da torre no segundo ponto. No triângulo menor (60°), temos tg 60° = h / x -> √3 = h / x -> h = x√3.\nPasso 2: No triângulo maior (30°), a base total mede (x + 40). Logo, tg 30° = h / (x + 40) -> √3/3 = h / (x + 40).\nPasso 3: Substituímos h = x√3 na segunda equação: √3/3 = (x√3) / (x + 40). Cancelando √3 dos dois lados, fica 1/3 = x / (x + 40). Multiplicando cruzado: 3x = x + 40 -> 2x = 40 -> x = 20 m.\nPasso 4: Voltamos em h = x√3 = 20 * 1,73 = 34,6 metros!\nSacada bônus: Como 60° é ângulo externo do triângulo da esquerda, o ângulo lá no topo vale 60° - 30° = 30°, tornando esse triângulo isósceles! Logo a hipotenusa do triângulo menor também mede 40 m, e h = 40 * sen 60° = 40 * (√3/2) = 20√3 ≈ 34,6 m!"
                },
                {
                    "type": "quote",
                    "content": "Desenhe o triângulo, ache os 90°, identifique quem está na frente e quem está ao lado do ângulo. O resto é apenas uma regra de três disfarçada.",
                    "author": "Aula de Trigonometria — Curso ENEM"
                }
            ],
            "quiz": []
        },

        # =====================================================================
        # CAPÍTULO 42
        # =====================================================================
        {
            "id": "mat-curso-cap-42-lei-senos-cossenos",
            "number": 42,
            "title": "Lei dos Senos e Lei dos Cossenos: Quando o Triângulo Não Tem 90°",
            "epigraph": {
                "text": "Quando o ângulo reto desaparece, a geometria não nos abandona; ela apenas se generaliza para abraçar qualquer triângulo do universo.",
                "author": "Trigonometria Plana — Curso ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Saindo da zona de conforto do ângulo reto"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! No capítulo anterior, vivemos felizes usando SOH-CAH-TOA e Teorema de Pitágoras porque todo triângulo tinha um belo ângulo de 90°. Mas e quando um navio faz uma curva de 120°, ou quando dois observadores miram uma montanha formando ângulos de 45° e 75°? Nesses triângulos quaisquer (acutângulos ou obtusângulos), SOH-CAH-TOA é proibido! É exatamente para esses momentos que existem duas ferramentas poderosíssimas: a Lei dos Senos e a Lei dos Cossenos."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Como escolher entre Lei dos Senos e Lei dos Cossenos sem hesitar"
                },
                {
                    "type": "paragraph",
                    "content": "Essa é a maior dúvida dos vestibulandos na hora H: qual das duas eu uso? Grave este critério visual infalível. Use a **Lei dos Senos** quando o problema trabalhar com pares opostos (um lado e o ângulo exatamente na frente dele), especialmente quando você conhece **dois ângulos e um lado**, ou dois lados e um ângulo oposto a um deles. Já a **Lei dos Cossenos** é a sua escolha quando você conhece **dois lados e o ângulo ENTRE eles** (formando uma 'boca de jacaré' ou sanduíche) e quer o terceiro lado — ou quando conhece os **três lados** e quer descobrir o cosseno de um ângulo."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Lei dos Senos na prática: pares opostos em proporção"
                },
                {
                    "type": "paragraph",
                    "content": "Em qualquer triângulo de lados a, b, c opostos respectivamente aos ângulos A, B, C, a razão entre um lado e o seno do seu ângulo oposto é sempre constante e igual ao diâmetro (2R) da circunferência que circunscreve esse triângulo: a / sen(A) = b / sen(B) = c / sen(C) = 2R. Na prática, você nunca usa as três frações juntas: escolhe apenas os dois pares que contêm o dado que você tem e a incógnita que você procura, e multiplica cruzado."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1 — Topografia na Margem do Rio (Lei dos Senos)",
                    "content": "Um topógrafo quer medir a distância entre um marco B, na sua margem do rio, e uma torre C, na margem oposta. Ele caminha 100 metros até outro ponto A, formando uma base AB = 100 m. Com um teodolito, mede o ângulo em A igual a 45° e o ângulo em B igual a 75°. Qual é a distância aproximada de B até C? (Use √2 ≈ 1,41 e √3 ≈ 1,73).\nPasso 1: O lado pedido é BC, que está oposto ao ângulo A = 45°. Mas ainda não temos o ângulo oposto ao lado conhecido AB = 100 m, que é o ângulo C!\nPasso 2: A soma dos ângulos internos é 180°, então C = 180° - (45° + 75°) = 180° - 120° = 60°! Que alívio: 45° e 60° são ângulos notáveis!\nPasso 3: Aplicamos a Lei dos Senos: BC / sen(45°) = 100 / sen(60°).\nSubstituindo: BC / (√2/2) = 100 / (√3/2). Cancelando o '/2' dos denominadores: BC / √2 = 100 / √3 -> BC = (100 * 1,41) / 1,73 = 141 / 1,73 ≈ 81,5 metros."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Lei dos Cossenos: o Teorema de Pitágoras com um ajuste fino"
                },
                {
                    "type": "paragraph",
                    "content": "Olhe bem para a Lei dos Cossenos: a² = b² + c² - 2 * b * c * cos(A). Reconheceu o começo dela? Sim, é o próprio Teorema de Pitágoras! Quando o ângulo A é de 90°, sabemos que cos(90°) = 0, então todo o termo final (-2bc * 0) desaparece e sobra exatamente a² = b² + c². Quando o ângulo A é menor que 90° (agudo), o cosseno é positivo, logo o lado oposto a² fica menor que b² + c². E atenção redobrada quando o ângulo A for obtuso (maior que 90°, como 120°, 135° ou 150°)!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI — O Sinal do Cosseno Obtuso",
                    "content": "No segundo quadrante (entre 90° e 180°), o SENO continua positivo (sen 120° = sen 60° = √3/2), mas o COSSENO fica NEGATIVO! Para ângulos suplementares (que somam 180°), vale: cos(180° - x) = -cos(x).\n• cos 120° = -cos 60° = -1/2\n• cos 135° = -cos 45° = -√2/2\n• cos 150° = -cos 30° = -√3/2\nComo a fórmula tem um sinal de MENOS (-2bc * cos A), menos com menos vira MAIS! Quem esquece o sinal negativo do cosseno erra a questão por completo."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2 — Navegação Marítima (Lei dos Cossenos)",
                    "content": "Um barco sai de um porto P e navega 30 km em linha reta até uma ilha A. Em A, o comandante altera a rota formando um ângulo interno de 120° entre o trajeto PA e o novo trajeto AB, navegando mais 50 km até o ponto B. Se o barco precisar voltar em linha reta de B diretamente ao porto P, quantos quilômetros percorrerá nessa volta?\nPasso 1: Temos dois lados (30 km e 50 km) e o ângulo ENTRE eles (120°), querendo o terceiro lado d = PB. É caso puro de Lei dos Cossenos!\nPasso 2: Montamos: d² = 30² + 50² - 2 * 30 * 50 * cos(120°).\nPasso 3: Substituímos cos(120°) = -1/2 com todo cuidado:\nd² = 900 + 2500 - 3000 * (-1/2)\nd² = 3400 + 1500 = 4900.\nPasso 4: Tirando a raiz quadrada: d = √4900 = 70 km! Perceba como o triângulo 3-5-7 com ângulo de 120° gera uma conta exata e maravilhosa."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Resumo estratégico para não travar na hora da prova"
                },
                {
                    "type": "paragraph",
                    "content": "Antes de partir para a próxima aula, faça este teste mental rápido: bateu o olho num triângulo sem 90°? Conte quantos ângulos foram dados. Se o problema deu 2 ângulos (ou deu 1 ângulo e você precisa achar outro ângulo oposto a um lado conhecido), vá de Lei dos Senos. Se o problema deu apenas 1 ângulo ensanduichado entre 2 lados, ou deu os 3 lados sem nenhum ângulo, vá direto de Lei dos Cossenos. E jamais se esqueça de verificar se o ângulo obtuso tem cosseno negativo!"
                },
                {
                    "type": "quote",
                    "content": "A Lei dos Cossenos é o Pitágoras que aprendeu a lidar com ângulos abertos e fechados; a Lei dos Senos é a harmonia entre cada lado e o ângulo que o enxerga.",
                    "author": "Aula de Trigonometria — Curso ENEM"
                }
            ],
            "quiz": []
        },

        # =====================================================================
        # CAPÍTULO 43
        # =====================================================================
        {
            "id": "mat-curso-cap-43-ciclo-periodicos",
            "number": 43,
            "title": "Trigonometria no Ciclo e Fenômenos Periódicos no ENEM",
            "epigraph": {
                "text": "Tudo o que oscila no universo — das marés dos oceanos às batidas do coração — canta na linguagem das ondas senoidais.",
                "author": "Joseph Fourier (adaptado)"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Saindo do triângulo e entrando na roda: o Ciclo Trigonométrico"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Até aqui falamos de ângulos entre 0° e 180° dentro de triângulos. Mas e o ângulo de 210°, de 300°, ou o giro contínuo de uma roda-gigante que dá várias voltas? Para ampliar a trigonometria para qualquer ângulo real, colocamos uma circunferência de raio 1 centrada na origem (0, 0) do plano cartesiano: é o Ciclo Trigonométrico! O ponto de partida (0°) fica lá na direita, em (1, 0), e caminhamos no sentido anti-horário (contrário ao dos ponteiros do relógio)."
                },
                {
                    "type": "paragraph",
                    "content": "Para nunca mais confundir qual eixo é qual, use uma brincadeira clássica: quem está **sem sono** fica em pé; quem está **com sono** fica deitado! Logo, o **Eixo Vertical (y)** é o eixo do **Seno** (positivo acima do centro, nos 1º e 2º quadrantes; negativo embaixo, nos 3º e 4º quadrantes). Já o **Eixo Horizontal (x)** é o eixo do **Cosseno** (positivo à direita, nos 1º e 4º quadrantes; negativo à esquerda, nos 2º e 3º quadrantes). Como o raio do ciclo vale 1, tanto o seno quanto o cosseno sempre ficam presos entre -1 e +1!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Graus versus Radianos: traduzindo os idiomas do ângulo"
                },
                {
                    "type": "paragraph",
                    "content": "Nos fenômenos periódicos do ENEM, os ângulos costumam aparecer em **radianos (rad)** em vez de graus. O radiano mede o ângulo pelo comprimento do arco correspondente dividido pelo raio. Como uma volta completa tem comprimento 2πR, uma volta de 360° equivale a **2π rad**, e meia volta (180°) equivale a **π rad**. Guarde essa ponte de ouro: **π rad = 180°**."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso — Conversões Instantâneas",
                    "content": "Substitua π por 180° e divida de cabeça:\n• π/6 = 180°/6 = 30°\n• π/4 = 180°/4 = 45°\n• π/3 = 180°/3 = 60°\n• π/2 = 180°/2 = 90°\n• 3π/2 = 3 * 90° = 270°\nE se quiser converter um ângulo qualquer, como 150°, para radianos? Monte uma regra de três com 180° — π: 150π / 180 = 5π/6 rad."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Desvendando a Função Periódica: Amplitude, Período e Valor Médio"
                },
                {
                    "type": "paragraph",
                    "content": "Chegamos ao coração do que o ENEM realmente cobra neste tema! Quase todos os anos aparece uma questão sobre roda-gigante, altura da maré, temperatura diária, pressão arterial ou consumo de energia modelados por uma função do tipo **f(t) = A + B * sen(k*t + c)** (ou com cosseno no lugar de seno). Você não precisa decorar gráficos difíceis: basta saber ler o papel físico de cada letra A, B e k!"
                },
                {
                    "type": "paragraph",
                    "content": "Vamos traduzir cada parâmetro. Lembre que o seno (ou cosseno) sempre oscila entre o mínimo -1 e o máximo +1. Assim, o valor mínimo da função será A - |B| e o valor máximo será A + |B|. Daí tiramos três relações vitais: 1) **Valor Médio (A)** é o ponto central da oscilação, dado por (Máx + Mín) / 2; 2) **Amplitude (|B|)** é o quanto a onda sobe ou desce a partir do meio, dada por (Máx - Mín) / 2; 3) **Período (P)** é o tempo que o fenômeno leva para completar um ciclo inteiro, calculado por **P = 2π / |k|**."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1 — Modelando uma Roda-Gigante",
                    "content": "Uma roda-gigante tem diâmetro de 20 metros (logo, raio = 10 m) e seu ponto mais baixo fica a 2 metros de altura do chão. Ela gira com velocidade constante, completando 1 volta a cada 4 minutos. Se uma pessoa embarca no ponto mais baixo no instante t = 0, qual função h(t) descreve sua altura em metros após t minutos?\nPasso 1: Achamos Mínimo e Máximo. Altura mínima = 2 m. Como o diâmetro é 20 m, altura máxima = 2 + 20 = 22 m.\nPasso 2: Valor médio A = (22 + 2) / 2 = 12 m (a altura do eixo central da roda). Amplitude |B| = (22 - 2) / 2 = 10 m (o raio da roda!).\nPasso 3: Período P = 4 min. Como P = 2π / k, temos 4 = 2π / k -> k = 2π / 4 = π/2.\nPasso 4: Em t = 0 ela está no MÍNIMO (2 m). Sabemos que cos(0) = 1. Para obter 12 - 10 = 2 no início, usamos sinal negativo no cosseno: h(t) = 12 - 10 * cos((π/2) * t). Teste rápido: em t = 2 min (meia volta), cos(π) = -1, logo h(2) = 12 - 10*(-1) = 22 m, bem no topo!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2 — Variação das Marés no Porto",
                    "content": "A profundidade da água em um porto varia periodicamente segundo a função P(t) = 7 + 3 * sen((π/6) * t), em que t é o tempo em horas (0 ≤ t ≤ 12) e P está em metros. Determine a profundidade máxima, a mínima, o período da maré e os instantes em que a profundidade atinge exatamente 8,5 metros.\nPasso 1: Máximo = 7 + 3*(1) = 10 m; Mínimo = 7 + 3*(-1) = 4 m. Período = 2π / (π/6) = 12 horas.\nPasso 2: Igualamos P(t) = 8,5: 7 + 3 * sen((π/6)*t) = 8,5 -> 3 * sen((π/6)*t) = 1,5 -> sen((π/6)*t) = 0,5 = 1/2.\nPasso 3: Na primeira volta do ciclo, quais ângulos têm seno igual a 1/2? São 30° (π/6) no 1º quadrante e 150° (5π/6) no 2º quadrante!\nPasso 4: Igualamos o argumento a cada um: (π/6)*t = π/6 -> t = 1 hora; e (π/6)*t = 5π/6 -> t = 5 horas. Portanto, a profundidade é de 8,5 m à 1h e às 5h."
                },
                {
                    "type": "quote",
                    "content": "Na função periódica do ENEM, você não precisa temer o seno gigante: lembre apenas que ele vive preso entre -1 e +1.",
                    "author": "Aula de Trigonometria — Curso ENEM"
                }
            ],
            "quiz": []
        },

        # =====================================================================
        # CAPÍTULO 44
        # =====================================================================
        {
            "id": "mat-curso-cap-44-ga-1",
            "number": 44,
            "title": "Geometria Analítica I: Plano Cartesiano, Coordenadas, Distância entre Pontos e Ponto Médio",
            "epigraph": {
                "text": "Com o plano cartesiano, Descartes uniu duas grandes províncias do pensamento: permitiu desenhar equações e transformar figuras em números.",
                "author": "História da Geometria Analítica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O GPS da Matemática: localizando pontos no espaço plano"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao módulo de Geometria Analítica. Sabe quando você abre um aplicativo de mapa no celular, joga uma partida de batalha naval ou programa a posição de um personagem na tela de um videogame? Por trás de tudo isso está a genial ideia de René Descartes: cruzar duas retas numéricas perpendiculares para dar um endereço único a cada ponto do plano!"
                },
                {
                    "type": "paragraph",
                    "content": "A reta horizontal é o eixo das **abscissas (x)** e a reta vertical é o eixo das **ordenadas (y)**. O ponto de cruzamento delas é a **origem O(0, 0)**. Todo ponto é escrito como um par ordenado **(x, y)** — atenção à ordem alfabética: primeiro você caminha na horizontal (x), depois sobe ou desce na vertical (y). Os eixos dividem o plano em **4 quadrantes**, numerados no sentido anti-horário começando lá em cima à direita: Q1 (+, +), Q2 (-, +), Q3 (-, -) e Q4 (+, -). E se o ponto estiver bem em cima do eixo x? Então sua altura y vale zero, como em (5, 0). Se estiver sobre o eixo y, seu x vale zero, como em (0, -3)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Distância entre Dois Pontos: o Teorema de Pitágoras disfarçado"
                },
                {
                    "type": "paragraph",
                    "content": "Não decore a fórmula da distância como uma receita mágica! Olhe para ela nascendo diante dos seus olhos. Suponha dois pontos A(xA, yA) e B(xB, yB) no mapa. Para ir de A até B em linha reta, podemos imaginar um caminho em 'L': primeiro andamos na horizontal uma distância Δx = |xB - xA|, e depois subimos ou descemos na vertical uma distância Δy = |yB - yA|. Esse 'L' forma um triângulo retângulo perfeito cuja hipotenusa é justamente a distância d entre A e B!"
                },
                {
                    "type": "paragraph",
                    "content": "Aplicando Pitágoras (hipotenusa² = cateto1² + cateto2²), obtemos d² = (xB - xA)² + (yB - yA)², ou seja: **d = √[(xB - xA)² + (yB - yA)²]**. Repare em uma vantagem maravilhosa: como elevamos Δx e Δy ao quadrado, não importa se a subtração der negativa ou positiva — o quadrado sempre transforma o resultado em positivo."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor — Triângulos Pitagóricos no Plano",
                    "content": "Antes de sair elevando números grandes ao quadrado e tirando raízes difíceis, olhe para Δx e Δy! Se você calcular Δx = 3 e Δy = 4, nem faça conta: a distância já é 5! Se der 6 e 8, a distância já é 10! Se der 5 e 12, a distância é 13! O ENEM ama os triângulos pitagóricos (3-4-5 e seus múltiplos) escondidos dentro da Geometria Analítica."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Ponto Médio de um Segmento: a média justa das coordenadas"
                },
                {
                    "type": "paragraph",
                    "content": "Agora imagine que duas cidades estão localizadas em A(xA, yA) e B(xB, yB) e você quer construir um posto de combustível ou uma torre de transmissão exatamente na metade do caminho entre elas. Qual é o endereço desse Ponto Médio M(xM, yM)? A resposta é tão intuitiva quanto calcular a média de duas notas de prova: basta fazer a média aritmética das coordenadas x e a média aritmética das coordenadas y! Logo, **xM = (xA + xB) / 2** e **yM = (yA + yB) / 2**."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1 — Rota de Drone no Mapa Urbano",
                    "content": "Um mapa urbano representado no plano cartesiano (com cada unidade valendo 1 km) posiciona um centro de distribuição em A(2, 3) e um cliente em B(8, 11). Calcule a distância em linha reta que um drone percorre de A até B e as coordenadas do ponto de recarga M localizado exatamente na metade do trajeto.\nPasso 1: Calculamos os deslocamentos: Δx = 8 - 2 = 6 km e Δy = 11 - 3 = 8 km.\nPasso 2: Aplicamos Pitágoras (distância): d = √(6² + 8²) = √(36 + 64) = √100 = 10 km.\nPasso 3: Calculamos o ponto médio: xM = (2 + 8) / 2 = 10 / 2 = 5; yM = (3 + 11) / 2 = 14 / 2 = 7. O ponto de recarga fica em M(5, 7)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2 — Descobrindo a outra ponta (Pegadinha Clássica)",
                    "content": "Sabemos que um segmento AB tem uma extremidade em A(-3, 4) e que seu ponto médio é M(2, 1). Quais são as coordenadas do ponto B(xB, yB)?\nCuidado para não fazer a média de A com M! Quem está no meio é o M!\nPasso 1: Usando a fórmula: (-3 + xB) / 2 = 2 -> -3 + xB = 4 -> xB = 7. Para o y: (4 + yB) / 2 = 1 -> 4 + yB = 2 -> yB = -2.\nPasso 2 (Atalho do Salto): Olhe de A para M. No x, fomos de -3 para 2 (somamos +5). Então damos o mesmo salto de +5 a partir de 2 e chegamos em 7! No y, fomos de 4 para 1 (diminuímos 3). Diminuímos 3 de novo a partir de 1 e chegamos em -2! Logo, B(7, -2), localizado no 4º quadrante."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Conectando o mapa ao cotidiano das provas"
                },
                {
                    "type": "paragraph",
                    "content": "Perceba que toda questão de coordenadas em mapas de parques, telas de radar ou tabuleiros no ENEM pede apenas clareza visual: ache a origem (0, 0), leia atentamente a escala do desenho (às vezes cada quadradinho vale 10 metros ou 500 metros, não 1!) e aplique Pitágoras para distâncias ou média simples para pontos centrais. Com essa base sólida, estamos prontos para traçar retas inteiras no próximo capítulo!"
                },
                {
                    "type": "quote",
                    "content": "No plano cartesiano, nenhuma distância exige esforço de memória: basta imaginar o triângulo retângulo apoiado nos eixos e chamar Pitágoras para ajudar.",
                    "author": "Aula de Geometria Analítica — Curso ENEM"
                }
            ],
            "quiz": []
        },

        # =====================================================================
        # CAPÍTULO 45
        # =====================================================================
        {
            "id": "mat-curso-cap-45-ga-2-reta",
            "number": 45,
            "title": "Geometria Analítica II: Inclinação e Equação da Reta",
            "epigraph": {
                "text": "Toda linha reta guarda um segredo constante: não importa o tamanho do passo horizontal que você dê, a subida vertical mantém sempre a mesma proporção.",
                "author": "Geometria Analítica — Curso ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O DNA de uma reta: a sua inclinação (Coeficiente Angular)"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Hoje vamos aprender a transformar qualquer estrada reta, rampa ou trajetória linear em uma equação algébrica elegante. Pense comigo: o que diferencia uma rampa bem suave de uma ladeira super íngreme? É a taxa com que ela sobe a cada metro que avançamos na frente! Na Geometria Analítica, medimos essa 'rampa' pelo **Coeficiente Angular**, representado pela letra **m**."
                },
                {
                    "type": "paragraph",
                    "content": "Dados dois pontos quaisquer A(xA, yA) e B(xB, yB) sobre uma reta não vertical, o coeficiente angular é a razão entre a variação vertical e a variação horizontal: **m = Δy / Δx = (yB - yA) / (xB - xA)**. E olhe que conexão linda com a Trigonometria: Δy é o cateto oposto ao ângulo de inclinação θ que a reta forma com o eixo x, e Δx é o cateto adjacente! Portanto, **m = tg(θ)**. Se m > 0, a reta sobe da esquerda para a direita (crescente); se m < 0, ela desce (decrescente); se m = 0, ela é totalmente horizontal; e se a reta for perfeitamente vertical, Δx = 0, então m não existe e sua equação é simplesmente x = constante."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Equação Reduzida e Equação Geral da Reta"
                },
                {
                    "type": "paragraph",
                    "content": "Uma vez que conhecemos a inclinação m e um ponto (x0, y0) por onde a reta passa, podemos escrever sua equação usando a fórmula do 'ioiô-mixoxô': **y - y0 = m * (x - x0)**. Isolando o y, chegamos à famosa **Equação Reduzida da Reta: y = m*x + n**. Nela, você lê o gráfico batendo o olho: **m** é o coeficiente angular (inclinação) e **n** é o coeficiente linear, que indica exatamente a altura onde a reta corta o eixo vertical y (ponto (0, n))."
                },
                {
                    "type": "paragraph",
                    "content": "Às vezes, porém, as alternativas do ENEM apresentam a reta com todo mundo do mesmo lado igualado a zero: é a **Equação Geral da Reta: a*x + b*y + c = 0**. Como transformar a geral em reduzida? Basta isolar o y! Por exemplo, se tivermos 6x + 2y - 10 = 0, passamos para lá: 2y = -6x + 10 -> dividindo tudo por 2, chegamos em y = -3x + 5. Pronto: já sabemos na hora que a inclinação é m = -3 e que a reta corta o eixo y no ponto (0, 5)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Retas Paralelas e Perpendiculares: quando rotas não se tocam ou se cruzam a 90°"
                },
                {
                    "type": "paragraph",
                    "content": "Duas estradas retas no mesmo plano podem ter exatamente a mesma direção sem nunca se cruzar: são as **retas paralelas**. Como têm a mesma inclinação, a condição é imediata: **m1 = m2** (e para serem paralelas distintas, n1 ≠ n2). Já quando duas avenidas se cruzam formando um ângulo exato de 90°, chamamos de **retas perpendiculares**. E qual é a regra mágica para o perpendicularismo? O produto dos coeficientes angulares deve ser igual a -1: **m1 * m2 = -1**, ou seja, **m2 = -1 / m1**."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor — 'Inverte e Troca o Sinal!'",
                    "content": "Quer achar o coeficiente angular de uma reta perpendicular em 1 segundo? Pegue o m1, vire a fração de cabeça para baixo e troque o sinal!\n• Se m1 = 2 (ou 2/1), o perpendicular é m2 = -1/2.\n• Se m1 = -3/4, o perpendicular é m2 = +4/3.\nTeste: (-3/4) * (4/3) = -1. Nunca falha!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1 — Achando a Equação da Rota",
                    "content": "Em um plano cartesiano, uma ciclovia retilínea liga o parque A(1, 3) à estação B(4, 9). Determine as equações reduzida e geral dessa ciclovia.\nPasso 1: Calculamos a inclinação: m = (9 - 3) / (4 - 1) = 6 / 3 = 2.\nPasso 2: Aplicamos y - y0 = m*(x - x0) usando o ponto A(1, 3): y - 3 = 2*(x - 1) -> y - 3 = 2x - 2 -> y = 2x + 1 (Equação Reduzida!).\nPasso 3: Passando tudo para um lado só: 2x - y + 1 = 0 (Equação Geral!)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2 — Estrada Perpendicular e Interseção de Rotas",
                    "content": "Considere a ciclovia r de equação y = 2x + 1 que acabamos de achar. Deseja-se construir uma rua s perpendicular a ela que passe pelo ponto P(6, 3). Qual é a equação da rua s e em que ponto exato as duas vias se cruzam?\nPasso 1: Como r tem m1 = 2, a rua perpendicular s terá m2 = -1/2 (inverte e troca o sinal!).\nPasso 2: Passando por P(6, 3): y - 3 = (-1/2)*(x - 6) -> y - 3 = -0,5x + 3 -> y = -0,5x + 6.\nPasso 3: Para achar o cruzamento (interseção) entre duas retas, resolvemos o sistema igualando os y: 2x + 1 = -0,5x + 6 -> 2,5x = 5 -> x = 2.\nPasso 4: Substituímos x = 2 em qualquer uma delas: y = 2*(2) + 1 = 5. Elas se cruzam exatamente no ponto (2, 5)!"
                },
                {
                    "type": "quote",
                    "content": "Na equação reduzida y = mx + n, o m comanda a subida da rampa e o n mostra o degrau inicial no eixo vertical.",
                    "author": "Aula de Geometria Analítica — Curso ENEM"
                }
            ],
            "quiz": []
        },

        # =====================================================================
        # CAPÍTULO 46
        # =====================================================================
        {
            "id": "mat-curso-cap-46-ga-3-circunferencia",
            "number": 46,
            "title": "Geometria Analítica III: A Circunferência e Áreas de Cobertura no Plano",
            "epigraph": {
                "text": "O círculo é a forma perfeita da equidistância: de um único centro irradia-se o mesmo alcance em todas as direções.",
                "author": "Geometria Analítica — Curso ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Do compasso à equação: nascendo a Equação da Circunferência"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos ao grand finale do nosso módulo, e o tema de hoje tem a cara do ENEM atual: antenas de celular, roteadores Wi-Fi, sensores de movimento, radares e áreas de irrigação circular. O que todas essas coisas têm em comum? Todas formam uma circunferência no plano! Por definição, uma circunferência é o conjunto de todos os pontos P(x, y) que estão a uma mesma distância fixa R (o raio) de um ponto central C(x0, y0) (o centro)."
                },
                {
                    "type": "paragraph",
                    "content": "Se você já aprendeu a fórmula da distância lá no Capítulo 44, já sabe a equação da circunferência sem precisar decorar nada! Basta escrever que a distância de (x, y) até (x0, y0) é igual a R: √[(x - x0)² + (y - y0)²] = R. Elevando os dois lados ao quadrado para sumir com a raiz, nasce a **Equação Reduzida da Circunferência: (x - x0)² + (y - y0)² = R²**."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Lendo Centro e Raio sem cair na pegadinha do sinal"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque essa é a pegadinha número um das provas! Como a fórmula traz sinais de menos antes de x0 e y0, na hora de ler o centro você precisa **trocar os sinais** dos números que acompanham x e y nos parênteses, e para achar o raio precisa **tirar a raiz quadrada** do número que está sozinho do lado direito! Veja um exemplo: na equação **(x - 3)² + (y + 5)² = 49**, o x0 vale **+3**, o y0 vale **-5** (pois y + 5 equivale a y - (-5)), e o raio vale **√49 = 7**. Se a circunferência estiver centrada na origem (0, 0), a equação fica ainda mais curta: x² + y² = R²."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Quando a equação vem aberta (Equação Geral): completando quadrados"
                },
                {
                    "type": "paragraph",
                    "content": "E se o enunciado der a equação toda desenvolvida, como **x² + y² - 6x + 4y - 12 = 0**, e pedir o centro e o raio? Calma, existe um truque rápido e infalível chamado 'completar quadrados' (ou divisão por -2)! Para achar o centro (x0, y0), basta olhar para os coeficientes que multiplicam x e y sozinhos (-6 e +4) e dividi-los por -2: x0 = -6 / (-2) = **3** e y0 = 4 / (-2) = **-2**. Já temos o centro C(3, -2)!"
                },
                {
                    "type": "paragraph",
                    "content": "Agora, como achamos o raio? Agrupando mentalmente os quadrados perfeitos: (x² - 6x + 9) + (y² + 4y + 4) = 12 + 9 + 4. Perceba que adicionamos 9 (que é 3²) e 4 (que é 2²) dos dois lados para manter a balança equilibrada! Isso vira **(x - 3)² + (y + 2)² = 25**. Tirando a raiz de 25, descobrimos que o raio é **R = 5**! Treine esse truque duas vezes e ele vira automático."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Antenas Wi-Fi, torres de celular e áreas de cobertura"
                },
                {
                    "type": "paragraph",
                    "content": "Como o ENEM transforma isso em problema real? Muito simples: uma antena instalada em C(x0, y0) com alcance máximo R cobre todos os pontos cuja distância até C seja menor ou igual a R. Algebricamente, a região coberta pelo sinal é descrita pela inequação **(x - x0)² + (y - y0)² ≤ R²**. Para testar se um usuário em P(x, y) tem sinal, você joga as coordenadas dele no lado esquerdo da fórmula: se o resultado der menor que R², ele está dentro da cobertura; se der igual a R², está exatamente na borda; se der maior que R², ficou sem sinal!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1 — Alcance da Torre de Celular",
                    "content": "Uma operadora instalou uma torre transmissora no ponto C(4, 2) de um mapa cartesiano (unidades em km), com raio de cobertura de 5 km. Escreva a equação da borda dessa área de cobertura e verifique se os moradores das casas U(7, 6) e V(8, 6) conseguem captar o sinal.\nPasso 1: Montamos a inequação da cobertura com C(4, 2) e R = 5: (x - 4)² + (y - 2)² ≤ 5², ou seja, (x - 4)² + (y - 2)² ≤ 25.\nPasso 2: Testamos a casa U(7, 6): (7 - 4)² + (6 - 2)² = 3² + 4² = 9 + 16 = 25. Como deu exatamente 25 (distância de 5 km), a casa U está na borda limite e recebe o sinal!\nPasso 3: Testamos a casa V(8, 6): (8 - 4)² + (6 - 2)² = 4² + 4² = 16 + 16 = 32. Como 32 > 25, a casa V está fora do alcance da torre."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2 — Área da Praça e Tangência entre Sensores",
                    "content": "Um sensor de irrigação cobre uma região circular dada por (x - 1)² + (y + 2)² ≤ 36 (unidades em metros). Qual é a área irrigada por esse sensor? E se quisermos instalar um segundo sensor de raio 4 m alinhado horizontalmente à direita do primeiro, de modo que os dois círculos se toquem externamente em apenas um ponto (tangentes), onde deve ficar o novo centro?\nPasso 1: Da equação lemos R² = 36, logo R = 6 m e centro C1(1, -2). A área irrigada é π * R² = 36π m² (aproximadamente 36 * 3,14 = 113,04 m²).\nPasso 2: Para dois círculos serem tangentes externamente, a distância entre seus centros deve ser a soma dos dois raios: d = R1 + R2 = 6 + 4 = 10 metros.\nPasso 3: Como o novo sensor está na mesma horizontal à direita de C1(1, -2), mantemos y = -2 e somamos 10 no x: C2(1 + 10, -2) = C2(11, -2)!"
                },
                {
                    "type": "quote",
                    "content": "A circunferência é o Teorema de Pitágoras girando em torno de um ponto fixo: troque os sinais para achar o centro, tire a raiz para encontrar o raio e domine todo o plano.",
                    "author": "Aula de Geometria Analítica — Curso ENEM"
                }
            ],
            "quiz": []
        }
    ]
