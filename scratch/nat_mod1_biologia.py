# -*- coding: utf-8 -*-
"""Eixo 1: Biologia Completa ENEM (Capítulos 1 a 9)"""

def get_chapters():
    return [
        {
            "id": "nat-bio-01-ecologia-dinamica",
            "number": 1,
            "title": "1. Ecologia e Dinâmica dos Ecossistemas: Cadeias, Teias e Ciclos",
            "epigraph": {
                "text": "Ecologia é a disciplina mais cobrada em Ciências da Natureza no ENEM, correspondendo a mais de 30% das questões de Biologia em quase todas as edições.",
                "author": "Estatística Oficial da Prova de Ciências da Natureza"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fluxo de Energia Unidirecional e Pirâmides Ecológicas"
                },
                {
                    "type": "paragraph",
                    "content": "Nos ecossistemas, a energia flui de maneira estritamente UNIDIRECIONAL e decrescente ao longo dos níveis tróficos: Produtores (autótrofos fotossintetizantes) -> Consumidores Primários (herbívoros) -> Consumidores Secundários (carnívoros) -> Consumidores Terciários. A cada nível trófico, cerca de 90% da energia é dissipada na forma de calor metabólico (respiração, locomoção e excreção), restando apenas cerca de 10% para o nível seguinte (Lei dos 10%). Por isso, a pirâmide de ENERGIA NUNCA pode ser invertida!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Relações Ecológicas e Ciclos Biogeoquímicos"
                },
                {
                    "type": "paragraph",
                    "content": "• Relações Harmônicas (positivas, sem prejuízo): Mutualismo (+/+ obrigatório, como líquens e micorrizas), Protocooperação (+/+ facultativo), Comensalismo (+/0 para alimentação) e Inquilinismo (+/0 para suporte, como epífitas em árvores).\n• Relações Desarmônicas (-): Predatismo (+/-), Parasitismo (+/-), Competição intra e interespecífica (-/-) e Amensalismo ou Antibiose (-/0).\n• Ciclo do Nitrogênio (o mais cobrado no ENEM!): Fixação (bactérias Rhizobium em leguminosas transformam N2 em NH3/NH4+) -> Nitrosação (Nitrosomonas transformam amônia em nitrito NO2-) -> Nitratação (Nitrobacter transformam nitrito em nitrato NO3-, assimilável pelas plantas) -> Desnitrificação (bactérias Pseudomonas devolvem N2 à atmosfera em solos anaeróbios)."
                },
                {
                    "type": "callout",
                    "title": "Atenção ao Distrator no ENEM: Sucessão Ecológica",
                    "content": "• Sucessão Primária: Ocorre em ambientes estéreis e nunca antes habitados (rocha nua, lava vulcânica resfriada, dunas). As espécies pioneiras são os líquens e musgos.\n• Sucessão Secundária: Ocorre em ambientes onde já existia uma comunidade, mas que foi desmatada, queimada ou abandonada. Ocorre muito mais rapidamente porque o solo já está formado e rico em nutrientes e sementes dormentes."
                }
            ],
            "quiz": [
                {
                    "question": "A rotação de culturas com leguminosas (como a soja e o feijão) é uma prática agrícola sustentável que melhora a fertilidade do solo porque:",
                    "options": [
                        "Possui bactérias mutualísticas nas raízes capazes de fixar o nitrogênio atmosférico.",
                        "Absorve diretamente gás nitrogênio através das folhas e o libera pelas raízes.",
                        "Elimina todas as bactérias desnitrificantes presentes nas camadas profundas do solo.",
                        "Aumenta a acidez do solo convertendo nitratos em amônia volátil."
                    ],
                    "correctAnswer": 0,
                    "explanation": "As leguminosas estabelecem relação mutualística com bactérias do gênero Rhizobium em nódulos radiculares. Essas bactérias convertem o N2 atmosférico em compostos nitrogenados assimiláveis, enriquecendo naturalmente o solo sem necessidade de fertilizantes químicos."
                }
            ]
        },
        {
            "id": "nat-bio-02-meio-ambiente-impactos",
            "number": 2,
            "title": "2. Meio Ambiente, Biomas Brasileiros e Impactos Antrópicos",
            "epigraph": {
                "text": "Eutrofização, magnificação trófica, efeito estufa e características dos biomas brasileiros caem todos os anos. O ENEM cobra a causa biológica, a consequência ecológica e a solução tecnológica.",
                "author": "Matriz de Ciências da Natureza"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Biomas Brasileiros: Adaptações Morfofisiológicas"
                },
                {
                    "type": "paragraph",
                    "content": "• Cerrado (a savana brasileira): Solos ácidos, pobres em nutrientes e ricos em alumínio tóxico; árvores com casca grossa (cortiça protetora contra o fogo natural), troncos tortuosos e raízes profundas (capazes de atingir o lençol freático).\n• Caatinga: Clima semiárido; xerofitismo extremo; folhas reduzidas ou modificadas em espinhos (para evitar a perda de água por transpiração); caules verdes fotossintetizantes e suculentos com armazenamento de água (parênquima aquífero nas cactáceas).\n• Amazônia e Mata Atlântica: Florestas pluviais tropicais; estratificadas, alta umidade, folhas latifoliadas (largas) e epifitismo abundante.\n• Pantanal: Maior planície inundável contínua do planeta, mosaico ecológico sob regime de cheias e secas periódicas."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Impactos Ambientais Críticos no ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "1. Eutrofização: Lançamento de esgoto ou fertilizantes agrícolas ricos em N e P em corpos d'água -> Proliferação explosiva de algas superficiais (bloqueando a luz solar) -> Morte dos vegetais submersos por falta de fotossíntese -> Proliferação maciça de bactérias decompositoras aeróbicas -> Esgotamento do oxigênio dissolvido (anóxia) -> Morte em massa de peixes e proliferação de anaeróbios produtores de gás sulfídrico.\n2. Magnificação Trófica (Bioacumulação): Substâncias não biodegradáveis e lipossolúveis (como mercúrio e agrotóxicos organoclorados) ACUMULAM-SE progressivamente ao longo dos níveis tróficos, atingindo a concentração MÁXIMA no TOPO da cadeia alimentar (predadores de topo e o ser humano)!"
                }
            ],
            "quiz": [
                {
                    "question": "Em uma baía poluída por mercúrio proveniente de rejeitos industriais, foram analisados quatro organismos: fitoplâncton, zooplâncton, pequenos peixes e gaivotas carnívoras. Em qual desses organismos será encontrada a MAIOR concentração de mercúrio por grama de tecido?",
                    "options": [
                        "Gaivotas carnívoras",
                        "Fitoplâncton",
                        "Zooplâncton",
                        "Pequenos peixes"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Por se tratar de um poluente não biodegradável e cumulativo (magnificação trófica), a concentração da substância tóxica aumenta exponencialmente a cada nível trófico, atingindo a concentração máxima no predador de topo da cadeia (as gaivotas carnívoras)."
                }
            ]
        },
        {
            "id": "nat-bio-03-citologia-celula",
            "number": 3,
            "title": "3. Citologia: Teoria Celular, Organelas e Transporte através da Membrana",
            "epigraph": {
                "text": "A célula é a unidade morfofuncional da vida. Compreender a membrana plasmática e a especialização das organelas é a base para decodificar biotecnologia e fisiologia.",
                "author": "Guia de Citologia ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Diferença Procarionte vs Eucarionte"
                },
                {
                    "type": "paragraph",
                    "content": "• Célula Procarionte (Bactérias e Arqueas): NÃO possui carioteca (núcleo delimitado por membrana); DNA circular disperso no nucleoide; NÃO possui organelas membranosas (sem mitocôndrias, sem complexo golgiense); possui apenas ribossomos 70S para síntese proteica; possui parede celular de peptideoglicano.\n• Célula Eucarionte (Animais, Vegetais, Fungos e Protozoários): Núcleo verdadeiro delimitado por dupla membrana (carioteca); DNA linear associado a proteínas histonas; rico sistema de endomembranas e organelas compartimentadas."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Mapa das Organelas Celulares e Suas Funções"
                },
                {
                    "type": "paragraph",
                    "content": "• Mitocôndria: Respiração celular aeróbica e síntese de ATP (possui DNA próprio e herança estritamente materna; Teoria Endossimbiótica).\n• Ribossomos: Síntese de proteínas.\n• Retículo Endoplasmático Rugoso (com ribossomos): Síntese de proteínas de exportação e enzimas lisossomais.\n• Retículo Endoplasmático Liso: Síntese de lipídios (colesterol, fosfolipídios, hormônios esteroides) e desintoxicação celular (metabolização de álcool e medicamentos no fígado).\n• Complexo Golgiense: Modificação, empacotamento, secreção celular e formação do acrossomo do espermatozoide e dos lisossomos.\n• Lisossomos: Digestão intracelular (autofagia e heterofagia).\n• Peroxissomos: Degradação de peróxido de hidrogênio (água oxigenada) pela enzima catalase."
                },
                {
                    "type": "callout",
                    "title": "Transporte de Membrana: Osmose e Soluções",
                    "content": "• Osmose: Movimento passivo exclusivo de ÁGUA do meio hipotônico (menos concentrado em soluto) para o meio hipertônico (mais concentrado em soluto).\n• Hemácia em meio hipertônico (muito salgado): perde água e encolhe (crenação).\n• Hemácia em meio hipotônico (água destilada): ganha água, incha e sofre lise (arrebenta).\n• Célula vegetal em meio hipotônico: ganha água, fica TURGIDA, mas NÃO arrebenta devido à resistência mecânica da parede celular de celulose!"
                }
            ],
            "quiz": [
                {
                    "question": "Um paciente submetido a quimioterapia faz uso de um medicamento que bloqueia a síntese de fosfolipídios e lipídios esteroides na célula. Qual organela citoplasmática terá sua atividade primária mais diretamente prejudicada?",
                    "options": [
                        "Retículo endoplasmático liso",
                        "Complexo golgiense",
                        "Ribossomo",
                        "Lisossomo"
                    ],
                    "correctAnswer": 0,
                    "explanation": "O retículo endoplasmático liso (ou agranular) é a organela responsável pela síntese de lipídios celulares (como esteroides e fosfolipídios da membrana) e pela desintoxicação de substâncias químicas."
                }
            ]
        },
        {
            "id": "nat-bio-04-metabolismo-bioenergetica",
            "number": 4,
            "title": "4. Metabolismo e Bioenergética: Respiração Celular, Fermentação e Fotossíntese",
            "epigraph": {
                "text": "O ATP é a moeda energética universal da célula. A respiração oxida compostos orgânicos para gerar energia; a fotossíntese fixa a energia luminosa em matéria orgânica estável.",
                "author": "Bioenergética Celular no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Respiração Celular Aeróbica em Três Etapas"
                },
                {
                    "type": "paragraph",
                    "content": "A equação geral da respiração é: C6H12O6 + 6 O2 -> 6 CO2 + 6 H2O + ~30-32 ATP.\n1. Glicólise (ocorre no hialoplasma/citosol): Quebra da glicose (6C) em dois piruvatos (3C). Etapa estritamente anaeróbica, com saldo líquido de 2 ATP e 2 NADH.\n2. Ciclo de Krebs ou do Ácido Cítrico (ocorre na matriz mitocondrial): Oxidação completa do acetil-CoA, liberando CO2 e gerando NADH, FADH2 e 2 ATP.\n3. Cadeia Respiratória e Fosforilação Oxidativa (ocorre nas cristas mitocondriais): Transporte de elétrons de alta energia gerando gradiente de prótons (H+) que alimenta a enzima ATP Sintase. O OXIGÊNIO (O2) atua como o ACEPTOR FINAL DE ELÉTRONS E PRÓTONS, formando água (H2O). Se faltar O2 ou se houver venenos como cianeto, a cadeia para e a célula morre por asfixia bioquímica!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fermentação: Estratégia Anaeróbica Emergencial"
                },
                {
                    "type": "paragraph",
                    "content": "Na ausência de O2, o piruvato não entra na mitocôndria. A célula realiza fermentação para regenerar o NAD+ e manter a glicólise funcionando (saldo de apenas 2 ATP por glicose):\n• Fermentação Lática: Realizada por bactérias láticas (iogurtes, queijos) e pelas fibras musculares humanas esqueléticas em esforço intenso com débito de oxigênio (produzindo ácido lático).\n• Fermentação Alcoólica: Realizada por leveduras (Saccharomyces cerevisiae), transformando piruvato em ETANOL e CO2 (utilizado na produção de pães, cervejas e biocombustíveis)."
                }
            ],
            "quiz": [
                {
                    "question": "Na fabricação de pães caseiros, adiciona-se fermento biológico à massa, que é deixada em repouso até dobrar de volume antes de ser assada. O crescimento característico da massa do pão decorre da liberação de:",
                    "options": [
                        "Dióxido de carbono (CO2) produzido pela fermentação alcoólica das leveduras.",
                        "Gás oxigênio (O2) liberado na fase clara da fotossíntese celular.",
                        "Etanol gasoso que evapora à temperatura ambiente inflando a massa.",
                        "Ácido lático que reage com a farinha desprendendo vapor de água."
                    ],
                    "correctAnswer": 0,
                    "explanation": "As leveduras do fermento biológico realizam fermentação alcoólica na massa, consumindo açúcares e liberando dióxido de carbono (CO2) e etanol. O CO2 forma bolhas presas na rede de glúten, fazendo a massa expandir e crescer."
                }
            ]
        },
        {
            "id": "nat-bio-05-divisao-celular",
            "number": 5,
            "title": "5. Divisão Celular: Mitose, Meiose e Ciclo Celular",
            "epigraph": {
                "text": "A mitose mantém a ploidia e a identidade genética para crescimento e cicatrização; a meiose reduz a ploidia pela metade e gera variabilidade genética para a reprodução sexuada.",
                "author": "Genética e Biologia do Desenvolvimento"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Ciclo Celular e a Intérfase"
                },
                {
                    "type": "paragraph",
                    "content": "A intérfase é o período de intensa atividade metabólica que antecede a divisão celular:\n• Fase G1: Crescimento celular, transcrição e síntese proteica intensa.\n• Fase S (Síntese): REPLICAÇÃO SEMICONSERVATIVA DO DNA. A quantidade de material genético é duplicada (de 2c para 4c), formando as cromátides-irmãs unidas pelo centrômero.\n• Fase G2: Síntese de proteínas para o fuso mitótico e checagem final (pontos de controle do ciclo celular; mutações aqui geram câncer)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Mitose vs Meiose: Quadro Comparativo de Ouro"
                },
                {
                    "type": "paragraph",
                    "content": "• Mitose (Divisão Equacional): 1 célula-mãe (2n) gera 2 células-filhas (2n) geneticamente idênticas. Fases: Prófase (condensação dos cromossomos e desintegração da carioteca) -> Metáfase (cromossomos alinhados na placa equatorial com condensação máxima) -> Anáfase (SEPARAÇÃO DAS CROMÁTIDES-IRMÃS) -> Telófase (reconstituição nuclear e citocinese).\n• Meiose (Divisão Reducional e Equacional): 1 célula-mãe (2n) gera 4 células-filhas haploides (n). Ocorrência do CROSSING-OVER (permutação gênica) na Prófase I (subfase paquíteno), gerando novas combinações de alelos e garantindo a variabilidade genética da espécie!"
                }
            ],
            "quiz": [
                {
                    "question": "A colchicina é uma droga antimitótica que se liga à tubulina e impede a formação e a polimerização dos microtúbulos do fuso acromático. Em qual fase da mitose as células tratadas com colchicina ficarão interrompidas?",
                    "options": [
                        "Metáfase",
                        "Anáfase",
                        "Telófase",
                        "Intérfase"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Sem microtúbulos funcionais do fuso acromático, os cromossomos atingem a condensação máxima mas não conseguem ser tracionados para os polos opostos na anáfase. As células ficam paradas na metáfase (técnica amplamente utilizada para construir cariótipos humanos em laboratório)."
                }
            ]
        },
        {
            "id": "nat-bio-06-genetica-biotecnologia",
            "number": 6,
            "title": "6. Genética e Biotecnologia: Leis de Mendel, DNA Recombinante e Transgênicos",
            "epigraph": {
                "text": "Da transmissão das ervilhas de Mendel à edição gênica por CRISPR-Cas9, a genética moderna é um dos temas mais valorizados no ENEM pela sua interdisciplinaridade com saúde e agricultura.",
                "author": "Matriz de Biotecnologia do INEP"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Leis de Mendel e Hereditariedade"
                },
                {
                    "type": "paragraph",
                    "content": "• 1ª Lei de Mendel (Lei da Segregação dos Fatores): Cada característica é determinada por um par de fatores (alelos) que se separam na formação dos gametas. Cruzamento heterozigoto Aa x Aa gera proporção genotípica 1 AA : 2 Aa : 1 aa e proporção fenotípica 3 dominantes : 1 recessivo (75% : 25%).\n• Sistema ABO: Exemplo clássico de alelos múltiplos (polialelia) e codominância (IA e IB são codominantes entre si e ambos dominam sobre i). Sangue O é o doador universal de hemácias (não possui antígenos A nem B); sangue AB é o receptor universal (não possui anticorpos anti-A nem anti-B no plasma).\n• Fator Rh e Eritroblastose Fetal: Ocorre quando mãe Rh- (previamente sensibilizada) gera feto Rh+. Os anticorpos anti-Rh maternos atravessam a placenta e destroem as hemácias do feto."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Biotecnologia: Transgênicos vs Clonagem"
                },
                {
                    "type": "paragraph",
                    "content": "• Organismo Geneticamente Modificado (OGM) / Transgênico: Recebeu e incorporou de forma estável genes de OUTRA espécie diferente (exemplo: milho Bt que recebeu gene da bactéria Bacillus thuringiensis para produzir toxina inseticida; soja resistente ao glifosato). Enzimas de restrição ('tesouras moleculares') cortam o DNA em sítios específicos e a DNA ligase une os fragmentos ao plasmídeo bacteriano.\n• Clonagem Reprodutiva: Transferência do núcleo diploide de uma célula somática adulta para um óvulo anucleado, gerando um indivíduo geneticamente IDÊNTICO ao doador do núcleo (sem combinação de gametas)."
                }
            ],
            "quiz": [
                {
                    "question": "Um casal procura aconselhamento genético. Ambos possuem visão normal para cores, mas o pai da mulher era daltônico (característica recessiva ligada ao cromossomo X). Qual é a probabilidade de esse casal ter uma criança do sexo masculino e daltônica?",
                    "options": [
                        "1/4 (25%)",
                        "1/2 (50%)",
                        "1/8 (12,5%)",
                        "0%"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Homem normal: X^D Y. Mulher: como seu pai era daltônico (X^d Y), ela recebeu obrigatoriamente o alelo recessivo, sendo heterozigota portadora: X^D X^d. Cruzamento: X^D X^D (menina normal), X^D X^d (menina portadora), X^D Y (menino normal), X^d Y (menino daltônico). A probabilidade de ser menino E daltônico é 1/4 (25%)."
                }
            ]
        },
        {
            "id": "nat-bio-07-evolucao-especies",
            "number": 7,
            "title": "7. Evolução Biológica: Darwinismo, Neodarwinismo e Especiação",
            "epigraph": {
                "text": "'Nada na biologia faz sentido exceto à luz da evolução.' — Theodosius Dobzhansky. O ENEM adora confrontar Lamarck e Darwin em contextos cotidianos de resistência bacteriana e camuflagem.",
                "author": "Fundamento Teórico da Biologia Moderna"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Lamarckismo vs Darwinismo vs Neodarwinismo"
                },
                {
                    "type": "paragraph",
                    "content": "• Lamarckismo: Lei do Uso e Desuso (órgãos muito utilizados desenvolvem-se; órgãos em desuso atrofiam) e Lei da Transmissão dos Caracteres Adquiridos. O meio ambiente MODIFICA o indivíduo de forma ativa e direcionada para adaptá-lo (erro conceitual).\n• Darwinismo: SELEÇÃO NATURAL. Os indivíduos de uma mesma espécie apresentam variações naturais pré-existentes. O meio ambiente NÃO induz a variação; ele apenas ATUA SELECIONANDO os indivíduos portadores das variações mais vantajosas que sobrevivem e deixam mais descendentes (reprodução diferencial).\n• Neodarwinismo (Teoria Sintética da Evolução): Incorpora a genética que Darwin desconhecia: as fontes primárias de variabilidade genética são as MUTAÇÕES GÊNICAS aleatórias e a RECOMBINAÇÃO GÊNICA (crossing-over e segregação independente)."
                },
                {
                    "type": "callout",
                    "title": "A Clássica Armadilha do Antibiótico no ENEM",
                    "content": "O uso indiscriminado de antibióticos NÃO 'torna as bactérias resistentes' nem 'induz mutações adaptativas'! As bactérias resistentes JÁ EXISTIAM previamente na população devido a mutações aleatórias. O antibiótico atua apenas como um poderoso AGENTE SELETOR: elimina as sensíveis e seleciona as resistentes sobreviventes, que se multiplicam livremente!"
                }
            ],
            "quiz": [
                {
                    "question": "O aparecimento de linhagens bacterianas multirresistentes em hospitais é explicado evolutivamente pelo fato de que o antibiótico:",
                    "options": [
                        "Atua como agente seletivo que elimina as bactérias sensíveis e preserva as resistentes pré-existentes.",
                        "Provoca mutações específicas no genoma bacteriano para conferir proteção contra a droga.",
                        "Induz o desuso de proteínas de membrana fazendo com que as bactérias se adaptem ativamente.",
                        "Estimula a recombinação gênica entre bactérias e células imunes do hospedeiro."
                    ],
                    "correctAnswer": 0,
                    "explanation": "Pela Teoria Sintética da Evolução, as mutações que conferem resistência bacteriana ocorrem ao acaso, de forma prévia. O antibiótico não cria nem induz a resistência; ele atua selecionando as variantes resistentes pré-existentes ao exterminar as sensíveis."
                }
            ]
        },
        {
            "id": "nat-bio-08-fisiologia-humana",
            "number": 8,
            "title": "8. Fisiologia Humana Comparada: Sistemas Vitais e Homeostase",
            "epigraph": {
                "text": "O corpo humano funciona em harmonia sinérgica para manter o equilíbrio dinâmico interno (homeostase). O ENEM foca nas conexões entre digestão, circulação, respiração, excreção e controle hormonal.",
                "author": "Fisiologia e Saúde no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sistema Digestório e pH das Enzimas"
                },
                {
                    "type": "paragraph",
                    "content": "• Boca: pH neutro (~7,0). A amilase salivar (ptialina) inicia a digestão de amido em maltose.\n• Estômago: pH fortemente ácido (~2,0) devido ao ácido clorídrico (HCl). A pepsina inicia a quebra de proteínas em peptídeos.\n• Duodeno (Intestino Delgado): pH básico (~8,0) neutralizado pelo bicarbonato do suco pancreático. Ocorre a digestão completa de carboidratos, proteínas e lipídios. A BILE (produzida no fígado e armazenada na vesícula biliar) NÃO possui enzimas: sua função é estritamente a EMULSIFICAÇÃO DE GORDURAS (age como detergente biológico, transformando gotas grandes em gotículas para ampliar a superfície de contato da enzima lipase pancreática)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sistema Circulatório e Excretor"
                },
                {
                    "type": "paragraph",
                    "content": "• Coração Humano: 4 cavidades (2 átrios e 2 ventrículos). Lado direito conduz exclusivamente sangue venoso (rico em CO2) em direção aos pulmões (pequena circulação). Lado esquerdo recebe sangue arterializado (oxigenado) dos pulmões e bombeia para todo o corpo pela artéria aorta (grande circulação).\n• Néfron e Fisiologia Renal: Filtração glomerular na cápsula de Bowman -> Reabsorção tubular ativa (glicose e aminoácidos são 100% reabsorvidos) -> Alça de Henle e Túbulo Coletor regulados pelo hormônio ADH (Antidiurético / Vasopressina). Quando você bebe álcool, o ADH é inibido na hipófise, provocando diurese intensa (urina clara e volumosa) e desidratação (ressaca)."
                }
            ],
            "quiz": [
                {
                    "question": "Um paciente que teve a vesícula biliar removida cirurgicamente (colecistectomia) recebe a recomendação médica de reduzir drasticamente a ingestão de alimentos gordurosos. Essa orientação se justifica porque:",
                    "options": [
                        "O paciente perdeu a capacidade de emulsionar eficientemente as gorduras devido à falta de armazenamento e liberação concentrada da bile.",
                        "A digestão das gorduras pelo suco gástrico no estômago foi completamente interrompida.",
                        "O fígado deixa de produzir a enzima lipase responsável pela quebra direta dos triglicerídeos.",
                        "As gorduras passam a ser absorvidas intactas pela mucosa estomacal causando acidose metabólica."
                    ],
                    "correctAnswer": 0,
                    "explanation": "A vesícula biliar não produz a bile (quem produz é o fígado), mas a armazena e concentra. Sem a vesícula, a bile goteja continuamente em pequenas quantidades no intestino, tornando a emulsificação de grandes refeições gordurosas insuficiente e provocando desconfortos gastrointestinais."
                }
            ]
        },
        {
            "id": "nat-bio-09-saude-imunizacao-doencas",
            "number": 9,
            "title": "9. Saúde Pública, Imunização, Doenças Infecciosas e ISTs",
            "epigraph": {
                "text": "Vacina é prevenção primária e confere imunidade ativa e duradoura com memória celular. Soro é tratamento curativo emergencial e confere imunidade passiva temporária.",
                "author": "Saúde Coletiva e Imunologia no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Vacina versus Soro: A Diferença Conceitual Definitiva"
                },
                {
                    "type": "paragraph",
                    "content": "• VACINA (Imunização Ativa / Preventiva): Contém o ANTÍGENO atenuado, inativado ou fragmentos proteicos (ou RNA mensageiro). Estimula o sistema imunológico do próprio indivíduo a produzir anticorpos específicos e, fundamentalmente, CÉLULAS DE MEMÓRIA (linfócitos B e T). A resposta é mais lenta no primeiro contato, mas gera proteção duradoura por anos ou décadas.\n• SORO (Imunização Passiva / Curativa Emergencial): Contém ANTICORPOS PRONTOS purificados (geralmente produzidos em cavalos inoculados). Usado em emergências toxicológicas (picada de cobra, escorpião, aranha ou tétano acidental) onde o organismo não teria tempo hábil de produzir seus próprios anticorpos. NÃO gera memória imunológica; após a degradação dos anticorpos administrados, a imunidade cessa."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Principais Doenças e Vetores no Brasil"
                },
                {
                    "type": "paragraph",
                    "content": "• Arboviroses (Dengue, Zika, Chikungunya, Febre Amarela Urbana): Transmitidas pelo mosquito vetor Aedes aegypti (fêmea hematófaga). Profilaxia: erradicação dos criadouros de água parada.\n• Doença de Chagas: Causada pelo protozoário Trypanosoma cruzi, transmitida pelas FEZES do inseto barbeiro (Triatoma infestans) eliminadas durante o repouso após a picada ou por ingestão de açaí/caldo de cana contaminados.\n• Esquistossomose (Barriga d'água): Causada pelo verme Schistosoma mansoni, com caramujo de água doce (Biomphalaria) como hospedeiro intermediário. Contaminação por penetração ativa da larva cercária na pele humana em lagoas de coceira."
                }
            ],
            "quiz": [
                {
                    "question": "Uma pessoa é picada por uma serpente peçonhenta da espécie jararaca (Bothrops jararaca). Qual é o procedimento médico correto de urgência para neutralizar o veneno circulante?",
                    "options": [
                        "Administração imediata de soro antiofídico específico contendo anticorpos pré-formados.",
                        "Aplicação de vacina antiofídica para estimular o sistema imune a produzir anticorpos próprios.",
                        "Injeção intravenosa de antígenos atenuados para acelerar a síntese de linfócitos de memória.",
                        "Ingestão de antibióticos de amplo espectro para destruir o vírus inoculado pela serpente."
                    ],
                    "correctAnswer": 0,
                    "explanation": "Em envenenamentos ofídicos, a ação tóxica é fulminante e o paciente não dispõe de dias para desenvolver uma resposta imune ativa. Deve-se administrar imediatamente o SORO antiofídico específico, que fornece anticorpos prontos para neutralizar as toxinas no sangue."
                }
            ]
        }
    ]
