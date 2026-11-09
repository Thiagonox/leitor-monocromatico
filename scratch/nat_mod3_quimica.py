# -*- coding: utf-8 -*-
"""Eixo 3: Química Completa ENEM (Capítulos 21 a 33)"""

def get_chapters():
    return [
        {
            "id": "nat-qui-21-estrutura-atomica",
            "number": 21,
            "title": "21. Estrutura Atômica da Matéria: Modelos Atômicos e Isótopos",
            "epigraph": {
                "text": "Da 'bola de bilhar' maciça de Dalton aos níveis quantizados de energia de Bohr, a evolução dos modelos atômicos explica as propriedades químicas e fenômenos cotidianos como os fogos de artifício.",
                "author": "Estrutura da Matéria no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Evolução Histórica dos Modelos Atômicos"
                },
                {
                    "type": "paragraph",
                    "content": "• Dalton (1808): Esfera maciça, indivisível e indestrutível ('bola de bilhar'). Explica as leis ponderais das reações químicas (conservação e proporções fixas).\n• Thomson (1897): Descoberta do elétron através dos raios catódicos. Esfera de carga positiva uniforme incrustada de elétrons negativos ('pudim de passas'). O átomo é divisível e de natureza elétrica neutra.\n• Rutherford (1911): Experimento do espalhamento de partículas alfa em folha de ouro. O átomo é composto por um núcleo central minúsculo, denso e positivo, cercado por uma imensa eletrosfera vazia ('modelo planetário').\n• Bohr (1913): Elétrons giram em órbitas circulares circundando o núcleo com níveis de energia quantizados e estacionários. Ao receber energia, o elétron SALTA para uma órbita mais externa (estado excitado); ao retornar para a órbita original mais interna, o elétron LIBERA A ENERGIA RECEBIDA NA FORMA DE FÓTONS DE LUZ VISÍVEL (base do teste de chama em química forense e da cor dos fogos de artifício)!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Partículas Subatômicas e Semelhanças Atômicas"
                },
                {
                    "type": "paragraph",
                    "content": "• Número Atômico (Z): Número de prótons no núcleo (identidade do elemento químico: Z = p).\n• Número de Massa (A): Soma de prótons e nêutrons no núcleo: A = Z + n.\n• Isótopos: Átomos com MESMO número de prótons (Z), mas diferentes números de nêutrons e massas (ex: Carbono-12 e Carbono-14; Hidrogênio prótio 1H, deutério 2H e trítio 3H).\n• Isóbaros: Mesma massa A, diferentes números atômicos Z.\n• Isótonos: Mesmo número de nêutrons (n = A - Z).\n• Isoeletrônicos: Átomos ou íons com o mesmo número total de elétrons."
                }
            ],
            "quiz": [
                {
                    "question": "Os fogos de artifício produzem cores brilhantes e variadas no céu noturno: o bário gera coloração verde, o estrôncio gera vermelho e o sódio produz amarelo intenso. A emissão dessas cores características é explicada pelo modelo atômico de:",
                    "options": [
                        "Bohr, no qual elétrons excitados retornam a níveis de menor energia emitindo fótons de frequências específicas.",
                        "Dalton, no qual átomos esféricos e maciços colidem liberando ondas luminosas por atrito.",
                        "Thomson, no qual elétrons incrustados vibram na massa positiva desprendendo calor.",
                        "Rutherford, no qual partículas alfa são ejetadas do núcleo atômico em alta velocidade."
                    ],
                    "correctAnswer": 0,
                    "explanation": "No modelo de Bohr, a energia térmica da explosão dos fogos de artifício excita elétrons para órbitas mais afastadas do núcleo. Quando esses elétrons decaem de volta aos níveis fundamentais mais baixos, liberam a diferença de energia na forma de radiação luminosa com comprimentos de onda específicos (cores características de cada elemento químico)."
                }
            ]
        },
        {
            "id": "nat-qui-22-tabela-periodica",
            "number": 22,
            "title": "22. Tabela Periódica dos Elementos e Propriedades Periódicas",
            "epigraph": {
                "text": "A Tabela Periódica moderna é organizada em ordem crescente de número atômico (Z). Elementos no mesmo grupo compartilham a mesma configuração da camada de valência e comportamentos químicos análogos.",
                "author": "Lei Periódica de Moseley"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Organização em Grupos (Famílias) e Períodos"
                },
                {
                    "type": "paragraph",
                    "content": "• Períodos (Linhas Horizontais, 1 a 7): Indicam o NÚMERO DE CAMADAS ELETRÔNICAS ocupadas pelo átomo (1ª camada K até 7ª camada Q).\n• Grupos / Famílias (Colunas Verticais, 1 a 18): Reúnem elementos com igual quantidade de elétrons na camada de valência e propriedades químicas semelhantes:\n- Grupo 1 (Metais Alcalinos: Li, Na, K...): 1 elétron na valência, formam cátions +1, extremamente reativos com água gerando H2 e bases fortes.\n- Grupo 2 (Metais Alcalinoterrosos: Mg, Ca, Ba...): 2 elétrons na valência, formam cátions +2.\n- Grupo 16 (Calcogênios: O, S, Se...): 6 elétrons na valência, tendem a receber 2 elétrons (ânions -2).\n- Grupo 17 (Halogênios: F, Cl, Br, I): 7 elétrons na valência, altíssima eletronegatividade, formam ânions -1.\n- Grupo 18 (Gases Nobres: He, Ne, Ar, Kr...): 8 elétrons na valência (exceto He com 2), octeto completo, quimicamente inertes e estáveis em condições normais."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Quatro Propriedades Periódicas Fundamentais"
                },
                {
                    "type": "paragraph",
                    "content": "1. Raio Atômico: Tamanho do átomo. Cresce de CIMA para BAIXO nas colunas (mais camadas eletrônicas) e da DIREITA para a ESQUERDA nos períodos (menor carga nuclear efetiva no núcleo, puxando os elétrons com menos força).\n2. Eletronegatividade: Força de atração que um átomo exerce sobre os elétrons de uma ligação química. Cresce no sentido OPOSTO ao raio: de BAIXO para CIMA e da ESQUERDA para a DIREITA (excluindo os gases nobres). Ordem decrescente dos mais eletronegativos: F > O > N > Cl > Br > I > S > C > P > H (Mnemônica: 'Fui Ontem No Clube Brasileiro, I Só Comi Pão Hoje').\n3. Energia de Ionização: Energia mínima necessária para arrancar um elétron de um átomo gasoso isolado no estado fundamental. Quanto menor o raio atômico, maior a atração nuclear e maior a energia necessária (cresce para cima e para a direita)."
                }
            ],
            "quiz": [
                {
                    "question": "Qual dos seguintes elementos químicos possui o MAIOR raio atômico e a MENOR eletronegatividade da lista apresentada?",
                    "options": [
                        "Frâncio (Fr) / Césio (Cs)",
                        "Flúor (F)",
                        "Cloro (Cl)",
                        "Oxigênio (O)"
                    ],
                    "correctAnswer": 0,
                    "explanation": "O raio atômico cresce para baixo e para a esquerda na tabela periódica. Elementos no canto inferior esquerdo (metais alcalinos como o Césio e o Frâncio) possuem o maior tamanho de átomo e, consequentemente, a menor eletronegatividade (maior caráter metálico e eletropositividade)."
                }
            ]
        },
        {
            "id": "nat-qui-23-ligacoes-quimicas-intermoleculares",
            "number": 23,
            "title": "23. Ligações Químicas e Forças Intermoleculares: Da Estrutura aos Pontos de Ebulição",
            "epigraph": {
                "text": "Ligações intramoleculares (iônica, covalente, metálica) mantêm os átomos unidos formando substâncias. Forças intermoleculares (London, dipolo-dipolo, ligações de hidrogênio) mantêm as moléculas unidas e determinam o ponto de ebulição e a solubilidade.",
                "author": "Química Molecular no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Tipos de Ligações Químicas Intramoleculares"
                },
                {
                    "type": "paragraph",
                    "content": "• Ligação Iônica (Metal + Não-metal / Ametais): Ocorre por TRANSFERÊNCIA DEFINITIVA DE ELÉTRONS (grande diferença de eletronegatividade), formando retículo cristalino de cátions e ânions unidos por forte atração eletrostática (ex: NaCl). Propriedades: sólidos à temperatura ambiente, altíssimos pontos de fusão e ebulição, NÃO conduzem eletricidade no estado sólido, mas CONDUZEM ELETRICIDADE QUANDO FUNDIDOS (derretidos) OU EM SOLUÇÃO AQUOSA (íons livres em movimento!).\n• Ligação Covalente (Ametal + Ametal / Hidrogênio): COMPARTILHAMENTO DE PARES DE ELÉTRONS formando moléculas discretas (ex: H2O, CO2, CH4). Podem ser polares (diferença de eletronegatividade) ou apolares.\n• Ligação Metálica (Metal + Metal): Átomos de metais perdem elétrons da valência e formam cátions envoltos por uma nuvem deslocalizada de elétrons livres ('mar de elétrons'). Explica a altíssima condutibilidade térmica e elétrica em estado sólido, brilho metálico, maleabilidade e ductilidade."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Forças Intermoleculares e Solubilidade ('Semelhante Dissolve Semelhante')"
                },
                {
                    "type": "paragraph",
                    "content": "A intensidade das forças intermoleculares dita os pontos de fusão e ebulição:\n1. Dipolo Induzido / Forças de London (Força Fraca): Ocorre em moléculas estritamente APOLARES (hidrocarbonetos como gasolina e óleo, O2, N2, CO2). Pontos de ebulição baixos.\n2. Dipolo Permanente / Dipolo-Dipolo (Força Média): Ocorre em moléculas POLARES sem hidrogênio ligado a FON (ex: HCl, SO2).\n3. Ligações de Hidrogênio (Força Altíssima!): Caso especial superintenso de atração dipolar onde o HIDROGÊNIO está covalentemente ligado diretamente a átomos minúsculos e ultraeletronegativos (Flúor, Oxigênio ou Nitrogênio - F, O, N: H2O, NH3, HF, álcoois, DNA e proteínas). Explica o ponto de ebulição anormalmente alto da água (100 °C) em relação a moléculas de mesma massa molar!"
                }
            ],
            "quiz": [
                {
                    "question": "O etanol (C2H5OH, massa molar 46 g/mol) e o éter dimetílico (H3C-O-CH3, massa molar 46 g/mol) possuem exatamente a mesma fórmula molecular (C2H6O). No entanto, o etanol ferve a 78 °C, enquanto o éter dimetílico ferve a -24 °C (sendo gás à temperatura ambiente). Essa enorme discrepância térmica decorre de:",
                    "options": [
                        "O etanol formar ligações de hidrogênio intermoleculares através do grupo hidroxila (-OH), muito mais intensas que as interações dipolo-dipolo do éter.",
                        "A ligação covalente interna entre carbono e hidrogênio ser muito mais fraca no éter dimetílico.",
                        "O etanol ser um composto iônico enquanto o éter é estritamente metálico.",
                        "O éter dimetílico possuir maior pressão de vapor devido à quebra de ligações pi na combustão."
                    ],
                    "correctAnswer": 0,
                    "explanation": "Embora ambos sejam isômeros de mesma massa, o etanol possui hidrogênio ligado diretamente a oxigênio (-OH), estabelecendo intensas ligações de hidrogênio intermoleculares que exigem muito mais energia térmica para serem rompidas, elevando seu ponto de ebulição para 78 °C. O éter não possui H ligado a O, realizando apenas forças dipolo-dipolo fracas."
                }
            ]
        },
        {
            "id": "nat-qui-24-reacoes-leis-ponderais",
            "number": 24,
            "title": "24. Reações Químicas e Leis Ponderais de Lavoisier e Proust",
            "epigraph": {
                "text": "'Na natureza nada se cria, nada se perde, tudo se transforma.' — Antoine Lavoisier. A conservação das massas exige que o número de átomos de cada elemento nos reagentes seja rigorosamente igual nos produtos.",
                "author": "Fundamentos da Reatividade Química"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Classificação das Reações Químicas"
                },
                {
                    "type": "paragraph",
                    "content": "1. Síntese ou Adição: Duas ou mais substâncias combinam-se formando um único produto (A + B -> AB; ex: 2 H2 + O2 -> 2 H2O).\n2. Decomposição ou Análise: Uma única substância divide-se em duas ou mais substâncias mais simples (AB -> A + B; ex: queima do calcário CaCO3 -> CaO + CO2).\n3. Simples Troca ou Deslocamento: Uma substância simples reage com uma composta, tomando o lugar de um elemento (A + BC -> AC + B; ex: Zn + 2 HCl -> ZnCl2 + H2; depende da fila de reatividade dos metais).\n4. Dupla Troca: Duas substâncias compostas trocam íons entre si (AB + CD -> AD + CB; ex: neutralização HCl + NaOH -> NaCl + H2O ou precipitação AgNO3 + NaCl -> AgCl(s) + NaNO3)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Leis Ponderais: Lavoisier e Proust"
                },
                {
                    "type": "paragraph",
                    "content": "• Lei de Lavoisier (Conservação da Massa): Em um sistema químico fechado, a massa total dos reagentes é SEMPRE igual à massa total dos produtos: Massa_reagentes = Massa_produtos.\n• Lei de Proust (Proporções Definidas ou Constantes): A proporção em massa das substâncias que reagem e se formam em uma reação química é constante e invariável. Se duplicarmos a massa de um reagente, a massa de todos os outros reagentes e produtos duplicará na mesma proporção."
                }
            ],
            "quiz": [
                {
                    "question": "Em um recipiente fechado, 12 gramas de carbono puro reagem completamente com 32 gramas de gás oxigênio gerando gás carbônico. Se em outro experimento sob as mesmas condições forem queimados 36 gramas de carbono puro com oxigênio suficiente, qual será a massa de gás carbônico obtida?",
                    "options": [
                        "132 gramas",
                        "44 gramas",
                        "88 gramas",
                        "96 gramas"
                    ],
                    "correctAnswer": 0,
                    "explanation": "No 1º experimento: 12 g C + 32 g O2 = 44 g CO2 (Lavoisier). No 2º experimento: a massa de carbono foi triplicada (36 g = 3 * 12 g). Pela Lei de Proust, a massa do produto também triplicará: Massa de CO2 = 3 * 44 g = 132 gramas."
                }
            ]
        },
        {
            "id": "nat-qui-25-estequiometria-calculos",
            "number": 25,
            "title": "25. Cálculos Estequiométricos: Mol, Avogadro, Rendimento e Pureza",
            "epigraph": {
                "text": "1 mol = 6,02 * 10^23 entidades elementares = Massa Molar em gramas = 22,4 L de gás nas CNTP. A regra de três estequiométrica resolve qualquer proporção de prova.",
                "author": "Cálculo Estequiométrico no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Passo a Passo Infalível da Estequiometria"
                },
                {
                    "type": "paragraph",
                    "content": "Toda questão de estequiometria do ENEM deve ser resolvida seguindo rigorosamente 4 passos:\n1. Escreva a equação química e BALANCEIE os coeficientes estequiométricos (sem balanceamento, todo o cálculo estará errado!).\n2. Destaque apenas as duas substâncias mencionadas no enunciado (a dada e a pedida).\n3. Na 1ª linha da regra de três, coloque os valores padrão da estequiometria tirados da equação balanceada (multiplicando os coeficientes pelas massas molares em g/mol, mols ou 22,4 L nas CNTP).\n4. Na 2ª linha, coloque o dado fornecido no enunciado e a incógnita 'x'."
                },
                {
                    "type": "callout",
                    "title": "Casos Especiais no ENEM: Pureza, Rendimento e Reagente Limitante",
                    "content": "• Grau de Pureza: As impurezas não reagem. O cálculo estequiométrico deve ser feito APENAS sobre a fração pura do reagente (ex: 100 g de calcário com 80% de pureza = use 80 g de CaCO3 no cálculo!).\n• Rendimento Percentual: A quantidade real obtida na prática é menor do que a prevista teoricamente. Calcule o valor teórico (100%) e depois aplique o rendimento real (ex: x * 0,90 para 90% de rendimento).\n• Reagente Limitante e Excesso: O reagente limitante é o que acaba primeiro e determina quanto produto será formado; o reagente em excesso sobra sem reagir. Para descobrir quem limita: divida o número de mols de cada reagente pelo seu respectivo coeficiente estequiométrico; o menor resultado indica o reagente limitante!"
                }
            ],
            "quiz": [
                {
                    "question": "A queima completa de 1 mol de gás metano (CH4, massa molar 16 g/mol) consome gás oxigênio e produz gás carbônico e água de acordo com a reação balanceada: CH4 + 2 O2 -> CO2 + 2 H2O. Qual é a massa de CO2 (massa molar 44 g/mol) produzida a partir da combustão de 32 g de metano?",
                    "options": [
                        "88 gramas",
                        "44 gramas",
                        "22 gramas",
                        "66 gramas"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Pela estequiometria da equação balanceada: 1 mol de CH4 (16 g) produz 1 mol de CO2 (44 g). Se queimamos 32 g de CH4 (o dobro: 2 mols), a massa de CO2 produzida será o dobro: 2 * 44 = 88 gramas."
                }
            ]
        },
        {
            "id": "nat-qui-26-solucoes-concentracao",
            "number": 26,
            "title": "26. Soluções e Concentrações: Molaridade, Diluição e Solubilidade",
            "epigraph": {
                "text": "Solução é uma mistura homogênea de soluto (o que se dissolve) e solvente (o que dissolve). Na diluição (C1*V1 = C2*V2), adiciona-se água, a concentração cai, mas a massa de soluto permanece constante.",
                "author": "Físico-Química de Soluções no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Tipos de Concentração mais Cobrados"
                },
                {
                    "type": "paragraph",
                    "content": "• Concentração Comum (C): C = m1 / V (massa do soluto em gramas dividida pelo volume total da solução em litros; unidade: g/L).\n• Concentração Molar / Molaridade (M ou [ ]): M = n1 / V = m1 / (M1 * V) (quantidade de matéria em mols de soluto por litro de solução; unidade: mol/L).\n• Título em Massa (tau) e ppm (partes por milhão): ppm é a razão entre a massa de soluto e a massa da solução multiplicada por 10^6 (usado para quantificar poluentes e contaminantes químicos em água potável: 1 ppm = 1 mg de soluto por 1 kg ou 1 litro de água)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Diluição de Soluções e Misturas"
                },
                {
                    "type": "paragraph",
                    "content": "Diluir significa adicionar mais solvente puro a uma solução já existente. A massa do soluto não muda:\nC1 * V1 = C2 * V2 (ou M1 * V1 = M2 * V2).\nComo o volume final V2 é maior que V1, a nova concentração C2 é obrigatoriamente menor que C1. Atenção: V2 = V1 + V_adicionado!"
                }
            ],
            "quiz": [
                {
                    "question": "Um técnico de laboratório dispõe de 100 mL de uma solução aquosa concentrada de ácido clorídrico (HCl) a 2,0 mol/L. Desejando preparar uma solução diluída a 0,5 mol/L para uso em análises clínicas, qual o volume de água destilada que ele deve adicionar à solução inicial?",
                    "options": [
                        "300 mL",
                        "400 mL",
                        "200 mL",
                        "150 mL"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Pela equação da diluição: M1 * V1 = M2 * V2 => 2,0 * 100 = 0,5 * V2 => 200 = 0,5 * V2 => V2 = 400 mL (volume final total). O volume de água que deve ser ADICIONADO é V_agua = V2 - V1 = 400 - 100 = 300 mL."
                }
            ]
        },
        {
            "id": "nat-qui-27-funcoes-inorganicas-ph",
            "number": 27,
            "title": "27. Funções Inorgânicas e pH: Ácidos, Bases, Sais, Óxidos e Neutralização",
            "epigraph": {
                "text": "Ácidos liberam íons H+ (H3O+) em água; bases liberam OH-. O pH mede a acidez em escala logarítmica: cada unidade a menos na escala de pH representa uma solução 10 vezes mais ácida.",
                "author": "Química Inorgânica no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Quatro Funções Inorgânicas de Arrhenius"
                },
                {
                    "type": "paragraph",
                    "content": "1. Ácidos: Compostos moleculares que se ionizam em meio aquoso liberando H+ (ex: HCl ácido clorídrico, H2SO4 ácido sulfúrico da chuva ácida e baterias, HNO3 ácido nítrico, H3PO4 refrigerantes de cola).\n2. Bases (Hidróxidos): Compostos iônicos que se dissociam liberando exclusivamente o ânion hidroxila OH- (ex: NaOH soda cáustica, Ca(OH)2 cal hidratada para neutralizar solo ácido, Mg(OH)2 leite de magnésia antiácido estomacal).\n3. Sais: Formados pela reação de neutralização entre um ácido e uma base (Ácido + Base -> Sal + Água; ex: HCl + NaOH -> NaCl + H2O).\n4. Óxidos: Compostos binários (dois elementos) onde o oxigênio é o mais eletronegativo:\n   - Óxidos Básicos (formados por metais alcalinos e alcalinoterrosos: Na2O, CaO): reagem com água formando bases fortes (a cal viva CaO reage com água gerando Ca(OH)2, usada na caiação e correção de acidez de solos!).\n   - Óxidos Ácidos ou Anidridos (formados por ametais: CO2, SO2, SO3, NO2): reagem com água da chuva gerando ácidos (os vilões da chuva ácida!)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Escala Logarítmica de pH e Indicadores"
                },
                {
                    "type": "paragraph",
                    "content": "A 25 °C, o produto iônico da água Kw = [H+] * [OH-] = 10^(-14):\n• pH = -log[H+] e pOH = -log[OH-]\n• pH + pOH = 14\n• Solução Neutra: pH = 7 ([H+] = [OH-] = 10^(-7) mol/L)\n• Solução Ácida: pH < 7 ([H+] > 10^(-7) mol/L)\n• Solução Básica (Alcalina): pH > 7 ([H+] < 10^(-7) mol/L).\nSe uma solução tem pH = 3 e outra tem pH = 5, a primeira é CEM VEZES mais ácida (10² = 100) que a segunda!"
                }
            ],
            "quiz": [
                {
                    "question": "Um agricultor detecta que o solo de sua plantação de milho está excessivamente ácido (pH = 4,5), o que impede a absorção eficiente de nutrientes pelas raízes. Qual substância inorgânica barata e acessível ele deve aplicar para realizar a calagem e elevar o pH do solo a níveis neutros?",
                    "options": [
                        "Calcário agrícola (CaCO3) ou cal virgem (CaO).",
                        "Ácido fosfórico concentrado (H3PO4).",
                        "Cloreto de sódio refinado (NaCl).",
                        "Sulfato de alumínio anidro (Al2(SO4)3)."
                    ],
                    "correctAnswer": 0,
                    "explanation": "A técnica de calagem utiliza óxido de cálcio (CaO) ou carbonato de cálcio (CaCO3, calcário). O óxido reage com a água formando hidróxido de cálcio (base) e o carbonato hidrolisa gerando íons básicos que neutralizam os íons H+ em excesso no solo, elevando o pH para a faixa ideal de cultivo."
                }
            ]
        },
        {
            "id": "nat-qui-28-termoquimica-entalpia",
            "number": 28,
            "title": "28. Termoquímica: Calor de Reação, Entalpia e Lei de Hess",
            "epigraph": {
                "text": "Reações exotérmicas liberam calor (delta_H < 0); reações endotérmicas absorvem calor (delta_H > 0). Pela Lei de Hess, a variação de entalpia depende exclusivamente dos estados inicial e final.",
                "author": "Termodinâmica Química no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Reações Exotérmicas vs Endotérmicas nos Gráficos do ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "• Variação de Entalpia (delta_H): delta_H = H_produtos - H_reagentes.\n• Reação Exotérmica (delta_H < 0): A energia dos reagentes é maior que a dos produtos. Há liberação de calor para o meio externo (a vizinhança aquece). Exemplos: toda reação de COMBUSTÃO (queima de gasolina, etanol, lenha, gás de cozinha), respiração celular e dissolução de soda cáustica em água.\n• Reação Endotérmica (delta_H > 0): A energia dos produtos é maior que a dos reagentes. Há absorção de calor do meio (a vizinhança resfria). Exemplos: fotossíntese, queima de calcário, bolsas de gelo instantâneo com nitrato de amônio e derretimento de gelo."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Lei de Hess: O Caminho das Equações Intermediárias"
                },
                {
                    "type": "paragraph",
                    "content": "A variação de entalpia de uma reação química é a soma das variações de entalpia das etapas intermediárias:\nRegras de Manipulação de Equações Termoquímicas:\n1. Se você INVERTER uma reação química, o sinal do delta_H DEVE SER INVERTIDO (se era negativo, fica positivo).\n2. Se você MULTIPLICAR ou DIVIDIR os coeficientes de uma equação por um número n, o valor do delta_H DEVE SER MULTIPLICADO ou DIVIDIDO pelo mesmo número n.\n3. Some as equações manipuladas cancelando termos idênticos opostos e some algebricamente os delta_H!"
                }
            ],
            "quiz": [
                {
                    "question": "A reação de combustão completa do gás hidrogênio (H2) é considerada uma fonte de energia limpa do futuro: 2 H2(g) + O2(g) -> 2 H2O(l) com delta_H = -572 kJ. Sobre esse processo, é correto afirmar que:",
                    "options": [
                        "Trata-se de uma reação exotérmica que libera 286 kJ de calor por mol de H2 consumido.",
                        "É uma reação endotérmica que absorve 572 kJ de calor da atmosfera.",
                        "A entalpia dos produtos formados é maior do que a entalpia dos gases reagentes.",
                        "A reação destrói a massa dos reagentes gerando energia elétrica direta."
                    ],
                    "correctAnswer": 0,
                    "explanation": "O sinal negativo (delta_H = -572 kJ) indica que a reação é exotérmica (libera calor). Como a equação balanceada consome 2 mols de H2 liberando 572 kJ, a queima de 1 mol de H2 libera exatamente 572 / 2 = 286 kJ."
                }
            ]
        },
        {
            "id": "nat-qui-29-cinetica-quimica-catalisadores",
            "number": 29,
            "title": "29. Cinética Química: Velocidade das Reações, Teoria das Colisões e Catalisadores",
            "epigraph": {
                "text": "Para que uma reação ocorra: contato, colisão orientada favorável e energia igual ou superior à Energia de Ativação. O catalisador cria um caminho alternativo de menor energia de ativação sem ser consumido.",
                "author": "Velocidade das Transformações no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Condições para Ocorrência de uma Reação (Teoria das Colisões)"
                },
                {
                    "type": "paragraph",
                    "content": "Nem toda colisão entre moléculas resulta em reação química. Para ser uma COLISÃO EFETIVA (ou eficaz):\n1. As moléculas devem colidir com ORIENTAÇÃO GEOMÉTRICA favorável.\n2. Devem possuir ENERGIA CINÉTICA mínima igual ou superior à ENERGIA DE ATIVAÇÃO (Ea) para formar o Complexo Ativado (estado de transição instável de máxima energia).\nQuanto menor a energia de ativação, mais fácil e mais rápida é a reação química!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fatores que Alteram a Velocidade da Reação"
                },
                {
                    "type": "paragraph",
                    "content": "• Temperatura: O aumento da temperatura aumenta a energia cinética média das moléculas, elevando drasticamente a frequência de colisões e a porcentagem de colisões com energia >= Ea (por isso a comida na geladeira demora mais para estragar: menor temperatura diminui a velocidade das reações de decomposição bacteriana!).\n• Superfície de Contato: Quanto mais triturado ou pulverizado o reagente sólido, maior a área exposta ao contato e mais rápida a reação (comprimido efervescente triturado dissolve muito mais rápido na água do que o comprimido inteiro).\n• Concentração dos Reagentes: Mais moléculas por unidade de volume aumentam a frequência de choques.\n• CATALISADORES (O Tópico Campeão do ENEM!): Aumentam a velocidade da reação criando um caminho alternativo com MENOR ENERGIA DE ATIVAÇÃO. Atenção crítica: O catalisador NÃO altera a entalpia (delta_H permanece idêntico), NÃO altera o rendimento e NÃO é consumido na reação (é totalmente regenerado ao final)!"
                }
            ],
            "quiz": [
                {
                    "question": "Os conversores catalíticos instalados no escapamento dos automóveis contêm metais nobres (como platina e paládio) que aceleram a conversão de gases tóxicos (como monóxido de carbono e óxidos de nitrogênio) em gases menos poluentes (CO2 e N2). A ação do catalisador nesse processo consiste em:",
                    "options": [
                        "Diminuir a energia de ativação da reação química sem alterar a variação de entalpia (delta_H).",
                        "Aumentar a temperatura dos gases para deslocar o equilíbrio térmico favorável.",
                        "Reagir estequiometricamente com os gases poluentes sendo consumido ao longo do tempo.",
                        "Tornar as reações endotérmicas mais exotérmicas elevando a energia do complexo ativado."
                    ],
                    "correctAnswer": 0,
                    "explanation": "A função biológica ou química de qualquer catalisador é diminuir a energia de ativação da reação química ao proporcionar um mecanismo alternativo de reação. O catalisador não altera a entalpia inicial e final do sistema, não altera a constante de equilíbrio e não é consumido no processo."
                }
            ]
        },
        {
            "id": "nat-qui-30-equilibrio-quimico-le-chatelier",
            "number": 30,
            "title": "30. Equilíbrio Químico e Princípio de Le Chatelier",
            "epigraph": {
                "text": "'Quando um sistema em equilíbrio sofre uma perturbação externa, ele se desloca no sentido que tende a minimizar ou anular essa perturbação.' — Henri Le Chatelier.",
                "author": "Princípio de Perturbação de Sistemas"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Estado de Equilíbrio Dinâmico"
                },
                {
                    "type": "paragraph",
                    "content": "Em uma reação química reversível em sistema fechado: aA + bB <=> cC + dD.\nO equilíbrio é atingido quando a VELOCIDADE da reação direta torna-se IGUAL à velocidade da reação inversa (v_direta = v_inversa). A partir desse instante, as CONCENTRAÇÕES de reagentes e produtos PERMANECEM CONSTANTES no tempo (embora as reações continuem ocorrendo nos dois sentidos em nível microscópico: equilíbrio dinâmico!).\nConstante de Equilíbrio em Concentração (Kc): Kc = [C]^c * [D]^d / ([A]^a * [B]^b). Sólidos puros e líquidos puros NÃO entram na expressão de Kc!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Deslocamento de Equilíbrio (Princípio de Le Chatelier)"
                },
                {
                    "type": "paragraph",
                    "content": "1. Efeito da Concentração: Adicionar uma substância desloca o equilíbrio para o LADO OPOSTO (para consumi-la); remover uma substância desloca o equilíbrio para o PRÓPRIO LADO (para repô-la).\n2. Efeito da Pressão (válido apenas para gases!): O aumento da pressão total desloca o equilíbrio para o lado de MENOR VOLUME gasoso (menor número de mols de gás); a diminuição da pressão desloca para o lado de maior volume gasoso.\n3. Efeito da Temperatura (o único que altera o valor numérico de Kc!):\n   - O aumento de temperatura favorece o sentido ENDOTÉRMICO (absorve o calor injetado).\n   - A diminuição de temperatura favorece o sentido EXOTÉRMICO (libera calor compensatório).\n4. Adição de Catalisador: NÃO DESLOCA O EQUILÍBRIO! Apenas faz o sistema atingir o estado de equilíbrio mais rápido."
                }
            ],
            "quiz": [
                {
                    "question": "A síntese da amônia pelo processo Haber-Bosch é uma reação gasosa reversível e exotérmica: N2(g) + 3 H2(g) <=> 2 NH3(g) (delta_H = -92 kJ). Qual das seguintes intervenções aumentará o rendimento na produção de amônia no equilíbrio?",
                    "options": [
                        "Aumentar a pressão total sobre o sistema e operar sob temperatura moderadamente resfriada.",
                        "Diminuir a pressão total e aumentar a temperatura da câmara de reação.",
                        "Adicionar mais catalisador de ferro metálico ao reator químico.",
                        "Remover continuamente gás hidrogênio e gás nitrogênio da mistura."
                    ],
                    "correctAnswer": 0,
                    "explanation": "No lado dos reagentes temos 1 + 3 = 4 mols de gás; no lado do produto temos apenas 2 mols de gás. O aumento de pressão desloca para o lado de menor volume (formação de NH3). Como a reação direta é exotérmica (libera calor), o abaixamento da temperatura favorece a síntese de NH3. Portanto, alta pressão e menor temperatura elevam o rendimento."
                }
            ]
        },
        {
            "id": "nat-qui-31-eletroquimica-pilhas-eletrolise",
            "number": 31,
            "title": "31. Eletroquímica: Pilhas, Potencial de Redução, Corrosão e Eletrólise",
            "epigraph": {
                "text": "Quem oxida dá elétrons (ânodo, polo negativo na pilha); quem reduz recebe elétrons (cátodo, polo positivo). A eletroquímica gera energia espontânea nas pilhas e consome energia na eletrólise.",
                "author": "Guia de Eletroquímica no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Pilhas Galvânicas (Processo Espontâneo, delta_E > 0)"
                },
                {
                    "type": "paragraph",
                    "content": "Uma pilha converte energia química em energia elétrica espontânea (Pilha de Daniell: Zn e Cu):\n• Mnemônica Universal 'CRAO': Cátodo Reduz, Ânodo Oxida.\n• Ânodo (Polo Negativo): Sofre OXIDAÇÃO (perda de elétrons, aumento do nox). A barra metálica é corroída e sua massa DIMINUI.\n• Cátodo (Polo Positivo): Sofre REDUÇÃO (ganho de elétrons, redução do nox). A barra metálica recebe depósito de metal e sua massa AUMENTA.\n• Sentido dos elétrons pelo fio externo: SEMPRE do ÂNODO para o CÁTODO (do negativo para o positivo).\n• Diferença de Potencial (DDP / delta_E°): delta_E° = E°_redução_maior - E°_redução_menor. O elemento que tiver maior potencial padrão de redução reduz obrigatoriamente!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Proteção contra Corrosão: O Metal de Sacrifício"
                },
                {
                    "type": "paragraph",
                    "content": "O ferro (Fe) oxida facilmente em presença de água e oxigênio formando ferrugem (Fe2O3.nH2O). Para proteger cascos de navios de aço e tubulações enterradas, conecta-se ao ferro blocos de um METAL DE SACRIFÍCIO (como Magnésio Mg ou Zinco Zn):\nO metal de sacrifício possui MENOR potencial de redução (ou seja, MAIOR facilidade de oxidação que o ferro). Por isso, ele OXIDA PREFERENCIALMENTE no lugar do ferro, preservando a estrutura de aço intacta!"
                }
            ],
            "quiz": [
                {
                    "question": "Dados os potenciais padrão de redução: E°(Fe²+/Fe) = -0,44 V e E°(Mg²+/Mg) = -2,37 V. Ao fixar placas de magnésio metálico no casco de aço (ferro) de uma embarcação marinha, o magnésio protege o ferro da ferrugem porque:",
                    "options": [
                        "Possui menor potencial de redução que o ferro, oxidando-se preferencialmente como metal de sacrifício.",
                        "Reveste o ferro com uma camada plástica isolante que bloqueia o oxigênio da água.",
                        "Reduz o ferro a cátions férricos impedindo a passagem de corrente elétrica.",
                        "Atua como catalisador inerte que bloqueia a perda de elétrons da água do mar."
                    ],
                    "correctAnswer": 0,
                    "explanation": "Como E°(Mg) = -2,37 V é muito mais negativo que E°(Fe) = -0,44 V, o magnésio possui muito maior tendência espontânea a oxidar (perder elétrons) do que o ferro. Ele se corrói voluntariamente, doando elétrons ao ferro e impedindo que o aço oxide (proteção catódica por metal de sacrifício)."
                }
            ]
        },
        {
            "id": "nat-qui-32-quimica-organica-funcoes",
            "number": 32,
            "title": "32. Química Orgânica: Cadeias, Funções Oxigenadas/Nitrogenadas e Polímeros",
            "epigraph": {
                "text": "O carbono é tetravalente (faz 4 ligações) e forma cadeias estáveis. Identificar grupos funcionais e reconhecer polímeros do dia a dia garante de 3 a 5 questões na prova de Ciências da Natureza.",
                "author": "Química do Carbono no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Guia Visual das Funções Orgânicas no ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "• Hidrocarbonetos (apenas C e H): Apolares, combustíveis (metano, propano, gasolina, diesel, querosene).\n• Álcool: Hidroxila (-OH) ligada a carbono saturado (ex: etanol C2H5OH, biocombustível e antisséptico).\n• Fenol: Hidroxila (-OH) ligada diretamente a anel aromático (benzeno).\n• Aldeído: Carbonila na extremidade da cadeia (-CHO; ex: metanal / formol).\n• Cetona: Carbonila entre dois carbonos (-C(=O)-; ex: propanona / acetona removedora de esmalte).\n• Ácido Carboxílico: Carboxila (-COOH; ex: ácido acético do vinagre, ácidos graxos dos óleos).\n• Éster: Derivado de ácido carboxílico com oxigênio na cadeia (-COO-R; responsáveis pelo aroma e sabor de frutas em alimentos industrializados / flavorizantes e produção de biodiesel).\n• Amina: Derivada da amônia com substituição por carbonos (-NH2, -NHR; caráter básico, cheiro de peixe podre).\n• Amida: Carbonila ligada diretamente a nitrogênio (-CO-NH2; presente nas ligações peptídicas que unem aminoácidos formando proteínas!)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Polímeros Sintéticos e Biodegradação"
                },
                {
                    "type": "paragraph",
                    "content": "Polímeros são macromoléculas formadas pela repetição de unidades menores chamadas monômeros:\n• Polímeros de Adição: Polietileno (PE, sacolas plásticas), Polipropileno (PP, potes plásticos), PVC (tubos e conexões hidráulicas) e Poliestireno (isopor).\n• Polímeros de Condensação: Formados com eliminação de pequenas moléculas (como água): PET (garrafas plásticas / poliéster), Náilon (poliamida) e Kevlar (coletes à prova de balas)."
                }
            ],
            "quiz": [
                {
                    "question": "A aspirina (ácido acetilsalicílico) é um fármaco amplamente consumido que apresenta em sua estrutura molecular um anel aromático ligado a um grupo carboxila (-COOH) e a um grupo éster (-O-CO-CH3). Quais são as duas funções orgânicas oxigenadas presentes na molécula da aspirina?",
                    "options": [
                        "Ácido carboxílico e éster",
                        "Álcool e cetona",
                        "Fenol e aldeído",
                        "Éter e amida"
                    ],
                    "correctAnswer": 0,
                    "explanation": "A presença do grupo -COOH caracteriza a função ácido carboxílico, e a presença do grupo -COO- ligado a radicais carbônicos caracteriza a função éster."
                }
            ]
        },
        {
            "id": "nat-qui-33-quimica-ambiental-sustentabilidade",
            "number": 33,
            "title": "33. Química Ambiental e Sustentabilidade: Chuva Ácida, Efeito Estufa e Tratamento de Água",
            "epigraph": {
                "text": "A química ambiental avalia o impacto dos ciclos de materiais e poluentes no equilíbrio planetário. Saber como tratar a água e combater a chuva ácida é exigência constante do ENEM.",
                "author": "Química Verde e Cidadania"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Chuva Ácida e Gases de Efeito Estufa"
                },
                {
                    "type": "paragraph",
                    "content": "• Chuva Ácida: Toda chuva natural é ligeiramente ácida (pH ~5,6) devido ao CO2 dissolvido formando ácido carbônico fraco (H2CO3). A chuva torna-se prejudicialmente ácida (pH < 4,5) pela queima de combustíveis fósseis (carvão e óleo diesel) contendo impurezas de ENXOFRE (S) e nitrogênio do ar nos motores a combustão:\nS + O2 -> SO2\n2 SO2 + O2 -> 2 SO3\nSO3 + H2O -> H2SO4 (Ácido Sulfúrico, corrosivo, destrói monumentos de mármore CaCO3, acidifica lagos e queima florestas).\n• Gases do Efeito Estufa: Dióxido de carbono (CO2, queima de fósseis e desmatamento), Metano (CH4, pecuária entérica, decomposição anaeróbia em lixões e plantações de arroz) e Óxido Nitroso (N2O)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Etapas de uma Estação de Tratamento de Água (ETA)"
                },
                {
                    "type": "paragraph",
                    "content": "A sequência oficial cobrada no ENEM para transformar água de rio em água potável:\n1. Coagulação: Adição de Sulfato de Alumínio Al2(SO4)3 para aglutinar partículas coloidais de sujeira.\n2. Floculação: Agitação lenta para formar flocos maiores e mais densos de sujeira.\n3. Decantação: Os flocos pesados afundam por gravidade no fundo do tanque sedimentador.\n4. Filtração: A água passa por camadas de areia, cascalho e carvão ativado (retém partículas finas e odores).\n5. Cloração (Desinfecção Química): Adição de cloro ou hipoclorito de sódio para matar bactérias e patógenos.\n6. Fluoretação: Adição de flúor para prevenção de cáries na população infantil."
                }
            ],
            "quiz": [
                {
                    "question": "Em uma Estação de Tratamento de Água (ETA), a etapa em que a água permanece em repouso permitindo que os flocos pesados de sujeira formados na coagulação afundem e se depositem no fundo do tanque pelo efeito da gravidade é denominada:",
                    "options": [
                        "Decantação",
                        "Filtração",
                        "Fluoretação",
                        "Cloração"
                    ],
                    "correctAnswer": 0,
                    "explanation": "A decantação é um processo físico mecânico de separação de misturas heterogêneas sólido-líquido baseado na diferença de densidade, no qual as partículas mais densas (flocos formados após a coagulação e floculação) sedimentam no fundo do tanque pela ação da gravidade."
                }
            ]
        }
    ]
