# -*- coding: utf-8 -*-
"""Curso de Ciências da Natureza ENEM - Módulo 2: Biologia (Genética, Citologia, Metabolismo e Divisão Celular)"""


def get_chapters():
    return [
        {
            "id": "nat-cap-06-genetica-molecular",
            "number": 6,
            "title": "6. Genética I: DNA, RNA, Genes, Cromossomos e Síntese Proteica",
            "epigraph": {
                "text": "O DNA não se importa com o que você sabe; ele é a partitura silenciosa que a célula lê todos os dias para tocar a sinfonia da vida.",
                "author": "Aula Magna de Biologia Molecular"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Livro de Receitas Mais Sofisticado do Universo"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao universo da Genética Molecular. Hoje você vai entender como uma única célula carrega as instruções para construir a cor dos seus olhos, a queratina do seu cabelo, a hemoglobina do sangue e as enzimas da digestão. Pense comigo: se o seu corpo fosse uma grande confeitaria, o DNA seria o livro mestre de receitas trancado na sala da gerência — o núcleo celular. Como esse original é precioso demais para circular pela cozinha cheia de reações químicas, um funcionário copia apenas uma receita em um bilhete descartável: o RNA mensageiro. Daí nasce o Dogma Central da Biologia Molecular: o DNA se duplica, transcreve informação para o RNA, e o RNA é traduzido em proteínas."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Arquitetura do DNA: Dupla Hélice, Nucleotídeos e Regra de Chargaff"
                },
                {
                    "type": "paragraph",
                    "content": "Em 1953, Watson e Crick — apoiados decisivamente pelas imagens de raios X obtidas por Rosalind Franklin — mostraram que o DNA (ácido desoxirribonucleico) tem o formato de uma escada retorcida: a dupla hélice. Seus tijolinhos são os nucleotídeos, cada um formado por três peças: um grupo fosfato, um açúcar de cinco carbonos (pentose) e uma base nitrogenada. Os corrimãos da escada alternam fosfato e desoxirribose unidos por fortes ligações fosfodiéster. Já os degraus surgem do encontro de duas bases unidas por pontes de hidrogênio: as purinas maiores (Adenina e Guanina, com dois anéis) sempre pareiam com as pirimidinas menores (Citosina, Timina e Uracila, com um anel), mantendo a largura da escada constante."
                },
                {
                    "type": "paragraph",
                    "content": "No DNA, o pareamento é rigoroso: Adenina (A) liga-se à Timina (T) por duas pontes de hidrogênio, e Citosina (C) liga-se à Guanina (G) por três pontes. Veja que detalhe genial: trechos ricos em C-G exigem mais calor para se separar! Além disso, como cada A tem um T na fita oposta e cada C tem um G, vale sempre a Regra de Chargaff: em dupla fita de DNA, %A = %T e %C = %G."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Aplicando a Regra de Chargaff em Segundos",
                    "content": "Enunciado: Ao analisar uma amostra de DNA em dupla fita, descobriu-se que 22% das bases são Guanina (G). Qual é a porcentagem de Adenina (A)?\n\nResolução passo a passo:\n1. Em dupla fita de DNA, G pareia com C. Logo, se G = 22%, obrigatoriamente C = 22%.\n2. Juntas, G + C somam 44% do total.\n3. Como o total é 100%, sobram 100% - 44% = 56% para dividir igualmente entre A e T.\n4. Logo, %A = %T = 56% / 2 = 28%. Resposta: 28% de Adenina!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "DNA versus RNA: Os Irmãos Químicos com Missões Diferentes"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção porque o ENEM adora comparar DNA e RNA! Primeiro, o formato: o DNA é fita dupla em hélice, enquanto o RNA (ácido ribonucleico) é fita simples. Segundo, a pentose: o DNA usa desoxirribose (mais estável), e o RNA usa ribose. Terceiro, as bases: o DNA tem A, T, C e G; o RNA troca a Timina pela Uracila (A, U, C e G). Quarto, o papel: o DNA fica guardado no núcleo (além de mitocôndrias e cloroplastos) como arquivo permanente; já o RNA atua sobretudo no citoplasma em três versões: RNA mensageiro (RNAm, leva a receita), RNA transportador (RNAt, traz aminoácidos) e RNA ribossômico (RNAr, compõe os ribossomos)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Genes, Cromatina e Cromossomos: Organizando Dois Metros de Fio"
                },
                {
                    "type": "paragraph",
                    "content": "Esticado, o DNA de uma única célula humana teria cerca de dois metros! Para caber no núcleo sem embolar, o fio se enrola ao redor de proteínas chamadas histonas, formando a cromatina: quando frouxa e ativa para leitura, é eucromatina; quando supercompactada e silenciada, é heterocromatina. Na divisão celular, a cromatina se condensa ao máximo formando os cromossomos. Um cromossomo duplicado tem formato de X, com duas cópias idênticas (cromátides-irmãs) presas pelo centrômero e pontas protetoras chamadas telômeros. Nossas células somáticas possuem 46 cromossomos (22 pares autossômicos + 1 par sexual XX ou XY). E um gene é exatamente um segmento de DNA que guarda a receita de um RNA funcional ou de uma proteína."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Duplicação, Transcrição e Tradução: A Linha de Montagem da Vida"
                },
                {
                    "type": "paragraph",
                    "content": "Antes de se dividir, a célula copia todo o DNA pela duplicação semiconservativa: a enzima helicase abre a dupla hélice e a DNA polimerase constrói novas fitas complementares (sempre no sentido 5' para 3'), de modo que cada DNA-filho guarda uma fita velha e uma nova. Já para produzir proteínas, ocorre primeiro a transcrição no núcleo: a RNA polimerase lê uma das fitas do gene (fita molde) e monta um RNAm complementar (trocando A por U). Em eucariontes, esse RNAm passa pelo splicing: os trechos não codificantes (íntrons) são removidos e os trechos úteis (éxons) são emendados, podendo gerar proteínas variadas pelo splicing alternativo."
                },
                {
                    "type": "paragraph",
                    "content": "No citoplasma, o RNAm acopla-se a um ribossomo para a tradução. O ribossomo lê o RNAm em trincas chamadas códons (há 64 códons para 20 aminoácidos). Cada RNAt traz um aminoácido específico e encaixa seu anticódon complementar no códon do RNAm. A leitura começa no códon de iniciação AUG (Metionina) e termina ao encontrar um códon de parada (UAA, UAG ou UGA), liberando a proteína pronta."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Características do Código Genético",
                    "content": "O código genético tem duas propriedades amadas pelo ENEM: ele é DEGENERADO (ou redundante), pois vários códons diferentes podem especificar o mesmo aminoácido — amortecendo muitas mutações — e é praticamente UNIVERSAL, pois AUG significa Metionina em humanos, plantas e bactérias. É essa universalidade que permite fabricar insulina humana dentro de bactérias!"
                },
                {
                    "type": "callout",
                    "title": "Exercício Resolvido: Da Fita Molde de DNA até a Proteína",
                    "content": "Dada a fita molde de DNA: 3'- T A C  G G A  C T A  A T T -5'.\n1. Transcrição (DNA -> RNAm, usando A-U, T-A, C-G, G-C): 5'- A U G  C C U  G A U  U A A -3'.\n2. Leitura dos códons: AUG (iniciação/Metionina), CCU (Prolina), GAU (Ácido Aspártico) e UAA (códon de parada!).\n3. Pegadinha clássica: quantos aminoácidos terá esse peptídeo? Apenas 3! Pois UAA encerra a síntese sem adicionar aminoácido. Os anticódons usados pelos RNAt serão UAC, GGA e CUA."
                },
                {
                    "type": "quote",
                    "content": "Não deciframos apenas a língua das estrelas; agora lemos o alfabeto de quatro letras escrito no coração de cada célula viva.",
                    "author": "Síntese de Genética Molecular"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-07-genetica-mendeliana",
            "number": 7,
            "title": "7. Genética II: Hereditariedade, Leis de Mendel, Dominância e Recessividade",
            "epigraph": {
                "text": "Antes mesmo de alguém enxergar um cromossomo, Mendel contou ervilhas no jardim e descobriu a matemática silenciosa da herança biológica.",
                "author": "Aula Magna de Genética Clássica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Vocabulário Sagrado: Alelos, Genótipo e Fenótipo"
                },
                {
                    "type": "paragraph",
                    "content": "Olá novamente! Hoje vamos olhar para a herança dentro das famílias. No século XIX, Gregor Mendel desvendou as leis da hereditariedade cultivando milhares de pés de ervilha (*Pisum sativum*), escolha genial por crescerem rápido, permitirem autofecundação e terem traços bem nítidos. Para dominar qualquer questão de genética no ENEM, alinhe quatro conceitos: variantes de um mesmo gene chamadas alelos ocupam a mesma posição (lócus gênico) em cromossomos homólogos (um paterno e um materno). O conjunto de alelos que você carrega é o genótipo (AA, Aa ou aa), enquanto a característica observável resultante — cor da flor, formato da hemácia ou tipo sanguíneo — é o fenótipo."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Fenótipo = Genótipo + Ambiente!",
                    "content": "Nunca ache que o fenótipo depende só dos genes! Fenótipo = Genótipo + Meio Ambiente. Gêmeos idênticos têm o mesmo genótipo, mas um fica mais bronzeado se trabalhar ao sol. Outro exemplo clássico do ENEM é a fenilcetonúria: a criança nasce com o genótipo recessivo que impede a quebra da fenilalanina; porém, se detectada no Teste do Pezinho e tratada com dieta controlada (ambiente), a deficiência intelectual (fenótipo da doença) não se manifesta!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "1ª Lei de Mendel: Dominância, Recessividade e Quadro de Punnett"
                },
                {
                    "type": "paragraph",
                    "content": "Indivíduos com alelos iguais (AA ou aa) são homozigotos; com alelos diferentes (Aa) são heterozigotos. Na dominância completa, um único alelo dominante (A) já expressa o fenótipo dominante, enquanto o recessivo (a) só aparece em dose dupla (aa). Ao cruzar ervilhas puras amarelas (VV) com verdes (vv), Mendel obteve na geração F1 100% de amarelas híbridas (Vv). Autofecundando F1 (Vv × Vv), o verde reapareceu na geração F2 na proporção de 3 amarelas para 1 verde!"
                },
                {
                    "type": "paragraph",
                    "content": "Nascia a 1ª Lei de Mendel (Segregação dos Fatores): os alelos de um par se separam na formação dos gametas, indo só um para cada gameta. Pelo Quadro de Punnett de Vv × Vv, cada planta gera metade de gametas V e metade v, produzindo 1 VV : 2 Vv : 1 vv (proporção genotípica 1:2:1) e 3/4 amarelas : 1/4 verdes (proporção fenotípica 3:1)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "2ª Lei de Mendel: Segregação Independente Sem Sofrimento"
                },
                {
                    "type": "paragraph",
                    "content": "E ao analisar duas características juntas, como cor (V/v) e textura (R/r) situadas em cromossomos diferentes? Pela 2ª Lei de Mendel (Segregação Independente), os pares se distribuem aos gametas de forma independente! No cruzamento VvRr × VvRr, nunca desenhe um quadro gigante de 16 casas: resolva cada gene separado e multiplique com a Regra do 'E' (eventos simultâneos independentes multiplicam) ou some com a Regra do 'OU' (eventos excludentes somam). Quer a chance de nascer amarela (V_) E lisa (R_)? Em Vv × Vv, V_ vale 3/4; em Rr × Rr, R_ vale 3/4. Logo: 3/4 × 3/4 = 9/16! Daí vem a famosa proporção 9:3:3:1."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Dominância Incompleta, Codominância e Sistema ABO/Rh"
                },
                {
                    "type": "paragraph",
                    "content": "Nem tudo segue dominância simples. Na dominância incompleta, o heterozigoto mostra fenótipo intermediário (na flor maravilha, vermelha VV × branca BB gera rosa VB). Na codominância, ambos os alelos se expressam plenamente juntos, sem mistura — como no sangue AB!"
                },
                {
                    "type": "paragraph",
                    "content": "O sistema ABO une alelos múltiplos (polialelia: três alelos possíveis na população — Iᴬ, Iᴮ e i) com codominância (Iᴬ e Iᴮ) e dominância sobre i. Quem é IᴬIᴬ ou Iᴬi tem sangue A (antígeno A na hemácia, anticorpo anti-B no plasma); IᴮIᴮ ou Iᴮi tem sangue B (antígeno B, anti-A); IᴬIᴮ é AB (antígenos A e B, nenhuma aglutinina — receptor universal); e ii é O (sem antígenos na hemácia, anti-A e anti-B no plasma — doador universal de hemácias!)."
                },
                {
                    "type": "paragraph",
                    "content": "Já o Fator Rh (R dominante = Rh+; rr = Rh-) protagoniza a eritroblastose fetal (doença hemolítica do recém-nascido): ocorre quando uma mãe Rh- (rr) gera um segundo filho Rh+ (Rr) de pai Rh+. Após sensibilização no primeiro parto, os anticorpos anti-Rh maternos atravessam a placenta na gestação seguinte e destroem as hemácias do feto — tragédia prevenida aplicando soro anti-Rh na mãe logo após o primeiro parto."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Passo a Passo Infalível para Decifrar Qualquer Heredograma"
                },
                {
                    "type": "paragraph",
                    "content": "Para nunca travar diante de quadradinhos (homens) e bolinhas (mulheres), use a regra de ouro: procure um casal com o MESMO fenótipo (ambos pintados ou ambos brancos) que gerou um filho com fenótipo DIFERENTE! Se os pais são iguais e o filho é diferente, essa característica do filho estava escondida nos pais: portanto, os pais são heterozigotos (Aa), o fenótipo dos pais é DOMINANTE e o do filho diferente é RECESSIVO (aa)!"
                },
                {
                    "type": "callout",
                    "title": "Exercício Resolvido em Heredograma: Passo a Passo",
                    "content": "Carlos (pintado, afetado) e Lúcia (pintada, afetada) têm Ana (branca, normal) e João (pintado). Qual a probabilidade de o casal ter uma próxima criança do sexo feminino E afetada?\n\nResolução:\n1. Pais iguais (afetados) tiveram filha diferente (Ana, normal). Logo, ser afetado é DOMINANTE (A_) e normal é RECESSIVO (aa)! Carlos e Lúcia são Aa × Aa.\n2. Cruzando Aa × Aa: 1/4 AA, 2/4 Aa, 1/4 aa. A chance de ser afetado (AA ou Aa) é 3/4.\n3. A chance de ser do sexo feminino é 1/2.\n4. Pela Regra do E: 1/2 × 3/4 = 3/8 (ou 37,5%). Direto ao ponto!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Herança Ligada ao Cromossomo X",
                    "content": "Na herança recessiva ligada ao X (como daltonismo e hemofilia), homens (XY) precisam de apenas um alelo (XᵃY), enquanto mulheres (XX) precisam de dois (XᵃXᵃ). Teste eliminatório rápido: se uma mãe afetada (XᵃXᵃ) tiver um filho homem normal (XᴬY), descarte herança recessiva ligada ao X na hora, pois o menino herda o X obrigatoriamente da mãe!"
                },
                {
                    "type": "quote",
                    "content": "Quando você enxerga pais iguais gerando um filho diferente, o véu da dúvida cai e o genótipo se revela diante dos seus olhos.",
                    "author": "Manual do Vestibulando 800+"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-08-biotecnologia-mutacoes",
            "number": 8,
            "title": "8. Genética III: Mutações, Biotecnologia, Transgênicos e Clonagem",
            "epigraph": {
                "text": "Do acaso de uma letra trocada no DNA à precisão cirúrgica das tesouras moleculares, a biotecnologia transformou o código da vida em ferramenta de cura e investigação.",
                "author": "Aula Magna de Biotecnologia Moderna"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Mutações Gênicas e Cromossômicas: A Origem da Variabilidade e das Síndromes"
                },
                {
                    "type": "paragraph",
                    "content": "Bem-vindo a um dos temas mais contemporâneos — e mais queridos pela banca do ENEM! Pense comigo: se a duplicação do DNA é tão cuidadosa, de onde vêm as novidades evolutivas e certas síndromes genéticas? Elas nascem das mutações, alterações permanentes no material genético que acontecem ao acaso (nunca 'para ajudar' ou por necessidade do organismo), fornecendo a matéria-prima original sobre a qual a seleção natural atua. Dividimo-las em gênicas e cromossômicas. Nas mutações gênicas, mudam poucas bases dentro de um gene: imagine a frase 'O RATO ROEU A ROUPA'. Uma substituição de letra pode ser silenciosa (o novo códon pede o mesmo aminoácido, graças ao código degenerado), missense (troca um aminoácido por outro — é o caso clássico da anemia falciforme, em que a troca de ácido glutâmico por valina deforma as hemácias em foice e dificulta o transporte de oxigênio) ou nonsense (cria um códon de parada precoce e trunca a proteína). Já inserções ou deleções fora de múltiplos de três causam deslocamento do quadro de leitura (frameshift), bagunçando toda a proteína dali em diante."
                },
                {
                    "type": "paragraph",
                    "content": "As mutações cromossômicas, por sua vez, alteram grandes trechos (estruturais: deleção, duplicação, inversão e translocação) ou o número inteiro de cromossomos (numéricas), quase sempre por erro de separação — a chamada não disjunção — durante a meiose que forma os gametas. Mudar um conjunto completo de cromossomos (3n, 4n) chama-se euploidia, algo muito comum na agricultura para gerar frutas sem sementes, como melancias e bananas triploides. Já ganhar ou perder cromossomos isolados é uma aneuploidia, gerando síndromes humanas muito conhecidas: Síndrome de Down (trissomia do 21: 47,XX+21 ou 47,XY+21), Síndrome de Turner (monossomia sexual 45,X0) e Síndrome de Klinefelter (47,XXY)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "DNA Recombinante: Tesouras, Colas e Insulina em Bactérias"
                },
                {
                    "type": "paragraph",
                    "content": "Como a biotecnologia passou a fabricar insulina humana segura para diabéticos sem depender de pâncreas de animais? Pela tecnologia do DNA recombinante! Primeiro, enzimas de restrição ('tesouras moleculares' de origem bacteriana) cortam o gene humano da insulina e abrem um plasmídeo (anel de DNA bacteriano) deixando pontas compatíveis. Em seguida, a enzima DNA ligase ('cola molecular') costura o gene humano dentro do plasmídeo. Devolvido à bactéria *Escherichia coli*, esse DNA recombinante é lido graças à universalidade do código genético, transformando as bactérias em biofábricas de insulina humana pura."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Transgênicos (OGMs) versus Edição Gênica via CRISPR-Cas9"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Todo Transgênico É OGM, Mas Nem Todo OGM É Transgênico!",
                    "content": "Organismo Geneticamente Modificado (OGM) é qualquer ser vivo cujo DNA foi alterado por engenharia genética. Já o TRANSGÊNICO é o OGM que recebeu um gene vindo de OUTRA espécie — como o milho Bt, que recebeu um gene da bactéria Bacillus thuringiensis para produzir proteína tóxica a lagartas e reduzir o uso de agrotóxicos."
                },
                {
                    "type": "paragraph",
                    "content": "A grande revolução atual é o sistema CRISPR-Cas9 (Nobel de 2020), um verdadeiro 'Localizar e Substituir' genético. Com um RNA-guia programado e a enzima Cas9, os cientistas cortam e corrigem ou desligam um gene específico no próprio genoma do organismo com precisão cirúrgica, sem precisar inserir DNA de outra espécie! Logo, um ser editado por CRISPR pode ser um OGM sem ser transgênico."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Clonagem Reprodutiva, Clonagem Terapêutica e Células-Tronco"
                },
                {
                    "type": "paragraph",
                    "content": "Na clonagem reprodutiva — caso da ovelha Dolly (1996) — busca-se gerar um indivíduo inteiro idêntico a um adulto. Retirou-se o núcleo diploide (2n) de uma célula mamária da ovelha A e inseriu-se esse núcleo dentro de um óvulo sem núcleo (anucleado) da ovelha B, implantando o embrião na barriga de aluguel C. Já na clonagem terapêutica, o embrião cresce só até blastocisto para fornecer células-tronco embrionárias pluripotentes e regenerar tecidos lesados (além delas, existem as totipotentes do zigoto, as multipotentes adultas da medula óssea e as iPSC reprogramadas)."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI sobre a Ovelha Dolly!",
                    "content": "De quem a Dolly era clone nuclear? Da ovelha A, doadora do núcleo! Mas atenção ao detalhe citológico que derruba candidatos: as mitocôndrias ficam no citoplasma do óvulo! Como o citoplasma veio da ovelha B, o DNA mitocondrial de Dolly era igual ao da ovelha B!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "PCR e Eletroforese em Gel: Teste de Paternidade e Perícia Forense"
                },
                {
                    "type": "paragraph",
                    "content": "Em testes de paternidade ou cenas de crime, poucas gotas de sangue são amplificadas milhões de vezes pela PCR (Reação em Cadeia da Polimerase), que resiste a ciclos quentes graças à enzima Taq polimerase de bactérias termais. Depois, o DNA cortado é colocado em um gel sob corrente elétrica: é a eletroforese. Como o DNA tem carga negativa (pelos fosfatos), migra para o polo positivo; fragmentos menores correm mais rápido e avançam mais longe no gel, gerando um padrão único de bandas ('impressão digital de DNA')."
                },
                {
                    "type": "callout",
                    "title": "Exercício Resolvido Passo a Passo: Lendo um Gel de Paternidade",
                    "content": "Regra absoluta: TODA banda do Filho veio obrigatoriamente da Mãe OU do Pai biológico!\n\nSuponha que o Filho tenha bandas nas posições 1, 3, 5 e 7.\n- A Mãe tem bandas 1, 4, 5 e 8 -> portanto, as bandas 1 e 5 do Filho vieram da Mãe.\n- Sobram as bandas 3 e 7 no Filho, ausentes na Mãe: o pai biológico TEM que possuir ambas!\n- Candidato P1 tem 2, 3, 6 e 8 (falta a 7 -> eliminado).\n- Candidato P2 tem 3, 4, 7 e 9 (possui 3 E 7 -> PAI BIOLÓGICO!).\n- Candidato P3 tem 1, 5, 7 e 8 (falta a 3 -> eliminado).\nLembre-se: bandas extras no pai que não passaram ao filho são normais; o que elimina é faltar uma banda exclusiva do filho!"
                },
                {
                    "type": "quote",
                    "content": "O DNA nunca mente no tribunal da biologia: metade do seu código de barras molecular veio da mãe, e cada traço restante aponta sem falha para o pai.",
                    "author": "Aula de Biologia Forense ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-09-citologia",
            "number": 9,
            "title": "9. Citologia: Teoria Celular, Células Procariontes vs. Eucariontes, Membrana e Organelas",
            "epigraph": {
                "text": "Toda célula nasce de outra célula preexistente, carregando dentro de sua membrana delicada uma cidade inteira em pleno funcionamento.",
                "author": "Rudolf Virchow (adaptado para o ENEM)"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Teoria Celular e Arquiteturas: Procarionte versus Eucarionte"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Bem-vindo à Citologia, o estudo da cidade microscópica que sustenta a vida. No século XIX, Schleiden, Schwann e Virchow firmaram os postulados da Teoria Celular: todo ser vivo é formado por células (unidade morfológica), todas as funções vitais acontecem dentro delas (unidade fisiológica) e toda célula nasce de outra preexistente (unidade genética). Os vírus são a célebre exceção: por não terem metabolismo próprio nem organelas, sendo parasitas intracelulares obrigatórios, são classificados como acelulares."
                },
                {
                    "type": "paragraph",
                    "content": "Nos seres celulares, há dois projetos principais. Células procariontes (bactérias e arqueas) não possuem carioteca — seu DNA circular fica disperso no nucleoide —, não têm organelas membranosas, exibem ribossomos menores (70S) e parede de peptidoglicano. Células eucariontes (protozoários, algas, fungos, plantas e animais) possuem núcleo verdadeiro com carioteca e um rico conjunto de organelas membranosas."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Célula Animal versus Célula Vegetal",
                    "content": "Ambas são eucariontes com núcleo, mitocôndrias, retículos, complexo golgiense e peroxissomos. Veja as diferenças-chave:\n- Exclusivos ou típicos da Célula Vegetal: parede celular rígida de celulose, plastos (cloroplastos), um grande vacúolo central regulando água e glioxissomos (convertem lipídios em açúcares na semente).\n- Típicos da Célula Animal (ausentes em plantas superiores): centríolos (formam cílios, flagelos e fuso mitótico animal) e lisossomos típicos."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Membrana Plasmática: O Modelo Mosaico Fluido"
                },
                {
                    "type": "paragraph",
                    "content": "A fronteira inteligente da célula é a membrana plasmática, descrita em 1972 por Singer e Nicolson pelo modelo do Mosaico Fluido: uma bicamada de fosfolipídios onde proteínas ficam mergulhadas (como peças de um mosaico) deslizando lateralmente (daí a fluidez!). Cada fosfolipídio é anfipático: tem 'cabeça' fosfato polar hidrofílica (voltada para a água de dentro e de fora da célula) e duas 'caudas' de ácidos graxos apolares hidrofóbicas (escondidas no miolo da bicamada, fugindo da água). Nas células animais, o colesterol encaixa-se entre as caudas para evitar que a membrana fique rígida demais no frio ou mole demais no calor; por fora, açúcares presos a proteínas e lipídios formam o glicocálix, o crachá químico de reconhecimento e proteção celular."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Transportes pela Membrana: Passivo, Osmose e Bomba de Na+/K+"
                },
                {
                    "type": "paragraph",
                    "content": "A membrana tem permeabilidade seletiva. No transporte passivo não há gasto de ATP, pois tudo corre a favor do gradiente de concentração (de onde há mais para onde há menos): pela difusão simples passam moléculas pequenas e apolares ($O_2$, $CO_2$); pela difusão facilitada, substâncias polares como a glicose e alguns íons atravessam de carona por dentro de proteínas canais ou permeases. Já na campeã absoluta do ENEM — a OSMOSE — quem se movimenta através da membrana semipermeável é a ÁGUA, indo sempre do meio menos concentrado em soluto (hipotônico, com mais água livre) para o meio mais concentrado em soluto (hipertônico)! Pense no cotidiano: temperar a salada de alface com sal e vinagre cedo demais cria um meio hipertônico fora das folhas, puxando água de dentro das células por osmose e deixando tudo murcho; pelo mesmo princípio, salgar carnes para fazer charque desidrata as bactérias e conserva o alimento."
                },
                {
                    "type": "callout",
                    "title": "Osmose na Prática: Hemácia versus Célula Vegetal",
                    "content": "Em água pura (meio hipotônico), a hemácia absorve água sem parar até estourar (hemólise); em água muito salgada (hipertônico), perde água e murcha (crenação). Já a célula vegetal em meio hipotônico enche o vacúolo e fica firme e túrgida, mas NÃO estoura graças à resistência mecânica da parede celular de celulose! Em meio hipertônico, ela perde água e sua membrana descola da parede: é a plasmólise."
                },
                {
                    "type": "paragraph",
                    "content": "Quando precisa transportar substâncias contra o gradiente (do menos concentrado para o mais concentrado), a célula gasta energia no transporte ativo, cuja estrela é a Bomba de $Na^+/K^+$: a cada ATP hidrolisado, ela bombeia 3 íons $Na^+$ para fora e traz 2 íons $K^+$ para dentro, mantendo o equilíbrio osmótico (impedindo a célula de inchar) e gerando o potencial elétrico essencial aos impulsos nervosos nos neurônios. Já partículas grandes ou blocos de alimento entram por endocitose (fagocitose para sólidos, como fazem nossos macrófagos ao engolir bactérias, e pinocitose para líquidos) e saem por exocitose."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Organelas em Ação: Do Núcleo à Endossimbiose das Mitocôndrias"
                },
                {
                    "type": "paragraph",
                    "content": "No comando está o Núcleo com sua carioteca porosa e o nucléolo (fábrica de RNAr que monta os ribossomos). Os Ribossomos traduzem proteínas. O Retículo Endoplasmático Rugoso (RER), pontilhado de ribossomos, produz proteínas para secreção ou membrana; o Retículo Endoplasmático Liso (REL) fabrica lipídios (como hormônios esteroides) e desintoxica álcool e medicamentos no fígado. Daí as vesículas seguem ao Complexo Golgiense — os 'Correios' da célula —, que modifica, empacota e exporta secreções, além de formar o acrossomo do espermatozoide e os Lisossomos (centrais ácidas de digestão intracelular, autofagia e apoptose, como na regressão da cauda do girino, ou na silicose pulmonar quando a sílica rompe lisossomos). Já os Peroxissomos degradam toxinas e quebram água oxigenada ($H_2O_2$) via catalase. Tudo isso fica sustentado pelo citoesqueleto proteico (microtúbulos e filamentos de actina), que dá forma à célula e guia o trânsito de vesículas."
                },
                {
                    "type": "callout",
                    "title": "Mitocôndrias, Cloroplastos e a Teoria da Endossimbiose",
                    "content": "Mitocôndrias (respiração celular) e Cloroplastos (fotossíntese) possuem membrana dupla, DNA circular próprio e ribossomos 70S — exatamente como bactérias! Segundo a Teoria da Endossimbiose de Lynn Margulis, células eucariontes primitivas englobaram bactérias aeróbias (futuras mitocôndrias) e cianobactérias (futuros cloroplastos) em uma parceria simbiótica permanente."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: A Rota de Uma Proteína de Exportação",
                    "content": "Enunciado: Aminoácidos radioativos foram fornecidos a células do pâncreas que secretam enzimas digestivas. Qual o trajeto da radioatividade?\n\nResolução: 1. Síntese nos ribossomos aderidos ao Retículo Endoplasmático Rugoso (RER) → 2. Endereçamento e empacotamento no Complexo Golgiense → 3. Saída em vesículas secretoras que se fundem à Membrana Plasmática por exocitose!"
                },
                {
                    "type": "quote",
                    "content": "Nenhuma organela trabalha isolada: a vida celular é um trabalho em equipe sincronizado entre membranas, motores moleculares e energia.",
                    "author": "Aula de Citologia Integrada"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-10-metabolismo-energetico",
            "number": 10,
            "title": "10. Metabolismo Energético: Enzimas, ATP, Respiração Celular, Fermentação e Fotossíntese",
            "epigraph": {
                "text": "A vida é um fluxo contínuo de elétrons: o sol carrega as moléculas orgânicas na fotossíntese, e a respiração descarrega essa energia no ritmo exato do ATP.",
                "author": "Aula Magna de Bioenergética"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "ATP e Enzimas: A Bateria e os Catalisadores da Vida"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Tudo o que o seu corpo realiza neste exato instante — ler esta frase, piscar ou manter a temperatura a 36,5 °C — consome energia química. O metabolismo reúne dois grandes times de reações: o anabolismo (construção de moléculas complexas consumindo energia, como a fotossíntese e a síntese de proteínas) e o catabolismo (quebra de moléculas liberando energia, como a respiração celular). Mas pense comigo: a célula não pode queimar glicose de uma só vez como uma fogueira descontrolada, senão ela cozinharia por dentro! Em vez disso, ela captura a energia aos poucos e a armazena em pequenas baterias recarregáveis universais chamadas ATP (adenosina trifosfato). Ao quebrar a ligação do último fosfato do ATP (hidrólise para ADP + Pi), libera-se a dose exata de energia para contrair músculos ou acionar bombas de membrana; depois, a respiração celular recarrega o ADP de volta em ATP!"
                },
                {
                    "type": "paragraph",
                    "content": "E como tantas reações vitais ocorrem em milésimos de segundo a apenas 36,5 °C? Graças às enzimas, catalisadores proteicos altamente específicos (modelo chave-fechadura e encaixe induzido) que diminuem a energia de ativação sem serem consumidos no processo! Exatamente por serem proteínas delicadas, as enzimas dependem rigorosamente de temperatura e pH ótimos: febre altíssima ou fervura provocam desnaturação irreversível (a enzima perde o formato tridimensional e para de funcionar); já o frio da geladeira não desnatura a enzima, apenas desacelera os choques entre moléculas — por isso alimentos congelados conservam por tanto tempo. No pH, veja o contraste perfeito do nosso tubo digestivo: a pepsina do estômago exige meio fortemente ácido (pH ~2), enquanto a tripsina do intestino delgado prefere pH levemente básico (~8)."
                },
                {
                    "type": "callout",
                    "title": "Saturação Enzimática e Inibição nos Gráficos do ENEM",
                    "content": "Aumentando a concentração de substrato para uma quantidade fixa de enzimas, a velocidade da reação sobe até atingir um platô horizontal: é o ponto de saturação enzimática, pois todas as enzimas estão ocupadas ao máximo! Além disso, muitos fármacos e venenos atuam como inibidores: os inibidores competitivos imitam o substrato e disputam o sítio ativo, enquanto os inibidores não competitivos ligam-se fora do sítio ativo e deformam a enzima."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Respiração Celular Aeróbia: As Três Etapas da Energia Máxima"
                },
                {
                    "type": "paragraph",
                    "content": "Na respiração celular aeróbia ($C_6H_{12}O_6 + 6 O_2 \\rightarrow 6 CO_2 + 6 H_2O$ + ~30 a 32 ATP), uma molécula de glicose é desmontada em três etapas conectadas:\n1. Glicólise (ocorre no citosol e NÃO precisa de oxigênio): a glicose (6 carbonos) é quebrada em 2 moléculas de piruvato (3 carbonos cada), rendendo saldo direto de 2 ATPs e 2 moléculas de NADH carregadas de elétrons.\n2. Ciclo de Krebs / do Ácido Cítrico (matriz mitocondrial): o piruvato perde um carbono na forma de $CO_2$, vira acetil-CoA e gira no ciclo liberando todo o restante do carbono na forma do $CO_2$ que você expira pelos pulmões, além de 2 ATPs diretos e muitos elétrons energizados em NADH e $FADH_2$."
                },
                {
                    "type": "paragraph",
                    "content": "3. Fosforilação Oxidativa / Cadeia Respiratória (cristas mitocondriais): é o grande clímax energético! Os NADH e $FADH_2$ entregam seus elétrons a uma escada de proteínas na membrana interna da mitocôndria; a energia dessa descida bombeia prótons ($H^+$) para o espaço intermembranas, e o retorno em turbilhão pela turbina ATP sintase fabrica a imensa maioria dos ATPs da célula! E quem recebe os elétrons no último degrau para formar água metabólica? O OXIGÊNIO ($O_2$). É exatamente por isso que asfixia ou venenos como o cianeto travam a cadeia respiratória na hora e derrubam a produção de ATP a zero."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fermentação: O Plano B do Pão, do Vinho e do Músculo"
                },
                {
                    "type": "paragraph",
                    "content": "E quando falta oxigênio? A célula aciona a fermentação, um plano B puramente citosólico que executa apenas a glicólise (gerando só 2 ATPs por glicose — rendimento bem menor!) seguida de regeneração do $NAD^+$. Na fermentação alcoólica, realizada por leveduras como *Saccharomyces cerevisiae*, o piruvato vira etanol e $CO_2$: na padaria, as bolhinhas de $CO_2$ fazem a massa do pão crescer e ficar fofa (o álcool evapora no forno); já na produção de vinhos, cervejas e etanol combustível, aproveita-se o álcool! Na fermentação lática, feita por lactobacilos (em iogurtes e queijos) e por nossas fibras musculares em corrida intensa sem $O_2$ suficiente, o piruvato vira ácido lático — sem soltar $CO_2$ — causando acidose e fadiga muscular temporária."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fotossíntese: Luz Solar e Água Virando Açúcar"
                },
                {
                    "type": "paragraph",
                    "content": "Nos cloroplastos de plantas, algas e cianobactérias ($6 CO_2 + 6 H_2O \\xrightarrow{luz} C_6H_{12}O_6 + 6 O_2$), guarde esta verdade sagrada: o oxigênio ($O_2$) liberado vem exclusivamente da quebra da ÁGUA ($H_2O$), e jamais do $CO_2$! Na Fase Clara (Fotoquímica), nos tilacoides, a clorofila absorve luz (especialmente vermelha e azul, refletindo a verde) para fazer a fotólise da água (soltando $O_2$) e a fotofosforilação, produzindo ATP e NADPH. Na Fase Escura (Química ou Ciclo de Calvin), no estroma, a enzima RuBisCO usa esse ATP e NADPH para fixar o $CO_2$ atmosférico em glicose — etapa que não usa luz diretamente, mas depende dos produtos da fase clara e sofre limitação pela concentração de $CO_2$, luz e temperatura."
                },
                {
                    "type": "callout",
                    "title": "Exercício Resolvido: Ponto de Compensação Fótico (PCF)",
                    "content": "Lembre-se: plantas respiram 24h por dia (consomem $O_2$, soltam $CO_2$), mas só fotossintetizam com luz!\n- No escuro: só respiração (saldo negativo de biomassa).\n- No Ponto de Compensação Fótico (PCF): Fotossíntese = Respiração. Todo $O_2$ gerado é consumido pela própria planta; saldo gasoso = ZERO (ela apenas se mantém viva, sem crescer).\n- Acima do PCF: Fotossíntese > Respiração → sobra $O_2$ para a atmosfera e a planta acumula reservas para crescer!"
                },
                {
                    "type": "quote",
                    "content": "Respiramos o oxigênio que uma folha arrancou da água sob o sol da manhã, e expiramos o carbono que alimentará a próxima folha.",
                    "author": "Síntese de Bioenergética Ecológica"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-11-divisao-celular",
            "number": 11,
            "title": "11. Divisão Celular: Ciclo Celular, Mitose e Meiose",
            "epigraph": {
                "text": "Mitose é a arte da fidelidade genética para construir e curar o corpo; meiose é a ousadia da mistura para reinventar cada nova geração.",
                "author": "Aula Magna de Biologia Celular"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Intérfase, Pontos de Controle e a Origem do Câncer"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos ao capítulo que conecta DNA, citologia e genética: a Divisão Celular. Pense comigo: você começou a vida como uma única célula — o zigoto — e hoje tem trilhões de células especializadas mantendo exatamente os mesmos 46 cromossomos. Ao mesmo tempo, seus gametas reduzem esses 46 cromossomos para exatamente 23! Como a célula executa esses dois truques com precisão milimétrica?"
                },
                {
                    "type": "paragraph",
                    "content": "Antes de se dividir, a célula passa cerca de 90% da sua vida em intensa preparação na Intérfase (nunca a chame de repouso!). Ela divide-se em três subfases: em G1 (Gap 1), a célula cresce e fabrica proteínas e RNA; em S (Síntese), ocorre a duplicação semiconservativa de todo o DNA e dos centrossomos; e em G2 (Gap 2), a célula revisa a cópia e produz as últimas proteínas do fuso. Células altamente diferenciadas que não se dividem mais, como a maioria dos neurônios, estacionam fora do ciclo em G0."
                },
                {
                    "type": "callout",
                    "title": "Guardiã p53, Checkpoints e a Origem do Câncer",
                    "content": "O ciclo celular possui pontos de controle rigorosos entre G1/S e G2/M. Se o DNA sofrer lesões por radiação UV ou substâncias do cigarro, a proteína supressora p53 freia o ciclo para reparo ou induz a apoptose (suicídio celular programado). Quando mutações acumulam e desligam esses freios moleculares (transformando proto-oncogenes em oncogenes e inativando genes supressores), a célula perde a inibição por contato, faz mitoses descontroladas e origina tumores malignos (câncer)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Mitose: A Divisão Equacional (PMAT) que Mantém 2n"
                },
                {
                    "type": "paragraph",
                    "content": "Na mitose, uma célula-mãe diploide (2n) dá origem a duas células-filhas também diploides (2n) e geneticamente idênticas entre si (divisão equacional: 2n → 2n). Em unicelulares, ela serve para reprodução assexuada; já em nós, multicelulares, garante o crescimento do organismo, a renovação contínua da pele e do sangue, e a cicatrização de tecidos lesionados."
                },
                {
                    "type": "paragraph",
                    "content": "Para nunca errar a sequência da mitose, grave a sigla PMAT:\n1. Prófase: a cromatina condensa-se em cromossomos visíveis (com duas cromátides-irmãs presas pelo centrômero), o nucléolo e a carioteca desaparecem, e os centrossomos migram para os polos montando o fuso mitótico.\n2. Metáfase: os cromossomos atingem condensação MÁXIMA e alinham-se no meio da célula (placa equatorial) — exatamente por isso é a melhor fase para fotografar e montar o cariótipo humano, além de ser o alvo de drogas como a colchicina!\n3. Anáfase: o encurtamento das fibras do fuso rompe os centrômeros e puxa as CROMÁTIDES-IRMÃS para polos opostos.\n4. Telófase e Citocinese: os cromossomos descondensam, carioteca e nucléolo reaparecem e o citoplasma se divide — de fora para dentro (centrípeta, por anel de actina) nas células animais, e de dentro para fora (centrífuga, pelo fragmoplasto) nas vegetais."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Meiose: Divisão Reducional, Crossing-Over e Variabilidade Genética"
                },
                {
                    "type": "paragraph",
                    "content": "Se nossos gametas tivessem 46 cromossomos, o bebê teria 92 e a espécie explodiria em DNA! Para impedir isso na reprodução sexuada, existe a Meiose: após uma única fase S na intérfase, a célula passa por duas divisões sucessivas (Meiose I e Meiose II), transformando 1 célula diploide (2n) em 4 células haploides (n) todas geneticamente únicas (gametas nos animais e esporos nas plantas)."
                },
                {
                    "type": "paragraph",
                    "content": "A Meiose I é reducional (2n → n) e concentra as duas maiores fontes de variabilidade genética da vida:\n- Prófase I (paquíteno): cromossomos homólogos emparelham-se lado a lado e trocam pedaços nos pontos chamados quiasmas — é o CROSSING-OVER (permutação), que mistura alelos no mesmo cromossomo!\n- Metáfase I: pares de homólogos alinham-se em dupla fila na placa equatorial.\n- Anáfase I: atenção absoluta! Aqui NÃO se separam cromátides-irmãs; quem migra para polos opostos são os CROMOSSOMOS HOMÓLOGOS inteiros (ainda duplicados!), sorteados ao acaso — a segregação independente que explica a 2ª Lei de Mendel! Falhas nessa separação (não disjunção) geram gametas com cromossomos a mais ou a menos (aneuploidias). Por fim, na Meiose II (equacional, parecida com uma mitose), separam-se finalmente as cromátides-irmãs na Anáfase II, formando 4 células n distintas."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: O Gráfico da Quantidade de DNA (C)",
                    "content": "No gráfico de DNA por célula ao longo do ciclo:\n- Em G1 a célula tem 2C; na fase S sobe em rampa para 4C (mantendo 4C em G2, Prófase e Metáfase).\n- Na MITOSE: cai uma única vez de 4C para 2C (2C → 4C → 2C).\n- Na MEIOSE: cai de 4C para 2C ao fim da Meiose I, e cai uma segunda vez de 2C para 1C (metade de G1!) ao fim da Meiose II (2C → 4C → 2C → C)."
                },
                {
                    "type": "callout",
                    "title": "Exercício Resolvido Passo a Passo: Contando Cromossomos e DNA",
                    "content": "Uma célula vegetal tem 2n = 14 cromossomos em G1. Quantos cromossomos e moléculas de DNA terá:\n1. Em G2 (após a fase S)? Terá 28 moléculas de DNA (cromátides), MAS ainda 14 cromossomos, pois cada par de cromátides-irmãs divide um único centrômero!\n2. Ao final da Meiose I? Terá n = 7 cromossomos (já pela metade!), cada um duplicado com 2 cromátides (= 14 moléculas de DNA).\n3. Ao final da Meiose II? Terá 7 cromossomos simples com 7 moléculas de DNA!"
                },
                {
                    "type": "quote",
                    "content": "Se a mitose garante que você continue sendo você a cada cicatrização, a meiose garante que nenhum ser humano seja cópia repetida na história da espécie.",
                    "author": "Encerramento do Módulo de Biologia Celular e Genética"
                }
            ],
            "quiz": []
        }
    ]
