# -*- coding: utf-8 -*-
"""Curso Completo ENEM — Matemática: Módulo 6 — Geometria Espacial (Capítulos 24 a 28)."""


def get_chapters():
    return [
        {
            "id": "mat-curso-cap-24-planificacao-visao-espacial",
            "number": 24,
            "title": "24. Planificação de Sólidos e Visão Espacial: Desmontando Caixas e Embalagens",
            "epigraph": {
                "text": "Antes de calcular o volume de qualquer embalagem, o segredo do mestre é saber desmontá-la na mente e enxergar sua sombra no chão.",
                "author": "Aula Inaugural de Geometria Espacial"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Bem-vindo à terceira dimensão: do papel para o mundo real"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao nosso módulo de Geometria Espacial. Até aqui, na Geometria Plana, a gente viveu num mundo achatado, como uma folha de caderno, trabalhando só com largura e altura. Agora o jogo ganha profundidade! Pense comigo em tudo que está ao seu redor neste exato momento: a caneca de café, a caixa de leite na geladeira, o cone de sinalização na rua, a bola de futebol. No ENEM, Geometria Espacial é figurinha carimbada e, curiosamente, uma das partes que mais derrubam candidatos não é nem a fórmula difícil, mas a capacidade de enxergar objetos em três dimensões. É por isso que começamos treinando o seu olhar."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Poliedros vs. Corpos Redondos: a primeira grande divisão"
                },
                {
                    "type": "paragraph",
                    "content": "Olhe para uma caixa de sapatos e depois para uma lata de refrigerante. A caixa é feita só de pedaços planos e retos, que são polígonos: chamamos esse sólido de poliedro. Já a lata, o cone e a bola têm pelo menos uma superfície curva que rola na mesa: são os corpos redondos. Nos poliedros, temos três elementos sagrados: as faces (cada polígono plano da casca, F), as arestas (os vincos retos onde duas faces se encontram, A) e os vértices (as quinas onde as arestas se encontram, V). Pegue mentalmente um dado comum: ele tem 6 faces quadradas, 12 arestas (4 em cima, 4 embaixo e 4 de pé) e 8 vértices (4 pontas em cima e 4 embaixo). Guarde: V = 8, F = 6, A = 12."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Relação de Euler e o segredo das costuras"
                },
                {
                    "type": "paragraph",
                    "content": "Teste comigo os números do dado: some V + F = 8 + 6 = 14. Agora some A + 2 = 12 + 2 = 14! Não é coincidência! Leonhard Euler provou que, para todo poliedro convexo (sem buracos passantes nem reentrâncias), vale sempre V + F = A + 2. Dica clássica da nossa aula: 'Vamos Fazer Amor a Dois', ou 'V + F = A + 2'. Nunca mais você esquece."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: O Mistério da Bola de Futebol e dos Poliedros",
                    "content": "Um poliedro convexo usado como cúpula tem 12 faces pentagonais e 20 faces hexagonais. Quantos vértices ele possui?\nPasso 1: Total de faces: F = 12 + 20 = 32 faces.\nPasso 2: Truque da costura para achar as arestas (A): cada pentágono tem 5 lados e cada hexágono tem 6. Somando os lados soltos: 12 * 5 + 20 * 6 = 60 + 120 = 180 lados. Como cada aresta une exatamente 2 lados, temos 2A = 180, logo A = 90 arestas.\nPasso 3: Aplique Euler (V + F = A + 2): V + 32 = 90 + 2 -> V = 60 vértices!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Quando Euler NÃO vale?",
                    "content": "Muita atenção aqui! A relação V + F = A + 2 vale para todo poliedro convexo, mas falha em poliedros com 'furos' (como uma moldura quadrada furada no meio). Se o enunciado disser 'poliedro convexo', aplique Euler sem medo!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Planificação: abrindo embalagens na tesoura"
                },
                {
                    "type": "paragraph",
                    "content": "Pegue uma tesoura imaginária e recorte as colagens de uma caixa até deixá-la esticada na mesa: isso é a planificação. O ENEM ama mostrar uma embalagem montada e perguntar qual planificação corresponde a ela. Para acertar de primeira, conheça a assinatura de cada família. O prisma reto tem duas bases iguais e faces laterais retangulares (um prisma triangular abre em três retângulos enfileirados e dois triângulos opostos). Já a pirâmide tem uma única base e triângulos que se fecham num bico (uma pirâmide quadrangular abre num quadrado central com quatro triângulos saindo dos lados)."
                },
                {
                    "type": "paragraph",
                    "content": "Nos corpos redondos, o segredo é igualmente claro. Ao abrir o rótulo de um cilindro reto, a lateral vira um retângulo perfeito entre dois círculos iguais. Já no cone (pense num chapéu de festa aberto), a base é um círculo, mas a lateral esticada na mesa NÃO é um triângulo — muita gente cai nisso! A lateral planificada do cone é um setor circular, ou seja, uma fatia de pizza."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: O Truque das Faces Opostas no Cubo",
                    "content": "Em questões de cubo planificado, guarde esta regra infalível: numa fileira de quadrados alinhados, faces separadas por exatamente UM quadrado intermediário são sempre OPOSTAS quando o cubo fecha! Faces opostas nunca se encostam. Se o desenho montado mostra um coração e uma estrela lado a lado, e na planificação há um quadrado entre eles, elimine essa alternativa na hora!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Projeções Ortogonais: a questão garantida do ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "Atenção máxima aqui, porque praticamente todo ano cai projeção ortogonal no ENEM. Imagine o sol exatamente a pino ao meio-dia: a sombra perfeita que um objeto faz no chão plano é a projeção ortogonal dele no plano horizontal. Veja que sacada genial para trajetórias: esqueça completamente o sobe e desce quando a pergunta pedir a projeção no piso! Se uma formiga sobe verticalmente pela quina de uma caixa e depois anda pela tampa, enquanto ela sobe parada na mesma posição horizontal, sua sombra no chão NÃO se move — fica num único ponto! Só quando ela anda sobre a tampa é que a sombra caminha no chão."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: O Drone e a Rampa Helicoidal",
                    "content": "Um estudante sobe uma escada em caracol perfeita que dá exatamente uma volta completa em torno de um poste central cilíndrico, partindo do térreo até o primeiro andar. Qual é a projeção ortogonal do caminho desse estudante sobre o piso térreo?\nPense comigo: visto bem de cima, como se você fosse um satélite olhando para baixo, o fato de o estudante estar subindo não aparece! Você só vê ele dando uma volta completa ao redor de um ponto central a uma distância fixa (o raio da escada). Portanto, a projeção ortogonal no piso é uma circunferência completa!\nE se uma pessoa anda por uma rampa reta inclinada que liga dois andares? Vista bem de cima, a rampa inclinada projeta apenas um segmento de reta no chão (menor que a rampa, igual à sua sombra horizontal)."
                },
                {
                    "type": "quote",
                    "content": "A visão espacial não é um dom místico: é o hábito de perguntar como uma caixa abre na mesa e qual sombra um movimento deixa no chão.",
                    "author": "Manual de Sobrevivência ENEM 800+"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-25-prismas-cubos-paralelepipedos",
            "number": 25,
            "title": "25. Prismas, Cubos e Paralelepípedos: Áreas, Volumes e Litros",
            "epigraph": {
                "text": "Se um sólido sobe reto com a mesma base do chão ao teto, seu volume é simplesmente a área dessa base multiplicada pela altura.",
                "author": "Princípio Fundamental dos Prismas"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O universo das caixas, piscinas e embalagens retas"
                },
                {
                    "type": "paragraph",
                    "content": "Olá, meu caro aluno! Hoje entramos nas contas mais práticas do ENEM: calcular quanto papelão vai numa caixa, quanta tinta pinta uma sala ou quantos litros cabem numa piscina. Todos esses objetos são prismas: sólidos com duas bases poligonais idênticas e paralelas ligadas por faces laterais retangulares (nos prismas retos). O nome do prisma vem da sua base: triangular, quadrangular, hexagonal, e assim por diante."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Paralelepípedo e Cubo: os reis do cotidiano"
                },
                {
                    "type": "paragraph",
                    "content": "O paralelepípedo retângulo (bloco retangular) é a caixa de sapatos, o aquário ou a sala de aula, com dimensões a, b e c. Para calcular a área total das 6 faces, pense comigo: chão e teto têm área ab cada; frente e fundo têm área ac cada; as laterais têm área bc cada. Logo, Área Total = 2(ab + ac + bc). Simples e lógico!"
                },
                {
                    "type": "paragraph",
                    "content": "E a diagonal interna (D), a maior vareta reta que cabe na caixa de um canto de baixo ao oposto de cima? Aplicando Pitágoras duas vezes (primeiro no chão, depois com a altura), temos D = raiz(a² + b² + c²). Se todas as arestas forem iguais a 'a', temos o Cubo: 6 faces quadradas dão Área Total = 6a², Volume = a³ e diagonal interna D = a * raiz(3)."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: O Aquário ou a Caixa Sem Tampa!",
                    "content": "Muita atenção aqui porque é aqui que a maioria cai! O enunciado pede a área de vidro de um aquário ou a área de azulejo de uma piscina de dimensões a, b e c. Um aquário aberto em cima NÃO tem teto! E uma piscina também não tem teto! Então você NÃO pode usar 2(ab + ac + bc) cegamente. O fundo (a * b) aparece apenas UMA vez! A conta certa para caixa sem tampa é: Área = ab + 2ac + 2bc. Sempre desenhe e confira quantas faces o problema realmente quer cobrir!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Volume Geral dos Prismas: V = Ab * h"
                },
                {
                    "type": "paragraph",
                    "content": "Imagine um maço de folhas de papel sulfite empilhado sobre a mesa. A área de uma folha é a Área da Base (Ab). Se você empilha folhas até atingir uma altura h, o espaço ocupado por todo o maço é simplesmente a área da base multiplicada pela altura: V = Ab * h. E veja que maravilha: mesmo se você der um empurrãozinho de lado na pilha e deixar o prisma inclinado (prisma oblíquo), a área da folha não muda e a altura vertical não muda, então o volume continua sendo exatamente Ab * h! No paralelepípedo, como Ab = a * b e a altura é c, temos V = a * b * c."
                },
                {
                    "type": "paragraph",
                    "content": "Nos prismas de base triangular ou hexagonal regular, o segredo é dominar a Geometria Plana da base. Se a base for um triângulo equilátero de lado L, lembre-se da fórmula da área: Ab = (L² * raiz(3)) / 4. E se o prisma tiver base hexagonal regular (como uma porca de parafuso, uma colmeia ou uma caixa de bombom elegante)? Basta dividir o hexágono regular em 6 triângulos equiláteros idênticos! Logo, Ab = 6 * (L² * raiz(3)) / 4 = (3 * L² * raiz(3)) / 2. Multiplicou pela altura h, achou o volume."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Conversão Sagrada: transformando metros cúbicos em litros"
                },
                {
                    "type": "paragraph",
                    "content": "Preste atenção total agora, porque essa conversão vale ouro na prova do ENEM. Quase nunca o exame te dá as dimensões em decímetros; ele te dá em metros ou em centímetros e exige a resposta em litros ou mililitros! Grave estas três igualdades na alma: 1 metro cúbico (1 m³) equivale a exatamente 1.000 litros. Uma caixa d'água cúbica de 1 m de lado comporta 1.000 litros de água! Segunda igualdade: 1 decímetro cúbico (1 dm³, um cubinho de 10 cm por 10 cm por 10 cm) equivale a exatamente 1 litro. Terceira igualdade: 1 centímetro cúbico (1 cm³, um dadinho pequeno de 1 cm de lado) equivale a exatamente 1 mililitro (1 mL)."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Escada das Unidades Cúbicas",
                    "content": "Na medida linear (comprimento), cada passo na escada multiplica ou divide por 10 (1 m = 10 dm = 100 cm). Na medida de volume (cúbica), você multiplica 10 em três dimensões (10 * 10 * 10), então cada passo vale 1.000!\n• 1 m³ = 1.000 dm³ = 1.000 litros\n• 1 dm³ = 1.000 cm³ = 1 litro = 1.000 mL\n• Portanto, 1 m³ = 1.000.000 cm³ (um milhão de centímetros cúbicos)!\nDica prática: se todas as medidas estiverem em centímetros, multiplique tudo para achar cm³ (que já é mL) e depois divida por 1.000 para passar para litros!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Colocando a mão na massa: dois problemas clássicos resolvidos"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: A Piscina do Condomínio",
                    "content": "Uma piscina em formato de paralelepípedo retângulo tem 8 m de comprimento, 4 m de largura e 1,5 m de profundidade. Deseja-se revestir o fundo e as quatro paredes laterais com azulejos que custam R$ 50,00 o metro quadrado, e depois enchê-la até 80% de sua capacidade. Qual o gasto com azulejos e quantos litros de água serão usados?\nPasso 1 (Área sem tampa): Fundo = 8 * 4 = 32 m². Duas paredes maiores = 2 * (8 * 1,5) = 24 m². Duas paredes menores = 2 * (4 * 1,5) = 12 m². Área total = 32 + 24 + 12 = 68 m². Gasto = 68 * 50 = R$ 3.400,00.\nPasso 2 (Volume e Litros): Volume total = 8 * 4 * 1,5 = 48 m³. Como queremos apenas 80%, Volume de água = 0,8 * 48 = 38,4 m³. Como 1 m³ = 1.000 L, temos 38,4 * 1.000 = 38.400 litros!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: A Caixinha de Suco em Centímetros",
                    "content": "Uma embalagem prismática de suco tem base quadrada de 5 cm de lado e altura de 20 cm. Quantos litros de suco cabem em um pacote com 12 dessas caixinhas?\nPasso 1: Volume de uma caixinha = 5 * 5 * 20 = 500 cm³.\nPasso 2: Lembre-se de que 1 cm³ = 1 mL! Então cada caixinha tem 500 mL (meio litro).\nPasso 3: Em 12 caixinhas, temos 12 * 500 mL = 6.000 mL. Dividindo por 1.000, obtemos exatamente 6 litros!"
                },
                {
                    "type": "paragraph",
                    "content": "Viu como fica gostoso quando você entende o porquê de cada conta? Não tenha pressa ao ler o enunciado: primeiro verifique se todas as dimensões estão na mesma unidade (tudo em metro ou tudo em centímetro), depois cheque quais faces existem de verdade na figura, calcule o volume e só no final converta para litros. Essa rotina limpa evita 95% dos erros bobos que roubam pontos preciosos na TRI."
                },
                {
                    "type": "quote",
                    "content": "Um milímetro de descuido nas unidades transforma 10 litros em 10.000 litros; na Geometria Espacial, converter antes de calcular é metade da questão ganha.",
                    "author": "Professor Titular ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-26-cilindros-latas-rotulos",
            "number": 26,
            "title": "26. Cilindros: Latas, Reservatórios e Rótulos",
            "epigraph": {
                "text": "Quando você desenrola o rótulo de uma lata, a curva desaparece e revela um simples retângulo cujo comprimento é o abraço exato da circunferência.",
                "author": "Segredo da Planificação Cilíndrica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O sólido mais popular da indústria e do ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "Seja muito bem-vindo ao capítulo dos cilindros! Se você abrir a despensa da sua cozinha, vai perceber por que o ENEM é apaixonado por cilindros: latas de leite em pó, latas de refrigerante, tubos de batata frita, potes de palmito, reservatórios de água, canos hidráulicos e rolos de papel toalha são todos cilindros circulares retos. Um cilindro reto é como um primo arredondado do prisma: em vez de ter um polígono na base, ele tem dois círculos idênticos e paralelos de raio R, separados por uma altura h perpendicular às bases."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Cilindro Reto vs. Cilindro Equilátero: atenção ao vocabulário!"
                },
                {
                    "type": "paragraph",
                    "content": "Antes das fórmulas, anote uma palavra que o ENEM adora: cilindro equilátero. Cortando o cilindro ao meio, de cima a baixo, pelo centro das bases (secção meridiana), vemos um retângulo de largura 2R (diâmetro) e altura h. Quando o cilindro é equilátero, essa secção é um QUADRADO perfeito! Ou seja, em todo cilindro equilátero vale h = 2R. Leu 'cilindro equilátero de raio 3 cm'? Já sabe na hora que h = 6 cm!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Rótulos e Planificação: o retângulo escondido na lata"
                },
                {
                    "type": "paragraph",
                    "content": "Agora tire o rótulo de uma lata cortando reto na vertical e estique-o sobre a mesa: aparece um retângulo perfeito! A altura dele é a altura da lata (h), e a largura abraçava a circunferência da tampa, medindo 2 * pi * R. Daí nasce a Área Lateral: Al = 2 * pi * R * h. Para a Área Total de uma lata fechada (com fundo e tampa), somamos os dois círculos (2 * pi * R²): At = 2 * pi * R * h + 2 * pi * R² = 2 * pi * R * (h + R). Se for copo ou lata sem tampa, conte apenas UMA base!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Enrolando uma Folha Retangular!",
                    "content": "Questão clássica de vestibular e ENEM: pegue uma folha de papel retangular de 20 cm por 30 cm. Você pode enrolá-la de dois jeitos para formar um tubo cilíndrico sem tampa. Jeito 1: a altura é 30 cm e o comprimento da circunferência é 20 cm (2*pi*R = 20 -> R = 10/pi). Jeito 2: a altura é 20 cm e o comprimento da circunferência é 30 cm (2*pi*R = 30 -> R = 15/pi). Qual dos dois tubos tem maior volume? Como o raio entra ao QUADRADO no volume, o tubo mais 'gordinho' e baixo (Jeito 2) sempre vence com folga!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Volume do Cilindro e o poder explosivo do raio ao quadrado"
                },
                {
                    "type": "paragraph",
                    "content": "O volume de qualquer cilindro segue a mesma lógica sagrada dos prismas: Área da Base vezes Altura. Como a base é um círculo de área pi * R², temos V = pi * R² * h. Agora pare tudo e olhe bem para esse expoente 2 em cima do R. Ele é a chave para resolver metade das questões de troca de embalagem do ENEM em 20 segundos!"
                },
                {
                    "type": "paragraph",
                    "content": "Veja que sacada genial: no volume V = pi * R² * h, a altura h tem expoente 1 (efeito linear), mas o raio R tem expoente 2 (efeito quadrático)! Isso quer dizer que, se você dobrar a altura de um reservatório mantendo o raio igual, o volume dobra (2x). Mas se você dobrar o raio mantendo a altura igual, o volume é multiplicado por 2² = 4 (quadruplica!). E se uma empresa quiser enganar ou adaptar uma embalagem, dobrando a altura mas reduzindo o raio pela metade? Faça a conta proporcional: novo volume = (1/2)² * 2 = (1/4) * 2 = 1/2. O volume cai pela metade! É por isso que latas mais largas enganam muito os olhos no supermercado."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Trocando o Copo da Festa",
                    "content": "Uma lanchonete serve suco em um copo cilíndrico de raio 4 cm e altura 10 cm, usando pi = 3. Para uma promoção, quer criar um copo novo com o dobro da altura e metade do raio, ou manter a altura e aumentar o raio em 50%? Vamos comparar usando proporção!\nCopo original: V0 = pi * 4² * 10 = 160 * pi cm³ (usando pi = 3, dá 480 mL).\nOpção A (dobro da altura, metade do raio): R = 2 cm, h = 20 cm. VA = pi * 2² * 20 = 80 * pi cm³ (240 mL — caiu pela metade!).\nOpção B (mesma altura, raio aumenta 50%, ou seja, vira 1,5 * R = 6 cm): VB = pi * 6² * 10 = 360 * pi cm³ (1.080 mL — aumentou 125%, pois 1,5² = 2,25!)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: O Reservatório Rural e o Valor de Pi",
                    "content": "Um fazendeiro construiu um reservatório cilíndrico fechado de 2 m de diâmetro e 3 m de altura. Adotando pi = 3,14, quantos litros de água cabem nele e quantos metros quadrados de chapa metálica foram usados na construção?\nCuidado número 1: o texto deu DIÂMETRO = 2 m! Logo, o raio R = 1 m! Muita gente erra colocando 2 no lugar de R.\nVolume: V = pi * R² * h = 3,14 * 1² * 3 = 9,42 m³. Multiplicando por 1.000, cabem 9.420 litros.\nÁrea Total de chapa (fechado): At = 2 * pi * R * h + 2 * pi * R² = 2 * 3,14 * 1 * 3 + 2 * 3,14 * 1² = 18,84 + 6,28 = 25,12 m²."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Diâmetro vs. Raio e Aproximação de Pi",
                    "content": "No ENEM, quase sempre a largura de uma lata ou reservatório é informada pelo DIÂMETRO, porque no mundo real é muito mais fácil medir de ponta a ponta com a trena do que achar o centro exato do círculo! Nunca use o diâmetro direto na fórmula: divida por 2 imediatamente e escreva 'R = ...' bem grande no rascunho. Além disso, use EXATAMENTE o valor de pi que a questão mandar (às vezes é 3, às vezes 3,1, às vezes 3,14, ou deixe em função de pi)."
                },
                {
                    "type": "quote",
                    "content": "Na geometria das embalagens, a altura soma devagar, mas o raio multiplica ao quadrado.",
                    "author": "Aula de Cilindros — Curso ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-27-piramides-cones-fator-um-terco",
            "number": 27,
            "title": "27. Pirâmides e Cones: Os Sólidos de Ponta e o Fator 1/3",
            "epigraph": {
                "text": "Todo sólido que nasce numa base e afunila até uma única ponta perde dois terços do caminho: seu volume é exatamente um terço do prisma ou cilindro irmão.",
                "author": "A Lei do Fator 1/3"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Por que os sólidos com ponta têm volume igual a 1/3?"
                },
                {
                    "type": "paragraph",
                    "content": "Olá, pessoal! Hoje vamos estudar os dois sólidos mais elegantes da Geometria Espacial: as pirâmides (que têm base poligonal, como as pirâmides do Egito) e os cones (que têm base circular, como o chapéu de palhaço e a casquinha de sorvete). O que ambos têm em comum? Ambos nascem de uma base plana e vão afinando suavemente até terminar num único ponto lá no alto, chamado vértice."
                },
                {
                    "type": "paragraph",
                    "content": "Agora pense comigo numa experiência clássica: pegue um copo cilíndrico e um copo cônico de mesma base e mesma altura. Encha o cone de água até a boca e despeje no cilindro: enche só um terço! Repita três vezes e o cilindro enche até a borda sem sobrar gota! Eis a regra dos sólidos com ponta: Volume = (1/3) * Área da Base * Altura. Na pirâmide, V = (1/3) * Ab * h. No cone, V = (1/3) * pi * R² * h."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Pirâmides regulares: nunca confunda os três segmentos!"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui, porque esta dúvida trava 80% dos alunos! Numa pirâmide regular (base quadrada, por exemplo), três medidas formam um triângulo retângulo interno fundamental: 1) a altura da pirâmide (h), que desce do bico até o centro da base a 90 graus; 2) o apótema da base (ab), distância no chão do centro até o meio de um lado (no quadrado de lado L, vale L/2); e 3) o apótema da pirâmide (ap), altura inclinada da face triangular lateral. Pelo Teorema de Pitágoras: ap² = h² + ab²."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: A Tenda Piramidal",
                    "content": "Uma barraca tem formato de pirâmide regular de base quadrada com lado L = 6 m e altura h = 4 m. Calcule seu volume e a área total de lona lateral (sem o chão).\nPasso 1 (Volume): Área da base quadrada Ab = 6² = 36 m². Volume V = (1/3) * 36 * 4 = 12 * 4 = 48 m³.\nPasso 2 (Apótema da pirâmide para achar a área das faces): O apótema da base vale metade do lado, então ab = 6/2 = 3 m. A altura é h = 4 m. Pelo triângulo mágico 3-4-5 (Pitágoras: ap² = 4² + 3² = 25), o apótema da pirâmide mede ap = 5 m!\nPasso 3 (Área Lateral): Cada uma das 4 faces é um triângulo de base 6 m e altura 5 m. Área de 1 face = (6 * 5)/2 = 15 m². Como são 4 faces, Área Lateral = 4 * 15 = 60 m²!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Cone Reto, a Geratriz e a Fatia de Pizza"
                },
                {
                    "type": "paragraph",
                    "content": "No cone circular reto, o triângulo retângulo interno é ainda mais limpo: os catetos são a altura (h) e o raio da base (R), e a hipotenusa é a rampa inclinada da lateral, chamada geratriz (g). Portanto, Pitágoras no cone é sempre: g² = h² + R². E qual é a área daquela 'fatia de pizza' que forma a lateral do cone quando o abrimos na mesa? A fórmula é linda e curtinha: Área Lateral = pi * R * g. Somando a base circular, temos Área Total = pi * R * g + pi * R²."
                },
                {
                    "type": "paragraph",
                    "content": "E se uma questão do ENEM perguntar qual é o ângulo central (em graus) da fatia de pizza ao planificar o cone? Veja o raciocínio proporcional: o arco da fatia de pizza tem de abraçar exatamente a circunferência da base do cone (2 * pi * R), enquanto a pizza inteira de raio g teria circunferência 2 * pi * g. Fazendo regra de três com 360 graus, os '2*pi' cortam e sobra: ângulo = (360° * R) / g. Por exemplo, se g = 2R (o famoso cone equilátero, cuja secção central é um triângulo equilátero), o ângulo da planificação é 360° / 2 = 180°, exatamente meio círculo!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Troncos de Cone e Pirâmide: o atalho da semelhança (nível 800+)"
                },
                {
                    "type": "paragraph",
                    "content": "Chegamos ao tópico que separa os candidatos de 650 pontos dos candidatos de 800+ no ENEM: o tronco de cone (pense num balde, num abajur ou num copo descartável) e o tronco de pirâmide. Quando cortamos a ponta de um cone ou pirâmide por um plano paralelo à base, sobra uma pontinha menor em cima e um tronco embaixo. Você até pode decorar a fórmula gigante do tronco de cone: V = (pi * h / 3) * (R² + R*r + r²). Mas existe um caminho mil vezes mais inteligente, que funciona para pirâmides, cones e até níveis de líquido em taças cônicas: a Razão de Semelhança!"
                },
                {
                    "type": "paragraph",
                    "content": "Guarde esta lei universal de proporção entre a pirâmide pequena (a ponta retirada) e a pirâmide grande (inteira): se todas as medidas lineares (altura, raio, aresta) forem multiplicadas por uma razão k = h_pequeno / H_grande, então: as áreas ficam multiplicadas por k², e os VOLUMES ficam multiplicados por k³! Por exemplo, se você encher uma taça cônica só até a METADE da altura (k = 1/2), o volume de líquido lá dentro NÃO é metade da taça! É (1/2)³ = 1/8 do volume total! Os outros 7/8 ficam vazios no tronco superior!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: O Copo Cônico e o Nível da Água (Clássica ENEM)",
                    "content": "Um reservatório em forma de cone invertido (ponta para baixo) tem capacidade total de 270 litros e altura de 3 metros. Se enchermos esse reservatório até a altura de 2 metros, quantos litros de água haverá lá dentro?\nVeja como a semelhança resolve em 3 linhas sem usar nenhuma fórmula de tronco:\nPasso 1: Ache a razão linear k entre o cone cheio de água (altura 2 m) e o cone total (altura 3 m): k = 2/3.\nPasso 2: Eleve k ao cubo para achar a razão entre os volumes: V_água / V_total = (2/3)³ = 8/27.\nPasso 3: Calcule o volume de água: V_água = (8/27) * 270 = 8 * 10 = 80 litros!\nE se perguntassem quanto falta para encher (volume do tronco vazio)? 270 - 80 = 190 litros!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: A Ponta para Cima vs. Ponta para Baixo",
                    "content": "Muita atenção na leitura! Se o cone está com a ponta para BAIXO (como uma taça ou funil), a água lá dentro forma um cone pequeno semelhante ao grande, então V_água = k³ * V_total direto. Mas se o balde está com a ponta cortada para baixo (base menor embaixo) ou o cone está com a ponta para CIMA e a água enche a parte de baixo, o que forma o cone semelhante é a parte VAZIA de cima, e a água ocupa o TRONCO (V_total - V_vazio)! Desenhe sempre antes de aplicar k³."
                },
                {
                    "type": "quote",
                    "content": "Em qualquer cone ou pirâmide, dobrar a altura multiplica o volume por oito; é a cúbica mostrando quem manda na terceira dimensão.",
                    "author": "Caderno de Ouro ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "mat-curso-cap-28-esferas-solidos-compostos",
            "number": 28,
            "title": "28. Esferas e Sólidos Compostos: Bolas, Cúpulas e Deslocamento de Líquidos",
            "epigraph": {
                "text": "Se a esfera é a forma mais perfeita da natureza para guardar volume gastando pouca casca, o princípio de Arquimedes é o jeito mais genial de medir qualquer sólido mergulhando-o na água.",
                "author": "Fechamento da Geometria Espacial"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Esfera: beleza simétrica e economia da natureza"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos ao último capítulo do nosso módulo de Geometria Espacial, e ele é simplesmente brilhante. Hoje vamos dominar a esfera (bolas de esporte, gotas, planetas, cúpulas de planetários, tanques de gás esféricos) e aprender a lidar com sólidos compostos e com a subida do nível da água quando mergulhamos objetos em recipientes. Ao contrário dos poliedros, do cilindro e do cone, a esfera não pode ser planificada de maneira exata sem esticar ou rasgar — é por isso que todo mapa-múndi plano distorce os continentes!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Área e Volume da Esfera: duas fórmulas para tatuar na mente"
                },
                {
                    "type": "paragraph",
                    "content": "Na esfera de raio R, tudo depende apenas de R. A área da superfície esférica (a casca da laranja) equivale a quatro círculos máximos: Área = 4 * pi * R². Já o volume é V = (4/3) * pi * R³. Dica mnemônica para não trocar: Área tem unidade quadrada (R² e 4 na frente); Volume tem unidade cúbica (R³ e 4/3). Numa semiesfera (metade de esfera), o volume cai pela metade: V_semi = (2/3) * pi * R³. Cuidado com a área da semiesfera: a casca curva vale 2 * pi * R², mas se for maciça e fechada embaixo, some o círculo do corte (+ pi * R²), dando 3 * pi * R²!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fuso e Cunha Esférica: os gomos da mexerica"
                },
                {
                    "type": "paragraph",
                    "content": "E se o ENEM pedir a área da casca ou o volume de apenas um 'gomo' da esfera, formado por um ângulo alfa no centro? Não decore fórmula nova! O fuso esférico (a casca do gomo) e a cunha esférica (o recheio do gomo) são resolvidos por uma simples regra de três com 360 graus (a volta completa)! Se 360° correspondem à área total 4*pi*R², um ângulo de 60° (que é 1/6 de 360°) terá área igual a 1/6 de 4*pi*R² e volume igual a 1/6 de (4/3)*pi*R³. Simples assim!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sólidos Compostos: o método do quebra-cabeça"
                },
                {
                    "type": "paragraph",
                    "content": "No mundo real — e nas questões contextualizadas do ENEM — os objetos quase nunca são um sólido isolado. Pense numa cápsula de remédio, num silo de grãos na fazenda, numa taça de sorvete ou numa garrafa de design moderno. Como calculamos o volume de um sólido composto? Quebrando-o em peças conhecidas! Uma cápsula farmacêutica, por exemplo, é formada por um cilindro no meio e duas semiesferas idênticas nas duas pontas. Juntando as duas semiesferas, você ganha UMA esfera inteira! Então o volume da cápsula é V_cilindro + V_esfera. Já um silo de cereais com corpo cilíndrico e telhado cônico tem volume igual a V_cilindro + V_cone."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: A Taça de Sorvete que Transborda?",
                    "content": "Um cone de biscoito tem raio da boca igual a 3 cm e altura de 12 cm. Coloca-se dentro dele uma bola perfeitamente esférica de sorvete de raio 3 cm. Se o sorvete derreter completamente dentro do cone, ele vai transbordar? (Deixe em função de pi).\nPasso 1: Volume da casquinha cônica = (1/3) * pi * R² * h = (1/3) * pi * 3² * 12 = (1/3) * pi * 9 * 12 = 36 * pi cm³.\nPasso 2: Volume da bola de sorvete = (4/3) * pi * R³ = (4/3) * pi * 3³ = (4/3) * pi * 27 = 36 * pi cm³!\nResposta surpreendente: deu EXATAMENTE igual (36*pi cm³)! O sorvete derretido enche a casquinha até a borda sem derramar uma única gota!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Princípio de Arquimedes: deslocamento de água e subida de nível"
                },
                {
                    "type": "paragraph",
                    "content": "Preste muita atenção agora a um dos modelos de questão mais amados pela banca do ENEM nos últimos anos. Imagine um aquário retangular ou um copo cilíndrico parcialmente cheio de água. Você pega uma pedra irregular, um cubo de metal ou três bolinhas de gude esféricas e mergulha totalmente lá dentro (sem que a água transborde). O que acontece com o nível da água? Ele sobe uma altura delta_h!"
                },
                {
                    "type": "paragraph",
                    "content": "Qual é a mágica matemática por trás disso? Pelo Princípio de Arquimedes, o volume de água deslocada para cima é exatamente igual ao volume total dos objetos que ficaram submersos! E qual é a forma dessa 'fatia' nova de água que subiu? Ela tem o formato exato da base do recipiente (seja retangular ou circular) multiplicada pela variação de altura delta_h! Portanto, grave esta igualdade de ouro: Volume Submerso = Área da Base do Recipiente * delta_h."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: As Bolinhas de Aço no Cilindro",
                    "content": "Um recipiente cilíndrico de raio da base 6 cm contém água até a altura de 10 cm. Mergulham-se nele 3 esferas maciças idênticas de raio 2 cm, que ficam totalmente submersas. Quanto centímetros o nível da água sobe?\nPasso 1: Volume das 3 esferas = 3 * (4/3) * pi * R³ = 4 * pi * 2³ = 4 * pi * 8 = 32 * pi cm³. (Repare como o 3 cortou com o 3!)\nPasso 2: O volume deslocado forma um 'disco' cilíndrico extra no recipiente de raio 6 cm e altura delta_h: V_deslocado = pi * 6² * delta_h = 36 * pi * delta_h.\nPasso 3: Iguale os dois volumes! 36 * pi * delta_h = 32 * pi. Cortando pi dos dois lados: delta_h = 32 / 36 = 8 / 9 cm (aproximadamente 0,89 cm). Se o copo tiver pelo menos 11 cm de altura, nada transborda!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Quando o Recipiente Já Está Quase Cheio!",
                    "content": "Cuidado extremo quando o problema pergunta 'quantos litros de água TRANSBORDARAM?'. Nesse caso, primeiro a água sobe até a borda do recipiente (preenchendo o volume vazio inicial), e só o excedente do volume submerso é que cai para fora! Volume transbordado = Volume do objeto submerso - Volume vazio inicial do recipiente. Nunca erre isso!"
                },
                {
                    "type": "paragraph",
                    "content": "Parabéns! Ao dominar estes cinco capítulos, você percorreu toda a Geometria Espacial cobrada no ENEM: da visão espacial e planificações até os prismas, cilindros, pirâmides, cones, troncos, esferas e deslocamentos de líquidos. Pratique fazendo desenhos ao lado de cada questão, respeitando as unidades e conferindo se o sólido tem tampa ou não. Com esse olhar treinado, Geometria Espacial deixa de ser um bicho de sete cabeças e vira sua fonte mais confiável de pontos rumo aos 800+!"
                },
                {
                    "type": "quote",
                    "content": "Todo sólido submerso confessa seu volume fazendo o nível da água subir; na matemática, até uma pedra irregular pode ser medida com precisão perfeita.",
                    "author": "Encerramento do Módulo 6 — Geometria Espacial"
                }
            ],
            "quiz": []
        }
    ]
