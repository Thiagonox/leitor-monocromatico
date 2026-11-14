# -*- coding: utf-8 -*-
"""Curso de Ciências da Natureza ENEM - Biologia Módulo 3: Evolução, Fisiologia Humana e Saúde Pública (Capítulos 12 a 15)"""


def get_chapters():
    return [
        {
            "id": "bio-cap-12-evolucao",
            "number": 12,
            "title": "12. Evolução: Darwinismo, Seleção Natural, Adaptação, Evidências e Especiação",
            "epigraph": {
                "text": "Nada na Biologia faz sentido senão à luz da evolução.",
                "author": "Theodosius Dobzhansky, geneticista e biólogo evolutivo"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas à Grande História da Vida: Por Que Tudo Muda?"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo a um dos capítulos mais apaixonantes e decisivos de toda a Biologia do ENEM. Pense comigo: quando olhamos para a biodiversidade da Terra — de uma bactéria em fontes termais até uma baleia-azul ou um beija-flor diante de uma flor —, surge uma pergunta inevitável: como tanta variedade surgiu e por que cada ser vivo parece tão ajustado ao lugar onde mora? A resposta que unifica a Biologia é a Evolução. Antes de avançar, vamos derrubar um mito comum: na ciência, evoluir NÃO significa 'progredir rumo à perfeição'. Evolução biológica é descendência com modificação ao longo das gerações, isto é, a mudança na frequência das características hereditárias de uma população com o passar do tempo."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Lamarck e Darwin Sem Caricaturas: O Que Cada Um Pensou"
                },
                {
                    "type": "paragraph",
                    "content": "Em resumos apressados, Jean-Baptiste Lamarck costuma aparecer como alguém ingênuo, mas vamos fazer justiça histórica! Em 1809, quando quase todos defendiam o fixismo (a ideia de espécies criadas imutáveis), Lamarck propôs a primeira teoria coerente explicando que os seres vivos mudam e se adaptam ao ambiente. Para ele, havia dois mecanismos: a Lei do Uso e Desuso (órgãos muito exigidos se desenvolvem, enquanto os pouco usados atrofiam) e a Herança dos Caracteres Adquiridos (essas mudanças conquistadas em vida seriam passadas aos filhotes). No exemplo das girafas, o esforço contínuo de esticar o pescoço para alcançar folhas altas o faria crescer, e a prole herdaria esse ganho. Hoje sabemos que isso falha porque alterações em células somáticas, como ganhar músculos treinando, não reescrevem o DNA dos gametas."
                },
                {
                    "type": "paragraph",
                    "content": "Cinquenta anos depois, em 1859, Charles Darwin — ao lado das descobertas independentes de Alfred Russel Wallace — publicou 'A Origem das Espécies'. Veja que sacada genial: o ambiente NÃO cria a variação nem molda o corpo pelo esforço; o ambiente apenas SELECIONA quem já nasceu diferente! O raciocínio darwinista tem quatro passos. Primeiro, toda população possui variabilidade natural pré-existente (algumas girafas já nascem com pescoço mais longo). Segundo, nascem mais indivíduos do que os recursos sustentam, gerando luta pela sobrevivência. Terceiro, os portadores de variações favoráveis naquele ambiente sobrevivem melhor e deixam mais descendentes férteis — a Seleção Natural, ou reprodução diferencial. Quarto, como as características são herdáveis, ao longo das gerações a população concentra a variação vantajosa, ligando todas as espécies por ancestralidade comum."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: O Antibiótico NÃO Cria Resistência na Bactéria!",
                    "content": "Muita atenção aqui porque é onde a maioria cai no ENEM! Dizer que 'a bactéria se acostumou com o antibiótico ou mutou para se defender' zera a questão! O antibiótico (ou o inseticida contra mosquitos e pragas agrícolas) NÃO induz mutações úteis. Em uma colônia gigante de bactérias, algumas já possuem, por mutações aleatórias prévias ao remédio, um gene de resistência. Quando o antibiótico entra, ele elimina as sensíveis e deixa as resistentes se multiplicarem sem concorrência. O remédio e o inseticida são agentes seletivos, jamais fabricantes da adaptação!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Neodarwinismo (Teoria Sintética) e Fatores Evolutivos"
                },
                {
                    "type": "paragraph",
                    "content": "Darwin não conhecia a genética de Mendel, então não sabia explicar como as variações surgiam e eram herdadas. No século XX, a fusão da Seleção Natural com a Genética originou o Neodarwinismo, ou Teoria Sintética da Evolução. Nessa síntese, a fonte primária de alelos novos é a mutação (alteração ao acaso no DNA). Já a recombinação gênica na reprodução sexuada — via crossing-over e segregação independente na meiose, além da fecundação — embaralha esses alelos gerando combinações inéditas."
                },
                {
                    "type": "paragraph",
                    "content": "Além da seleção natural, outros fatores alteram a frequência gênica das populações. A Deriva Genética é a mudança aleatória das frequências de alelos por puro acaso, muito intensa em populações pequenas — como num incêndio que mata quase toda uma população (efeito gargalo) ou em poucos indivíduos que colonizam uma ilha (efeito fundador). Há também o Fluxo Gênico por migração. E a própria seleção natural pode ser direcional (favorece um extremo, como no melanismo industrial das mariposas escuras em troncos com fuligem), estabilizadora (favorece a média, como o peso ideal de recém-nascidos) ou disruptiva (favorece ambos os extremos, como aves com bicos ou bem pequenos ou bem grandes)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Evidências Evolutivas: Anatomia Comparada, Fósseis e DNA"
                },
                {
                    "type": "paragraph",
                    "content": "Na anatomia comparada, domine dois conceitos opostos. Órgãos homólogos têm a mesma origem embrionária e estrutura básica, mesmo com funções distintas: o braço humano, a pata do cavalo, a nadadeira da baleia e a asa do morcego têm os mesmos ossos por virem de um ancestral comum, indicando irradiação adaptativa (divergência evolutiva). Já órgãos análogos têm origens embrionárias diferentes, mas mesma função sob pressões ambientais parecidas — como a asa de uma abelha e a de uma águia, ou o corpo hidrodinâmico de tubarões e golfinhos, revelando convergência adaptativa."
                },
                {
                    "type": "paragraph",
                    "content": "Somam-se os órgãos vestigiais (estruturas reduzidas sem função essencial atual, como ossos pélvicos em baleias e apêndice ou siso em humanos), os fósseis de transição (como o Archaeopteryx, unindo traços de réptil e ave), a embriologia comparada e a Biologia Molecular. Como o código genético é praticamente universal, comparar sequências de DNA e proteínas revela com exatidão o grau de parentesco evolutivo entre as espécies."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Como Nascem Novas Espécies: Especiação Alopátrica e Simpátrica"
                },
                {
                    "type": "paragraph",
                    "content": "Pelo conceito biológico, espécie é um grupo de populações que cruzam na natureza gerando descendentes férteis. Na especiação alopátrica ('outra pátria'), uma barreira geográfica — rio, montanha ou fragmentação florestal — separa a população e interrompe o fluxo gênico. Mutação, deriva e seleção atuam separadamente até surgir isolamento reprodutivo, seja pré-zigótico (canto ou época reprodutiva incompatível) ou pós-zigótico (híbrido estéril, como a mula). Já na especiação simpátrica ('mesma pátria'), novas espécies surgem sem barreira geográfica, comum em plantas por poliploidia (duplicação cromossômica) ou em animais por seleção disruptiva e exploração de nichos distintos."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido (Padrão ENEM 800+): A Praga Resistente no Milharal",
                    "content": "Enunciado: Um agricultor usou o mesmo inseticida por seis safras contra uma lagarta. Na primeira safra, 98% morreram; na sexta, o veneno quase não fez efeito. Como o Neodarwinismo explica isso?\n\nResolução passo a passo:\n1. Descartamos ideias lamarckistas ('as lagartas se acostumaram' ou 'mutaram para se defender').\n2. Antes da primeira aplicação, já havia na população lagartas com mutações aleatórias prévias que conferiam resistência.\n3. O inseticida atuou como agente seletivo: eliminou as sensíveis e deixou as resistentes sobreviverem e se reproduzirem.\n4. Após seis gerações de reprodução diferencial, a frequência do alelo de resistência dominou a lavoura."
                },
                {
                    "type": "quote",
                    "content": "Não é o mais forte que sobrevive, nem o mais inteligente, mas o que melhor se adapta às mudanças.",
                    "author": "Síntese tradicional do pensamento darwiniano"
                }
            ],
            "quiz": []
        },
        {
            "id": "bio-cap-13-fisiologia-1",
            "number": 13,
            "title": "13. Fisiologia Humana I: Sistemas Digestório, Respiratório, Circulatório e Urinário",
            "epigraph": {
                "text": "A constância do meio interno é a condição para uma vida livre e independente.",
                "author": "Claude Bernard, pai da fisiologia moderna"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Bem-vindo à Fábrica Viva: Como o Corpo Mantém a Homeostase"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Agora vamos viajar por dentro da máquina mais sofisticada que existe: o corpo humano. Cada uma das suas trilhões de células precisa receber nutrientes prontos, captar oxigênio para produzir energia, eliminar gás carbônico e manter o sangue limpo para garantir a homeostase (equilíbrio do meio interno). Quatro sistemas formam essa equipe: o digestório desmonta alimentos, o respiratório realiza trocas gasosas, o circulatório distribui tudo pelas rodovias vasculares e o urinário filtra o sangue ajustando água e sais. Vamos percorrer cada estação!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sistema Digestório: Uma Linha de Montagem Guiada pelo pH"
                },
                {
                    "type": "paragraph",
                    "content": "A digestão une ação mecânica (trituração) e química (hidrólise enzimática). Na boca, a mastigação aumenta a superfície de contato e a saliva (pH neutro ~7) traz a ptialina ou amilase salivar, que inicia a quebra do amido em maltose. Pelo esôfago, movimentos peristálticos levam o bolo alimentar ao estômago, onde o suco gástrico com ácido clorídrico (HCl) derruba o pH para ~2. Esse ácido mata micróbios e ativa o pepsinogênio em pepsina, enzima que quebra proteínas em peptídeos, enquanto um muco espesso protege a parede estomacal contra autodigestão."
                },
                {
                    "type": "paragraph",
                    "content": "O quimo ácido entra no duodeno (início do intestino delgado), onde enzimas só funcionam em meio alcalino. Por isso, o pâncreas libera suco pancreático rico em bicarbonato de sódio, elevando o pH para ~8, além de tripsina (proteínas), amilase pancreática (amido), nucleases (DNA/RNA) e lipase pancreática (lipídios). E a bile? Produzida pelo fígado e armazenada na vesícula biliar, a bile NÃO contém nenhuma enzima! Seus sais biliares agem como detergente: emulsificam gorduras em gotículas minúsculas para facilitar o trabalho da lipase. O suco entérico finaliza tudo com maltase, sacarase, lactase e peptidases, liberando glicose, aminoácidos e ácidos graxos para absorção nas vilosidades intestinais. No intestino grosso ocorre absorção de água e sais, além da produção de vitamina K pela microbiota antes da formação das fezes."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Retirada da Vesícula Biliar",
                    "content": "Quem retira a vesícula biliar por cálculos NÃO deixa de produzir bile, pois quem a produz é o FÍGADO! Sem a vesícula para estocar e concentrar bile, ela goteja direto e devagar no duodeno. Assim, após refeições muito gordurosas, falta bile concentrada naquele instante para emulsificar tanta gordura, reduzindo a eficiência da lipase e causando fezes gordurosas."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sistema Respiratório: Mecânica, Hematose e Efeito Tampão"
                },
                {
                    "type": "paragraph",
                    "content": "Na inspiração (processo ativo), o diafragma e os músculos intercostais externos contraem, expandindo a caixa torácica. Com maior volume pulmonar, a pressão interna cai abaixo da atmosférica e o ar entra. Na expiração tranquila (passiva), os músculos relaxam, o volume reduz, a pressão sobe e o ar sai. Quem regula o ritmo respiratório é o bulbo raquidiano, que detecta principalmente a elevação de CO2 e a queda de pH no sangue."
                },
                {
                    "type": "paragraph",
                    "content": "Nos alvéolos ocorre a hematose por difusão simples: O2 entra no sangue e CO2 sai para o alvéolo. Cerca de 98% do O2 viaja ligado ao ferro da hemoglobina (oxi-hemoglobina). Já o CO2 viaja cerca de 70% convertido dentro das hemácias pela enzima anidrase carbônica: CO2 + H2O ⇌ H2CO3 ⇌ H+ + HCO3- (íon bicarbonato no plasma). Esse equilíbrio forma um tampão vital mantendo o pH sanguíneo em ~7,4: prender o ar acumula CO2/H+ (acidose respiratória); hiperventilar elimina CO2 demais consumindo H+ (alcalose respiratória)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sistema Circulatório: O Motor Duplo e Completo"
                },
                {
                    "type": "paragraph",
                    "content": "Nossa circulação é fechada, dupla e completa: sangue arterial e venoso nunca se misturam. O coração tem quatro câmaras: dois átrios que recebem sangue e dois ventrículos que o ejetam (o ventrículo esquerdo tem miocárdio bem mais espesso para bombear ao corpo inteiro). Valvas (tricúspide, bicúspide/mitral e semilunares) garantem fluxo único entre sístole (contração) e diástole (relaxamento), comandadas pelo nó sinoatrial."
                },
                {
                    "type": "paragraph",
                    "content": "Guarde a regra de ouro: ARTÉRIAS sempre SAEM do coração (alta pressão) e VEIAS sempre CHEGAM ao coração (baixa pressão e válvulas). Na Pequena Circulação (pulmonar), o ventrículo direito envia sangue VENOSO pela artéria pulmonar aos pulmões para hematose, retornando sangue ARTERIAL pelas veias pulmonares ao átrio esquerdo. Na Grande Circulação (sistêmica), o ventrículo esquerdo ejeta sangue arterial pela aorta para todo o corpo e ele volta venoso pelas veias cavas ao átrio direito."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sistema Urinário: O Néfron e o Controle pelo ADH"
                },
                {
                    "type": "paragraph",
                    "content": "Cada rim possui cerca de um milhão de néfrons funcionando em três etapas: 1) Filtração glomerular (pressão empurra água, sais, glicose, aminoácidos e ureia do glomérulo para a cápsula de Bowman, retendo proteínas e células); 2) Reabsorção tubular (no túbulo proximal, quase 100% da glicose e aminoácidos voltam ao sangue por transporte ativo — no diabetes descompensado o excesso de glicose satura os transportadores e sai na urina; na alça de Henle e túbulo distal ajusta-se água e sais); 3) Secreção tubular (excreção ativa de H+, K+ e fármacos)."
                },
                {
                    "type": "paragraph",
                    "content": "O volume e a concentração da urina são regulados pelo ADH (hormônio antidiurético), produzido no hipotálamo e liberado pela neuro-hipófise quando o sangue está concentrado. O ADH abre canais de água (aquaporinas) nos túbulos distais e ductos coletores, aumentando a reabsorção de água e gerando pouca urina, bem concentrada. O álcool INIBE o ADH: os ductos ficam impermeáveis à água, gerando muita urina diluída e desidratação (ressaca!). Paralelamente, a aldosterona reabsorve Na+ e água para elevar a pressão arterial."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido (Padrão ENEM): A Cerveja na Praia e a Ação Renal",
                    "content": "Enunciado: Após beber cerveja ao sol sem ingerir água, um jovem urinou muito e claro, sentindo depois sede intensa e tontura. Explique fisiologicamente.\n\nResolução passo a passo:\n1. O etanol inibe a liberação de ADH pela neuro-hipófise.\n2. Com baixo ADH, os ductos coletores dos néfrons permanecem pouco permeáveis à água.\n3. A água não é reabsorvida, gerando grande volume de urina diluída (poliúria).\n4. A perda hídrica concentra o plasma e reduz a volemia, disparando sede e tontura."
                },
                {
                    "type": "quote",
                    "content": "Cada órgão é uma cidade especializada dentro da mesma república fisiológica: nenhum sobrevive sem a troca solidária com os demais.",
                    "author": "Síntese de Fisiologia Integrada ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "bio-cap-14-fisiologia-2",
            "number": 14,
            "title": "14. Fisiologia Humana II: Sistemas Nervoso, Endócrino, Imunológico e Reprodução Humana",
            "epigraph": {
                "text": "O corpo humano possui uma sabedoria bioquímica que responde em milissegundos ao perigo e planeja em ciclos de semanas a continuidade da vida.",
                "author": "Inspirado em Walter Bradford Cannon"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Maestros Invisíveis: Comando Rápido, Hormônios e Defesa"
                },
                {
                    "type": "paragraph",
                    "content": "Olá de novo! Vimos como o corpo se nutre e filtra o sangue; agora vamos entender os sistemas de comando, comunicação e continuidade da vida. Quando você encosta em algo quente, não dá para esperar um hormônio viajar pelo sangue — o Sistema Nervoso responde em milissegundos. Já para ajustar glicose ou metabolismo ao longo das horas e semanas, entra o Sistema Endócrino. Enquanto isso, o Sistema Imunológico combate invasores e o Sistema Reprodutor garante novas gerações. Vamos dominar os quatro!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sistema Nervoso: Neurônio, Sinapse e Arco Reflexo"
                },
                {
                    "type": "paragraph",
                    "content": "O neurônio possui dendritos (antenas receptoras), corpo celular e axônio (cabo condutor). Muitos axônios contam com a bainha de mielina (células de Schwann no SNP e oligodendrócitos no SNC), um isolante lipídico com lacunas chamadas nódulos de Ranvier. Graças a ela ocorre a condução saltatória, multiplicando a velocidade do impulso! Em repouso, o interior celular é negativo (mantido pela bomba Na+/K+). Um estímulo acima do limiar abre canais de Na+, que invade a célula invertendo a carga para positiva (despolarização ou potencial de ação); logo depois sai K+ (repolarização), propagando o sinal pela lei do tudo ou nada."
                },
                {
                    "type": "paragraph",
                    "content": "Entre neurônios existe a fenda sináptica. Na sinapse química, o impulso abre canais de Ca2+, liberando neurotransmissores (acetilcolina, noradrenalina, dopamina, serotonina) que se encaixam nos receptores da célula vizinha. Veja o arco reflexo medular na prática: ao encostar a mão numa panela quente, o receptor aciona um neurônio sensitivo (aferente) até a medula espinhal, onde um interneurônio dispara o neurônio motor (eferente) para puxar o braço ANTES mesmo de a dor chegar ao cérebro! Já o Sistema Autônomo divide-se em Simpático (luta ou fuga via noradrenalina: taquicardia, pupila dilatada, broncodilatação) e Parassimpático (repouso e digestão via acetilcolina, desacelerando os batimentos)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sistema Endócrino: Glicemia, Adrenalina e Tireoide"
                },
                {
                    "type": "paragraph",
                    "content": "Nas Ilhotas de Langerhans do pâncreas, a glicemia é controlada por dois hormônios antagônicos. Após refeições ricas em carboidratos, a glicose sobe e as células beta liberam INSULINA, agindo como chave para a glicose entrar nas células e ser guardada como glicogênio no fígado e músculos (reduz a glicemia). No jejum, células alfa liberam GLUCAGON, quebrando glicogênio hepático em glicose (eleva a glicemia). No Diabetes tipo 1 (autoimune) falta insulina; no tipo 2 as células desenvolvem resistência à insulina."
                },
                {
                    "type": "paragraph",
                    "content": "Em sustos ou perigos, a medula das suprarrenais secreta ADRENALINA, provocando taquicardia, broncodilatação, desvio de sangue para os músculos e quebra rápida de glicogênio. Já o metabolismo basal depende do eixo hipotálamo-hipófise-tireoide: a adeno-hipófise libera TSH, estimulando a tireoide a fabricar tiroxina (T4) e T3 — que exigem IODO! Por feedback negativo, T3/T4 altos freiam o TSH. A carência de iodo na dieta impede a síntese de T3/T4; a hipófise despeja TSH sem parar e a glândula cresce no pescoço (bócio endêmico). Hipotireoidismo desacelera o metabolismo (cansaço e ganho de peso); hipertireoidismo acelera tudo (emagrecimento, calor e agitação)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Sistema Imunológico: Imunidade Inata vs Adaptativa"
                },
                {
                    "type": "paragraph",
                    "content": "A imunidade inata (natural) forma nossa primeira barreira rápida, inespecífica e sem memória: pele íntegra, muco e cílios respiratórios, suco gástrico ácido, febre, inflamação e células fagocitárias (neutrófilos e macrófagos) que englobam e destroem qualquer invasor genérico."
                },
                {
                    "type": "paragraph",
                    "content": "Quando ela não basta, entra a imunidade adaptativa (adquirida), que é altamente específica contra um antígeno e cria MEMÓRIA IMUNOLÓGICA duradoura. Macrófagos apresentam fragmentos do invasor aos linfócitos T auxiliares (CD4+), os verdadeiros generais da defesa (justamente o alvo destruído pelo HIV!). Eles ativam linfócitos T citotóxicos (CD8+), que eliminam células infectadas por vírus ou tumorais (imunidade celular), e estimulam linfócitos B a virarem plasmócitos secretores de ANTICORPOS (imunoglobulinas) específicos que neutralizam patógenos (imunidade humoral), deixando células de memória para respostas futuras fulminantes."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Reprodução Humana, Ciclo Menstrual e Contracepção"
                },
                {
                    "type": "paragraph",
                    "content": "Nos homens, espermatozoides nascem nos túbulos seminíferos dos testículos, amadurecem no epidídimo e recebem secreções nutritivas (frutose das vesículas seminais) e alcalinas (próstata). Nas mulheres, ovários liberam o ovócito II; grave dois endereços clássicos de prova: a fecundação normal acontece na TUBA UTERINA, e a nidação do embrião ocorre no ENDOMÉTRIO do útero."
                },
                {
                    "type": "paragraph",
                    "content": "No ciclo menstrual (28 dias), durante a fase folicular (dias 1 a 13) o FSH da hipófise amadurece o folículo ovariano, que produz ESTROGÊNIO para reconstruir o endométrio. Por volta do 14º dia, um pico abrupto de LH dispara a OVULAÇÃO. Na fase lútea (dias 15 a 28), o folículo vira corpo lúteo e secreta PROGESTERONA mantendo o endométrio espesso e vascularizado. Sem fecundação, o corpo lúteo regride, os hormônios despencam e ocorre a menstruação; havendo gravidez, o embrião produz hCG mantendo o corpo lúteo ativo."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Métodos Contraceptivos e Proteção contra ISTs",
                    "content": "1. Barreira (camisinha masculina/feminina, diafragma): ÚNICOS que também previnem ISTs são os preservativos!\n2. Hormonais (pílula combinada de estrogênio + progesterona): inibem FSH e LH por feedback negativo, bloqueando a ovulação. A pílula do dia seguinte atrasa a ovulação (não é abortiva).\n3. Intrauterinos (DIU de cobre ou hormonal): tornam o ambiente uterino hostil aos espermatozoides.\n4. Cirúrgicos (laqueadura e vasectomia): bloqueiam o encontro dos gametas sem alterar hormônios sexuais ou libido."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido (Padrão ENEM): Como a Pílula Impede a Ovulação?",
                    "content": "Enunciado: Um exame mostra FSH e LH baixos e constantes o mês todo, sem pico no 14º dia, em uma usuária de pílula anticoncepcional combinada. Explique o mecanismo.\n\nResolução passo a passo:\n1. A pílula fornece estrogênio e progesterona sintéticos em doses regulares.\n2. Esses hormônios exercem feedback negativo sobre o hipotálamo e a adeno-hipófise.\n3. A hipófise reduz FSH e suprime o pico de LH.\n4. Sem o pico de LH, não ocorre ovulação."
                },
                {
                    "type": "quote",
                    "content": "O sistema nervoso acende o relâmpago da ação; o sistema endócrino sustenta a música contínua da vida.",
                    "author": "Síntese de Neuroendocrinologia"
                }
            ],
            "quiz": []
        },
        {
            "id": "bio-cap-15-saude-publica",
            "number": 15,
            "title": "15. Saúde Pública: Vírus, Bactérias, Parasitas, Vacinas, Epidemiologia e ISTs",
            "epigraph": {
                "text": "Na saúde coletiva, conhecer o ciclo de vida do parasita é ter nas mãos a chave exata para fechar a porta da doença.",
                "author": "Inspirado no legado de Oswaldo Cruz"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Biologia a Serviço da Vida: Saúde Pública no ENEM"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos ao último capítulo deste módulo com um tema campeão absoluto do ENEM: Saúde Pública. Pense comigo: quase todo ano a prova traz textos sobre campanhas de vacinação, boletins de dengue, resistência bacteriana ou saneamento básico. E por que tantos candidatos erram? Porque confundem o agente causador (vírus, bactéria, protozoário ou verme) com o vetor transmissor, ou misturam o papel preventivo da vacina com o papel emergencial do soro. Nesta aula vamos amarrar cada doença ao seu ciclo biológico e à sua profilaxia exata!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Vírus vs Bactérias: Por Que Antibiótico Não Cura Gripe?"
                },
                {
                    "type": "paragraph",
                    "content": "Vírus são entidades acelulares, sem ribossomos nem metabolismo próprio: resumem-se a um capsídeo proteico protegendo DNA ou RNA (além de um possível envelope lipoproteico roubado da célula hospedeira, como no HIV e no coronavírus). Por isso são parasitas intracelulares obrigatórios, multiplicando-se pelo ciclo lítico (produz cópias e explode a célula) ou lisogênico (integra o material viral ao DNA celular em estado latente). Destaque para os retrovírus, como o HIV, que carregam RNA e a enzima transcriptase reversa para sintetizar DNA a partir de RNA!"
                },
                {
                    "type": "paragraph",
                    "content": "Já as bactérias são seres vivos unicelulares procariontes completos, com ribossomos 70S e parede celular de peptidoglicano. Os antibióticos funcionam destruindo exatamente essa parede ou travando os ribossomos bacterianos — logo, são totalmente inúteis contra gripes e resfriados virais! Além disso, tomar antibiótico sem receita ou interromper o tratamento antes da hora seleciona as cepas mutantes mais resistentes que já existiam na população, gerando as temidas superbactérias hospitalares."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Grandes Endemias Brasileiras: Arboviroses, Protozooses e Verminoses"
                },
                {
                    "type": "paragraph",
                    "content": "Entre as arboviroses virais urbanas, Dengue, Zika, Chikungunya e Febre Amarela urbana são transmitidas pela picada da fêmea do mosquito Aedes aegypti; como ela deposita ovos em água limpa e parada, a profilaxia central é eliminar criadouros (caixas d'água destampadas, pratinhos de vasos, pneus e calhas). Nas protozooses, a Malária (protozoário Plasmodium, transmitido pela fêmea do mosquito Anopheles ou mosquito-prego) provoca febres cíclicas no instante em que os parasitas rompem sincronizadamente as hemácias. Já a Doença de Chagas (Trypanosoma cruzi) transmite-se pelas fezes do inseto barbeiro (Triatoma) depositadas ao lado da picada enquanto ele suga sangue à noite — e também por via oral em caldo de cana ou açaí contaminados pelo inseto triturado! O parasita lesa o miocárdio e o esôfago."
                },
                {
                    "type": "paragraph",
                    "content": "Entre as verminoses por platelmintos, a Esquistossomose ('barriga d'água', Schistosoma mansoni) é figurinha carimbada no ENEM: ovos eliminados nas fezes humanas chegam à água doce e liberam larvas (miracídios) que infectam o caramujo Biomphalaria (hospedeiro intermediário). Dele saem cercárias que nadam e penetram ativamente pela pele humana em 'lagoas de coceira'. Por isso, a profilaxia definitiva exige saneamento básico (esgoto tratado) e tratamento dos doentes."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha Mortal: Teníase vs Cisticercose",
                    "content": "Ambas ligam-se à Taenia solium (porco; T. saginata no boi), mas mudam radicalmente conforme O QUE foi ingerido:\n• TENÍASE: ingestão de carne crua ou malpassada com a larva (cisticerco) -> desenvolve o verme adulto ('solitária') no intestino (humano = hospedeiro definitivo). Prevenção: cozinhar bem as carnes e fiscalização sanitária.\n• CISTICERCOSE: ingestão de OVOS da Taenia solium em água ou verduras contaminadas por fezes humanas -> as larvas migram pela circulação e alojam-se nos músculos, olhos ou cérebro (neurocisticercose, causando convulsões), tornando o humano hospedeiro intermediário! Prevenção: saneamento básico e higienização de alimentos."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Vacina vs Soro: A Diferença Absoluta que Vale Questão"
                },
                {
                    "type": "paragraph",
                    "content": "Grave no mármore essa diferença! A VACINA é imunização ATIVA artificial com função PREVENTIVA. Ela injeta antígenos (microrganismos mortos, atenuados, proteínas ou RNAm) para treinar o seu próprio sistema imunológico a fabricar anticorpos e células de memória: demora dias para proteger, mas oferece imunidade duradoura. Já o SORO terapêutico (antiofídico para picada de cobra, antitetânico ou antirrábico) é imunização PASSIVA artificial com função CURATIVA ou emergencial. Ele injeta ANTICORPOS PRONTOS (geralmente produzidos em cavalos hiperimunizados), age imediatamente neutralizando venenos e toxinas fatais, mas não gera células de memória e desaparece em poucas semanas."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Epidemiologia na Prática e Prevenção de ISTs"
                },
                {
                    "type": "paragraph",
                    "content": "Para interpretar boletins e gráficos do ENEM sem erro, domine cinco termos: Endemia (ocorrência habitual e constante em certa região, como a malária na Amazônia), Epidemia (aumento súbito de casos muito acima do esperado), Surto (epidemia localizada em espaço pequeno, como uma escola ou bairro), Pandemia (epidemia que atinge vários continentes em escala global, como a COVID-19) e Profilaxia (qualquer medida preventiva antes do adoecimento, como saneamento, vacinas e controle de vetores)."
                },
                {
                    "type": "paragraph",
                    "content": "Por fim, nas Infecções Sexualmente Transmissíveis (ISTs), o HIV (retrovírus causador da aids) destrói linfócitos T CD4+; previne-se com preservativo, testagem, tratamento antirretroviral (carga viral indetectável não transmite HIV sexualmente), PrEP e PEP. A Sífilis (bactéria Treponema pallidum) tem cura com penicilina, sendo vital o pré-natal para evitar sífilis congênita. Já o HPV (associado ao câncer de colo do útero) e a Hepatite B são prevenidos com camisinha e vacinas gratuitas no SUS."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido (Padrão ENEM): Picada de Jararaca vs Campanha de Sarampo",
                    "content": "Enunciado: Um agricultor picado por uma jararaca recebeu aplicação emergencial no hospital e se recuperou; na mesma semana, crianças receberam vacina contra sarampo no posto de saúde. Compare os dois procedimentos.\n\nResolução passo a passo:\n1. O agricultor recebeu SORO antiofídico: imunização passiva artificial de caráter curativo/emergencial, contendo anticorpos prontos que neutralizam o veneno imediatamente, sem gerar memória imunológica.\n2. As crianças receberam VACINA: imunização ativa artificial de caráter preventivo, contendo antígenos que estimulam os linfócitos próprios a produzir anticorpos e células de memória duradouras."
                },
                {
                    "type": "quote",
                    "content": "O micróbio não é nada; a prevenção, a ciência e o terreno preparado pela saúde pública são tudo.",
                    "author": "Inspirado em Louis Pasteur"
                }
            ],
            "quiz": []
        }
    ]
