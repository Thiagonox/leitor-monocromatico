# -*- coding: utf-8 -*-
"""Módulo III: Gramática Aplicada ao Sentido e Mecânica Textual (Capítulos 18 a 23)"""

def get_chapters():
    chapters = []

    # CAPÍTULO 18
    chapters.append({
        "number": "ESTAÇÃO XVIII",
        "title": "Classes de Palavras e Modalizadores: Os Rastros da Opinião",
        "epigraph": {
            "text": "O adjetivo é a sombra da alma que escreve.",
            "author": "Linguística da Enunciação"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "O ENEM não pergunta 'qual é o substantivo da frase'. Ele quer saber o efeito de sentido das escolhas lexicais. Modalizadores são palavras que revelam o grau de certeza, adesão, obrigatoriedade ou avaliação do autor sobre o que ele mesmo afirma: advérbios avaliativos ('lamentavelmente', 'surpreendentemente', 'certamente', 'talvez'), verbos modais ('deve', 'pode', 'precisa') e adjetivos axiológicos ('medíocre', 'admirável', 'urgente')."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "Fórmula consagrada: 'No texto, o vocábulo [infelizmente / supostamente / necessário] atua como um modalizador discursivo que indica...', 'A escolha do adjetivo [X] em detrimento de [Y] confere ao texto um tom de...' ou 'O grau de engajamento do autor manifesta-se pelo uso de...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Achar que todo texto jornalístico é isento e neutro. Advérbios como 'supostamente' ou 'curiosamente' revelam desconfiança e ironia do jornalista, destruindo a suposta neutralidade da informação."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Frase: 'O projeto, pretensiosamente revolucionário, fracassou em sua execução.' O advérbio 'pretensiosamente' qualifica o adjetivo 'revolucionário', revelando a postura crítica e irônica do autor quanto à empáfia e à falta de substância da proposta."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Modalizador é a impressão digital ideológica do autor. Se o texto tem 'certamente', há certeza absoluta; se tem 'supostamente', há desconfiança irônica; se tem 'lamentavelmente', há julgamento de valor!"}
        ]
    })

    # CAPÍTULO 19
    chapters.append({
        "number": "ESTAÇÃO XIX",
        "title": "Verbos, Tempos e Modos: O Relógio Psicológico da Narrativa",
        "epigraph": {
            "text": "O tempo gramatical é a moldura viva da memória e da imaginação.",
            "author": "Morfossintaxe Discursiva"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "A escolha dos tempos verbais carrega efeitos semânticos decisivos: 1. Presente do Indicativo Histórico/Universal (traz um fato do passado para o presente, criando intimidade e dinamismo; ou expressa verdades científicas atemporais); 2. Pretérito Perfeito (ação pontual, concluída, que empurra a narrativa para frente); 3. Pretérito Imperfeito (ação habitual, contínua ou inacabada no passado, que descreve cenários e estados de espírito); 4. Futuro do Pretérito (hipótese, polidez, dúvida ou condição irrealizada)."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "A prova pergunta pela intenção discursiva: 'O emprego predominante do pretérito imperfeito no fragmento tem o efeito de criar uma atmosfera de...', 'A alternância entre o pretérito perfeito e o imperfeito marca a distinção entre...' ou 'O futuro do pretérito é utilizado para atenuar...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Dizer que o pretérito imperfeito indica ação que 'nunca aconteceu'. Não! Ele indica ação que ocorria com frequência ('ele caminhava toda manhã') ou que servia de pano de fundo para outra que a interrompeu ('ele caminhava quando a chuva desabou')."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Texto de memória: 'A casa rangeva sob o vento e as janelas batiam sem parar.' O pretérito imperfeito constrói um cenário descritivo estendido e durativo, imergindo o leitor na ambiência sensorial da recordação de infância."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Pretérito Perfeito = Aconteceu e acabou rápido (pá! aconteceu!). Pretérito Imperfeito = Acontecendo por um tempo, repetido ou pano de fundo descritivo (estava lá acontecendo...). Futuro do Pretérito = Hipótese incerta ('seria', 'faria')!"}
        ]
    })

    # CAPÍTULO 20
    chapters.append({
        "number": "ESTAÇÃO XX",
        "title": "Concordância e Variação Linguística: A Gramática Viva do Brasil",
        "epigraph": {
            "text": "Não existe erro de português; existe inadequação linguística ao contexto comunicativo.",
            "author": "Marcos Bagno"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "O ENEM NUNCA considera a fala popular, regional, periférica ou caipira como 'português errado' ou 'inferior'. Para o INEP, a língua é diversa e dinâmica: existem variedades linguísticas (diatópicas/regionais, diastráticas/sociais, diafásicas/formais e informais). A norma-padrão (culta) é necessária em documentos oficiais, leis e redações do vestibular, mas a oralidade coloquial segue regras gramaticais internas consistentes e cumpre plenamente sua função comunicativa."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "Atenção máxima: o gabarito JAMAIS será preconceituoso. Comandos: 'O texto acolhe marcas da linguagem coloquial com o intuito de conferir verossimilhança e espontaneidade à fala de...', 'O uso de construções como [a gente fomos / os menino chegou] evidencia uma regra da variedade popular que opera por...' ou 'A adequação da linguagem ao contexto de circulação demonstra que...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Qualquer alternativa que afirme que a linguagem popular 'revela ignorância', 'empobrece a língua', 'viola a lógica' ou 'deve ser erradicada'. Tais alternativas são DISTRATORES DE PRECONCEITO LINGUÍSTICO que a banca coloca para eliminar quem não estudou sociolinguística!"},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Poema de Patativa do Assaré ou letra de rap de Emicida com termos regionais e marcas da oralidade: a função desse registro é legitimar a identidade sociocultural do falante e conferir expressividade e representatividade estética à poesia popular."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Se a alternativa disser que o povo 'fala errado' ou 'destrói a gramática', elimine na hora! A resposta certa no ENEM sempre valoriza a riqueza da variação e a adequação ao contexto social!"}
        ]
    })

    # CAPÍTULO 21
    chapters.append({
        "number": "ESTAÇÃO XXI",
        "title": "Regência, Sentido e Crase Sem Mistério: Onde Mora o Significado",
        "epigraph": {
            "text": "Mudar a preposição de um verbo é mudar o rumo de sua intenção.",
            "author": "Sintaxe Aplicada"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "Regência no ENEM é cobrada pelo efeito de sentido: 1. Assistir algo (ver/presenciar: 'assistiu ao filme'; prestar socorro: 'assistiu o paciente'); 2. Aspirar algo (respirar: 'aspirou o ar fresco'; almejar/desejar: 'aspirava a um cargo melhor'); 3. Visar algo (mirar ou assinar: 'visou o alvo/cheque'; ter por objetivo: 'visa à igualdade'). A crase (fusão da preposição 'a' com o artigo 'a') só ocorre diante de palavras femininas que admitam artigo e sejam regidas por termo que exija a preposição 'a'. Jamais antes de verbo, pronome pessoal ou substantivo masculino genérico."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "O ENEM cobra regência inserida em textos reais, charges ou campanhas publicitárias: 'A mudança na regência do verbo no trecho [X] provocaria a alteração de seu sentido para...' ou 'O acento grave indicativo de crase na frase justifica-se pela...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Colocar crase antes de verbo ('disposto à lutar' — ERRADO!) ou antes de substantivo masculino ('vendeu à prazo' — ERRADO!). Teste infalível de troca: substitua a palavra feminina por uma masculina ('vou à feira' -> 'vou ao mercado'; deu 'ao', tem crase!)."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Frase de campanha: 'Esta lei visa a garantir direitos fundamentais.' O verbo 'visar' exige preposição 'a' pelo sentido de almejar, mas antes do verbo 'garantir' a crase é terminantemente proibida. Perfeito."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Crase antes de verbo: NUNCA! Crase antes de homem: NUNCA! Trocou pelo masculino e virou 'AO'? CRASE NO 'A' COM CERTEZA!"}
        ]
    })

    # CAPÍTULO 22
    chapters.append({
        "number": "ESTAÇÃO XXII",
        "title": "Pontuação Expressiva: Travessões, Dois-Pontos e Parênteses",
        "epigraph": {
            "text": "A pontuação não é apenas a respiração da voz; é a arquitetura da ênfase.",
            "author": "Estilística Textual"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "Pontuação no ENEM não serve só para não morrer sem fôlego: é um recurso estético e argumentativo de alto nível: 1. Dois-pontos introduzem uma explicação, síntese, enumeração ou citação de fala direta; 2. Travessões duplos e Parênteses isolam comentários à parte, ressalvas irônicas ou esclarecimentos adicionais, conferindo destaque enfático ao trecho intercalado; 3. Ponto e vírgula separa itens de uma lista complexa ou orações coordenadas com vírgulas internas; 4. Reticências marcam suspensão de pensamento, hesitação lírica ou cumplicidade com o subentendido."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "Comandos: 'O emprego dos travessões no segundo parágrafo cumpre a função estilística de...', 'Os dois-pontos foram utilizados com o propósito de introduzir uma...' ou 'As reticências no final da frase sugerem ao leitor que...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Confundir travessão de diálogo (fala de personagem) com travessão de isolamento explicativo em texto dissertativo. Em artigos de opinião, o par de travessões atua como substituto enfático de parênteses ou vírgulas para destacar a opinião do autor."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "Trecho: 'A reforma tributária — que há três décadas dormia em gavetas burocráticas — foi finalmente votada.' Os travessões isolam uma oração explicativa, imprimindo um tom crítico de desabafo à lentidão do processo legislativo."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "Dois-pontos anunciam explicação ou prova. Par de travessões dá um megafone para uma fofoca/opinião no meio da frase. Reticências piscam o olho para o que não foi dito!"}
        ]
    })

    # CAPÍTULO 23
    chapters.append({
        "number": "ESTAÇÃO XXIII",
        "title": "Coesão, Conectivos e Vozes Verbais: A Mecânica da Costura Textual",
        "epigraph": {
            "text": "Um texto sem conectivos precisos é como uma parede de tijolos sem cimento.",
            "author": "Coesão e Coerência"
        },
        "sections": [
            {"type": "heading", "level": 2, "content": "⚡ O Raio-X em 30 Segundos"},
            {"type": "paragraph", "content": "A coesão textual opera em dois eixos: 1. Coesão Referencial: anáfora (pronomes como 'este', 'esse', 'o qual', 'ele' retomando termos já ditos para evitar repetição viciosa) e catáfora (antecipando termos futuros: 'Quero apenas isto: aprovação'); 2. Coesão Sequencial: os conectivos lógicos indispensáveis: Adversativos (oposição pura: mas, porém, contudo, todavia); Concessivos (ressalva que NÃO anula a ideia principal: embora, ainda que, apesar de, conquanto); Conclusivos (portanto, logo, destarte, dessarte); Causais (porque, já que, visto que, dado que). 3. Voz Passiva Sintética com 'se': 'Construíram-se escolas' (escolas foram construídas) oculta o agente para conferir impessoalidade institucional."},
            {"type": "heading", "level": 2, "content": "🎯 Como o ENEM Cobra no Enunciado"},
            {"type": "paragraph", "content": "Comandos de peso na TRI: 'O conectivo [embora / contudo / portanto] estabelece entre as orações uma relação semântica de...', 'O pronome [isso / este] retoma por anáfora a ideia de...' ou 'O emprego da voz passiva no trecho visa a conferir ao relato um efeito de impessoalidade ao...'."},
            {"type": "callout", "title": "⚠️ O Distrator Fatal (A Pegadinha da Alternativa)", "content": "Trocar Causa por Consequência! 'Choveu tanto que a cidade alagou' -> A chuva é a CAUSA; o alagamento é a CONSEQUÊNCIA. O distrator inverte a flecha lógica. E nunca confunda adversidade ('mas' = anula o anterior) com concessão ('embora' = ressalva que não impede a ação principal)."},
            {"type": "heading", "level": 2, "content": "💡 Aplicação Relâmpago Resolvida"},
            {"type": "paragraph", "content": "'Embora o PIB tenha crescido 3%, a desigualdade social permaneceu intocada.' O conectivo 'embora' introduz uma concessão: a melhoria do indicador macroeconômico é admitida como fato, mas é insuficiente para barrar a constatação crítica de que a renda continuou concentrada."},
            {"type": "callout", "title": "📌 Flashcard Mental de Bolso", "content": "'Mas/porém' = Quebra e anula o que veio antes. 'Embora/apesar de' = Dá o braço a torcer, mas a tese principal segue firme! Voz passiva com 'se' = Esconde quem fez e destaca a coisa feita!"}
        ]
    })

    return chapters
