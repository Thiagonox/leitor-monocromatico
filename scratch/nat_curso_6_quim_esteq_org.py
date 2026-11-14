# -*- coding: utf-8 -*-
"""Curso de Ciências da Natureza ENEM - Módulo 6: Estequiometria e Química Orgânica (Capítulos 29 a 31)"""


def get_chapters():
    return [
        {
            "id": "nat-cap-29-estequiometria",
            "number": 29,
            "title": "29. Estequiometria Sem Mistério: Mol, Massa Molar, Avogadro, Cálculos Químicos e Reagente Limitante",
            "epigraph": {
                "text": "Na natureza, nada se cria, nada se perde, tudo se transforma — e na estequiometria, tudo se pesa, se conta e se equilibra com a precisão de uma receita perfeita.",
                "author": "Inspirado em Antoine Lavoisier"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas à Arte de Fazer Contas na Cozinha da Química"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo a um dos capítulos mais temidos — e, depois de hoje, um dos mais rentáveis — de toda a prova de Ciências da Natureza do ENEM. Eu sei que basta ouvir a palavra estequiometria para muita gente já sentir um frio na espinha, imaginando fórmulas complicadas e números gigantescos. Mas respire fundo e venha comigo: estequiometria nada mais é do que a matemática das receitas químicas. Se você já dobrou uma receita de bolo ou calculou quantos pães e fatias de queijo precisa comprar para fazer sanduíches para os amigos, você já sabe a lógica inteira deste capítulo! Nas provas do ENEM, estequiometria aparece todo ano — seja na neutralização da acidez do solo com calcário, na queima de combustíveis como etanol e gasolina para calcular emissão de CO₂, no funcionamento do airbag do carro ou na produção industrial de medicamentos e metais. Quem domina o método passo a passo resolve qualquer questão sem decorar dezenas de fórmulas, garantindo pontos preciosos na faixa dos 800+."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Analogia da Dúzia: Entendendo o Mol e o Número de Avogadro"
                },
                {
                    "type": "paragraph",
                    "content": "Pense comigo: quando você vai à feira comprar laranjas ou ovos, você pede 1 dúzia e sabe na hora que o feirante vai colocar 12 unidades na sacola. Se pedir 1 centena de docinhos para uma festa, recebe 100 unidades. Se comprar 1 resma de papel, leva 500 folhas. A humanidade inventou nomes de pacotes para não ficar contando itens pequenos um por um. Agora imagine o tamanho de um átomo ou de uma molécula: eles são tão absurdamente minúsculos que até em uma única gota d'água cabem trilhões e trilhões de moléculas. Para resolver esse problema, os químicos criaram a 'dúzia da química', que se chama MOL. Enquanto 1 dúzia vale 12 unidades, 1 mol vale exatamente 6,02 × 10²³ unidades — esse número famoso é a Constante de Avogadro. Só para você ter noção da grandeza, 6,02 × 10²³ é o número 602 seguido de 21 zeros! Então, 1 mol de átomos de ferro contém 6,02 × 10²³ átomos de ferro; 1 mol de moléculas de água (H₂O) contém 6,02 × 10²³ moléculas de água; e, se você tivesse 1 mol de bolinhas de gude, cobriria o planeta Terra inteiro com quilômetros de profundidade."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Massa Molar na Tabela Periódica: Ligando Quantidade à Balança"
                },
                {
                    "type": "paragraph",
                    "content": "No laboratório, ninguém consegue contar 6,02 × 10²³ moléculas com uma pinça, certo? Nós usamos uma balança! E é aí que entra a Massa Molar (M), medida em gramas por mol (g/mol). Olhe para a Tabela Periódica: aquele número decimal que aparece em cada quadradinho — chamado de massa atômica — tem um superpoder duplo. Para o carbono (C), o valor é 12; para o hidrogênio (H), é 1; para o oxigênio (O), é 16; para o nitrogênio (N), é 14. Isso significa que 1 mol de átomos de carbono pesa exatamente 12 gramas, e 1 mol de átomos de oxigênio pesa 16 gramas! Para achar a massa molar de uma substância composta, basta somar as massas atômicas de todos os átomos da fórmula. Vamos treinar com a água (H₂O): são 2 hidrogênios (2 × 1 = 2) mais 1 oxigênio (1 × 16 = 16), totalizando 18 g/mol — ou seja, 18 gramas de água (menos de duas colheres de sopa!) contêm 6,02 × 10²³ moléculas de H₂O. Vamos fazer com o gás carbônico (CO₂): 1 carbono (12) + 2 oxigênios (2 × 16 = 32) = 44 g/mol. E com o carbonato de cálcio (CaCO₃, dado Ca = 40, C = 12, O = 16): 40 + 12 + (3 × 16) = 100 g/mol. Guarde esses três valores (18, 44 e 100), pois eles aparecem o tempo todo no ENEM!"
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: As 3 Portas de Entrada do Mol",
                    "content": "Para qualquer substância pura, 1 mol representa sempre o mesmo pacote visto por três ângulos diferentes: (1) Em massa: vale a Massa Molar em gramas (ex.: 44 g de CO₂). (2) Em entidades: vale 6,02 × 10²³ moléculas, átomos ou íons. (3) Em volume gasoso nas CNTP (0 °C e 1 atm): qualquer gás ideal ocupa 22,4 litros! (Atenção: se a questão der condições ambientais como 25 °C e 1 atm, ela informará o volume molar, geralmente 24,5 L/mol ou 25 L/mol)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Roteiro Infalível em 4 Passos para Qualquer Cálculo Estequiométrico"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui, porque este roteiro vai salvar você em 100% das questões de cálculo químico. Não tente pular etapas de cabeça! Siga sempre esta sequência sagrada: Passo 1 — Escreva e BALANCEIE a equação química. Sem balanceamento correto, a proporção da receita desanda. Passo 2 — Sublinhe apenas as duas substâncias que o enunciado relaciona: quem ele deu (dado) e quem ele pediu (incógnita). Passo 3 — Monte a primeira linha da regra de três usando os coeficientes estequiométricos da equação, convertendo cada um para a unidade que a pergunta usou (mol, gramas, litros nas CNTP ou moléculas). Passo 4 — Coloque na segunda linha o valor do enunciado e o X, multiplique cruzado e corra para o abraço."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Combustão do Etanol (Nível ENEM)",
                    "content": "Pergunta: Na queima completa de 92 g de etanol (C₂H₆O, massa molar = 46 g/mol), qual é a massa de gás carbônico (CO₂, massa molar = 44 g/mol) liberada para a atmosfera? Resolução: Passo 1 (equação balanceada): 1 C₂H₆O + 3 O₂ → 2 CO₂ + 3 H₂O. Veja que 2 carbonos à esquerda exigem 2 CO₂ à direita, 6 hidrogênios exigem 3 H₂O, e os 7 oxigênios à direita fecham com 1 do etanol + 6 de 3 O₂. Passo 2 (relacionar dado e pedido): 1 mol de C₂H₆O produz 2 mols de CO₂. Passo 3 (converter para gramas, pois a pergunta trabalha em massa): 1 × 46 g de etanol produzem 2 × 44 g = 88 g de CO₂. Passo 4 (regra de três): Se 46 g de etanol geram 88 g de CO₂, então 92 g (exatamente o dobro!) geram X. Fazendo 46X = 92 × 88, temos X = 176 g de CO₂. Viu como foi limpo e direto?"
                },
                {
                    "type": "paragraph",
                    "content": "E se o mesmo problema perguntasse o volume de CO₂ liberado nas CNTP em vez da massa? No Passo 3, para o etanol continuaríamos usando massa (46 g), porque o dado veio em gramas, mas para o CO₂ usaríamos o volume nas CNTP: 2 mols × 22,4 L = 44,8 L. Veja que maravilha: você pode misturar unidades diferentes entre uma substância e outra (massa de um lado, volume ou moléculas do outro), desde que na mesma coluna vertical as unidades sejam idênticas!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Reagente Limitante vs. Reagente em Excesso: A Analogia do Sanduíche"
                },
                {
                    "type": "paragraph",
                    "content": "Agora vamos ao ponto em que muita gente cai na prova: quando a questão fornece as quantidades de DOIS reagentes ao mesmo tempo! Pense comigo na cozinha: sua receita de misto-quente exige 2 fatias de pão e 1 fatia de queijo para montar 1 sanduíche. Se você tiver 10 fatias de pão e apenas 3 fatias de queijo na geladeira, quantos sanduíches completos você consegue fazer? Apenas 3! Depois do terceiro sanduíche, o queijo acaba, e sobram 4 fatias de pão soltas no pacote. Na química é idêntico: quem acaba primeiro e trava a reação é o Reagente Limitante (o queijo), e quem sobra no final é o Reagente em Excesso (o pão)."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Como Descobrir o Limitante sem Chutar",
                    "content": "Sempre que o enunciado der a massa ou o número de mols de DOIS reagentes, pare tudo e teste qual acaba primeiro! Regra prática: passe ambos os reagentes para mols e divida o número de mols disponível pelo seu coeficiente na equação balanceada. O MENOR resultado indica o reagente limitante! A partir daí, jogue fora o dado do reagente em excesso para calcular o produto: todo cálculo de produto gerado é feito EXCLUSIVAMENTE usando o reagente limitante. Por exemplo, na síntese da água (2 H₂ + 1 O₂ → 2 H₂O), se misturarmos 6 mols de H₂ com 2 mols de O₂: dividindo pelos coeficientes, temos 6/2 = 3 para H₂ e 2/1 = 2 para O₂. Como 2 < 3, o O₂ é o limitante! Ele consome apenas 4 mols de H₂, produz 4 mols de água e sobram 2 mols de H₂ em excesso."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Pureza de Reagentes e Rendimento das Reações"
                },
                {
                    "type": "paragraph",
                    "content": "No mundo real — e o ENEM adora química do mundo real —, os minérios retirados da natureza não são 100% puros, e nenhuma indústria consegue transformar 100% dos reagentes em produto sem perdas por evaporação ou reações paralelas. É aqui que entram dois conceitos primos, mas aplicados em momentos opostos do cálculo: Pureza e Rendimento. A Pureza diz respeito ao REAGENTE, logo aplicamos ANTES de fazer a regra de três da equação. Se uma amostra de 500 g de calcário tem 80% de pureza em CaCO₃, significa que os outros 20% são barro, areia ou impureza que não reage: calculamos 80% de 500 g = 400 g de CaCO₃ puro, e é com esses 400 g que entramos na estequiometria. Já o Rendimento diz respeito ao PRODUTO obtido no final, logo aplicamos DEPOIS da regra de três (ou sobre o produto teórico). Se a conta teórica previu a formação de 200 g de produto, mas o rendimento da reação foi de 75%, a massa real obtida será 75% de 200 g = 150 g."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Calcário Impuro e Rendimento Industrial",
                    "content": "Enunciado: Uma indústria aquece 250 kg de calcário com 80% de pureza em CaCO₃ (M = 100 g/mol) para produzir cal virgem, CaO (M = 56 g/mol), segundo a reação CaCO₃ → CaO + CO₂. Sabendo que o rendimento do processo é de 90%, qual a massa de CaO obtida? Resolução passo a passo: Primeiro, tiramos a pureza do reagente antes de reagir: 80% de 250 kg = 0,80 × 250 = 200 kg de CaCO₃ puro. Segundo, olhamos a equação (já balanceada 1:1:1): 100 g de CaCO₃ produzem 56 g de CaO (a mesma proporção vale em kg: 100 kg geram 56 kg!). Terceiro, regra de três com a parte pura: 100 kg de CaCO₃ → 56 kg de CaO; logo 200 kg → X. Como dobrou, X teórico = 112 kg de CaO. Quarto, aplicamos o rendimento de 90% no final: 0,90 × 112 kg = 100,8 kg de cal virgem produzidos! Perceba a elegância: pureza limpa a entrada; rendimento corrige a saída."
                },
                {
                    "type": "quote",
                    "content": "Pureza limpa o reagente antes da reação começar; rendimento corrige o produto depois que a reação terminou. Nunca confunda a entrada com a saída.",
                    "author": "Regra de Ouro da Estequiometria Aplicada"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-30-organica-1-hidrocarbonetos",
            "number": 30,
            "title": "30. Química Orgânica I: O Carbono, Cadeias Carbônicas e Hidrocarbonetos",
            "epigraph": {
                "text": "O carbono é o arquiteto da vida: com apenas quatro braços de ligação, ele constrói desde o gás simples do fogão até a dupla hélice do nosso DNA.",
                "author": "Aula Magna de Química Orgânica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Elemento Camaleão: Por Que o Carbono É o Rei da Química Orgânica?"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Bem-vindo à Química Orgânica, uma das áreas mais gostosas de estudar e mais presentes no nosso dia a dia. Pense comigo: o plástico da sua garrafa, a gasolina do carro, o perfume que você usa, o comprimido para dor de cabeça, as proteínas dos seus músculos e até as roupas de poliéster têm um protagonista em comum: o átomo de carbono (C). Existem literalmente milhões de compostos orgânicos conhecidos — muito mais do que todos os compostos do resto da Tabela Periódica juntos! A resposta começou a ser decifrada no século XIX por Friedrich August Kekulé, que formulou três postulados fundamentais que você precisa carregar no bolso para o ENEM. O primeiro é a tetravalência constante: localizado na família 14 (4A), o carbono possui 4 elétrons na camada de valência e faz sempre 4 ligações covalentes para ficar estável. O segundo postulado diz que essas quatro valências são equivalentes — não importa se você desenha um átomo ligado em cima, embaixo ou ao lado do carbono tetraédrico. E o terceiro postulado é o segredo da variedade infinita: o carbono consegue se ligar a outros átomos de carbono formando longas cadeias, anéis fechados e redes ramificadas."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Hibridização do Carbono (sp³, sp² e sp) Sem Decoreba"
                },
                {
                    "type": "paragraph",
                    "content": "As quatro ligações do carbono podem se organizar de três jeitos diferentes, e basta contar quantas ligações simples, duplas ou triplas saem dele para identificar sua hibridização na hora! Quando o carbono faz 4 ligações simples (todas sigma, σ), sua hibridização é sp³: sua geometria no espaço é tetraédrica — imagine um tripé com um pino apontando para cima — com ângulo aproximado de 109,5° entre as ligações, como ocorre no gás metano (CH₄). Quando o carbono faz 1 ligação dupla (uma sigma e uma pi, π) e 2 simples, sua hibridização é sp², com geometria trigonal plana e ângulo de 120°, como nos carbonos do eteno (H₂C=CH₂) e do anel benzênico. Por fim, quando o carbono faz 1 ligação tripla (uma sigma e duas pi) e 1 simples — ou duas ligações duplas seguidas, como no CO₂ — sua hibridização é sp, com geometria linear e ângulo de 180°. Veja que macete visual infalível: conte o número de nuvens eletrônicas (ligações simples contam 1, dupla conta 1, tripla conta 1) ao redor do carbono. Quatro nuvens = sp³; três nuvens = sp²; duas nuvens = sp!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Classificando os Carbonos na Cadeia",
                    "content": "No ENEM, também é comum pedir a classificação dos carbonos dentro de uma molécula complexa (como um hormônio ou fármaco). O critério é simples: conte a quantos OUTROS átomos de carbono aquele carbono está diretamente ligado! Carbono primário liga-se a no máximo 1 outro carbono (pontas da cadeia). Carbono secundário liga-se a 2 outros carbonos. Carbono terciário liga-se a 3 outros carbonos (onde nasce uma ramificação). Carbono quaternário liga-se a 4 outros carbonos. Atenção: átomos como O, N ou Cl NÃO contam nessa contagem, apenas outros carbonos!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Classificação das Cadeias Carbônicas: O Raio-X Estrutural"
                },
                {
                    "type": "paragraph",
                    "content": "Antes de dar nomes aos compostos, precisamos aprender a descrever o 'esqueleto' da molécula. Classificamos uma cadeia carbônica usando quatro pares de critérios bem intuitivos. Primeiro, quanto ao fechamento: ela é aberta (ou acíclica) se tem pontas livres, fechada (ou cíclica) se forma anel, ou mista se junta um anel a uma cauda aberta. Segundo, quanto à disposição: é normal (reta, sem bifurcações, só com carbonos primários e secundários) ou ramificada (tem pelo menos um carbono terciário ou quaternário criando um 'galho')."
                },
                {
                    "type": "paragraph",
                    "content": "Terceiro, quanto ao tipo de ligação ENTRE carbonos: ela é saturada se só tem ligações simples entre carbonos, ou insaturada se possui pelo menos uma ligação dupla ou tripla entre carbonos. Cuidado com a pegadinha clássica da TRI: uma dupla ligação entre carbono e oxigênio (C=O) NÃO torna a cadeia insaturada! A insaturação tem que estar ENTRE carbonos. Quarto, quanto à natureza dos átomos na espinha dorsal da cadeia: ela é homogênea se só há carbonos na sequência principal, ou heterogênea se houver um heteroátomo (O, N, S, P) exatamente ENTRE dois carbonos, interrompendo a fila carbônica — como acontece no éter (CH₃–O–CH₃). Se o oxigênio estiver na ponta ou pendurado para fora, como no etanol (CH₃–CH₂–OH), a cadeia continua homogênea!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Hidrocarbonetos: Os Combustíveis do Mundo Moderno"
                },
                {
                    "type": "paragraph",
                    "content": "Chegamos à família mais simples e energeticamente mais importante da Química Orgânica: os hidrocarbonetos, formados EXCLUSIVAMENTE por carbono (C) e hidrogênio (H). Eles compõem o gás de cozinha, o gás natural, a gasolina, o diesel, o querosene de aviação e a parafina das velas. Dividimos os hidrocarbonetos em grandes famílias conforme suas ligações e formatos."
                },
                {
                    "type": "paragraph",
                    "content": "Os Alcanos são hidrocarbonetos de cadeia aberta e saturada (só ligações simples), seguindo a fórmula geral CₙH₂ₙ₊₂. Exemplo: o metano (CH₄, 1 carbono) é o principal componente do gás natural e do biogás; o propano (C₃H₈) e o butano (C₄H₁₀) formam o gás de cozinha (GLP); o octano (C₈H₁₈) é referência da gasolina. Os Alcenos (ou olefinas) têm cadeia aberta e 1 ligação dupla (fórmula geral CₙH₂ₙ), como o eteno ou etileno (C₂H₄), gás usado para amadurecer frutas e fabricar plástico polietileno. Os Alcinos têm cadeia aberta e 1 ligação tripla (fórmula geral CₙH₂ₙ₋₂), cujo astro é o etino ou acetileno (C₂H₂), usado em maçaricos de solda por atingir altíssimas temperaturas."
                },
                {
                    "type": "paragraph",
                    "content": "Temos ainda os Cicloalcanos (ou ciclanos), que são anéis fechados apenas com ligações simples (fórmula CₙH₂ₙ), e os Hidrocarbonetos Aromáticos, que carregam pelo menos um anel benzênico (C₆H₆): um hexágono de seis carbonos sp² com três duplas ligações alternadas que ficam girando em ressonância — por isso desenhamos frequentemente um hexágono com um círculo no meio. O benzeno e seus derivados (como o tolueno, usado em colas e solventes, e o naftaleno da naftalina) são altamente estáveis graças a essa ressonância, mas exigem cuidado ambiental por sua toxicidade."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Nomenclatura IUPAC Passo a Passo: Dando o Nome Certo"
                },
                {
                    "type": "paragraph",
                    "content": "Dar nome a um composto orgânico pela regra oficial da IUPAC funciona como montar um código de três peças: PREFIXO (quantos carbonos tem a cadeia principal) + INFIXO (tipo de ligação) + SUFIXO (função química). Os prefixos básicos que você precisa saber de cor até 10 carbonos são: 1 = met, 2 = et, 3 = prop, 4 = but, 5 = pent, 6 = hex, 7 = hept, 8 = oct, 9 = non, 10 = dec. O infixo é 'an' (só simples), 'en' (uma dupla) ou 'in' (uma tripla). Para qualquer hidrocarboneto, o sufixo é sempre a letra 'o'. Assim, 3 carbonos com uma dupla formam prop + en + o = propeno!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Nomeando um Hidrocarboneto Ramificado",
                    "content": "Vamos nomear a estrutura CH₃–CH(CH₃)–CH=CH–CH₃ passo a passo. Regra 1: Escolha a cadeia principal, que deve ser a maior sequência contínua de carbonos que CONTENHA a insaturação (a dupla ligação). Aqui ela tem 5 carbonos (pent). Regra 2: Numere a cadeia da ponta mais próxima da insaturação (e não da ramificação!). Da direita para a esquerda, a dupla fica entre os carbonos 2 e 3 (menor número = 2); da esquerda para a direita, ficaria no 3. Logo, numeramos da direita para a esquerda: C1 é o CH₃ da ponta direita, a dupla está no C2, e a ramificação metil (–CH₃) cai no carbono 4. Regra 3: Junte tudo citando primeiro a ramificação com sua posição: 4-metilpent-2-eno! Viu como a numeração obedece a uma hierarquia clara: função > insaturação > ramificação?"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Polaridade e Ponto de Ebulição nos Hidrocarbonetos"
                },
                {
                    "type": "paragraph",
                    "content": "Como só possuem carbono e hidrogênio — cuja diferença de eletronegatividade é mínima —, todos os hidrocarbonetos são substâncias APOLARES. Por isso não se misturam com a água (que é polar), como você vê quando cai óleo ou gasolina em uma poça de chuva: 'semelhante dissolve semelhante'. Como são apolares, suas moléculas se atraem apenas pelas forças intermoleculares mais fracas que existem, chamadas dipolo induzido (ou forças de London). E o que faz o ponto de ebulição (PE) de um hidrocarboneto subir ou descer? Duas regras de ouro que o ENEM adora comparar! Primeira regra: quanto MAIOR a cadeia carbônica (maior massa molar), maior a área de contato entre as moléculas, mais fortes ficam as forças de London e MAIOR é o ponto de ebulição. É por isso que de 1 a 4 carbonos eles são gases à temperatura ambiente (metano, butano), de 5 a 17 carbonos são líquidos (gasolina, querosene) e acima de 18 carbonos viram sólidos pastosos ou duros (parafina, asfalto). Segunda regra: entre isômeros com o mesmo número de carbonos, a cadeia NORMAL (esticada) tem ponto de ebulição MAIOR do que a cadeia RAMIFICADA (bolinha compacta), porque moléculas esticadas encostam melhor umas nas outras do que moléculas arredondadas!"
                },
                {
                    "type": "quote",
                    "content": "Moléculas maiores e mais esticadas têm mais superfície de contato, atraem-se com mais força e fervem em temperaturas mais altas.",
                    "author": "Resumo Prático de Propriedades Físicas"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-31-organica-2-funcoes-polimeros",
            "number": 31,
            "title": "31. Química Orgânica II: Funções Orgânicas, Álcoois, Ácidos Carboxílicos, Ésteres, Polímeros e Petróleo",
            "epigraph": {
                "text": "Quando o oxigênio e o nitrogênio entram na cadeia do carbono, a molécula ganha cheiro de fruta, sabor de remédio, poder de limpeza e plasticidade para moldar o mundo moderno.",
                "author": "Aula Magna de Funções Orgânicas"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas ao Universo das Funções Orgânicas e da Química do Cotidiano"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Agora que você já domina o esqueleto carbônico, vamos colocar os 'enfeites' nesse esqueleto — os grupos funcionais com oxigênio e nitrogênio! E quero tranquilizar você desde o primeiro minuto: no ENEM, quase nunca cai nomenclatura gigantesca de funções complexas. O que cai TODOS OS ANOS é uma molécula real (um medicamento como paracetamol ou ibuprofeno, um hormônio como adrenalina, um agrotóxico ou uma essência de perfume) com setinhas ou alternativas pedindo: 'Quais funções orgânicas estão presentes nesta estrutura?'. Quem bate o olho e reconhece os grupos funcionais em 5 segundos garante questões fáceis e médias valiosíssimas na TRI!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Funções Oxigenadas I: Álcool, Fenol e Éter (Sem Oxigênio Duplado)"
                },
                {
                    "type": "paragraph",
                    "content": "Vamos separar as funções oxigenadas em dois blocos visuais para nunca mais confundir. No primeiro bloco, o oxigênio faz apenas ligações simples. Quando você vê uma hidroxila (–OH) ligada a um carbono SATURADO (que só faz ligações simples), você tem um ÁLCOOL, cujo sufixo na IUPAC é '-ol' (ex.: etanol, CH₃–CH₂–OH, do combustível e das bebidas; glicerol, presente nos hidratantes). Agora, se essa mesma hidroxila (–OH) estiver grudada DIRETAMENTE no anel aromático (benzeno), ela muda de personalidade e ganha caráter ácido: é um FENOL! Cuidado com a pegadinha clássica: se o –OH estiver pendurado em um CH₂ fora do anel benzênico, ele volta a ser álcool (álcool benzílico), pois não tocou diretamente no anel aromático. E quando o oxigênio aparece como um 'sanduíche' exatamente ENTRE dois carbonos (R–O–R'), sem nenhuma dupla com oxigênio por perto? Temos um ÉTER! O exemplo famoso é o éter dietílico (CH₃–CH₂–O–CH₂–CH₃), antigo anestésico e excelente solvente orgânico. Resumo rápido do bloco 1: –OH em carbono saturado = álcool; –OH direto no benzeno = fenol; –O– entre dois carbonos = éter."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Funções Oxigenadas II: O Poder da Carbonila (Aldeído, Cetona, Ácido e Éster)"
                },
                {
                    "type": "paragraph",
                    "content": "No segundo bloco entra a estrela da Química Orgânica: a carbonila (C=O). Olhe sempre para o que está ligado dos dois lados do carbono da carbonila! Se a carbonila estiver na PONTA da cadeia, ligada a pelo menos um hidrogênio (–CHO), temos um ALDEÍDO (sufixo '-al'), como o metanal (formol) e o etanal. Se a carbonila estiver NO MEIO da cadeia, espremida entre dois outros carbonos (R–CO–R'), temos uma CETONA (sufixo '-ona'), como a propanona (acetona removedora de esmalte). Agora, se a carbonila estiver casada com uma hidroxila no mesmo carbono, formando a carboxila (–COOH), temos um ÁCIDO CARBOXÍLICO (sufixo '-oico'), responsável pelo azedo do vinagre (ácido etanoico ou acético) e pelo cheiro das formigas (ácido metanoico ou fórmico). Por fim, troque esse H da carboxila por outra cadeia de carbono (–COO–R'): nasce o ÉSTER! Os ésteres são os flavorizantes da natureza — dão o aroma e o sabor artificial de banana, abacaxi, morango e maçã verde nos alimentos e perfumes."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Esterificação, Saponificação e Solubilidade",
                    "content": "Duas reações de ésteres despencam no ENEM! A primeira é a ESTERIFICAÇÃO: Ácido Carboxílico + Álcool ⇌ Éster + Água (usada para fazer essências e biodiesel). A segunda é a SAPONIFICAÇÃO (fazer sabão!): quando fervemos um triéster de gordura ou óleo vegetal (triglicerídeo) com uma base forte como soda cáustica (NaOH), quebramos o éster formando glicerol e o sal de ácido graxo, que é o sabão! O sabão limpa porque tem uma cabeça polar iônica (que ama água) e uma cauda apolar longa (que dissolve a gordura). E lembre-se da solubilidade: ácidos carboxílicos e álcoois pequenos fazem ligações de hidrogênio com a água, sendo muito solúveis e tendo pontos de ebulição bem altos!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Funções Nitrogenadas: Aminas e Amidas"
                },
                {
                    "type": "paragraph",
                    "content": "Para fechar o reconhecimento de funções, olhe para o nitrogênio (N). Ele faz 3 ligações. Se o nitrogênio estiver ligado diretamente a carbonos comuns (sem carbonila C=O grudada nele), temos uma AMINA — derivada da amônia (NH₃), com forte caráter BÁSICO (pH > 7) e cheiro característico de peixe em decomposição. Exemplo: a adrenalina, a nicotina e a cafeína possuem grupos amina. Já se o nitrogênio estiver colado diretamente a uma carbonila (–CO–N–), nasce uma AMIDA, que é neutra em termos ácido-base e forma a ligação peptídica que une os aminoácidos nas proteínas! Exemplos clássicos do ENEM: a ureia (presente na urina e em fertilizantes) e o paracetamol (que tem uma amida e um fenol na mesma molécula)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Isomeria Plana, Geométrica e Óptica nos Fármacos"
                },
                {
                    "type": "paragraph",
                    "content": "Você já ouviu falar de gêmeos que têm o mesmo peso, mas personalidades diferentes? Na Química, isso se chama ISOMERIA: compostos diferentes que possuem exatamente a MESMA fórmula molecular. Na isomeria plana, identificamos a diferença no papel: isômeros de função pertencem a grupos diferentes (ex.: etanol CH₃CH₂OH e éter dimetílico CH₃OCH₃ são ambos C₂H₆O, mas um ferve a 78 °C e o outro é gás a -24 °C!); isômeros de cadeia mudam o esqueleto (normal vs. ramificada); isômeros de posição mudam o lugar da dupla, da ramificação ou do grupo funcional; na metameria (compensação), muda a posição do heteroátomo; e na tautomeria, ocorre equilíbrio dinâmico entre enol e aldeído/cetona."
                },
                {
                    "type": "paragraph",
                    "content": "Na isomeria espacial, os átomos estão ligados na mesma ordem, mas apontam para lados diferentes no espaço 3D! A isomeria geométrica (cis-trans) exige uma ligação dupla entre carbonos (ou anel fechado) e ligantes diferentes em cada carbono da dupla (R₁ ≠ R₂ e R₃ ≠ R₄). Quando os grupos iguais ou maiores ficam do mesmo lado, é CIS; quando ficam em lados opostos em diagonal, é TRANS — como na famosa gordura trans das margarinas. Já a isomeria óptica acontece quando a molécula tem um carbono quiral (ou assimétrico), ou seja, um carbono sp³ ligado a QUATRO grupos totalmente diferentes entre si. Essa molécula não tem plano de simetria e gera dois isômeros espaciais (enantiômeros), exatamente como sua mão esquerda e sua mão direita no espelho: um desvia a luz polarizada para a direita (dextrógiro) e o outro para a esquerda (levógiro). Em fármacos, isso é questão de vida ou morte: no ibuprofeno, só um enantiômero combate a dor; no famoso caso da talidomida, um isômero aliviava enjoos enquanto seu 'irmão espelho' causava má-formação fetal!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Polímeros Sintéticos e Naturais: Construindo Correntes Gigantes"
                },
                {
                    "type": "paragraph",
                    "content": "A palavra polímero significa 'muitas partes': são macromoléculas gigantes formadas pela repetição de milhares de peças pequenas chamadas monômeros. Na natureza, já temos polímeros incríveis como a celulose, o amido, as proteínas (poli-aminoácidos) e a borracha natural (poli-isopreno). Na indústria, fabricamos polímeros sintéticos por dois grandes tipos de reação. Na polimerização por ADIÇÃO, monômeros que contêm ligação dupla (C=C) abrem essa dupla e vão dando as mãos uns aos outros sem perder nenhum átomo! É assim que milhares de moléculas de eteno formam o polietileno (sacolas e potes), o propeno vira polipropileno (tampas e para-choques), o cloreto de vinila vira PVC (canos) e o estireno vira poliestireno (isopor). Já na polimerização por CONDENSAÇÃO, dois monômeros diferentes com grupos funcionais reagem eliminando uma molécula pequena no processo — quase sempre água (H₂O). Assim nascem o poliéster PET das garrafas de refrigerante (ácido dicarboxílico + diálcool) e a poliamida Nylon (ácido dicarboxílico + diamina)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Destilação Fracionada e Craqueamento do Petróleo"
                },
                {
                    "type": "paragraph",
                    "content": "Para fechar nossa jornada com chave de ouro, vamos até a refinaria de petróleo! O petróleo bruto é uma mistura escura e viscosa de centenas de hidrocarbonetos diferentes. Como separá-los? Pela DESTILAÇÃO FRACIONADA! Aquecemos o petróleo na base de uma torre alta com bandejas em várias temperaturas. Como vimos no Capítulo 30, moléculas pequenas têm ponto de ebulição baixo: elas sobem como gás até o topo mais frio da torre (gás de cozinha GLP, C₁–C₄). Logo abaixo condensam a gasolina (C₅–C₁₂) e a nafta; no meio ficam o querosene e o óleo diesel (C₁₃–C₁₈); e lá embaixo, no fundo quentíssimo, sobram os óleos lubrificantes, a parafina e o piche do asfalto (cadeias gigantes que nem evaporam)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido / Pegadinha Clássica: Craqueamento (Cracking)",
                    "content": "Imagine que o mercado está comprando muita gasolina (C₈H₁₈), mas sobrando muito óleo pesado (como C₁₆H₃₄) no fundo da torre. Como a refinaria resolve isso? Fazendo o CRAQUEAMENTO térmico ou catalítico! Craquear significa 'quebrar' moléculas grandes e pesadas de hidrocarbonetos, usando alta temperatura e catalisadores, em moléculas menores de maior valor comercial, como a gasolina e o eteno (usado para fazer plásticos). Exemplo real: C₁₆H₃₄ → C₈H₁₈ (octano da gasolina) + C₈H₁₆ (alceno menor). Resumo final para nunca errar: destilação fracionada é um processo FÍSICO (separa por ponto de ebulição sem quebrar ligações); craqueamento é um processo QUÍMICO (quebra moléculas grandes em menores)!"
                },
                {
                    "type": "quote",
                    "content": "Reconhecer funções orgânicas é ler o código de barras das moléculas: em cinco segundos você descobre se ela é ácida, básica, perfumada, solúvel ou plástica.",
                    "author": "Fechamento do Módulo de Química Orgânica ENEM"
                }
            ],
            "quiz": []
        }
    ]
