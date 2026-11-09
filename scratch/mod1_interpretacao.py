# -*- coding: utf-8 -*-
"""Módulo I: Interpretação de Texto e Raciocínio Crítico (Capítulos 01 a 09)"""

def get_chapters():
    chapters = []

    # CAPÍTULO 1
    chapters.append({
        "number": "ESTAÇÃO I",
        "title": "Tema, Tese e Funil de Assunto: O Filtro em 5 Segundos",
        "epigraph": {
            "text": "A clareza de pensamento precede a precisão da resposta.",
            "author": "Princípio da TRI"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "No ENEM, assunto, tema e tese são três andares de um funil que você não pode misturar. Assunto é o terreno amplo (ex: 'Cinema'). Tema é o recorte específico delimitado pelo autor (ex: 'O acesso elitizado às salas de cinema no Brasil'). Tese é a tomada de posição crítica diante desse tema (ex: 'A concentração das salas nos grandes centros urbanos viola o direito constitucional à cultura'). Toda questão de interpretação que pergunta o 'objetivo central do texto' quer a TESE, nunca o mero assunto genérico."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "Procure verbos de comando e expressões como: 'O propósito comunicativo central do autor é...', 'A tese defendida no texto sustenta que...' ou 'O posicionamento expresso pelo articulista evidencia que...'. Quando o enunciado falar em 'propósito', 'tese' ou 'intuito principal', descarte imediatamente as alternativas que apenas descrevem um exemplo periférico ou repetem o assunto vago."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "A alternativa distratora clássica traz uma afirmação 100% verdadeira sobre o texto, mas que se refere apenas a um detalhe do segundo parágrafo ou ao assunto amplo demais. Lembre-se: estar escrito no texto não significa responder à pergunta. Se a alternativa não sintetizar a tese do autor, ela é um distrator de tangenciamento ou redução."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Texto rápido: 'Embora a tecnologia conecte pessoas a milhares de quilômetros, as redes sociais criaram bolhas de convivência onde o contraditório é sumariamente silenciado, enfraquecendo o debate democrático.' Se a pergunta for 'A tese central do excerto é:', a resposta certa apontará que as redes comprometem a democracia pelo isolamento em bolhas. Distrator típico: 'A tecnologia permitiu a conexão de pessoas distantes' (fato citado, mas oposto à tese crítica)."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Assunto é 'sobre o quê' (cinema). Tema é 'qual recorte' (falta de acesso). Tese é 'qual a bronca do autor' (isso fere a cidadania). A questão de propósito comunicativo SEMPRE cobra a bronca do autor!"}
        ]
    })

    # CAPÍTULO 2
    chapters.append({
        "number": "ESTAÇÃO II",
        "title": "Ideia Principal versus Secundária: A Armadilha do Detalhe",
        "epigraph": {
            "text": "Nem tudo que reluz no texto é a viga que o sustenta.",
            "author": "Guia de Leitura Analítica"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "Textos do ENEM possuem uma espinha dorsal (ideia principal) e costelas (ideias secundárias). As ideias secundárias servem apenas para ilustrar, exemplificar, comparar ou justificar a espinha dorsal. Se você retirar um exemplo do texto, a tese continua em pé; se retirar a ideia principal, o texto desmorona. A TRI pune candidatos que marcam o exemplo ilustrativo achando que ele é a mensagem nuclear."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "O enunciado costuma questionar: 'No desenvolvimento da argumentação, o autor recorre à menção de [X] com a finalidade de...'. Note que a questão não quer saber o que [X] significa isoladamente, mas sim qual função de apoio [X] exerce em relação à tese mestra do parágrafo."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Distrator de Elevação: transforma uma ilustração secundária em finalidade mestra do artigo. Por exemplo, se o autor cita brevemente a Finlândia para ilustrar um modelo educacional, o distrator dirá que o objetivo do autor era 'apresentar um panorama histórico da educação escandinava'."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Se o texto afirma: 'A evasão escolar no ensino médio decorre da necessidade precoce de geração de renda, como atesta o caso do jovem Pedro, que abandonou os estudos para trabalhar como entregador.' Pergunta: 'A referência ao jovem Pedro visa a...' Resposta: 'Concretizar por meio de um caso particular o impacto da pressão econômica na evasão escolar.' Distrator: 'Narrar a biografia de um entregador urbano.'"},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Exemplo nunca é tese! Dados estatísticos, casos particulares e comparações são apenas tijolos de sustentação; o objetivo da questão é sempre a parede que eles erguem."}
        ]
    })

    # CAPÍTULO 3
    chapters.append({
        "number": "ESTAÇÃO III",
        "title": "Inferência Válida versus Extrapolação Indevida",
        "epigraph": {
            "text": "Interpretar é deduzir com autorização prévia das pistas da escrita.",
            "author": "Umberto Eco"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "Inferência é a dedução lógica e obrigatória a partir de pistas explícitas deixadas pelo texto. Extrapolação é quando você usa suas opiniões pessoais, ideologias ou conhecimentos de mundo prévios para inventar conclusões que o autor jamais autorizou. No ENEM, se o texto não fornece a premissa de sustentação, a alternativa é falsa, mesmo que você concorde pessoalmente com ela na vida real."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "Comandos clássicos: 'Depreende-se do texto que...', 'Infere-se da leitura que...' ou 'A reflexão proposta permite concluir que...'. O verbo 'depreender' significa puxar o fio lógico escondido na tessitura das palavras."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "O distrator sedutor é aquela alternativa que parece politicamente perfeita, inteligente ou filosoficamente bonita, mas que diz muito mais do que o texto permitiu. O candidato desatento pensa: 'Isso é verdade no mundo real!' e marca. Erro fatal de extrapolação!"},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Texto: 'O percentual de jovens que declaram ler ao menos um livro por mês caiu 14% na última década.' O que se infere validamente: 'Houve uma retração no hábito mensal de leitura entre o público jovem recente.' O que é extrapolação indevida: 'Os smartphones destruíram a capacidade cognitiva das novas gerações.' (O texto não citou smartphones nem destruição cognitiva)."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Regra de ouro da inferência: se a alternativa depende de um fato que não está ancorado em nenhuma palavra ou conector do texto, é extrapolação. Fique preso ao texto como um detetive às pistas da cena!"}
        ]
    })

    # CAPÍTULO 4
    chapters.append({
        "number": "ESTAÇÃO IV",
        "title": "Pressupostos e Subentendidos: Lendo os Não-Ditos",
        "epigraph": {
            "text": "As palavras dizem o que mostram; a sintaxe revela o que escondem.",
            "author": "Oswald Ducrot"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "Pressuposto é uma informação não dita explicitamente, mas marcada obrigatoriamente por um elemento linguístico (um verbo, um advérbio ou uma oração adjetiva). Se eu digo 'Mariana deixou de fumar', o verbo 'deixou' pressupõe gramaticalmente que ela fumava antes. Já o subentendido é uma insinuação que depende totalmente do contexto e da sagacidade do leitor, podendo ser negada pelo emissor ('Está frio aqui' subentende 'feche a janela')."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "O ENEM adora questionar o papel de advérbios e adjetivos: 'O emprego do advérbio [ainda / já / até] no trecho denota o pressuposto de que...' ou 'A estratégia argumentativa constrói o subentendido de que...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Gatilhos gramaticais de pressuposto: verbos que indicam mudança ou continuidade ('voltou a', 'começou a', 'parou de'), advérbios temporais ('ainda' pressupõe que algo continuava até então; 'já' pressupõe mudança antes do esperado) e orações subordinadas adjetivas explicativas."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Frase de propaganda: 'Até os bancos estatais agora oferecem taxas justas.' O vocábulo 'até' é um operador inclusivo de escala extrema que pressupõe que os bancos estatais eram os mais improváveis ou os últimos a praticar tais taxas. Gabarito imediato."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Pressuposto tem carimbo gramatical indiscutível no texto ('deixou', 'ainda', 'já'). Subentendido fica solto no ar e depende da malícia do contexto!"}
        ]
    })

    # CAPÍTULO 5
    chapters.append({
        "number": "ESTAÇÃO V",
        "title": "Ironia, Humor e Ruptura de Expectativa",
        "epigraph": {
            "text": "A ironia é a elegância de dizer o oposto para revelar a verdade.",
            "author": "Machado de Assis"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "O humor e a ironia no ENEM nunca são gratuitos: são sempre ferramentas de crítica social, política ou comportamental. A ironia se baseia na dissonância entre o que é dito e o que se pretende comunicar (antífrase). O humor quase sempre nasce da quebra brusca de expectativa (o desfecho do último quadrinho que desconstrói a premissa séria dos anteriores) ou da ambiguidade lexical (duplo sentido)."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "Os enunciados apontam diretamente para o recurso: 'O efeito de humor decorre da quebra de expectativa provocada por...', 'O tom irônico do texto constrói-se pela contraposição entre...' ou 'O recurso à ambiguidade no último quadrinho evidencia...'. Foco sempre no efeito crítico gerado."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Leitura literal do texto irônico. A banca coloca entre as alternativas exatamente aquilo que o texto disse na superfície, mas que na verdade era uma ironia escrachada. Quem lê ironia de forma literal cai imediatamente no distrator ingênuo."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Tirinha: Personagem olha para uma montanha de lixo em um rio poluído e diz: 'Que maravilhoso progresso alcançamos!'. Pergunta: 'O efeito de sentido decorre do emprego de ironia que visa a...'. Gabarito: 'Criticar a degradação ambiental promovida sob a justificativa do avanço econômico.' Distrator: 'Elogiar as conquistas industriais contemporâneas.'"},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Viu ironia no ENEM? Inverta o sentido literal e procure a denúncia social por trás do sorriso. O riso na prova do INEP é sempre reflexivo e político!"}
        ]
    })

    # CAPÍTULO 6
    chapters.append({
        "number": "ESTAÇÃO VI",
        "title": "Intertextualidade: Paródia, Paráfrase, Alusão e Pastiche",
        "epigraph": {
            "text": "Um texto é um tecido construído a partir de citações antigas.",
            "author": "Roland Barthes"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "Intertextualidade é o diálogo explícito ou implícito entre dois textos. Suas duas formas rainhas no ENEM são: 1. Paráfrase (diálogo concordante que reafirma as ideias do texto-fonte com outras palavras, mantendo o sentido original, como uma citação de apoio); 2. Paródia (diálogo subversivo, irônico ou crítico que deforma o texto-fonte para rir dele, criticar uma realidade presente ou contestar o original)."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "O exame traz dois textos (Texto I clássico, ex: 'Canção do Exílio' de Gonçalves Dias; Texto II moderno, ex: poema de Oswald de Andrade ou Murilo Mendes) e pergunta: 'A comparação entre os dois textos evidencia que o Texto II estabelece com o Texto I uma relação de...' ou 'O Texto II retoma o Texto I com a finalidade de ressignificar...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Confundir Paráfrase com Paródia. Se o segundo texto mantém a reverência patriótica ao primeiro, é paráfrase. Se o segundo texto diz 'Minha terra tem palmeiras onde canta o sabiá / As aves que aqui gorjeiam não cantam como as de lá / Mas aqui tem fome e corrupção', houve quebra crítica: é PARÓDIA subversiva!"},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Texto clássico: Mona Lisa serena. Imagem contemporânea: Mona Lisa usando máscara de proteção e segurando álcool em gel durante a pandemia. Pergunta: 'A releitura da obra clássica configura um diálogo intertextual cujo propósito é...'. Gabarito: 'Ressignificar um ícone da história da arte para dialogar com as urgências sanitárias contemporâneas.'"},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Paráfrase confirma e respeita o original (voz uníssona). Paródia distorce, critica ou satiriza o original (voz dissonante). Alusão apenas cita brevemente de passagem!"}
        ]
    })

    # CAPÍTULO 7
    chapters.append({
        "number": "ESTAÇÃO VII",
        "title": "Estratégias de Argumentação: O Arsenal da Persuasão",
        "epigraph": {
            "text": "Opinião sem evidência é apenas ruído; argumento é arquitetura lógica.",
            "author": "Lógica do Discurso"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "O autor de um artigo de opinião ou ensaio precisa convencer o leitor. Para isso, ele recorre a 5 estratégias clássicas: 1. Autoridade (citação de especialista respeitado, filósofo, cientista ou órgão institucional renomado); 2. Evidência / Dados Estatísticos (números do IBGE, IPEA, pesquisas empíricas); 3. Causa e Consequência (relação causal de que A inevitavelmente desencadeia B); 4. Exemplificação / Caso Real (concretude dramática); 5. Contra-argumentação (antecipar o argumento do adversário para desmontá-lo em seguida)."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "Enunciado típico: 'Para conferir credibilidade e força persuasiva à sua tese, o articulista recorre prioritariamente ao recurso de...' ou 'O encadeamento argumentativo do segundo parágrafo constrói-se mediante a relação de...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Identificar erroneamente o tipo de recurso: chamar dado estatístico de 'opinião subjetiva', ou chamar citação de filósofo de 'exemplificação cotidiana'. Atente para a fonte: órgão científico = autoridade/evidência; relato pessoal = exemplificação empírica."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Se o texto diz: 'Como alerta o sociólogo Zygmunt Bauman, a modernidade líquida fragilizou os laços comunitários.' A estratégia é argumento de AUTORIDADE filosófica para legitimar o diagnóstico social do articulista."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Citação de pensador/instituto = Autoridade. Gráficos/porcentagens = Evidência/Comprovação. Se aconteceu X, logo acontece Y = Causa e Efeito. 'Dizem que X, mas na verdade Y' = Contra-argumentação!"}
        ]
    })

    # CAPÍTULO 8
    chapters.append({
        "number": "ESTAÇÃO VIII",
        "title": "Função Social dos Textos: Para Quem e Para Que Serve",
        "epigraph": {
            "text": "Nenhum texto nasce no vácuo; todo texto cumpre uma missão no mundo.",
            "author": "Linguística Pragmática"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "A competência fundamental de Linguagens no ENEM avalia se você compreende que todo texto tem uma função social na esfera pública: informar, conscientizar, reivindicar direitos, mobilizar comportamentos, entreter, denunciar abusos ou regular ações da cidadania. O texto não é julgado por sua beleza abstrata, mas pela sua utilidade comunicativa dentro da sociedade em que circula."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "Comandos diretos: 'Considerando o suporte em que foi veiculado, o texto cumpre a função social de...', 'A mensagem da campanha publicitária atua na esfera comunitária com o intuito de...' ou 'O estatuto legal apresentado destina-se a assegurar...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Ignorar o suporte e o público-alvo. Um cartaz colado em um posto de saúde tem função social diferente de uma coluna assinada na Folha de S.Paulo ou de um termo de uso de aplicativo. Olhe sempre para o rodapé (fonte): saber de onde o texto foi extraído entrega metade do gabarito!"},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Texto: Guia prático de combate ao assédio no transporte público publicado no metrô. Função social: conscientizar a população sobre a gravidade da conduta e orientar as vítimas sobre os canais imediatos de denúncia e acolhimento."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Olhe a fonte no rodapé: site governamental quer orientar/regular; jornal quer noticiar/opinar; ONG quer conscientizar/mobilizar; dicionário quer normatizar/definir!"}
        ]
    })

    # CAPÍTULO 9
    chapters.append({
        "number": "ESTAÇÃO IX",
        "title": "Texto e Contexto Histórico: O Diálogo com Sua Época",
        "epigraph": {
            "text": "A literatura e a arte são os sismógrafos das convulsões de seu tempo.",
            "author": "Antonio Candido"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "Todo texto reflete, refrata ou contesta o momento histórico em que foi produzido: a censura da ditadura militar, o autoritarismo do Estado Novo, a euforia modernista dos anos 1920, as dores da escravidão no século XIX ou o isolamento pandêmico recente. Interpretar no ENEM exige articular as escolhas estéticas e lexicais do autor com as tensões sociais, econômicas e políticas daquele período."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "Comandos típicos: 'Produzido durante o período da ditadura militar brasileira, o poema expressa resistência por meio de...', 'O romance de 1930 reflete o contexto socioeconômico regional marcado por...' ou 'A crônica dialoga com as transformações urbanas do início do século XX ao focalizar...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Anacronismo! Julgar um texto colonial do Barroco ou do Arcadismo com os valores morais e científicos do século XXI, ou desvincular um poema de Drummond da Segunda Guerra Mundial e da crise política da Era Vargas quando o próprio texto dá pistas explícitas da angústia bélica."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Canção 'Cálice' de Chico Buarque e Gilberto Gil (1973): 'Pai, afasta de mim esse cálice'. A homofonia entre 'cálice' (taça litúrgica de sofrimento) e 'cale-se' (ordem autoritária de censura) dialoga diretamente com o contexto de repressão e cerceamento à liberdade de expressão do AI-5."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Sempre confira a data da publicação original no rodapé! 1888 = Abolição; 1922 = Semana de Arte Moderna; 1930 = Seca e Crise Social; 1964-1985 = Ditadura e Censura. A data é a chave secreta do texto!"}
        ]
    })

    return chapters
