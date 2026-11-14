# -*- coding: utf-8 -*-
"""Curso de Ciências da Natureza ENEM - Módulo 7: Química Geral e Inorgânica (Capítulos 32 a 37)"""


def get_chapters():
    return [
        {
            "id": "nat-cap-32-estrutura-atomica",
            "number": 32,
            "title": "32. Estrutura da Matéria: Modelos Atômicos, Partículas Subatômicas e Isótopos",
            "epigraph": {
                "text": "Tudo o que você toca, respira e enxerga nasce da dança invisível entre um núcleo minúsculo e elétrons que saltam como notas musicais em camadas de energia.",
                "author": "Aula Inaugural de Química Geral"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas ao Coração da Matéria: Do Filósofo ao Laboratório"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao nosso módulo de Química Geral e Inorgânica. Pense comigo: olhe para a tela do seu celular, para um copo de água e para o ar que entra nos seus pulmões agora. Parece impossível que coisas tão diferentes sejam feitas dos mesmos tijolinhos básicos, não é? Pois é exatamente essa a beleza da Química! Hoje vamos viajar para dentro do átomo, entendendo como a humanidade descobriu sua arquitetura e como o ENEM cobra partículas subatômicas, íons e isótopos."
                },
                {
                    "type": "paragraph",
                    "content": "Nossa história científica começa no início do século XIX com John Dalton. Em 1808, ele propôs o primeiro modelo atômico com base experimental, conhecido como modelo da bola de bilhar. Para Dalton, o átomo seria uma esfera maciça, homogênea, indivisível e indestrutível. Átomos de um mesmo elemento teriam a mesma massa e o mesmo tamanho, e as reações químicas seriam apenas o rearranjo dessas bolinhas sem criar nem destruir matéria."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Thomson, Rutherford e a Descoberta do Grande Vazio Atômico"
                },
                {
                    "type": "paragraph",
                    "content": "Quase cem anos depois, em 1897, Joseph John Thomson fez experimentos com tubos de raios catódicos e provou que Dalton estava incompleto: existiam partículas negativas ainda menores dentro do átomo, os elétrons! Como a matéria no dia a dia é eletricamente neutra, Thomson concluiu que o átomo não era indivisível. Surgiu o famoso modelo do pudim de passas: uma esfera gelatinosa positiva na qual os elétrons negativos ficavam incrustados, equilibrando as cargas."
                },
                {
                    "type": "paragraph",
                    "content": "Em 1911, Ernest Rutherford preparou um experimento brilhante para testar o pudim de passas: bombardeou uma finíssima lâmina de ouro com partículas alfa positivas. Se o átomo fosse um pudim maciço, todas atravessariam quase sem desvio. Porém, a imensa maioria passou direto como se não houvesse nada ali, poucas desviaram e cerca de 1 em cada 20 mil bateu e voltou! Rutherford concluiu que o átomo é quase todo espaço vazio, propondo o modelo planetário: no centro há um núcleo minúsculo, muito denso e positivo, e ao redor, numa imensa eletrosfera, giram os elétrons — como uma ervilha no centro de um estádio inteiro."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Bohr, os Saltos Quânticos e o Brilho dos Fogos de Artifício"
                },
                {
                    "type": "paragraph",
                    "content": "Havia um problema no modelo de Rutherford: pela Física Clássica, um elétron girando em torno do núcleo perderia energia em forma de luz e cairia sobre o núcleo em uma fração de segundo. Em 1913, Niels Bohr resolveu o enigma trazendo a Física Quântica. Ele propôs que os elétrons só podem girar em órbitas circulares permitidas, chamadas camadas ou níveis de energia estacionários, sem perder energia enquanto permanecem nelas."
                },
                {
                    "type": "paragraph",
                    "content": "Veja que sacada genial de Bohr que o ENEM adora cobrar: quando um átomo recebe energia do calor ou da eletricidade, um elétron dá um salto quântico para uma camada mais externa e energética. Como esse estado excitado é instável, o elétron retorna rapidamente para sua camada original liberando exatamente a diferença de energia na forma de um fóton de luz colorida! É por isso que fogos de artifício ficam verdes com bário, vermelhos com estrôncio e amarelos com sódio, e é também assim que funcionam lâmpadas de vapor de sódio e muitos LEDs."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Evolução dos Modelos Atômicos",
                    "content": "Dalton (1808): bola de bilhar (maciço, indivisível, neutro).\nThomson (1897): pudim de passas (divisível, descobre o elétron).\nRutherford (1911): planetário (núcleo pequeno, denso e positivo + eletrosfera vazia).\nBohr (1913): níveis quantizados (camadas de energia + saltos quânticos explicam emissão de luz)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Partículas Subatômicas, Número Atômico (Z) e Número de Massa (A)"
                },
                {
                    "type": "paragraph",
                    "content": "Com a descoberta do nêutron por James Chadwick em 1932, completamos o trio fundamental. No núcleo moram os prótons (carga +1, massa relativa 1) e os nêutrons (carga zero, massa relativa 1), que estabilizam o núcleo contra a repulsão dos prótons. Na eletrosfera giram os elétrons (carga -1, massa cerca de 1.836 vezes menor que a do próton, desprezível no cálculo da massa). A identidade do elemento é dada pelo Número Atômico (Z = prótons), e a soma das partículas pesadas do núcleo dá o Número de Massa (A = Z + N), escrito acima do símbolo enquanto Z vem abaixo."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Íons (Cátions e Ânions) e Semelhanças Atômicas"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque é aqui que a maioria cai! Em um átomo eletricamente neutro, o número de prótons é igual ao de elétrons. Quando o átomo participa de reações, ele NUNCA altera o núcleo; ele só ganha ou perde elétrons na eletrosfera, transformando-se em um íon. Se o átomo PERDE elétrons (cargas negativas), sobram prótons positivos e ele vira um cátion, como o Na+ ou o Ca2+. Se ele GANHA elétrons, fica com excesso negativo e vira um ânion, como o Cl- ou o O2-."
                },
                {
                    "type": "paragraph",
                    "content": "Para fechar com chave de ouro, memorize as três semelhanças atômicas usando a última consoante de cada palavra! IsótoPos têm o mesmo número de Prótons (Z), portanto pertencem ao mesmo elemento químico, como o carbono-12 e o carbono-14 usados na datação de fósseis, ou o prótio, deutério e trítio do hidrogênio. IsóbAros têm o mesmo número de mAssa (A). IsótoNos têm o mesmo número de Nêutrons (N = A - Z). E espécies isoeletrônicas possuem a mesma quantidade de elétrons."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Íons, Massas e Isótopos",
                    "content": "Enunciado: Considere um átomo X com número de massa 40 e 20 prótons, e um íon Y2+ que possui 18 elétrons e 22 nêutrons. Qual é a relação entre X e Y?\n\nResolução:\n1. Para o átomo X: Z = 20 prótons e A = 40. Logo, N = 40 - 20 = 20 nêutrons.\n2. Para o íon Y2+: a carga +2 mostra que ele perdeu 2 elétrons. Se ficou com 18 elétrons, no estado neutro tinha 18 + 2 = 20 elétrons, logo seu número de prótons é Z = 20!\n3. Calculando a massa de Y: A = Z + N = 20 + 22 = 42.\n4. Comparando X (A=40, Z=20, N=20) e Y (A=42, Z=20, N=22): ambos possuem o mesmo Z = 20! Portanto, X e Y são ISÓTOPOS do mesmo elemento químico (cálcio)."
                },
                {
                    "type": "quote",
                    "content": "Mexer nos elétrons muda a carga e as ligações do átomo; mexer nos prótons muda quem o átomo é no Universo.",
                    "author": "Regra de Ouro da Estrutura Atômica"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-33-tabela-periodica",
            "number": 33,
            "title": "33. Tabela Periódica: Organização, Famílias, Períodos e Propriedades Periódicas",
            "epigraph": {
                "text": "A Tabela Periódica não é uma lista para decorar: é um mapa de forças onde distância do núcleo e atração dos prótons explicam o comportamento de toda a matéria.",
                "author": "Aula de Periodicidade Química"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Mapa do Tesouro da Química: Como Ler a Tabela"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Vamos descomplicar hoje um dos maiores ícones da Ciência: a Tabela Periódica. Muita gente acha que precisa decorar todos os 118 elementos, mas no ENEM os dados atômicos são fornecidos; o que a prova testa é ler a posição e prever propriedades! Enquanto Dmitri Mendeleev (1869) organizou os elementos pela massa atômica deixando espaços para futuras descobertas, Henry Moseley (1913) mostrou que a identidade periódica real está no Número Atômico (Z), gerando a tabela atual em ordem crescente de Z."
                },
                {
                    "type": "paragraph",
                    "content": "A leitura funciona como uma batalha naval com dois eixos claríssimos. As 7 linhas horizontais são os PERÍODOS: o número do período indica exatamente quantas camadas eletrônicas ocupadas o átomo tem. Um elemento do 3º período tem 3 camadas (K, L e M). Já as 18 colunas verticais são as FAMÍLIAS ou GRUPOS: elementos da mesma coluna têm o mesmo número de elétrons na camada de valência e, por isso, exibem propriedades químicas muito parecidas."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Metais, Ametais, Gases Nobres e as Principais Famílias"
                },
                {
                    "type": "paragraph",
                    "content": "Cerca de 80% da tabela é formada por METAIS, que ocupam o lado esquerdo e o centro. Metais têm brilho característico, conduzem muito bem calor e eletricidade, são maleáveis (viram chapas) e dúcteis (viram fios) e têm grande tendência a perder elétrons, formando cátions. À direita, acima de uma escadinha imaginária, ficam os AMETAIS (ou não metais): opacos, isolantes térmicos e elétricos (com exceção do carbono grafite) e ávidos por ganhar ou compartilhar elétrons."
                },
                {
                    "type": "paragraph",
                    "content": "Na coluna 18, no extremo direito, moram os GASES NOBRES (He, Ne, Ar, Kr, Xe, Rn), famosos por sua estabilidade e baixíssima reatividade. Já o Hidrogênio, lá no topo esquerdo, é um cidadão sem família fixa: tem 1 elétron como o grupo 1, mas é um gás ametal! Conheça também os nomes das famílias mais cobradas: Grupo 1 (Metais Alcalinos, super-reativos com água), Grupo 2 (Metais Alcalino-terrosos), Grupo 16 (Calcogênios, família do oxigênio) e Grupo 17 (Halogênios, formadores de sais como flúor e cloro)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Distribuição Eletrônica Básica: Encontrando o Endereço do Átomo"
                },
                {
                    "type": "paragraph",
                    "content": "Como saber em qual período e família um átomo mora olhando apenas para seu Z? Pela distribuição eletrônica! As camadas K, L, M, N, O, P e Q comportam até 2, 8, 18, 32, 32, 18 e 8 elétrons, e o diagrama de Linus Pauling ordena os subníveis em 1s², 2s², 2p⁶, 3s², 3p⁶, 4s², 3d¹⁰, 4p⁶... No cloro (Z = 17), temos 1s² 2s² 2p⁶ 3s² 3p⁵: são 2 elétrons na camada 1, 8 na camada 2 e 7 na camada 3. Como o maior nível ocupado é o 3, ele está no 3º período; e com 7 elétrons na valência (subnível p), somamos 12 + 5 e achamos o Grupo 17 (Halogênios)!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Atalho dos Representativos",
                    "content": "Para elementos representativos (subnível mais energético s ou p):\n- Termina em ns¹ → Grupo 1 (Alcalinos) | ns² → Grupo 2 (Alcalino-terrosos).\n- Termina em np¹ a np⁶ → Some 12 ao expoente do p para achar a coluna moderna! Exemplo: 3p⁵ → 12 + 5 = Grupo 17.\n- O maior número antes da letra (n) entrega na hora o Período!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Propriedades Periódicas: A Guerra entre Camadas e Carga Nuclear"
                },
                {
                    "type": "paragraph",
                    "content": "Agora vem a parte mais bonita da aula! Nunca tente decorar setas na tabela sem entender o porquê físico delas. Tudo nas propriedades periódicas nasce de uma disputa entre dois fatores: o número de camadas (que afasta os elétrons externos do núcleo) e o número de prótons no núcleo (que puxa os elétrons para dentro com força elétrica)."
                },
                {
                    "type": "paragraph",
                    "content": "Comecemos pelo RAIO ATÔMICO, o tamanho do átomo. Descendo na mesma família, o átomo ganha uma camada nova a cada período, logo o raio AUMENTA de cima para baixo. No mesmo período, todos têm as mesmas camadas, mas da esquerda para a direita cresce o número de prótons no núcleo, puxando a nuvem eletrônica com mais força e encolhendo o átomo. Logo, o raio atômico cresce PARA BAIXO e PARA A ESQUERDA! E nos íons: cátions perdem elétrons e ficam MENORES que o átomo neutro, enquanto ânions ganham elétrons que se repelem e ficam MAIORES."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Energia de Ionização e Eletronegatividade"
                },
                {
                    "type": "paragraph",
                    "content": "A ENERGIA DE IONIZAÇÃO é a energia mínima necessária para arrancar um elétron de um átomo isolado no estado gasoso. Pense comigo: se o átomo é pequenininho, o elétron está colado no núcleo positivo e sofre uma atração brutal — dá um trabalho danado arrancar! Já num átomo grandão, o elétron de fora está longe e blindado pelas camadas internas, saindo fácil. Por isso, a Energia de Ionização cresce no sentido oposto ao raio: PARA CIMA e PARA A DIREITA!"
                },
                {
                    "type": "paragraph",
                    "content": "Já a ELETRONEGATIVIDADE mede a força com que um átomo atrai o par de elétrons em uma ligação química. Como gases nobres em geral não formam ligações, eles ficam fora da fila tradicional. Quanto menor o átomo e maior sua carga nuclear efetiva, maior seu poder de puxar elétrons alheios. Portanto, a eletronegatividade também cresce PARA CIMA e PARA A DIREITA até o Flúor! Memorize a fila famosa de Pauling: F > O > N > Cl > Br > I > S > C > P > H (a clássica frase: 'Fui Ontem No Clube, Briguei I Saí Correndo Para o Hospital')."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Prevendo Propriedades no ENEM",
                    "content": "Enunciado: Considere os átomos neutros sódio (Z = 11), enxofre (Z = 16) e potássio (Z = 19). Ordene-os em ordem crescente de raio atômico e identifique o de maior energia de ionização.\n\nResolução:\n1. Distribuição: Na (Z=11) → 2, 8, 1 (3º período, Grupo 1). S (Z=16) → 2, 8, 6 (3º período, Grupo 16). K (Z=19) → 2, 8, 8, 1 (4º período, Grupo 1).\n2. Comparando os tamanhos: S e Na têm 3 camadas, mas S tem 16 prótons puxando contra 11 do Na, logo S é menor que Na. Já o K tem 4 camadas, sendo maior que o Na.\n3. Ordem crescente de raio atômico: S < Na < K.\n4. Energia de ionização cresce para cima e para a direita (oposto do raio): o menor e mais à direita é o enxofre (S), logo S possui a maior energia de ionização."
                },
                {
                    "type": "quote",
                    "content": "Raio atômico cresce para baixo e para a esquerda; energia de ionização e eletronegatividade crescem no sentido oposto: para cima e para a direita.",
                    "author": "Bússola das Propriedades Periódicas"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-34-ligacoes-polaridade-forcas",
            "number": 34,
            "title": "34. Ligações Químicas, Polaridade e Forças Intermoleculares: Por Que Água e Óleo Não se Misturam",
            "epigraph": {
                "text": "As ligações químicas constroem as moléculas; as forças intermoleculares decidem quem ferve primeiro, quem se dissolve e por que a vida existe em água líquida.",
                "author": "Aula de Interações Moleculares"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Busca pela Estabilidade e os Três Tipos de Ligação Química"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Hoje vamos responder a uma das perguntas mais famosas da cozinha e do ENEM: por que água e óleo não se misturam, mas o detergente lava a panela engordurada com tanta facilidade? Para entender isso de verdade, precisamos construir a escada completa: primeiro como os átomos se unem por dentro (ligações químicas), depois a forma e a polaridade das moléculas, e por fim como as moléculas conversam entre si (forças intermoleculares)."
                },
                {
                    "type": "paragraph",
                    "content": "Na natureza, os átomos buscam menor energia e estabilidade imitando os gases nobres. Pela Regra do Octeto, a maioria alcança estabilidade com 8 elétrons na camada de valência — exceto átomos pequenos como H e Li, que estabilizam com 2 elétrons, além de exceções como Boro e Berílio. Para isso, existem três caminhos."
                },
                {
                    "type": "paragraph",
                    "content": "O primeiro é a LIGAÇÃO IÔNICA, típica entre metal (que quer doar elétrons) e ametal (que quer receber elétrons). No sal de cozinha (NaCl), o sódio transfere definitivamente 1 elétron para o cloro, formando o cátion Na+ e o ânion Cl-. Essas cargas opostas se atraem com força absurda formando um retículo cristalino organizado. Por isso, compostos iônicos são sólidos à temperatura ambiente, têm pontos de fusão e ebulição altíssimos, são duros e quebradiços, e só conduzem eletricidade quando derretidos (fundidos) ou dissolvidos em água, pois aí seus íons ficam livres para se mover!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Ligação Covalente e Ligação Metálica: Compartilhar ou Navegar em Mar de Elétrons"
                },
                {
                    "type": "paragraph",
                    "content": "Quando dois ametais (ou hidrogênio com ametal) se encontram, ninguém quer perder elétrons! A solução é a LIGAÇÃO COVALENTE: eles compartilham pares de elétrons, formando moléculas discretas, com ligações simples, duplas, triplas ou coordenadas (dativas). Compostos moleculares costumam ter pontos de fusão e ebulição bem mais baixos que os iônicos (como água, oxigênio e açúcar) e, em regra, não conduzem corrente elétrica — salvo ácidos quando ionizam em água."
                },
                {
                    "type": "paragraph",
                    "content": "E quando metais se juntam apenas com outros metais, como no fio de cobre ou nas ligas metálicas? Nasce a LIGAÇÃO METÁLICA! Os átomos metálicos soltam seus elétrons de valência facilmente, formando um 'mar de elétrons' móveis que banha todos os cátions fixos. Essa nuvem livre explica por que os metais conduzem eletricidade e calor até no estado sólido e podem ser martelados em lâminas sem quebrar o cristal. Ligas metálicas como o aço (ferro + carbono), o bronze (cobre + estanho) e o latão (cobre + zinco) ajustam dureza e resistência à corrosão para aplicações industriais."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Geometria Molecular e Polaridade: O Segredo dos Vetores"
                },
                {
                    "type": "paragraph",
                    "content": "Depois que os átomos se ligam covalentemente, a molécula ganha um formato 3D definido pela repulsão entre os pares de elétrons ao redor do átomo central. Veja os cinco formatos essenciais: Linear (CO2 e HCl, ângulo de 180°), Angular (H2O, onde dois pares de elétrons livres empurram os hidrogênios para baixo!), Trigonal Plana (BF3, 120°), Piramidal (NH3, com um par livre no topo do nitrogênio empurrando as ligações) e Tetraédrica (CH4, 109,5°)."
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque é aqui que a maioria cai: ligação polar não significa automaticamente molécula polar! Cada ligação entre átomos diferentes gera um vetor puxando para o lado mais eletronegativo. Se os vetores se cancelarem por simetria, o momento dipolar resultante é nulo e a molécula é APOLAR. É o caso do gás carbônico (CO2): o oxigênio puxa para a direita e o outro oxigênio puxa com a mesma força para a esquerda em linha reta — empate técnico, molécula apolar! Já na água (H2O), como a geometria é angular, os dois puxões apontam inclinados para o oxigênio e se somam, tornando a água fortemente POLAR."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Teste Rápido de Polaridade",
                    "content": "Molécula binária de átomos iguais (O2, N2, Cl2) ou hidrocarbonetos (CxHy, como metano e gasolina): sempre APOLARES!\nPara moléculas com átomo central ligado a átomos periféricos iguais: se NÃO sobrar par de elétrons livres no átomo central (CO2, CH4, BF3), é simétrica e APOLAR. Se SOBRAR par livre no átomo central (H2O, NH3, SO2), entorta a simetria e fica POLAR!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Três Forças Intermoleculares e o Mistério da Água com Óleo"
                },
                {
                    "type": "paragraph",
                    "content": "Quando você ferve água na panela, você NÃO quebra as ligações covalentes O-H dentro da molécula (se quebrasse, sairia gás hidrogênio e oxigênio explosivos!). Você rompe apenas as forças INTERMOLECULARES, isto é, as atrações entre uma molécula inteira e sua vizinha. Existem três intensidades principais."
                },
                {
                    "type": "paragraph",
                    "content": "A mais fraca é o Dipolo Induzido (ou Forças de London), presente em todas as moléculas e única interação entre moléculas apolares como metano (CH4), CO2 e óleos vegetais. Ela surge de distorções momentâneas na nuvem eletrônica e cresce quando a massa molar ou a cadeia carbônica aumenta. A intermediária é o Dipolo Permanente (dipolo-dipolo), que ocorre entre moléculas polares como HCl e acetona, onde o polo positivo de uma atrai o polo negativo da outra."
                },
                {
                    "type": "paragraph",
                    "content": "A campeã de força entre moléculas neutras é a LIGAÇÃO DE HIDROGÊNIO (antiga ponte de hidrogênio). Ela acontece quando o Hidrogênio está ligado diretamente a um dos três elementos mais eletronegativos e pequenos: Flúor, Oxigênio ou Nitrogênio (o famoso trio FON!). Como o H fica quase sem nuvem eletrônica, cria um polo positivo fortíssimo que se agarra ao F, O ou N da molécula vizinha. É graças às ligações de hidrogênio que a água ferve a altos 100 °C enquanto o H2S é um gás fedorento, que insetos caminham sobre a tensão superficial da água e que as duas fitas do DNA se mantêm unidas."
                },
                {
                    "type": "paragraph",
                    "content": "Agora tudo se conecta na regra de ouro da solubilidade: 'semelhante dissolve semelhante'! Moléculas polares (como água e etanol, que fazem ligações de hidrogênio entre si) se misturam perfeitamente. Moléculas apolares (como óleo e gasolina) preferem interagir por dipolo induzido. Como as moléculas de água se atraem muito mais fortemente entre si do que pelo óleo apolar, elas simplesmente expulsam o óleo, formando duas fases separadas."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Como o Sabão Vence a Gordura",
                    "content": "Enunciado: Explique por que o sabão remove gordura usando água e compare os pontos de ebulição de propano (C3H8, 44 g/mol) e etanol (C2H6O, 46 g/mol).\n\nResolução:\n1. Sabão e Micelas: O sabão é anfifílico: sua cauda carbônica apolar se dissolve na gordura por dipolo induzido, e sua cabeça iônica/polar interage com a água. Várias moléculas cercam a gotícula formando uma micela, permitindo que a água carregue a sujeira!\n2. Pontos de ebulição: Embora tenham massas próximas, o propano é apolar (dipolo induzido fraco, ferve a -42 °C), enquanto o etanol possui grupo -OH e faz ligações de hidrogênio intensas, fervendo a 78 °C!"
                },
                {
                    "type": "quote",
                    "content": "Quem quebra água líquida em vapor vence ligações de hidrogênio; quem junta água e óleo precisa da ponte diplomática de uma micela de sabão.",
                    "author": "Síntese das Forças Intermoleculares"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-35-reacoes-balanceamento-leis",
            "number": 35,
            "title": "35. Reações Químicas: Classificação, Balanceamento e Leis Ponderais",
            "epigraph": {
                "text": "Na natureza nada se cria, nada se perde, tudo se transforma; os átomos apenas trocam de parceiros mantendo intacta a contabilidade da massa.",
                "author": "Inspirado em Antoine-Laurent de Lavoisier"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Que Muda Quando Ocorre uma Reação Química?"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Até aqui olhamos para os átomos isolados e para as ligações que formam substâncias. Hoje vamos colocá-las para agir! Quando você derrete um cubo de gelo, ocorre um fenômeno físico: as moléculas de H2O continuam idênticas. Mas quando um prego enferruja, uma fruta amadurece ou um comprimido efervescente borbulha no copo, temos uma REAÇÃO QUÍMICA: ligações antigas se rompem e novas ligações formam substâncias inéditas, reveladas por mudança de cor, liberação de gás, formação de sólido (precipitado) ou troca de calor."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Quatro Grandes Tipos de Reações Inorgânicas"
                },
                {
                    "type": "paragraph",
                    "content": "Para reconhecer qualquer equação no ENEM, observe quantos reagentes entram antes da seta e quantos produtos saem depois da seta. Na reação de SÍNTESE ou ADIÇÃO (A + B → AB), dois ou mais reagentes se juntam para formar um único produto, como na queima do magnésio (2 Mg + O2 → 2 MgO) ou na produção industrial da amônia (N2 + 3 H2 → 2 NH3)."
                },
                {
                    "type": "paragraph",
                    "content": "O caminho inverso é a ANÁLISE ou DECOMPOSIÇÃO (AB → A + B), quando uma substância única se quebra em duas ou mais. Ela ganha sobrenomes famosos conforme o agente que provoca a quebra: pirólise (pelo calor, como a calcinação do calcário CaCO3 → CaO + CO2), fotólise (pela luz, motivo pelo qual água oxigenada H2O2 vem em frasco escuro!) e eletrólise (pela corrente elétrica, usada para obter alumínio e gás hidrogênio)."
                },
                {
                    "type": "paragraph",
                    "content": "Na SIMPLES TROCA ou DESLOCAMENTO (A + BC → AC + B), uma substância simples 'toma o lugar' de outro elemento dentro de uma substância composta. Mas cuidado: o invasor precisa ser mais reativo que o elemento substituído! Metais muito reativos como zinco e ferro deslocam cobre do sulfato de cobre (Zn + CuSO4 → ZnSO4 + Cu) e liberam gás H2 em ácidos, enquanto metais nobres como ouro, prata e cobre não deslocam o hidrogênio de ácidos comuns como o HCl. Nos halogênios, a reatividade segue F > Cl > Br > I."
                },
                {
                    "type": "paragraph",
                    "content": "Por fim, na DUPLA TROCA (AB + CD → AD + CB), duas substâncias compostas trocam seus pares iônicos. Para a dupla troca acontecer de verdade em solução, precisa formar pelo menos um produto insolúvel que afunda (precipitado, como AgNO3 + NaCl → AgCl↓ + NaNO3), um gás que escapa (como calcário + ácido liberando CO2) ou água/eletrólito fraco (como na neutralização entre ácido e base)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Balanceamento por Tentativas e Noção de Oxirredução"
                },
                {
                    "type": "paragraph",
                    "content": "Toda equação química precisa ter exatamente a mesma quantidade de átomos de cada elemento antes e depois da seta — nunca mudando os índices pequenos das fórmulas, apenas ajustando os coeficientes grandes na frente delas! Para acertar de primeira no método das tentativas, siga a famosa sequência MACHO: balanceie primeiro Metais, depois Ametais, depois Carbono, em seguida Hidrogênio e deixe o Oxigênio por último."
                },
                {
                    "type": "paragraph",
                    "content": "Veja funcionando na combustão do propano: C3H8 + O2 → CO2 + H2O. Seguindo MACHO: não há metal nem outro ametal fora C, H e O. Começamos pelo Carbono: 3 à esquerda exigem 3 CO2 à direita. Depois Hidrogênio: 8 à esquerda exigem 4 H2O à direita (4 × 2 = 8). Agora contamos o Oxigênio à direita: 3 × 2 + 4 × 1 = 10 átomos! Logo, precisamos de 5 O2 à esquerda. Equação perfeita: C3H8 + 5 O2 → 3 CO2 + 4 H2O."
                },
                {
                    "type": "paragraph",
                    "content": "Muitas reações de síntese, combustão e simples troca também são reações de OXIRREDUÇÃO (redox), nas quais há transferência de elétrons e variação do Número de Oxidação (NOX). Quem perde elétrons sofre OXIDAÇÃO (seu NOX aumenta) e atua como agente redutor; quem ganha elétrons sofre REDUÇÃO (seu NOX diminui) e atua como agente oxidante. Pense na ferrugem: o ferro metálico (NOX 0) perde elétrons e oxida para Fe3+, enquanto o oxigênio do ar (NOX 0) ganha elétrons e reduz para O2-."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Regra Prática do NOX e Redox",
                    "content": "Substância simples (O2, Fe, H2) tem NOX = 0. Metais alcalinos (Grupo 1) sempre +1; alcalino-terrosos (Grupo 2) sempre +2; H ligado a ametal vale +1; O vale -2 (exceto peróxidos -1 e com F).\nMacete infalível: 'Oxidação Aumenta o NOX (perde elétrons); Redução Reduz o NOX (ganha elétrons)'."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Leis Ponderais: Lavoisier e Proust na Balança do ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "O balanceamento que acabamos de fazer existe por causa da Lei da Conservação das Massas, formulada por Lavoisier em 1785: em um sistema fechado, a soma das massas dos reagentes é rigorosamente igual à soma das massas dos produtos. Muita atenção à pegadinha clássica do ENEM: em sistema ABERTO, a balança pode parecer mentir! Se você queimar madeira ao ar livre, a cinza pesa menos porque CO2 e vapor de água escaparam para a atmosfera. Se você queimar palha de aço (ferro) aberta, a massa AUMENTA porque o ferro incorporou oxigênio do ar formando óxido de ferro!"
                },
                {
                    "type": "paragraph",
                    "content": "Já Joseph Proust estabeleceu a Lei das Proporções Definidas (ou Constantes): uma substância pura composta tem sempre a mesma proporção em massa entre seus elementos, e toda reação obedece a uma receita fixa. Se 3 g de carbono se combinam exatamente com 8 g de oxigênio formando 11 g de CO2, e você colocar 3 g de carbono com 10 g de oxigênio, não vão surgir 13 g de gás: 2 g de oxigênio ficarão sobrando sem reagir (reagente em excesso), produzindo os mesmos 11 g de CO2."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Lavoisier e Proust Juntos",
                    "content": "Enunciado: Na decomposição térmica do carbonato de cálcio (CaCO3 → CaO + CO2), aqueceram-se 100 g de CaCO3 em um cadinho aberto, restando ao final 56 g de sólido branco (CaO). Em um segundo experimento em recipiente fechado, usaram-se 250 g de CaCO3 puro. Qual massa de gás CO2 foi formada no segundo experimento?\n\nResolução:\n1. Pelo 1º experimento (Lavoisier): 100 g de CaCO3 geram 56 g de CaO + massa de CO2 que escapou. Logo, m(CO2) = 100 - 56 = 44 g.\n2. Pela Lei de Proust, a proporção é fixa: cada 100 g de CaCO3 produzem 44 g de CO2.\n3. No 2º experimento, usamos 250 g de CaCO3, que é 2,5 vezes maior que 100 g (250 / 100 = 2,5).\n4. Multiplicando o CO2 por 2,5: 44 g × 2,5 = 110 g de CO2 (e 56 × 2,5 = 140 g de CaO; somando 140 + 110 = 250 g, confirmando Lavoisier!)."
                },
                {
                    "type": "quote",
                    "content": "Quando a balança parece errar em uma reação química, quase sempre algum gás invisível entrou ou saiu do sistema aberto.",
                    "author": "Alerta de Prova das Leis Ponderais"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-36-solucoes-concentracao-diluicao",
            "number": 36,
            "title": "36. Soluções: Soluto, Solvente, Concentrações, Diluição e Solubilidade",
            "epigraph": {
                "text": "Do soro fisiológico na veia ao café passado pela manhã, dominar concentrações e diluições é saber dosar a química exata do cotidiano.",
                "author": "Aula de Físico-Química Aplicada"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Que É uma Solução? Soluto, Solvente e Limites de Dissolução"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Pense comigo na hora de preparar um suco ou tomar um remédio líquido. Quando você mistura uma colher de açúcar em um copo de água e mexe bem, o açúcar desaparece à vista e até ao microscópio comum, formando uma mistura homogênea de uma única fase. Na Química, toda mistura homogênea recebe o nome de SOLUÇÃO! Nela, quem se dissolve (em regra em menor quantidade) é o SOLUTO, e quem dissolve (em regra em maior quantidade) é o SOLVENTE — sendo a água o solvente universal para compostos iônicos e polares."
                },
                {
                    "type": "paragraph",
                    "content": "Vale uma distinção rápida que o ENEM adora: se as partículas dispersas forem um pouco maiores (entre 1 nm e 1.000 nm), como na gelatina, maionese, leite e fumaça, temos um COLOIDE (que espalha a luz no chamado Efeito Tyndall). Se forem maiores ainda e sedimentarem com o tempo, como água barrenta ou antibiótico em pó com água, temos uma SUSPENSÃO."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Coeficiente de Solubilidade e Curvas: Insaturada, Saturada e Supersaturada"
                },
                {
                    "type": "paragraph",
                    "content": "Existe um limite para quanto sal ou açúcar cabe na água antes de sobrar no fundo do copo! Esse limite máximo de soluto que se dissolve em uma quantidade padrão de solvente (geralmente 100 g de água) a uma dada temperatura é o COEFICIENTE DE SOLUBILIDADE (CS). Imagine que o CS de um sal a 20 °C seja 36 g em 100 g de água."
                },
                {
                    "type": "paragraph",
                    "content": "Se você colocar 20 g em 100 g de água a 20 °C, tudo dissolve e ainda cabe mais: solução INSATURADA. Se colocar 36 g, atingiu o limite exato: SATURADA. Se jogar 50 g a 20 °C, apenas 36 g dissolvem e 14 g caem no fundo (corpo de fundo), mas o líquido acima continua SATURADO! Agora, se aquecer para dissolver tudo e resfriar devagar sem agitar, pode reter mais de 36 g dissolvidos a 20 °C: é a solução SUPERSATURADA, extremamente instável."
                },
                {
                    "type": "paragraph",
                    "content": "Nos gráficos de curva de solubilidade, a maioria dos sais tem curva crescente com a temperatura (dissolução endotérmica: absorve calor para dissolver, como açúcar no chá quente). Porém, existem exceções exotérmicas cuja curva cai quando esquenta — e esse é sempre o caso dos GASES dissolvidos em líquidos! É por isso que o refrigerante perde o gás rapidamente quando esquenta e que o aquecimento térmico das águas de um rio reduz o oxigênio dissolvido, sufocando os peixes."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Quatro Grandes Unidades de Concentração"
                },
                {
                    "type": "paragraph",
                    "content": "Para dosar medicamentos, bebidas e poluentes, usamos quatro medidas de concentração que você precisa dominar com naturalidade. A primeira é a CONCENTRAÇÃO COMUM (C), que divide a massa do soluto em gramas pelo volume total da solução em litros: C = m / V (unidade em g/L). Se um litro de soro caseiro contém 20 g de açúcar, sua concentração de açúcar é 20 g/L."
                },
                {
                    "type": "paragraph",
                    "content": "A segunda é a CONCENTRAÇÃO MOLAR ou MOLARIDADE (M), que conta partículas em mols por litro de solução: M = n / V = m / (MM × V), onde MM é a massa molar do soluto em g/mol. Veja que sacada genial que economiza tempo na prova: como m / V é a própria concentração comum C, vale a ponte mágica C = M × MM! Para ir de g/L para mol/L, basta dividir pela massa molar."
                },
                {
                    "type": "paragraph",
                    "content": "A terceira é o TÍTULO ou PORCENTAGEM: título em massa divide massa do soluto pela massa total da solução (multiplicado por 100 dá % m/m). Já em rótulos de farmácia e bebidas, aparecem muito % m/v (gramas de soluto em 100 mL de solução, como no soro fisiológico 0,9%, que tem 0,9 g de NaCl em 100 mL, ou 9 g/L) e % v/v (mL de álcool em 100 mL de bebida, como um vinho de 12 °GL). Por fim, para quantidades minúsculas de poluentes, flúor na água ou metais pesados, usamos PARTES POR MILHÃO (ppm): 1 ppm significa 1 mg de soluto em cada 1 kg (ou 1 litro, em soluções aquosas diluídas) de solução!"
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Fórmulas Essenciais de Concentração",
                    "content": "Concentração Comum: C = m(g) / V(L) [g/L]\nMolaridade: M = n(mol) / V(L) = m / (MM · V) [mol/L]\nRelação Mágica: C = M · MM\nTítulo % m/v: massa(g) em 100 mL de solução\nppm (em água): mg de soluto por litro de solução (1 ppm = 1 mg/L)"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Diluição e Mistura de Soluções: A Conservação do Soluto"
                },
                {
                    "type": "paragraph",
                    "content": "Pense comigo: você prepara um copo de suco concentrado muito doce e resolve adicionar água pura até dobrar o volume. A concentração caiu pela metade, certo? Mas a quantidade de açúcar dentro do copo mudou? Claro que NÃO! Você só colocou solvente! Esse princípio físico simples gera a fórmula mais famosa de laboratório e farmácia: na DILUIÇÃO, a massa ou o número de mols do soluto antes e depois são idênticos, logo C1 · V1 = C2 · V2 (ou M1 · V1 = M2 · V2), onde V2 = V1 + V(água adicionada)."
                },
                {
                    "type": "paragraph",
                    "content": "E se em vez de água pura você misturar duas soluções diferentes do MESMO soluto (sem reação química), como um café forte com um café fraco? Basta somar a massa de soluto da primeira com a massa da segunda para achar a massa final no volume total (Vf = V1 + V2): Cf · Vf = C1 · V1 + C2 · V2. É uma média ponderada pelos volumes!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Diluição de Remédio e Conversão para Molaridade",
                    "content": "Enunciado: Uma ampola contém 20 mL de solução de cloreto de potássio (KCl, massa molar = 74,5 g/mol) na concentração de 149 g/L. Um enfermeiro transfere todo o conteúdo da ampola para um frasco e completa com água destilada até atingir o volume final de 500 mL. Qual será a concentração comum final em g/L e a molaridade final da solução preparada?\n\nResolução:\n1. Aplicando a diluição C1 · V1 = C2 · V2 (com ambos os volumes em mL, pois a unidade cancela):\n149 · 20 = C2 · 500\n2.980 = 500 · C2 → C2 = 2.980 / 500 = 5,96 g/L.\n(Veja o raciocínio lógico: o volume aumentou 25 vezes de 20 mL para 500 mL, logo a concentração caiu 25 vezes: 149 / 25 = 5,96 g/L!)\n2. Convertendo para molaridade com C = M · MM:\n5,96 = M · 74,5 → M = 5,96 / 74,5 = 0,08 mol/L.\n(Ou calculando antes: 149 g/L dividido por 74,5 g/mol dava 2,0 mol/L inicial; dividido por 25 dá os mesmos 0,08 mol/L!)"
                },
                {
                    "type": "quote",
                    "content": "Na diluição, entra apenas solvente: o volume cresce, a concentração cai na mesma proporção e o soluto permanece exatamente o mesmo.",
                    "author": "Princípio da Conservação do Soluto"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-37-funcoes-inorganicas-ph",
            "number": 37,
            "title": "37. Funções Inorgânicas: Ácidos, Bases, Sais, Óxidos e Escala de pH",
            "epigraph": {
                "text": "Entre o azedo do limão, o ardor do suco gástrico, o sabão que escorrega nas mãos e a calagem que ressuscita o solo, vivem as quatro grandes funções inorgânicas.",
                "author": "Aula de Química Inorgânica e Equilíbrio Iônico"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Quatro Famílias Inorgânicas Segundo Arrhenius"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos ao capítulo que fecha com chave de ouro nossa Química Geral e Inorgânica. Você já notou como milhares de substâncias diferentes apresentam comportamentos parecidos na cozinha, no corpo humano e na agricultura? Para organizar essa diversidade, Svante Arrhenius criou uma classificação brilhante baseada no que acontece quando colocamos essas substâncias em água."
                },
                {
                    "type": "paragraph",
                    "content": "Os ÁCIDOS são substâncias moleculares que, ao entrar em contato com a água, sofrem ionização e liberam como único cátion o íon H+ (que na água se junta formando o hidrônio, H3O+). Têm sabor azedo característico e conduzem corrente elétrica quando dissolvidos. Exemplos vitais no ENEM: ácido clorídrico (HCl, o suco gástrico do estômago), ácido sulfúrico (H2SO4, bateria de carro e chuva ácida), ácido carbônico (H2CO3, água com gás e refrigerante) e ácido acético (CH3COOH, vinagre)."
                },
                {
                    "type": "paragraph",
                    "content": "Sobre a força dos ácidos: entre os hidrácidos (sem oxigênio), apenas HCl, HBr e HI são fortes; HF é moderado e os demais como HCN e H2S são fracos. Já nos oxiácidos (com oxigênio), subtraia o número de oxigênios pelo de hidrogênios: dando 2 ou mais (como H2SO4: 4 - 2 = 2 e HNO3: 3 - 1 = 2), o ácido é forte; dando 1 é moderado; dando zero (como H2CO3 e H3BO3), é fraco!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Bases, Sais e o Mapa Completo dos Óxidos"
                },
                {
                    "type": "paragraph",
                    "content": "As BASES (ou hidróxidos) são compostos geralmente iônicos que, em água, sofrem dissociação liberando como único ânion a hidroxila (OH-). Têm sabor adstringente (aquele que 'amarra' a boca como banana verde) e deixam a pele escorregadia ao toque porque reagem com a gordura formando sabão! As bases dos metais alcalinos (NaOH, soda cáustica; KOH) são fortes e muito solúveis; as dos alcalino-terrosos (Ca(OH)2, cal hidratada; Ba(OH)2) são fortes mas pouco solúveis — com destaque para o Mg(OH)2 (leite de magnésia) que é fraco e quase insolúvel; e as demais, como Al(OH)3 e NH4OH (amônia), são fracas."
                },
                {
                    "type": "paragraph",
                    "content": "Os SAIS são compostos iônicos que em água dissociam liberando pelo menos um cátion diferente de H+ e um ânion diferente de OH-. Estão em toda parte: o cloreto de sódio (NaCl, sal de cozinha), o bicarbonato de sódio (NaHCO3, fermento químico e antiácido), o carbonato de cálcio (CaCO3, mármore, calcário e casca de ovo) e o hipoclorito de sódio (NaClO, água sanitária)."
                },
                {
                    "type": "paragraph",
                    "content": "Já os ÓXIDOS são compostos binários (apenas dois elementos) nos quais o oxigênio é o elemento mais eletronegativo, aparecendo à direita da fórmula (com exceção do OF2). Veja os tipos que mais caem no ENEM: ÓXIDOS ÁCIDOS (ou anidridos), formados por ametais como CO2, SO2, SO3 e NO2 — reagem com água formando ácidos (causadores da chuva ácida e acidificação dos oceanos!) e com bases formando sal e água. ÓXIDOS BÁSICOS, formados por metais alcalinos e alcalino-terrosos como CaO (cal virgem) e Na2O — reagem com água formando bases e com ácidos formando sal e água."
                },
                {
                    "type": "paragraph",
                    "content": "Não esqueça ainda dos ÓXIDOS ANFÓTEROS, como Al2O3 (bauxita) e ZnO: são verdadeiros camaleões químicos que funcionam como base diante de um ácido forte e como ácido diante de uma base forte! E temos os ÓXIDOS NEUTROS (CO, NO e N2O), que não reagem nem com água, nem com ácidos, nem com bases."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Neutralização na Prática: Do Estômago à Calagem Agrícola"
                },
                {
                    "type": "paragraph",
                    "content": "Quando um ácido encontra uma base, o H+ do ácido se junta ao OH- da base formando água (H2O), enquanto o cátion da base e o ânion do ácido formam um sal: Ácido + Base → Sal + Água! Essa é a reação de NEUTRALIZAÇÃO, protagonista em duas aplicações clássicas do ENEM."
                },
                {
                    "type": "paragraph",
                    "content": "No corpo humano, combatemos a azia (excesso de HCl gástrico) com antiácidos como o leite de magnésia, Mg(OH)2, que neutraliza o excesso ácido: 2 HCl + Mg(OH)2 → MgCl2 + 2 H2O. Na agricultura brasileira, solos muito ácidos travam nutrientes e liberam alumínio tóxico às raízes. O produtor aplica a CALAGEM: espalha calcário moído (CaCO3) ou cal (CaO / Ca(OH)2) para neutralizar a acidez, elevar o pH perto de 6,5 e fornecer cálcio e magnésio às plantas!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Por Que Calcário (CaCO3) Neutraliza Ácidos?",
                    "content": "Embora o CaCO3 seja um sal e não uma base de Arrhenius, seu ânion carbonato (CO3 2-) sofre hidrólise básica e reage com ácidos formando sal, água e gás carbônico: CaCO3 + 2 H+ → Ca2+ + H2O + CO2↑. Por isso, tanto o calcário quanto o bicarbonato de sódio (NaHCO3) são excelentes neutralizantes!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Escala de pH de 0 a 14: Entendendo o Salto Logarítmico 10x"
                },
                {
                    "type": "paragraph",
                    "content": "Para medir o grau de acidez ou alcalinidade de uma solução aquosa sem lidar com potências negativas gigantescas, usamos o pH (potencial hidrogeniônico), definido por pH = -log[H+]. A 25 °C, a escala padrão vai de 0 a 14 e a soma pH + pOH vale sempre 14. Valores com pH < 7 são ÁCIDOS (como suco gástrico ~1,5, limão ~2,2 e chuva ácida < 5,6); pH = 7 é NEUTRO (água pura a 25 °C, onde [H+] = [OH-] = 10^-7 mol/L); e pH > 7 são BÁSICOS ou ALCALINOS (como sangue humano ~7,4, água sanitária ~12 e soda cáustica ~14)."
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque é aqui que a maioria cai na prova: a escala de pH NÃO é linear, ela é LOGARÍTMICA na base 10! Cada 1 unidade que o pH DIMINUI significa que a concentração de íons H+ (a acidez) ficou 10 VEZES MAIOR. Se o pH cair 2 unidades, ficou 10² = 100 vezes mais ácido! Se cair 3 unidades, 10³ = 1.000 vezes mais ácido! Da mesma forma, se você diluir uma solução de ácido forte 10 vezes com água pura (aumentando o volume em 10×), a concentração de H+ cai 10 vezes e o pH SOBE em 1 unidade (por exemplo, de pH 2 para pH 3)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Chuva Ácida e Escala de pH",
                    "content": "Enunciado: A chuva limpa tem pH 5,6. Em região industrial, registrou-se pH 3,6. Quantas vezes a concentração de H+ é maior na chuva ácida? E se 100 mL de ácido forte com pH = 2 forem diluídos com água até 10 L, qual será o novo pH?\n\nResolução:\n1. Diferença de pH: 5,6 - 3,6 = 2,0 unidades para baixo.\n2. Na base 10, cair 2 unidades multiplica [H+] por 10² = 100 vezes mais ácida!\n3. Na diluição: o volume foi de 0,1 L para 10 L, aumentando 100 vezes (10²). Logo, [H+] cai 100 vezes e o pH sobe 2 unidades: de pH 2 para pH 4!"
                },
                {
                    "type": "quote",
                    "content": "No pH, andar uma casa para baixo multiplica a acidez por dez; neutralizar é juntar H+ e OH- para devolver equilíbrio em forma de água e sal.",
                    "author": "Fechamento de Química Inorgânica ENEM"
                }
            ],
            "quiz": []
        }
    ]
