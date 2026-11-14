# -*- coding: utf-8 -*-
"""Curso de Ciências da Natureza ENEM - Módulo 5: Física (Hidrostática, Termologia, Termodinâmica, Magnetismo, Ondulatória, Óptica e Física Moderna - Capítulos 22 a 28)"""


def get_chapters():
    return [
        {
            "id": "nat-cap-22-hidrostatica",
            "number": 22,
            "title": "22. Hidrostática: Pressão, Densidade, Empuxo, Princípios de Pascal e Arquimedes",
            "epigraph": {
                "text": "Por que um navio de aço maciço flutua serenamente no oceano enquanto um pequeno prego do mesmo metal afunda em segundos? A resposta não está no peso absoluto, mas na genialidade dos fluidos em repouso.",
                "author": "Aula Magna de Hidrostática Aplicada"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas e Densidade vs. Massa Específica"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo a uma das aulas mais visuais da Física do ENEM. Pense em três cenas: alguém de salto agulha afundando na areia enquanto você caminha descalço sem esforço; seus ouvidos entupindo no fundo da piscina; e um caminhão pesado sendo erguido com uma mão no macaco hidráulico. Tudo isso é Hidrostática, o estudo dos fluidos em equilíbrio."
                },
                {
                    "type": "paragraph",
                    "content": "Comecemos por uma distinção que salva pontos na prova: massa específica (μ ou ρ) é propriedade da substância maciça (μ = m / V). A água pura tem 1 g/cm³ (1.000 kg/m³), e o aço tem cerca de 7,8 g/cm³. Já a densidade do corpo (d = m_total / V_externo) considera o objeto inteiro, inclusive espaços ocos. Um navio de aço possui enormes compartimentos cheios de ar, derrubando sua densidade média para menos de 1 g/cm³ — por isso flutua!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Conversão Rápida de Densidade",
                    "content": "Na prova do ENEM, passe de g/cm³ para kg/m³ multiplicando por 1.000! Assim, 0,8 g/cm³ (álcool ou óleo) vira 800 kg/m³, e 13,6 g/cm³ (mercúrio) vira 13.600 kg/m³. E lembre: 1 litro equivale a 1 dm³ (1.000 cm³), e 1 m³ comporta exatos 1.000 litros."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Pressão Mecânica: Salto Alto, Sapato Largo e o Segredo do Prego"
                },
                {
                    "type": "paragraph",
                    "content": "Imagine duas pessoas de 60 kg (peso = 600 N, com g = 10 m/s²) sobre um gramado fofo. A primeira usa tênis de sola larga (área = 0,03 m²), gerando pressão P = F / A = 600 / 0,03 = 20.000 Pa. A segunda usa salto agulha com ponteira de 0,0001 m² (1 cm²): a mesma força concentrada gera 600 / 0,0001 = 6.000.000 Pa! Quando queremos cortar ou furar (faca afiada, ponta fina do prego), reduzimos a área para maximizar a pressão; quando queremos evitar afundar (trator de esteira na lama ou esqui na neve), aumentamos a área para espalhar o peso."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Pressão Hidrostática (Stevin): Mergulhos e Barragens"
                },
                {
                    "type": "paragraph",
                    "content": "Na piscina, a pressão cresce com a profundidade porque, além da pressão atmosférica na superfície (Patm ≈ 1,0 × 10⁵ Pa ou 1 atm ao nível do mar), você carrega o peso da coluna de água acima. Pelo Teorema de Stevin, P = Patm + d · g · h — note que o formato do recipiente não importa, apenas densidade d, gravidade g e profundidade h! Na água (d = 1.000 kg/m³), cada 10 m acrescentam ΔP = 1.000 × 10 × 10 = 100.000 Pa (+1 atm). Assim, um mergulhador a 20 m suporta 3 atm (1 do ar + 2 da água). É também por Stevin que barragens de hidrelétricas têm paredes bem mais grossas na base do que no topo."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Princípio de Pascal: Multiplicando Forças na Prensa Hidráulica"
                },
                {
                    "type": "paragraph",
                    "content": "Blaise Pascal mostrou que qualquer acréscimo de pressão em um líquido confinado se transmite integralmente a todos os pontos do fluido. Apertando o êmbolo menor (área A1) com força F1, o acréscimo ΔP = F1 / A1 viaja até o êmbolo maior (área A2), gerando F2 = ΔP · A2. Logo, F1 / A1 = F2 / A2."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Elevador de Oficina",
                    "content": "Um mecânico quer erguer um carro de 1.500 kg (peso = 15.000 N) num elevador hidráulico com A2 = 0,50 m² e A1 = 0,01 m². Aplicando Pascal: F1 / 0,01 = 15.000 / 0,50 → F1 / 0,01 = 30.000 → F1 = 300 N (equivalente a 30 kg)! Pegadinha da TRI: a força multiplicou por 50, mas a energia se conserva; para o carro subir 10 cm, o pistão menor precisa descer 50 × 10 cm = 5 metros!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Empuxo de Arquimedes: O Segredo da Flutuação e dos Submarinos"
                },
                {
                    "type": "paragraph",
                    "content": "Pelo Teorema de Stevin, a pressão embaixo de um corpo submerso é maior que em cima, criando uma força vertical para cima chamada Empuxo (E). Arquimedes provou que o empuxo iguala o peso do fluido deslocado: E = d_liq · V_sub · g, onde V_sub é apenas o volume submerso! Se o peso do corpo superar o empuxo máximo (d_corpo > d_liq), ele afunda; se for menor, sobe e flutua em equilíbrio (E = P). O submarino controla isso com tanques de lastro: admite água para ficar mais denso e mergulhar; injeta ar comprimido para expulsar a água, reduzir o peso e emergir!"
                },
                {
                    "type": "callout",
                    "title": "Questão Comentada Estilo ENEM: O Bloco de Madeira em Água e Óleo",
                    "content": "Um bloco maciço flutua na água pura (d = 1,0 g/cm³) com 60% do volume submerso. Qual porcentagem ficará submersa no álcool (d = 0,8 g/cm³)? Na água, E = P: d_agua · (0,60 · V) · g = d_bloco · V · g → d_bloco = 0,60 g/cm³. No álcool, o peso continua igual: 0,8 · V_sub · g = 0,60 · V · g → V_sub / V = 0,60 / 0,80 = 0,75 (75% submerso). Em líquidos menos densos, o corpo afunda mais para deslocar o mesmo peso!"
                },
                {
                    "type": "quote",
                    "content": "Dê-me um fluido em repouso e eu lhe mostrarei que toda pressão exercida na superfície ecoa intacta até o último milímetro das profundezas, enquanto a água devolve para o alto exatamente o peso do espaço que o corpo ousou tomar.",
                    "author": "Síntese de Pascal e Arquimedes"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-23-termologia",
            "number": 23,
            "title": "23. Termologia: Temperatura, Calor, Escalas, Dilatação, Calorimetria e Mudanças de Estado",
            "epigraph": {
                "text": "Quando você toca uma barra de metal e uma tábua de madeira na mesma sala, ambas estão à mesma temperatura; o que muda é a pressa com que o calor viaja entre sua mão e cada material.",
                "author": "Aula Magna de Termologia"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Temperatura vs. Calor: O Erro que Ninguém Mais Comete"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Vamos começar a Termologia tirando da cabeça uma confusão linguística que o ENEM adora cobrar. Na conversa de rua, dizemos 'hoje estou com calor' ou 'fecha a janela que está entrando frio'. Na Física, ninguém 'tem' calor e não existe 'frio' entrando! Temperatura é a medida do grau de agitação térmica média das partículas de um corpo: quanto mais agitadas estão as moléculas, maior a temperatura. Já o calor é energia térmica em trânsito, que flui espontaneamente do corpo de maior temperatura para o de menor temperatura até que ambos atinjam o equilíbrio térmico. Quando você pega uma pedra de gelo, não é o frio que entra na sua mão; é o calor da sua mão que foge para o gelo!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Escalas Termométricas: Celsius, Fahrenheit e Kelvin"
                },
                {
                    "type": "paragraph",
                    "content": "Para medir temperatura, criamos termômetros calibrados em pontos fixos da água ao nível do mar: fusão do gelo e ebulição da água. Na escala Celsius (°C), esses pontos valem 0 °C e 100 °C (intervalo de 100 divisões). Na escala Fahrenheit (°F), usada nos Estados Unidos, valem 32 °F e 212 °F (intervalo de 180 divisões). Já na escala absoluta Kelvin (K), usada no Sistema Internacional, o zero absoluto (0 K, que equivale a -273 °C) representa a menor agitação molecular teoricamente possível, e a água ferve a 373 K (273 K a 373 K, também 100 divisões)."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Fórmulas de Conversão Sem Decoreba",
                    "content": "Para converter valores exatos de temperatura: T_K = T_C + 273 e T_C / 5 = (T_F - 32) / 9. Exemplo prático: uma febre de 104 °F assusta, mas quanto é em Celsius? (104 - 32) / 9 = 72 / 9 = 8. Multiplicando por 5, temos 40 °C! Agora atenção à Pegadinha da TRI: se a questão pedir VARIAÇÃO de temperatura (ΔT), o +273 e o -32 somem! Como 100 divisões Celsius equivalem a 100 Kelvin, ΔT_C = ΔT_K sempre. E entre Celsius e Fahrenheit, ΔT_C / 5 = ΔT_F / 9: um aquecimento de 20 °C equivale a um salto de 36 °F!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Dilatação Térmica: Trilhos de Trem, Lâminas Bimetálicas e a Anomalia da Água"
                },
                {
                    "type": "paragraph",
                    "content": "Quando aquecemos um sólido, suas moléculas vibram mais e o corpo se dilata! Na dilatação linear (fios, trilhos, pontes), ΔL = L0 · α · ΔT, por isso engenheiros deixam juntas de dilatação entre placas de pontes e trilhos para evitar empenamento no verão. Na superficial, ΔA = A0 · β · ΔT (β = 2α); na volumétrica (sólidos ou líquidos em tanques), ΔV = V0 · γ · ΔT (γ = 3α)."
                },
                {
                    "type": "paragraph",
                    "content": "Duas aplicações clássicas do ENEM: primeiro, a lâmina bimetálica do termostato do ferro de passar, feita de cobre (α maior) colado ao ferro (α menor); ao esquentar, o cobre cresce mais, entortando a lâmina para o lado do ferro e abrindo o circuito. Segundo, a anomalia da água entre 0 °C e 4 °C: ao esfriar abaixo de 4 °C, a água se expande formando cristais abertos. Logo, a água a 4 °C (mais densa) fica no fundo dos lagos, enquanto o gelo flutua na superfície como isolante térmico, preservando a vida aquática no inverno!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Calorimetria: Calor Sensível vs. Calor Latente"
                },
                {
                    "type": "paragraph",
                    "content": "Ao fornecer calor a um corpo, se a temperatura mudar sem troca de estado físico, temos Calor Sensível ('que macete'): Q = m · c · ΔT, onde c é o calor específico (para a água, c = 1 cal/g·°C ou 4,2 J/g·°C, altíssimo!). Esse alto calor específico explica por que cidades litorâneas variam menos de temperatura que desertos. Já durante uma mudança de estado físico (gelo fundindo a 0 °C ou água fervendo a 100 °C), a temperatura fica travada enquanto o calor rompe ligações intermoleculares — é o Calor Latente ('que moleza'): Q = m · L (L_fusão = 80 cal/g e L_vaporização = 540 cal/g para a água)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Trocas de Calor e Leitura de Curvas de Aquecimento"
                },
                {
                    "type": "paragraph",
                    "content": "Em um sistema termicamente isolado (como uma garrafa térmica ou calorímetro ideal), o calor não se cria nem se perde: a soma algébrica de todos os calores trocados é zero (ΣQ = 0). Quem está mais quente cede calor (Q negativo), quem está mais frio recebe (Q positivo). E como isso aparece nos gráficos do ENEM? Em uma curva de aquecimento (Temperatura no eixo Y versus Calor ou Tempo no eixo X), os trechos inclinados representam aquecimento (Calor Sensível: quanto menos inclinada a reta, maior a capacidade térmica C = m·c do material!), e os patamares horizontais mostram as mudanças de estado (Calor Latente: fusão e ebulição), onde a temperatura permanece constante."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Café Quente com Leite Gelado",
                    "content": "Você mistura 200 g de café (trate como água, c = 1 cal/g·°C) a 80 °C com 50 g de leite frio (c ≈ 1 cal/g·°C) a 5 °C, dentro de um copo térmico ideal. Qual será a temperatura final T de equilíbrio? Montamos ΣQ = 0: Q_cafe + Q_leite = 0. Logo, 200 · 1 · (T - 80) + 50 · 1 · (T - 5) = 0. Dividindo toda a equação por 50 para facilitar a conta: 4(T - 80) + 1(T - 5) = 0 → 4T - 320 + T - 5 = 0 → 5T = 325 → T = 65 °C. Passo limpo, conta rápida e nota garantida!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Gelo Derretendo Completamente?",
                    "content": "Se uma questão misturar gelo a 0 °C com água morna, nunca chute que todo o gelo vai derreter! Calcule primeiro quanto calor a água morna consegue ceder até baixar a 0 °C (Q_cedido = m_agua · c · ΔT) e compare com o calor necessário para derreter todo o gelo (Q_fusao = m_gelo · 80). Se Q_cedido for menor que Q_fusao, parte do gelo sobra inteira e a temperatura final de equilíbrio será exatamente 0 °C!"
                },
                {
                    "type": "quote",
                    "content": "Aquecer não é apenas elevar o termômetro: às vezes a energia inteira se oculta no silêncio de um patamar horizontal, desatando os laços invisíveis que prendem um sólido ao seu estado rígido.",
                    "author": "Aula Magna de Calorimetria"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-24-termodinamica",
            "number": 24,
            "title": "24. Termodinâmica: Leis da Termodinâmica, Máquinas Térmicas e Rendimento",
            "epigraph": {
                "text": "A Primeira Lei diz que você não pode criar energia do nada; a Segunda Lei avisa que, em toda troca térmica real, a natureza sempre cobra um pedágio inevitável em calor desperdiçado.",
                "author": "Aula Magna de Termodinâmica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Do Calor ao Movimento: O Nascimento das Máquinas"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Bem-vindo ao capítulo que explica como o calor vira movimento nos motores de carros, nas locomotivas a vapor e nas usinas termelétricas — e por que o sonho de construir um motor perpétuo com 100% de eficiência é fisicamente impossível. Na Termodinâmica, o protagonista costuma ser um gás confinado em um cilindro com êmbolo móvel. Se você aquece o gás, ele pode guardar essa energia aumentando sua própria agitação interna (energia interna U) ou pode expandir o volume empurrando o êmbolo e realizando trabalho mecânico (τ)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Primeira Lei da Termodinâmica e as Quatro Transformações Gasosas"
                },
                {
                    "type": "paragraph",
                    "content": "A Primeira Lei é a conservação da energia vestida de gala: ΔU = Q - τ. Preste muita atenção aos sinais! Q é positivo quando o gás recebe calor e negativo quando perde. τ (trabalho) é positivo quando o gás se expande (empurra o mundo) e negativo quando é comprimido (o mundo empurra o gás). E ΔU (variação de energia interna) depende exclusivamente da variação da temperatura absoluta (ΔT) em um gás ideal: esquentou, ΔU > 0; esfriou, ΔU < 0."
                },
                {
                    "type": "paragraph",
                    "content": "Veja como as quatro transformações clássicas simplificam essa equação num piscar de olhos. Na transformação ISOCÓRICA (volume constante, recipiente rígido), o êmbolo não se mexe, então τ = 0; todo calor recebido vira energia interna (ΔU = Q). Na ISOTÉRMICA (temperatura constante), não muda a agitação média, logo ΔU = 0; todo calor que entra sai imediatamente em forma de trabalho (Q = τ). Na ISOBÁRICA (pressão constante), o trabalho vale exatamente τ = P · ΔV, e tudo varia junto (pressão constante, volume e temperatura crescem em proporção). Por fim, na ADIABÁTICA (sem troca de calor, muito rápida ou isolada, como o ar saindo gelado de um spray aerossol), Q = 0, então ΔU = -τ: ao se expandir rápido empurrando o ar de fora (τ > 0), o gás gasta sua própria energia interna (ΔU < 0) e esfria bruscamente!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Trabalho no Gráfico Pressão × Volume",
                    "content": "Sempre que o ENEM mostrar um gráfico de Pressão (P) no eixo vertical contra Volume (V) no eixo horizontal, o trabalho (τ) realizado pelo gás é numericamente igual à ÁREA abaixo da curva! E se o gás completar um ciclo fechado? A variação total de energia interna no ciclo completo volta ao ponto inicial, então ΔU_ciclo = 0 e o trabalho líquido vale a área interna do ciclo: positivo se o ciclo girar no sentido horário (máquina térmica gerando movimento) e negativo no anti-horário (refrigerador consumindo trabalho)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Segunda Lei, Entropia e o Fim do Sonho do Rendimento 100%"
                },
                {
                    "type": "paragraph",
                    "content": "Pense comigo: a Primeira Lei não proibiria um navio de sugar calor da água do mar, convertê-lo integralmente em trabalho para girar a hélice e deixar um rastro de gelo atrás de si. Mas isso nunca acontece! Quem proíbe é a Segunda Lei da Termodinâmica. Segundo Kelvin e Planck, é impossível uma máquina térmica operar em ciclos retirando calor de uma única fonte quente e convertendo 100% dele em trabalho útil. Parte do calor absorvido (Q_q) precisa obrigatoriamente ser rejeitada para uma fonte fria (Q_f), como o radiador e o escapamento de um carro."
                },
                {
                    "type": "paragraph",
                    "content": "Esse sentido único dos fenômenos naturais está ligado à Entropia, a grandeza que mede o grau de desordem e dispersão da energia em um sistema isolado. Espontaneamente, a entropia do universo sempre aumenta: o café quente esfria se misturando com a sala, nunca rouba calor do quarto frio para ferver sozinho; um perfume aberto se espalha pelo ambiente, nunca se recolhe de volta para o frasco. Quanto mais energia se degrada em calor espalhado para a fonte fria, menor é a fração aproveitável para gerar trabalho."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Motores a Combustão vs. Geladeiras e Ar-Condicionado"
                },
                {
                    "type": "paragraph",
                    "content": "Uma máquina térmica (motor a gasolina, diesel ou turbina a vapor) funciona recebendo calor Q_q da queima na fonte quente, convertendo parte disso em trabalho útil τ = Q_q - Q_f, e jogando o resto Q_f na fonte fria. Seu rendimento η é a razão entre o que você ganhou (τ) e o que você pagou (Q_q): η = τ / Q_q = 1 - (Q_f / Q_q). Já a geladeira ou o ar-condicionado é uma máquina térmica invertida! Ela faz o calor ir contra o fluxo natural — do interior frio (congelador) para o exterior quente (cozinha) —, mas só consegue fazer essa 'subida' forçada porque ligamos o compressor na tomada, gastando trabalho elétrico τ. Por isso, deixar a porta da geladeira aberta no verão não refresca a cozinha: o motor trabalha dobrado e despeja atrás da geladeira todo o calor que tirou de dentro MAIS a energia elétrica do compressor, aquecendo ainda mais o ambiente!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Ciclo de Carnot: O Teto Máximo Permitido pela Natureza"
                },
                {
                    "type": "paragraph",
                    "content": "Em 1824, o engenheiro Sadi Carnot imaginou a máquina térmica ideal e reversível, formada por duas isotermas intercaladas por duas adiabáticas. Mesmo sem nenhum atrito, a Máquina de Carnot não chega a 100%! Seu rendimento máximo teórico depende apenas das temperaturas absolutas (SEMPRE EM KELVIN!) das fontes quente (T_q) e fria (T_f): η_Carnot = 1 - (T_f / T_q). Nenhuma máquina real operando entre essas duas temperaturas consegue superar Carnot."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Usina Termelétrica e Carnot",
                    "content": "Uma usina termelétrica opera com vapor superaquecido a 327 °C e condensa o vapor em um rio a 27 °C. Se ela absorve 1.000 MJ de calor da queima de combustível a cada minuto, qual a potência máxima teórica (em MJ/min) que ela poderia gerar? Passo 1 (Pegadinha mortal se pular!): converta tudo para Kelvin! T_q = 327 + 273 = 600 K; T_f = 27 + 273 = 300 K. Passo 2: aplique Carnot: η_max = 1 - (300 / 600) = 1 - 0,5 = 0,5 (ou 50%). Passo 3: calcule o trabalho máximo: τ_max = 50% de 1.000 MJ = 500 MJ por minuto. Os outros 500 MJ são despejados obrigatoriamente no rio ou na atmosfera!"
                },
                {
                    "type": "quote",
                    "content": "Mesmo no motor mais perfeito que a mente humana puder desenhar, a natureza exige que parte da energia aquecida pague passagem para o frio antes de o pistão girar.",
                    "author": "Lição de Sadi Carnot"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-25-magnetismo-eletromagnetismo",
            "number": 25,
            "title": "25. Magnetismo e Eletromagnetismo: Ímãs, Campos e Geração de Energia",
            "epigraph": {
                "text": "Correntes elétricas criam campos magnéticos; campos magnéticos variáveis criam correntes elétricas. Nesse abraço invisível entre eletricidade e magnetismo gira todo o mundo moderno.",
                "author": "Aula Magna de Eletromagnetismo"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Ímãs, Polos Inseparáveis e a Grande Bússola Planetária"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos a um dos capítulos que mais conectam a Física à tecnologia que alimenta a sua casa: o Magnetismo e o Eletromagnetismo. Todo ímã tem dois polos — Norte (N) e Sul (S) — onde as propriedades magnéticas são mais intensas. Polos de mesmo nome se repelem e polos opostos se atraem. Mas atenção à primeira lei de ouro do magnetismo: a inseparabilidade dos polos! Se você partir um ímã ao meio tentando isolar o polo Norte, não vai conseguir: surgirão instantaneamente dois ímãs completos, cada um com seu Norte e seu Sul. Não existem monopolos magnéticos isolados na natureza."
                },
                {
                    "type": "paragraph",
                    "content": "Do lado de fora de qualquer ímã, as linhas de campo magnético (vetor B, medido em Tesla - T) saem do polo Norte e entram no polo Sul, formando curvas fechadas. E olhe que curiosidade deliciosa o ENEM ama cobrar sobre a Terra: por que o polo Norte da agulha de uma bússola aponta para o Norte Geográfico? Porque polos opostos se atraem! Logo, perto do Norte Geográfico da Terra existe, magneticamente falando, um grande Polo SUL Magnético (e perto do Sul Geográfico está o Norte Magnético)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Oersted e a Regra da Mão Direita: Eletricidade Gerando Magnetismo"
                },
                {
                    "type": "paragraph",
                    "content": "Até 1820, achava-se que eletricidade e magnetismo eram mundos separados. Foi quando Hans Christian Oersted ligou um fio com corrente elétrica perto de uma bússola e viu a agulha girar na hora! Cargas elétricas em movimento (corrente elétrica) geram campo magnético ao seu redor. Para achar a direção desse campo sem errar, usamos a famosa Regra da Mão Direita Envolvente: aponte o polegar da mão direita no sentido da corrente elétrica (i) de um fio reto; os outros quatro dedos abraçando o fio indicam o sentido circular das linhas de campo magnético."
                },
                {
                    "type": "paragraph",
                    "content": "E se enrolarmos esse fio em várias voltas formando uma bobina ou solenoide, e colocarmos um núcleo de ferro dentro? Criamos um Eletroímã! Quando a corrente passa, o campo das espiras se soma dentro do tubo e o núcleo vira um ímã potentíssimo, capaz de erguer sucatas de toneladas em ferros-velhos ou acionar campainhas e fechaduras eletrônicas. Desligou a corrente, o magnetismo desaparece e a sucata cai!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Força Magnética e o Segredo dos Motores Elétricos"
                },
                {
                    "type": "paragraph",
                    "content": "Se um fio com corrente cria um campo magnético, o que acontece quando colocamos uma carga elétrica em movimento (ou um fio com corrente) dentro de um campo magnético externo? Surge uma Força Magnética! Para uma carga q com velocidade v entrando num campo B sob ângulo θ, a força vale F = |q| · v · B · sen(θ). Note dois segredos fundamentais aqui: primeiro, se a carga estiver parada (v = 0) ou viajar paralela ao campo (θ = 0° ou 180°), a força magnética é ZERO! Segundo, a força magnética é sempre perpendicular à velocidade, por isso ela nunca acelera ou freia a carga — ela apenas desvia sua trajetória, fazendo partículas carregadas do vento solar espiralarem perto dos polos da Terra e criarem as belíssimas auroras boreais e austrais!"
                },
                {
                    "type": "paragraph",
                    "content": "Em um fio condutor de comprimento L com corrente i imerso em um campo B, essa força vale F = B · i · L · sen(θ). Quando colocamos uma espira quadrada com corrente entre os polos de um ímã, um lado é empurrado para cima e o outro para baixo, gerando um torque contínuo que faz o eixo girar sem parar. Pronto: você acabou de entender o coração de todo motor elétrico (liquidificador, ventilador, carro elétrico)!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Indução Eletromagnética: Faraday, Lenz e as Usinas Hidrelétricas"
                },
                {
                    "type": "paragraph",
                    "content": "Se eletricidade gera magnetismo, Michael Faraday perguntou: o contrário funciona? Um campo magnético pode gerar corrente elétrica sem pilha nem bateria? Sim — mas com uma condição rigorosa: é preciso HAVER VARIAÇÃO do fluxo magnético (ΔΦ) atravessando a espira! Deixar um ímã paradinho dentro de uma bobina não acende lâmpada nenhuma. Mas movimente o ímã para dentro e para fora, ou gire a bobina dentro do campo magnético: imediatamente nasce uma força eletromotriz induzida (ε = -ΔΦ / Δt) e a corrente flui!"
                },
                {
                    "type": "paragraph",
                    "content": "É exatamente assim que funcionam o dínamo da bicicleta e os geradores gigantes de Itaipu e das usinas eólicas: a água caindo ou o vento empurrando as pás faz uma turbina girar um eletroímã diante de bobinas estacionárias, variando o fluxo magnético 60 vezes por segundo e gerando a corrente alternada (60 Hz) da nossa tomada. E aquele sinal de menos na Lei de Faraday vem da Lei de Lenz: a corrente induzida sempre cria um campo magnético próprio que se OPÕE à variação que a gerou! Aproximou o polo Norte? A bobina cria um Norte para tentar repelir o ímã. Afastou o Norte? Ela cria um Sul para tentar segurá-lo. Isso garante a conservação da energia!"
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Fogões por Indução e Transformadores",
                    "content": "No fogão por indução, uma bobina sob o vidro cria um campo magnético que oscila milhares de vezes por segundo. Esse fluxo variável induz correntes elétricas circulares (correntes de Foucault) diretamente no fundo metálico da panela ferromagnética, esquentando a panela por Efeito Joule sem esquentar o vidro! Já o transformador usa duas bobinas ligadas por um núcleo de ferro para elevar ou abaixar a tensão alternada conforme o número de espiras: U1 / U2 = N1 / N2. Atenção à Pegadinha da TRI: transformador NÃO funciona com corrente contínua (pilha/bateria), porque corrente contínua gera campo constante e sem variação de fluxo não há indução!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Carregador e Transformador Ideal",
                    "content": "Um transformador ideal reduz a tensão da rede elétrica de U1 = 220 V para U2 = 11 V a fim de alimentar um aparelho eletrônico. Se a bobina primária possui N1 = 1.000 espiras e o aparelho consome corrente de i2 = 2,0 A no secundário, quantas espiras N2 tem o secundário e qual a corrente i1 no primário? Primeiro achamos N2: 220 / 11 = 1.000 / N2 → 20 = 1.000 / N2 → N2 = 50 espiras. Como o transformador é ideal, a potência se conserva (P1 = P2, ou seja, U1 · i1 = U2 · i2): 220 · i1 = 11 · 2,0 → 220 · i1 = 22 → i1 = 0,1 A. Repare que ao reduzir a tensão 20 vezes, a corrente disponível aumentou 20 vezes!"
                },
                {
                    "type": "quote",
                    "content": "Um ímã imóvel diante de um fio é apenas silêncio metálico; basta fazê-los dançar um em relação ao outro para que o movimento do mundo se transforme em luz dentro de casa.",
                    "author": "Lição de Faraday e Lenz"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-26-ondulatoria",
            "number": 26,
            "title": "26. Ondulatória: Ondas, Frequência, Comprimento de Onda, Som e Efeito Doppler",
            "epigraph": {
                "text": "Uma onda não transporta matéria de um ponto a outro; ela transporta energia e informação fazendo cada pedacinho do caminho vibrar no compasso perfeito.",
                "author": "Aula Magna de Ondulatória"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Que é Uma Onda e Como Elas se Classificam"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo à Ondulatória, um dos temas campeões absolutos de incidência no ENEM. Pense em uma 'ola' no estádio de futebol: a onda corre toda a arquibancada em segundos, mas cada torcedor apenas levanta e senta no próprio assento! Isso resume a definição perfeita: onda é uma perturbação que se propaga transportando energia e momento, SEM transportar matéria. Quanto à natureza, dividimos em ondas mecânicas (precisam de meio material para viajar, como som, ondas na água e terremotos — não existem no vácuo!) e ondas eletromagnéticas (campos elétricos e magnéticos oscilantes que viajam até no vácuo a 300.000 km/s, como luz visível, micro-ondas, Wi-Fi, raio X e ondas de rádio)."
                },
                {
                    "type": "paragraph",
                    "content": "Quanto à direção de vibração, se as partículas vibram perpendicularmente ao avanço da onda (como uma corda sacudida para cima e para baixo ou toda onda eletromagnética), temos uma onda transversal. Se vibram na mesma direção em que a onda caminha, alternando compressões e rarefações (como uma mola empurrada para frente e para trás ou o SOM no ar), temos uma onda longitudinal."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Anatomia da Onda e a Equação Fundamental (v = λ · f)"
                },
                {
                    "type": "paragraph",
                    "content": "Olhe para o desenho clássico de uma onda senoidal: o ponto mais alto chama-se crista e o mais baixo é o vale. A Amplitude (A) é a altura do eixo central até a crista — ela mede a energia carregada pela onda. O Comprimento de Onda (λ) é a distância entre duas cristas consecutivas (um ciclo completo no espaço). O Período (T) é o tempo de uma oscilação completa, e a Frequência (f = 1 / T) é quantas oscilações ocorrem por segundo, medida em Hertz (Hz). Juntando espaço e tempo, nasce a equação mais famosa da ondulatória: v = λ · f."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: Quem Manda na Frequência e na Velocidade?",
                    "content": "Guarde esta regra de ouro para nunca cair em pegadinha de interpretação: a FREQUÊNCIA (f) depende exclusivamente da fonte que emitiu a onda e NÃO muda quando a onda troca de meio (por exemplo, luz entrando do ar na água). Já a VELOCIDADE (v) depende exclusivamente das propriedades do meio por onde a onda viaja (elasticidade, densidade, índice de refração)! Logo, se a onda muda de meio e sua velocidade cai pela metade, pela fórmula v = λ · f seu comprimento de onda λ também cai pela metade."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Grandes Fenômenos Ondulatórios no Cotidiano"
                },
                {
                    "type": "paragraph",
                    "content": "A onda encontra obstáculos e interage com o mundo de cinco formas que o ENEM ama perguntar. Na REFLEXÃO, a onda bate e volta no mesmo meio (eco do som no vale, sonar de morcegos e ultrassom). Na REFRAÇÃO, a onda muda de meio, alterando sua velocidade e seu comprimento de onda, frequentemente mudando de direção (som viajando diferente no ar quente e no ar frio). Na DIFRAÇÃO, a onda contorna obstáculos ou se espalha ao passar por frestas comparáveis ao seu comprimento de onda λ: é por isso que você ouve seu amigo falando atrás do muro (ondas sonoras têm λ da ordem de dezenas de centímetros e difratam fácil!), mas não consegue vê-lo (luz tem λ minúsculo!)."
                },
                {
                    "type": "paragraph",
                    "content": "Na INTERFERÊNCIA, duas ou mais ondas se cruzam e somam suas amplitudes: crista com crista gera interferência construtiva (som mais alto, brilho forte); crista com vale gera interferência destrutiva (cancelamento — é exatamente assim que fones de ouvido com cancelamento ativo de ruído criam uma anti-onda para silenciar o barulho do avião!). E na RESSONÂNCIA, uma força externa empurra um sistema exatamente na frequência natural dele, multiplicando a amplitude até limites impressionantes — como a cantora quebrando a taça de cristal ou o forno de micro-ondas vibrando na frequência exata para agitar moléculas de água! Só cuidado: a POLARIZAÇÃO, que filtra vibrações em um único plano (como nos óculos escuros polarizados), ocorre APENAS em ondas transversais, nunca em ondas sonoras longitudinais."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Acústica: Altura, Intensidade e Timbre"
                },
                {
                    "type": "paragraph",
                    "content": "No linguajar popular, quando alguém diz 'abaixa o som que está muito alto', um físico dá um sorriso nervoso! Para a Física, as três qualidades fisiológicas do som têm significados precisos. A ALTURA diz respeito à frequência (f): som 'alto' é som agudo (frequência alta, como apito ou violino); som 'baixo' é som grave (frequência baixa, como trovão ou contrabaixo). A INTENSIDADE (o popular 'volume', medido em decibéis - dB) está ligada à amplitude da onda (energia transportada): som forte tem grande amplitude; som fraco tem pequena amplitude. Já o TIMBRE é a 'assinatura' ou formato complexo da onda, que permite distinguir um dó tocado no piano de um dó exato tocado na flauta ou na voz de um amigo."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Efeito Doppler: A Sirene da Ambulância e os Radares"
                },
                {
                    "type": "paragraph",
                    "content": "Você já reparou na sirene de uma ambulância passando por você em alta velocidade? Enquanto ela se aproxima, o som parece mais agudo ('fiiiii...'); no instante em que cruza e começa a se afastar, o som cai subitamente para mais grave ('fooooo...')! Isso é o Efeito Doppler: quando fonte e observador se aproximam, as frentes de onda são comprimidas à frente, reduzindo o comprimento de onda aparente e AUMENTANDO a frequência percebida (som mais agudo ou luz desviada para o azul). Quando se afastam, as ondas se esticam, reduzindo a frequência percebida (som mais grave ou desvio para o vermelho nas galáxias distantes!). Radares de trânsito e aparelhos de ecocardiograma Doppler usam exatamente essa diferença de frequência entre a onda emitida e a refletida para medir velocidades de carros e do sangue nas artérias."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Rádio FM e Comprimento de Onda",
                    "content": "Uma emissora de rádio transmite em 100 MHz (100 × 10⁶ Hz = 10⁸ Hz). Sabendo que as ondas de rádio são eletromagnéticas e viajam no ar com velocidade praticamente igual à da luz (v = 3,0 × 10⁸ m/s), qual é o comprimento de onda λ dessa transmissão? Aplicamos v = λ · f: 3,0 × 10⁸ = λ · 10⁸. Cortando 10⁸ dos dois lados, descobrimos imediatamente λ = 3,0 metros! É por isso que ondas de rádio contornam prédios e morros com facilidade pela difração, enquanto sinais de Wi-Fi de 5 GHz (λ ≈ 6 cm) têm alcance muito menor atrás de paredes grossas."
                },
                {
                    "type": "quote",
                    "content": "Mudar de meio transforma o passo e a velocidade da onda, mas jamais altera o ritmo com que a fonte começou a cantar.",
                    "author": "Axioma da Ondulatória"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-27-optica",
            "number": 27,
            "title": "27. Óptica: Reflexão, Refração, Espelhos, Lentes e Formação de Imagens",
            "epigraph": {
                "text": "Toda a magia dos espelhos, das miragens no asfalto quente, da fibra óptica e dos óculos que devolvem nitidez ao mundo nasce de duas regras elegantes da luz: refletir e refratar.",
                "author": "Aula Magna de Óptica Geométrica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Luz, Reflexão e o Espelho Plano do Banheiro"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Vamos iluminar agora a Óptica Geométrica. No vácuo ou em meios transparentes homogêneos, a luz se propaga em linha reta (princípio que explica sombras, eclipses e câmaras escuras). Quando um raio de luz bate em uma superfície polida e volta para o mesmo meio, ocorre a Reflexão Regular, obedecendo a uma lei simples: o ângulo de incidência (medido em relação à reta Normal, perpendicular ao espelho) é exatamente igual ao ângulo de reflexão (i = r)."
                },
                {
                    "type": "paragraph",
                    "content": "No espelho plano do seu banheiro, a imagem formada é sempre VIRTUAL (parece estar atrás do espelho, formada pelo prolongamento dos raios), DIREITA (de cabeça para cima), do MESMO TAMANHO do objeto e SIMÉTRICA: se você está a 1 metro do espelho, sua imagem parece estar 1 metro atrás dele, ficando a 2 metros de você! Além disso, ocorre inversão lateral (enantiomorfismo): por isso a palavra AMBULÂNCIA vem escrita espelhada no capô da viatura, para que o motorista da frente leia corretamente pelo retrovisor plano."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Espelhos Esféricos: Côncavos na Maquiagem vs. Convexos no Retrovisor"
                },
                {
                    "type": "paragraph",
                    "content": "Curvando um espelho, criamos espelhos esféricos com poderes incríveis. Comece pelo mais simples de decorar: o ESPELHO CONVEXO (parte refletora do lado de fora, como a barriga de uma colher ou aqueles espelhos redondos de cantos de garagem e lojas). Não importa onde você coloque o objeto diante de um espelho convexo, ele forma SEMPRE uma imagem VIRTUAL, DIREITA e MENOR! Por que usamos espelhos convexos nos retrovisores laterais dos carros e em portarias? Porque ao encolher os objetos, eles oferecem um CAMPO VISUAL gigantesco, permitindo enxergar várias faixas da rua de uma só vez (embora façam os carros parecerem um pouco mais longe do que estão)."
                },
                {
                    "type": "paragraph",
                    "content": "Já o ESPELHO CÔNCAVO (parte refletora por dentro, como o fundo de uma colher ou antenas parabólicas) depende da posição do objeto! Longe do espelho (além do centro de curvatura ou entre o centro e o foco), ele projeta imagens REAIS e invertidas (que podem ser capturadas em uma tela, como em projetores e telescópios refletores). Mas se você aproximar o rosto entre o Foco (F) e o Vértice (V) do espelho côncavo, acontece a mágica do espelho de maquiagem e do espelhinho do dentista: ele cria uma imagem VIRTUAL, DIREITA e MAIOR (ampliada), revelando cada detalhe do rosto ou do dente!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Refração da Luz, Lei de Snell e o Segredo da Fibra Óptica"
                },
                {
                    "type": "paragraph",
                    "content": "Quando a luz atravessa a fronteira entre dois meios transparentes (como do ar para a água da piscina), sua velocidade muda e ocorre a Refração. Definimos o Índice de Refração absoluto de um meio como n = c / v, onde c é a velocidade da luz no vácuo (300.000 km/s) e v é a velocidade no meio. Quanto maior o n (mais 'refringente' o meio: n_ar ≈ 1,0; n_agua ≈ 1,33; n_vidro ≈ 1,5), mais devagar a luz anda e mais o raio entorta aproximando-se da reta Normal, obedecendo à Lei de Snell: n1 · sen(θ1) = n2 · sen(θ2). É a refração que faz a piscina parecer mais rasa do que realmente é e entorta visualmente uma colher dentro do copo d'água."
                },
                {
                    "type": "paragraph",
                    "content": "Agora veja um fenômeno espetacular: quando a luz tenta passar de um meio MAIS refringente para um MENOS refringente (como do núcleo de vidro para a casca da fibra óptica, ou da água para o ar), o raio se afasta da Normal. Se o ângulo de incidência superar um valor chamado Ângulo Limite (sen L = n_menor / n_maior), o raio não consegue sair para o outro meio e sofre REFLEXÃO INTERNA TOTAL! É assim que a internet viaja milhares de quilômetros por cabos submarinos de fibra óptica quase sem perder sinal, quicando dentro do vidro. O mesmo princípio explica a miragem no asfalto quente: camadas de ar quente junto ao chão têm menor índice de refração que o ar frio acima; a luz do céu sofre refração gradual até atingir reflexão total perto do asfalto, enganando nosso cérebro como se houvesse uma poça d'água espelhando o céu!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Lentes Esféricas e a Correção dos Defeitos da Visão"
                },
                {
                    "type": "paragraph",
                    "content": "Nos óculos, lupas e câmeras usamos lentes que funcionam por refração. Lentes CONVERGENTES (bordas finas, centro gordo) reúnem raios paralelos em um foco real; funcionam como lupa (imagem virtual, direita e maior quando o objeto está perto) ou projetam imagens reais invertidas quando o objeto está além do foco (como a lente do olho humano, o cristalino, projetando na retina). Lentes DIVERGENTES (bordas grossas, centro fino) espalham os raios e formam sempre imagem VIRTUAL, DIREITA e MENOR, reduzindo o campo de foco."
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Defeitos da Visão Humana no ENEM",
                    "content": "1) MIOPIA (dificuldade para enxergar de LONGE): o globo ocular é alongado ou o cristalino converge demais; a imagem se forma ANTES da retina. Correção: Lente DIVERGENTE (abre um pouco os raios antes de entrarem no olho). 2) HIPERMETROPIA (dificuldade para enxergar de PERTO): globo ocular curto demais; a imagem se formaria DEPOIS da retina. Correção: Lente CONVERGENTE. 3) PRESBIOPIA ('vista cansada' após os 40 anos): o cristalino perde elasticidade e não consegue mais focar objetos próximos; corrige-se também com Lente CONVERGENTE. 4) ASTIGMATISMO (visão borrada/distorcida em certos eixos): irregularidade na curvatura da córnea; corrige-se com Lente CILÍNDRICA."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: A Receita do Oftalmologista (Vergência)",
                    "content": "Um paciente recebe uma receita de óculos indicando '-2,0 di' (ou 2,0 graus negativos). O que isso significa fisicamente? A Vergência (V) de uma lente, medida em dioptrias (di), é o inverso da distância focal em metros: V = 1 / f. Como V = -2,0 di (negativa), trata-se de uma lente DIVERGENTE usada para corrigir MIOPIA! E qual é sua distância focal? f = 1 / (-2,0) = -0,50 m, ou seja, -50 cm. Se a receita fosse +4,0 di, seria lente convergente (f = +0,25 m = 25 cm) para hipermetropia ou presbiopia."
                },
                {
                    "type": "quote",
                    "content": "Quando o raio encontra a fronteira certa sob o ângulo exato, o vidro recusa-se a deixá-lo escapar, aprisionando a luz num zigue-zague luminoso que conecta continentes.",
                    "author": "Aula Magna sobre Fibra Óptica"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-28-fisica-moderna",
            "number": 28,
            "title": "28. Física Moderna: Radioatividade, Energia Nuclear e Efeito Fotoelétrico",
            "epigraph": {
                "text": "No século XX, descobrimos que a energia vem em pacotes discretos, os átomos se transmutam liberando forças colossais e um único fóton de luz pode arrancar um elétron do metal.",
                "author": "Aula Magna de Física Moderna"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Radioatividade: Quando o Núcleo Atômico Busca Estabilidade"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Chegamos ao grand finale do nosso módulo de Física: a Física Moderna, um assunto cada vez mais queridinho pelas provas interdisciplinares do ENEM (juntando Física, Química, Biologia e até História). Todo núcleo atômico tem prótons positivos se repelindo e nêutrons ajudando a manter o núcleo unido pela força nuclear forte. Quando o núcleo é grande demais ou tem desequilíbrio entre prótons e nêutrons, ele se torna instável e emite espontaneamente radiação para alcançar um estado mais estável. Esse fenômeno é a Radioatividade."
                },
                {
                    "type": "paragraph",
                    "content": "As três emissões clássicas têm personalidades bem diferentes. A partícula ALFA (α) é pesada e lenta — na verdade é um núcleo de Hélio com 2 prótons e 2 nêutrons (carga +2, número de massa 4). Por ser grandona, interage fácil com o ar e tem BAIXÍSSIMO poder de penetração: uma simples folha de papel ou a camada morta da nossa pele a barra! Quando um núcleo emite uma alfa, seu número atômico Z cai 2 unidades e sua massa A cai 4. A partícula BETA (β⁻) é um elétron rápido expelido do núcleo quando um nêutron se transforma em próton (carga -1, massa desprezível ~0): tem poder de penetração MÉDIO (barra-se com uma chapa fina de alumínio) e faz Z subir 1 unidade mantendo A igual. Já a radiação GAMA (γ) não é partícula com massa, mas uma onda eletromagnética de altíssima frequência e energia! Sem massa e sem carga (não muda Z nem A), ela atravessa quase tudo, exigindo grossas paredes de chumbo ou concreto para ser freada."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Tempo de Meia-Vida, Carbono-14 e Medicina Nuclear"
                },
                {
                    "type": "paragraph",
                    "content": "Não dá para prever quando UM núcleo isolado vai decair, mas para bilhões de núcleos a estatística é exata! Chamamos de Tempo de Meia-Vida (T_1/2) o intervalo necessário para que METADE dos núcleos radioativos de uma amostra se desintegre. Passada 1 meia-vida, resta 1/2 (50%); após 2 meias-vidas, resta 1/4 (25%); após 3 meias-vidas, resta 1/8 (12,5%), seguindo a fórmula M_final = M_inicial / 2^n, onde n é o número de meias-vidas decorridas."
                },
                {
                    "type": "paragraph",
                    "content": "Veja duas aplicações fascinantes no cotidiano e no ENEM: na Arqueologia, todo ser vivo absorve Carbono-14 radioativo da atmosfera enquanto respira ou come; quando morre, a reposição para e o C-14 decai com meia-vida de cerca de 5.730 anos, permitindo datar ossos, pergaminhos e fósseis! Na Medicina Nuclear (radioterapia contra tumores e exames de cintilografia com Tecnécio-99m, cuja meia-vida é de apenas 6 horas), escolhem-se isótopos de meia-vida curta para fazer o diagnóstico preciso e desaparecer rápido do corpo do paciente sem deixá-lo irradiado por anos."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Datação com Fósseis",
                    "content": "Um laboratório analisa um pedaço de madeira antiga de uma fogueira pré-histórica e descobre que a concentração de Carbono-14 caiu para 12,5% da concentração encontrada em árvores vivas hoje. Considerando a meia-vida do C-14 igual a 5.730 anos, qual é a idade aproximada dessa fogueira? Vamos passo a passo sem complicar: começamos com 100%. Após 1 meia-vida, cai para 50%. Após 2 meias-vidas, cai para 25%. Após 3 meias-vidas, chega exatamente a 12,5%! Logo, passaram-se n = 3 meias-vidas. Multiplicando: 3 × 5.730 = 17.190 anos!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fissão vs. Fusão Nuclear e a Equação de Einstein (E = m · c²)"
                },
                {
                    "type": "paragraph",
                    "content": "De onde vem a energia monstruosa das usinas nucleares e das estrelas? Da equivalência entre massa e energia descoberta por Albert Einstein: E = m · c²! Como c² (velocidade da luz ao quadrado) é um número gigantesco (9 × 10¹⁶ m²/s²), transformar uma pitada microscópica de massa em energia libera quantidades colossais de calor. Na FISSÃO NUCLEAR (usada nas usinas de Angra dos Reis e em bombas atômicas), um núcleo pesado e instável como o Urânio-235 é bombardeado por um nêutron lento e se quebra em dois núcleos menores, liberando energia e mais nêutrons que provocam uma reação em cadeia controlada por barras de controle no reator (que absorvem o excesso de nêutrons)."
                },
                {
                    "type": "paragraph",
                    "content": "Já na FUSÃO NUCLEAR (o motor do Sol e de todas as estrelas!), acontece o oposto: núcleos muito leves, como isótopos de Hidrogênio (deutério e trítio), colidem sob temperaturas e pressões absurdas e se fundem formando Hélio! A fusão libera ainda mais energia por quilo de combustível que a fissão e praticamente não gera lixo radioativo de longa duração, sendo o grande sonho da engenharia energética do século XXI — o desafio está em confinar um plasma a mais de 100 milhões de graus sem derreter o reator."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Efeito Fotoelétrico: Planck, Einstein, Placas Solares e Sensores"
                },
                {
                    "type": "paragraph",
                    "content": "Fechamos o módulo com a descoberta que rendeu o Prêmio Nobel a Albert Einstein em 1921 (não foi a Relatividade!): o Efeito Fotoelétrico. Na Física Clássica, achava-se que qualquer luz brilhante o suficiente deveria esquentar um metal até arrancar elétrons dele. Mas nos experimentos acontecia algo bizarro: luz vermelha fortíssima não arrancava NENHUM elétron de certos metais, enquanto luz ultravioleta fraquinha arrancava elétrons instantaneamente! Como explicar isso?"
                },
                {
                    "type": "paragraph",
                    "content": "Usando a ideia de Max Planck, Einstein propôs que a luz não chega como um fluxo contínuo de água, mas em pacotes discretos de energia chamados FÓTONS, onde a energia de cada pacote depende exclusivamente da FREQUÊNCIA da luz: E = h · f (sendo h a constante de Planck). Para libertar um elétron preso no metal, é preciso pagar uma taxa mínima chamada Função Trabalho (Φ). Um único fóton entrega tudo para um único elétron! Se o fóton vermelho tem energia menor que Φ, aumentar o brilho apenas manda mais fótons fracos — nenhum elétron sai! Se aumentarmos a frequência (como na luz azul ou ultravioleta) para que h·f > Φ, o elétron é ejetado na hora com energia cinética máxima E_cin = h·f - Φ. E onde você vê isso hoje? Nas placas solares fotovoltaicas (que convertem fótons do Sol diretamente em corrente elétrica nas casas!), nos sensores de portas automáticas de shopping e no acendimento automático dos postes de iluminação pública ao entardecer!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI no Efeito Fotoelétrico: Intensidade vs. Frequência",
                    "content": "No efeito fotoelétrico, uma vez que a frequência da luz já está acima da frequência de corte (h·f > Φ): aumentar a FREQUÊNCIA da luz aumenta a energia cinética com que cada elétron sai voando; já aumentar a INTENSIDADE (brilho) da luz manda mais fótons por segundo, aumentando o NÚMERO de elétrons arrancados (maior corrente elétrica), sem mudar a energia individual de cada elétron!"
                },
                {
                    "type": "quote",
                    "content": "Da dança invisível de um fóton arrancando um elétron ao coração ardente das estrelas fundindo hidrogênio, a Física Moderna mostrou que o infinitamente pequeno sustenta todo o cosmos.",
                    "author": "Encerramento do Módulo de Física ENEM"
                }
            ],
            "quiz": []
        }
    ]
