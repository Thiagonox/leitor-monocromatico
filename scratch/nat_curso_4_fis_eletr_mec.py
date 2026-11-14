# -*- coding: utf-8 -*-
"""Curso de Ciências da Natureza ENEM - Módulo 4: Física - Eletricidade e Mecânica (Capítulos 16 a 21)"""


def get_chapters():
    return [
        {
            "id": "nat-cap-16-eletricidade-1",
            "number": 16,
            "title": "16. Eletricidade I: Carga Elétrica, Corrente, Tensão, Resistência e Lei de Ohm",
            "epigraph": {
                "text": "Entender eletricidade fica fácil no instante em que você enxerga os elétrons como gotas de água buscando um desnível: a tensão empurra, a corrente flui e a resistência aperta a passagem.",
                "author": "Aula Magna de Eletrodinâmica Aplicada"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas à Eletricidade Sem Mistério"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo a um dos blocos mais gostosos e rentáveis da Física no ENEM. Pense comigo: desde a hora em que você acorda, aperta o interruptor do quarto, toma um banho quente no chuveiro elétrico e coloca o celular para carregar, você está cercado de eletrodinâmica. Mesmo assim, muita gente trava nas questões porque tenta decorar letras soltas — U, i, R, Q, rho — sem visualizar o que está acontecendo lá dentro do fio. Hoje vamos construir essa imagem mental do zero, com uma analogia tão clara que você nunca mais vai confundir tensão com corrente."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Carga Elétrica, Carga Elementar e Eletrização"
                },
                {
                    "type": "paragraph",
                    "content": "Tudo começa no átomo. No núcleo moram os prótons (carga positiva) e os nêutrons (sem carga); na eletrosfera giram os elétrons (carga negativa). Em condições normais, um corpo tem a mesma quantidade de prótons e elétrons, ou seja, está eletricamente neutro. Quando dizemos que um corpo ficou eletrizado, quase sempre o que mudou foi o número de elétrons, pois os prótons estão presos no núcleo: se ganha elétrons, fica negativo; se perde, fica positivo. Mas atenção: não dá para transferir 'meio elétron'. A menor porção de carga livre na natureza é a carga elementar, e = 1,6 × 10⁻¹⁹ Coulomb (C). Logo, a carga total Q de qualquer corpo é um múltiplo inteiro dessa carga elementar: Q = n · e, onde n é o número de elétrons em excesso ou em falta. Além disso, vale o Princípio da Conservação da Carga: em um sistema isolado, a soma algébrica das cargas antes e depois de qualquer contato permanece rigorosamente igual."
                },
                {
                    "type": "paragraph",
                    "content": "Como eletrizamos um corpo no cotidiano? De três maneiras clássicas que o ENEM adora cobrar. Na eletrização por atrito, esfregamos dois materiais diferentes — como um pente de plástico no cabelo seco — e um arranca elétrons do outro, deixando os dois com cargas de sinais opostos. Na eletrização por contato, encostamos um corpo carregado em outro neutro; os elétrons se redistribuem e ambos terminam com o mesmo sinal (se as esferas condutoras forem idênticas, ficam com exatamente a média aritmética das cargas iniciais!). Já na eletrização por indução, apenas aproximamos um corpo carregado (indutor) de um condutor neutro (induzido) sem encostar, ligamos o induzido à Terra para escoar cargas e depois desfazemos a ligação: o induzido termina com sinal oposto ao do indutor."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Analogia da Caixa d'Água: Tensão (U), Corrente (i) e Resistência (R)"
                },
                {
                    "type": "paragraph",
                    "content": "Agora vem a sacada genial da aula. Imagine a caixa d'água lá em cima do telhado da sua casa ligada por um cano até a torneira do quintal. A altura da caixa d'água em relação à torneira cria uma pressão que empurra a água para baixo. Na eletricidade, essa 'pressão elétrica' que empurra os elétrons de um ponto a outro é a Tensão Elétrica (ou diferença de potencial, ddp), representada por U e medida em Volts (V). Quanto maior a tensão da tomada (127 V ou 220 V) ou da pilha (1,5 V), maior o empurrão energético por unidade de carga."
                },
                {
                    "type": "paragraph",
                    "content": "Quando você abre a torneira, a água começa a descer pelo cano. A quantidade de água que atravessa o cano a cada segundo equivale à Corrente Elétrica (i), medida em Ampères (A). Matematicamente, definimos corrente como a carga ΔQ que passa por uma seção do fio em um intervalo de tempo Δt: i = ΔQ / Δt. Dizer que uma corrente vale 2 A significa que passam 2 Coulombs de carga a cada segundo — cerca de 1,25 × 10¹⁹ elétrons desfilando dentro do cobre! E o que dificulta a descida da água? Se o cano for estreito, comprido ou cheio de pedrinhas, a água passa com dificuldade. Esse obstáculo ao fluxo é a Resistência Elétrica (R), medida em Ohms (Ω): nos fios metálicos, os elétrons trombam o tempo todo com os átomos do metal, de modo que quanto maior a resistência, menor será a corrente para uma mesma tensão."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A 1ª Lei de Ohm e o Efeito Joule no Chuveiro e no Ferro de Passar"
                },
                {
                    "type": "paragraph",
                    "content": "Georg Simon Ohm percebeu que, em muitos condutores mantidos a temperatura constante (os chamados resistores ôhmicos), a tensão aplicada U é diretamente proporcional à corrente i que atravessa o resistor. Nasce aí a fórmula mais famosa da eletrodinâmica: U = R · i. Se você dobra a tensão sobre um resistor ôhmico, a corrente dobra junto, mantendo a razão U / i constante igual a R. Cuidado apenas com um detalhe de prova 800+: se o gráfico U × i for uma curva em vez de uma reta passando pela origem, o resistor é não ôhmico — sua resistência muda conforme ele esquenta, exatamente como acontece no filamento incandescente de certas lâmpadas."
                },
                {
                    "type": "paragraph",
                    "content": "E por que um resistor esquenta? Pense naquelas colisões dos elétrons com os átomos do fio. A cada batida, o elétron transfere parte da sua energia cinética para os átomos do metal, que passam a vibrar mais rápido — e na Física, aumento da agitação térmica significa aumento de temperatura! Essa transformação direta de energia elétrica em energia térmica recebe o nome de Efeito Joule. É o coração do chuveiro elétrico, do ferro de passar, da torradeira, do secador de cabelo e do aquecedor de ambiente."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Corrente, Carga Elementar e 1ª Lei de Ohm no Chuveiro",
                    "content": "Enunciado: Um ferro de passar roupas possui resistência elétrica constante de 22 Ω e é ligado a uma tomada de 220 V durante 10 segundos. Calcule: (a) a corrente elétrica que atravessa o ferro; (b) a carga elétrica total que passa pelo cabo nesse intervalo; e (c) quantos elétrons atravessam a seção do fio.\n\nResolução passo a passo:\n1. Pela 1ª Lei de Ohm: U = R · i → 220 = 22 · i → i = 220 / 22 = 10 A.\n2. Pela definição de corrente: i = ΔQ / Δt → ΔQ = i · Δt = 10 · 10 = 100 Coulombs.\n3. Pela quantização da carga: Q = n · e → 100 = n · 1,6 × 10⁻¹⁹ → n = 100 / (1,6 × 10⁻¹⁹) = 62,5 × 10¹⁹ = 6,25 × 10²⁰ elétrons.\nVeja como três fórmulas conversam perfeitamente quando você domina o significado de cada grandeza!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A 2ª Lei de Ohm: Por Que o Fio do Chuveiro Precisa Ser Grosso?"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque o ENEM adora conectar física com segurança residencial! De que depende a resistência elétrica de um fio real? Pense de novo no cano d'água: um cano muito comprido (comprimento L grande) oferece mais atrito; um cano bem largo (área da seção transversal A grande, ou 'bitola' grossa) deixa a água passar folgada. Além disso, o material importa: cobre deixa passar fácil, borracha quase não deixa."
                },
                {
                    "type": "paragraph",
                    "content": "Ohm traduziu isso na 2ª Lei de Ohm: R = ρ · L / A, onde ρ (rô) é a resistividade elétrica do material (baixa em bons condutores como prata, cobre e alumínio; altíssima em isolantes como plástico, vidro e borracha), L é o comprimento do fio e A é a área da seção transversal. Olhe o poder dessa fórmula no dia a dia: como o chuveiro puxa uma corrente altíssima (30 A, 40 A ou mais), o fio que vem do quadro de energia até o banheiro precisa ter resistência baixíssima para não esquentar dentro da parede e causar incêndio. Para diminuir R, precisamos de uma área A bem grande — é por isso que o eletricista exige cabo de bitola grossa (como 6 mm² ou 10 mm²) no chuveiro, enquanto para uma simples lâmpada de LED basta um fio fino de 1,5 mm²!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Posição Inverno vs. Verão do Chuveiro",
                    "content": "Como a chave seletora do chuveiro muda a temperatura da água se a tensão da casa (127 V ou 220 V) é fixa? Na posição INVERNO (água bem quente), a chave encurta o caminho da corrente dentro da resistência metálica! Com menor comprimento L, pela 2ª Lei de Ohm (R = ρ·L/A), a resistência R DIMINUI. Como U é constante e i = U/R, menor resistência deixa passar MAIOR corrente elétrica, intensificando o Efeito Joule e aquecendo muito mais a água. No VERÃO, usa-se o resistor inteiro (maior L, maior R, menor corrente, água morna)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Esticando um Fio na 2ª Lei de Ohm",
                    "content": "Enunciado: Um fio cilíndrico homogêneo de cobre tem resistência de 12 Ω. Se substituirmos esse fio por outro do mesmo material e mesmo comprimento, porém com o dobro do diâmetro (e portanto o quádruplo da área da seção transversal), qual será a nova resistência?\n\nResolução passo a passo:\n1. Escrevemos a 2ª Lei de Ohm: R = ρ · L / A = 12 Ω.\n2. Lembre-se da geometria: área do círculo é A = π · r² = π · (d/2)². Dobrar o diâmetro multiplica a área por 2² = 4!\n3. Mantendo ρ e L iguais e trocando A por 4A: R_nova = ρ · L / (4A) = (1/4) · (ρ · L / A) = 12 / 4 = 3 Ω.\nResposta: A resistência cai para um quarto, isto é, 3 Ω!"
                },
                {
                    "type": "quote",
                    "content": "Na eletrodinâmica, o fio grosso é uma avenida larga onde os elétrons caminham sem engarrafamento térmico; o fio fino demais sob alta corrente é o atalho para o superaquecimento.",
                    "author": "Manual de Segurança Elétrica do Vestibulando"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-17-eletricidade-2",
            "number": 17,
            "title": "17. Eletricidade II: Circuitos Elétricos, Potência Elétrica e Consumo de Energia",
            "epigraph": {
                "text": "Saber montar circuitos em série e em paralelo é entender por que você consegue apagar a luz do quarto sem desligar a geladeira da cozinha — e por que o chuveiro é o vilão da conta de luz.",
                "author": "Aula Magna de Circuitos e Energia"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Circuitos em Série, em Paralelo e o Segredo das Tomadas da Sua Casa"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Agora que você já domina tensão, corrente e resistência, vamos ligar vários aparelhos juntos e ver como a rede elétrica funciona de verdade. Imagine que você tem dois caminhos possíveis para ligar duas lâmpadas a uma bateria: colocá-las em fila indiana, uma atrás da outra, ou colocá-las em ramos separados, lado a lado. Esses são os dois arranjos fundamentais de qualquer circuito: associação em série e associação em paralelo."
                },
                {
                    "type": "paragraph",
                    "content": "Na associação em série, existe apenas um único caminho para a corrente elétrica passar. Isso gera três consequências obrigatórias: primeiro, a corrente i é exatamente a mesma em todos os resistores (o que entra no primeiro tem que passar pelo segundo); segundo, a tensão total da fonte se divide entre eles (U_total = U₁ + U₂ + ...); terceiro, a resistência equivalente é simplesmente a soma das resistências: R_eq = R₁ + R₂ + ... + R_n. O problema prático da série é óbvio: se uma lâmpada queimar e abrir o circuito, o único caminho é interrompido e todas as outras apagam na hora, como naqueles antigos pisca-piscas de Natal!"
                },
                {
                    "type": "paragraph",
                    "content": "Já na associação em paralelo, a corrente chega a um nó e se divide em ramos independentes, voltando a se juntar depois. Aqui, as regras se invertem: todos os aparelhos ficam submetidos exatamente à MESMA tensão U da rede (por exemplo, todos recebem 127 V ou 220 V), enquanto a corrente total se divide pelos ramos (i_total = i₁ + i₂ + ...). Quanto mais aparelhos você liga em paralelo, mais caminhos novos abre para a corrente; por isso, a resistência equivalente DIMINUI e vale 1/R_eq = 1/R₁ + 1/R₂ + ... Para dois resistores em paralelo, guarde o atalho do 'produto pela soma': R_eq = (R₁ · R₂) / (R₁ + R₂). E para n resistores iguais de valor R em paralelo: R_eq = R / n!"
                },
                {
                    "type": "paragraph",
                    "content": "É exatamente por isso que a instalação elétrica da sua casa inteira é ligada em PARALELO! Cada lâmpada e cada tomada precisa receber a tensão nominal da rede (127 V ou 220 V) para funcionar com potência máxima, além de precisar funcionar de forma independente: se a lâmpada da sala queimar ou você desligar a televisão, a geladeira continua funcionando normalmente."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Circuito Misto, Disjuntores, Fusíveis e Curto-Circuito"
                },
                {
                    "type": "paragraph",
                    "content": "E quando um circuito mistura trechos em série com trechos em paralelo — a famosa associação mista? Não tem mistério: você resolve 'de dentro para fora', reduzindo primeiro os ramos que estão claramente em série ou em paralelo até sobrar um único resistor equivalente. Quer ver uma aplicação real disso? Os dispositivos de proteção — fusíveis e disjuntores — são sempre ligados em SÉRIE com o trecho que protegem!"
                },
                {
                    "type": "paragraph",
                    "content": "Por que em série? Porque toda a corrente do circuito precisa passar por dentro do disjuntor ou do fusível. Se você ligar ferro de passar, micro-ondas e secador no mesmo benjamim ('T') em paralelo, a resistência equivalente cai muito e a corrente total sobe além do limite seguro do fio. Quando i ultrapassa o valor máximo suportado, o fusível derrete por Efeito Joule (ou o disjuntor desarma magneticamente/termicamente), abrindo o circuito em série e cortando a corrente antes que os fios derretam na parede. Já o curto-circuito acontece quando dois pontos de potenciais diferentes se encostam por um fio de resistência praticamente nula: a corrente desvia quase toda por esse caminho livre, cresce absurdamente e dispara o disjuntor ou provoca faíscas."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Associação Mista e Corrente no Disjuntor",
                    "content": "Enunciado: Em uma fonte de 120 V, ligam-se dois resistores em paralelo, de 60 Ω e 30 Ω. Em série com esse conjunto paralelo, está um resistor de 10 Ω e um disjuntor de 4 A. O disjuntor vai desarmar?\n\nResolução passo a passo:\n1. Reduza primeiro o paralelo de 60 Ω com 30 Ω pelo produto pela soma: R_p = (60 · 30) / (60 + 30) = 1800 / 90 = 20 Ω.\n2. Agora R_p (20 Ω) está em série com o resistor de 10 Ω: R_eq = 20 + 10 = 30 Ω.\n3. Pela 1ª Lei de Ohm para o circuito todo: i_total = U / R_eq = 120 / 30 = 4 A.\n4. Como o disjuntor suporta até 4 A, ele opera exatamente no limite máximo sem desarmar — mas basta acrescentar mais um aparelho em paralelo para a corrente subir acima de 4 A e fazê-lo desarmar!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Potência Elétrica e o Duelo das Lâmpadas: Qual Brilha Mais?"
                },
                {
                    "type": "paragraph",
                    "content": "Potência elétrica (P) é a rapidez com que a energia elétrica é transformada em luz, calor ou movimento, medida em Watts (W = Joule por segundo). A fórmula mãe da potência é P = U · i ('Piu'). Combinando essa equação com a 1ª Lei de Ohm (U = R · i), nascem duas irmãs poderosíssimas: substituindo U, temos P = R · i²; substituindo i = U/R, temos P = U² / R. Memorize as três juntas, porque escolher a certa economiza metade das contas no ENEM!"
                },
                {
                    "type": "paragraph",
                    "content": "Veja que sacada genial na questão clássica das duas lâmpadas! Suponha que uma lâmpada A tem especificações nominais (100 W - 127 V) e uma lâmpada B tem (50 W - 127 V). Primeiro passo obrigatório: calcule quem tem maior resistência olhando para os valores nominais com P = U² / R, logo R = U² / P. Como U é igual (127 V), quanto MENOR a potência nominal, MAIOR é a resistência! Ou seja, a lâmpada B (50 W) tem o dobro da resistência da lâmpada A (100 W)."
                },
                {
                    "type": "paragraph",
                    "content": "Agora vem a mágica: se ligarmos as duas em PARALELO na tomada de 127 V, ambas recebem os mesmos 127 V; usando P = U² / R, brilha mais a de menor resistência, que é a lâmpada A (100 W), exatamente como promete o fabricante. Mas e se ligarmos as duas em SÉRIE na mesma tomada? Em série, o que é igual para as duas é a CORRENTE i! Então olhamos para P = R · i²: para a mesma corrente, dissipa mais potência a lâmpada de MAIOR resistência! Surpresa total: em série, a lâmpada de 50 W brilha MAIS do que a de 100 W! É por isso que o ENEM ama essa pergunta."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Conta de Luz na Prática: Energia em kWh"
                },
                {
                    "type": "paragraph",
                    "content": "Quando a companhia de energia bate na sua porta, você não paga por potência (kW), nem por corrente (A), nem por tensão (V): você paga por ENERGIA elétrica consumida, que é o produto da potência pelo tempo de uso: E = P · Δt. No Sistema Internacional, Joule é uma unidade minúscula para uma casa inteira; por isso a conta de luz usa o quilowatt-hora (kWh). A regra prática é infalível: passe a potência de Watts (W) para quilowatts (kW) dividindo por 1.000, passe o tempo para horas (h) e multiplique os dois!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Calculando a Conta Mensal do Chuveiro Elétrico",
                    "content": "Enunciado: Uma família de 4 pessoas toma banhos diários de 15 minutos cada em um chuveiro elétrico de 6.000 W. Considerando um mês de 30 dias e a tarifa de R$ 0,80 por kWh, qual é o custo mensal apenas com esse chuveiro?\n\nResolução passo a passo:\n1. Potência em kW: P = 6.000 W / 1.000 = 6 kW.\n2. Tempo total diário: 4 pessoas × 15 min = 60 minutos = 1 hora por dia.\n3. Tempo mensal em horas: 1 h/dia × 30 dias = 30 horas no mês.\n4. Energia consumida: E = P · Δt = 6 kW · 30 h = 180 kWh.\n5. Valor na conta: 180 kWh × R$ 0,80 = R$ 144,00.\nDica do Professor: se cada pessoa reduzir o banho de 15 para 10 minutos, economiza um terço dessa fatia da conta imediatamente!"
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: As 3 Fórmulas de Potência e Quando Usar Cada Uma",
                    "content": "• P = U · i → Use quando souber tensão e corrente (ou para achar a corrente máxima de um aparelho: i = P / U).\n• P = R · i² → Use em associações em SÉRIE (corrente i igual) ou para calcular perda por Efeito Joule em linhas de transmissão (quanto menor i, muito menor a perda!).\n• P = U² / R → Use em associações em PARALELO (tensão U igual) e para descobrir a resistência R de um aparelho a partir da etiqueta nominal (R = U_nominal² / P_nominal)."
                },
                {
                    "type": "quote",
                    "content": "Na conta de luz, potência alta ligada por poucos minutos pode empatar com potência baixa ligada o mês inteiro: o vilão sempre nasce da multiplicação da potência pelo tempo.",
                    "author": "Guia Prático de Consumo Consciente no ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-18-mecanica-1",
            "number": 18,
            "title": "18. Mecânica I: Movimento, Referencial, Velocidade, Aceleração, MU e MUV",
            "epigraph": {
                "text": "Antes de perguntar a que velocidade algo se move, pergunte em relação a quem você está olhando: na Física, até estar parado depende do ponto de vista.",
                "author": "Aula Magna de Cinemática Escalar"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Referencial: Por Que Você Está Parado e a 107.000 km/h ao Mesmo Tempo?"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo à Mecânica, o outro grande pilar da Física no ENEM. Comece fazendo um teste mental comigo agora: você está parado ou em movimento enquanto lê esta aula? Se o seu referencial for a cadeira ou o chão do quarto, você está em repouso, porque sua posição não muda com o passar do tempo. Mas se um astronauta olhar para você lá da Lua, ele vê você girando junto com a Terra em torno do Sol a cerca de 107.000 km/h! Essa é a primeira lição de ouro da Cinemática: repouso e movimento são sempre relativos ao referencial adotado."
                },
                {
                    "type": "paragraph",
                    "content": "Pense em um passageiro sentado dentro de um ônibus viajando em linha reta a 80 km/h numa rodovia. Em relação ao motorista e ao banco do ônibus, o passageiro está em repouso; em relação a uma placa na beira da estrada, o passageiro está em movimento a 80 km/h. E mais curioso ainda: a trajetória também depende do referencial! Se o passageiro deixa cair uma moeda da mão, ele a vê caindo em linha reta vertical para baixo; já quem está na calçada vê a moeda avançando para frente enquanto cai, descrevendo um arco de parábola."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Distância Percorrida vs. Deslocamento e a Velocidade Média Real"
                },
                {
                    "type": "paragraph",
                    "content": "Muita atenção aqui porque essa diferença derruba candidatos apressados: distância percorrida não é sinônimo de deslocamento escalar! Imagine que você sai do marco quilômetro 10 de uma estrada, dirige até o quilômetro 50 e depois volta para o quilômetro 20. Quanto o hodômetro do seu carro marcou de distância percorrida? Ele andou 40 km na ida mais 30 km na volta, totalizando 70 km rodados. Já o deslocamento escalar olha apenas para onde você terminou menos onde começou: ΔS = S_final - S_inicial = 20 - 10 = +10 km!"
                },
                {
                    "type": "paragraph",
                    "content": "A velocidade escalar média é definida exatamente por v_m = ΔS / Δt. Para falar a mesma língua nas provas, você precisa dominar a conversão entre metros por segundo (m/s, unidade oficial do SI) e quilômetros por hora (km/h, unidade do velocímetro). Como 1 km tem 1.000 metros e 1 hora tem 3.600 segundos, a razão vale 3,6. Logo, de m/s para km/h você MULTIPLICA por 3,6; de km/h para m/s você DIVIDE por 3,6. Guarde os pares clássicos de cabeça para ganhar tempo: 36 km/h = 10 m/s; 72 km/h = 20 m/s; 108 km/h = 30 m/s!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: A Armadilha da Média Aritmética das Velocidades",
                    "content": "Um carro vai de A até B a 60 km/h e volta de B até A pelo mesmo caminho a 40 km/h. Qual é a velocidade média do percurso de ida e volta? Quem respondeu (60 + 40)/2 = 50 km/h caiu direto na armadilha!\nComo ele demora MAIS tempo na volta (que é mais lenta), o 40 km/h pesa mais na conta. Veja como resolver sem erro atribuindo uma distância fácil, como o MMC = 120 km para cada trecho:\n• Tempo de ida: t₁ = 120 / 60 = 2 horas.\n• Tempo de volta: t₂ = 120 / 40 = 3 horas.\n• Distância total rodada = 120 + 120 = 240 km; tempo total = 2 + 3 = 5 horas.\n• Rapidez média real = 240 / 5 = 48 km/h! (E se o enunciado pedir o vetor deslocamento total de volta ao ponto de partida, ΔS = 0, logo a velocidade vetorial média é nula!)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Movimento Uniforme (MU): Velocidade Constante e Ultrapassagens"
                },
                {
                    "type": "paragraph",
                    "content": "No Movimento Uniforme (MU), a velocidade permanece constante e diferente de zero ao longo do tempo — não há aceleração. A posição do móvel a cada instante obedece à famosa 'função do sorvete': S = S₀ + v · t, onde S₀ é a posição inicial, v é a velocidade (positiva se o móvel anda a favor da trajetória, negativa se anda contra) e t é o tempo."
                },
                {
                    "type": "paragraph",
                    "content": "Onde o ENEM cobra MU com força? Em questões de encontro de dois veículos (basta igualar S_A = S_B!) e em questões de ultrapassagem ou travessia de pontes e túneis envolvendo trens ou carretas. Quando um trem de 200 m precisa atravessar completamente uma ponte de 300 m, lembre-se: a travessia só termina quando o ÚLTIMO vagão sai da ponte. Portanto, a frente do trem precisa andar o comprimento da ponte MAIS o próprio comprimento do trem: ΔS = 300 + 200 = 500 m!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Aceleração e Movimento Uniformemente Variado (MUV)"
                },
                {
                    "type": "paragraph",
                    "content": "Na vida real, carros arrancam no sinal verde e freiam na faixa de pedestres — ou seja, a velocidade muda! A grandeza que mede quão rápido a velocidade muda é a aceleração escalar média: a = Δv / Δt, medida em m/s². Dizer que um carro acelera a 3 m/s² significa que a velocidade dele aumenta 3 m/s a cada segundo que passa. Atenção a um conceito sutil: aceleração negativa não significa obrigatoriamente que o carro está freando! O movimento é acelerado quando velocidade e aceleração têm o MESMO sinal (ambas positivas ou ambas negativas), e é retardado (frenagem) quando têm SINAIS OPOSTOS."
                },
                {
                    "type": "paragraph",
                    "content": "Quando a aceleração é constante e diferente de zero, estamos no Movimento Uniformemente Variado (MUV). Aqui moram três ferramentas cirúrgicas que resolvem qualquer problema de arrancada, queda livre ou frenagem:"
                },
                {
                    "type": "paragraph",
                    "content": "1) Função da Velocidade ('vovô ateu'): v = v₀ + a · t, usada quando você quer relacionar velocidade e tempo. 2) Função da Posição ('sorvetão'): S = S₀ + v₀ · t + (a · t²) / 2, usada quando o problema envolve posição ou deslocamento com o tempo. 3) Equação de Torricelli: v² = v₀² + 2 · a · ΔS. Veja que sacada genial tem a Equação de Torricelli: ela NÃO tem a variável tempo t! Sempre que o enunciado der velocidades, aceleração e distância — sem falar em tempo nem perguntar o tempo — vá direto em Torricelli."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Tempo de Reação e Distância Total de Frenagem",
                    "content": "Enunciado: Um motorista dirige a 72 km/h quando avista um galho caído na pista. Seu tempo de reação até pisar no freio é de 0,5 s. A partir do momento em que aciona os freios, o carro desacelera uniformemente a 5 m/s² até parar. Qual a distância total percorrida desde o instante em que ele avistou o galho até parar?\n\nResolução passo a passo:\n1. Converta a velocidade para o SI: v₀ = 72 / 3,6 = 20 m/s.\n2. Fase 1 — Tempo de reação (MU, pois ainda não pisou no freio): ΔS₁ = v₀ · t_reação = 20 · 0,5 = 10 metros.\n3. Fase 2 — Frenagem até parar (MUV, sem tempo informado → Torricelli!): v = 0, v₀ = 20 m/s, a = -5 m/s².\n   0² = 20² + 2 · (-5) · ΔS₂ → 0 = 400 - 10 · ΔS₂ → 10 · ΔS₂ = 400 → ΔS₂ = 40 metros.\n4. Distância total de parada: ΔS_total = 10 + 40 = 50 metros!\nPerceba por que dirigir mexendo no celular aumenta tanto os acidentes: se o tempo de reação subir para 1,5 s, o carro anda 30 m só antes de o motorista encostar o pé no freio!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Ultrapassagem em Rodovia com Velocidade Relativa",
                    "content": "Enunciado: Um carro de 4 m de comprimento viaja a 108 km/h e ultrapassa uma carreta de 16 m de comprimento que segue no mesmo sentido a 72 km/h. Quanto tempo dura a ultrapassagem completa?\n\nResolução passo a passo:\n1. Converta as velocidades: v_carro = 108 / 3,6 = 30 m/s; v_carreta = 72 / 3,6 = 20 m/s.\n2. No mesmo sentido, a velocidade relativa de aproximação é a subtração: v_rel = 30 - 20 = 10 m/s.\n3. Distância relativa para o carro sair atrás da traseira da carreta e passar totalmente pela frente dela: ΔS_rel = 4 + 16 = 20 m.\n4. Tempo de ultrapassagem: Δt = ΔS_rel / v_rel = 20 / 10 = 2 segundos!"
                },
                {
                    "type": "quote",
                    "content": "O motorista atento respeita a distância de seguimento porque sabe que seu carro percorre dezenas de metros no intervalo em que o cérebro apenas decide pisar no freio.",
                    "author": "Física no Trânsito — Módulo de Cinemática"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-19-mecanica-2",
            "number": 19,
            "title": "19. Mecânica II: Leitura Cirúrgica de Gráficos do Movimento",
            "epigraph": {
                "text": "No ENEM, um bom gráfico vale por três fórmulas: a inclinação revela taxas de variação, e a área esconde o caminho percorrido.",
                "author": "Aula Magna de Análise Gráfica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Protocolo de 3 Segundos Antes de Olhar Qualquer Gráfico"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo a uma aula que vale ouro puro na sua nota de Ciências da Natureza. Se existe um padrão que se repete todo ano na prova de Física do ENEM, é colocar uma situação cotidiana — um carro freando no semáforo, um elevador subindo entre andares, um corredor em uma prova de 100 metros — e apresentar gráficos para você interpretar. Quem olha só para o desenho da linha cai em pegadinhas bobas, porque uma mesma reta inclinada para cima significa 'velocidade constante' no gráfico S × t, mas significa 'aceleração constante' no gráfico v × t!"
                },
                {
                    "type": "paragraph",
                    "content": "Por isso, adote o Protocolo de 3 Segundos antes de resolver qualquer questão gráfica: primeiro, leia com calma o nome e a unidade do eixo vertical (é Posição em metros, Velocidade em m/s ou Aceleração em m/s²?) e do eixo horizontal (geralmente Tempo em segundos, mas às vezes minutos ou horas!). Segundo, identifique onde o movimento começa (instante t = 0). Terceiro, verifique se a curva sobe, desce, fica reta na horizontal ou cruza o eixo."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Gráficos Posição × Tempo (S × t): Inclinação e Parábolas"
                },
                {
                    "type": "paragraph",
                    "content": "Comecemos pelo gráfico da Posição em função do Tempo (S × t). No Movimento Uniforme (MU), a função S = S₀ + v · t é do 1º grau, então o gráfico é obrigatoriamente uma RETA. Se a reta é horizontal (paralela ao eixo do tempo), a posição não muda: o corpo está PARADO (v = 0). Se a reta sobe da esquerda para a direita, a posição cresce: movimento progressivo (v > 0). Se a reta desce, a posição diminui: movimento retrógrado (v < 0). E atenção ao detalhe decisivo: quanto mais em pé (mais inclinada) estiver a reta, maior é o módulo da velocidade! Numericamente, a velocidade é igual à inclinação (ΔS / Δt) da reta."
                },
                {
                    "type": "paragraph",
                    "content": "Agora mude para o Movimento Uniformemente Variado (MUV). Como a função S = S₀ + v₀ · t + (a · t²) / 2 é do 2º grau (tem t²), o gráfico S × t NÃO é mais uma reta — ele vira uma PARÁBOLA! E o sinal da aceleração entrega a concavidade igualzinho na Matemática: se a parábola tem concavidade para cima ('carinha feliz'), a aceleração é positiva (a > 0); se tem concavidade para baixo ('carinha triste'), a aceleração é negativa (a < 0)."
                },
                {
                    "type": "paragraph",
                    "content": "Onde está o momento mais famoso do gráfico S × t no MUV? No VÉRTICE da parábola! Se o objeto vinha subindo (posição aumentando) e passa a descer (posição diminuindo), exatamente no topo da curva ele parou por um instante para inverter o sentido do movimento. Portanto, no vértice de qualquer parábola S × t, a velocidade instantânea é ZERO (v = 0)!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Gráficos Velocidade × Tempo (v × t): O Superpoder da Área"
                },
                {
                    "type": "paragraph",
                    "content": "Prepare o marca-texto porque o gráfico v × t é o rei da Cinemática no ENEM. Nele, o eixo vertical já mostra diretamente o valor da velocidade a cada instante. Se a linha está horizontal acima do zero, temos MU (velocidade constante). Se a linha está exatamente em cima do eixo horizontal (v = 0), o móvel está parado. Se a linha é uma reta inclinada, temos MUV (aceleração constante!), e a inclinação dessa reta (Δv / Δt) nos dá exatamente a aceleração!"
                },
                {
                    "type": "paragraph",
                    "content": "Mas o verdadeiro superpoder escondido no gráfico v × t chama-se ÁREA SOB A CURVA. Toda vez que você calcula a área geométrica compreendida entre a linha do gráfico e o eixo do tempo, você encontra automaticamente o DESLOCAMENTO ESCALAR (ΔS) naquele intervalo de tempo! Não importa se o gráfico forma um retângulo, um triângulo, um trapézio ou vários pedaços grudados: você resolve a questão inteira usando geometria básica de escola, sem precisar montar sistema de equações do MUV."
                },
                {
                    "type": "paragraph",
                    "content": "Só tenha um cuidado cirúrgico com os sinais no gráfico v × t: enquanto a linha está ACIMA do eixo do tempo (v > 0), a área é positiva (o corpo avança para frente). Quando a linha cruza o eixo horizontal (v = 0, momento de inversão de sentido!) e passa a ficar ABAIXO do eixo (v < 0), o corpo deu marcha à ré; essa área abaixo do eixo entra negativa no deslocamento líquido (ΔS = Área_acima - Área_abaixo). Porém, se a questão perguntar a DISTÂNCIA TOTAL PERCORRIDA pelo hodômetro, você soma os módulos das áreas (Área_acima + Área_abaixo)!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Lendo um Gráfico v × t de Frenagem e Marcha à Ré",
                    "content": "Enunciado: Um carrinho de teste parte em linha reta com velocidade de +20 m/s em t = 0 e sofre aceleração constante, exibida em um gráfico v × t como uma reta decrescente que cruza o eixo do tempo (v = 0) em t = 4 s e continua descendo até atingir v = -10 m/s em t = 6 s. Determine: (a) a aceleração; (b) o deslocamento nos 6 segundos; e (c) a distância total percorrida.\n\nResolução passo a passo:\n1. Aceleração é a inclinação da reta: a = Δv / Δt = (-10 - 20) / (6 - 0) = -30 / 6 = -5 m/s².\n2. Área acima do eixo (de t = 0 a t = 4 s): um triângulo de base 4 e altura 20 → A₁ = (4 · 20) / 2 = +40 m (andou 40 m para frente até parar em t = 4 s).\n3. Área abaixo do eixo (de t = 4 a t = 6 s): um triângulo de base (6 - 4) = 2 e altura 10 → A₂ = (2 · 10) / 2 = 10 m para trás (-10 m no deslocamento).\n4. Deslocamento escalar líquido: ΔS = 40 - 10 = +30 m.\n5. Distância total percorrida: d = 40 + 10 = 50 m!\nOlhe como a geometria resolveu em 4 linhas o que levaria o dobro do tempo com funções horárias."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Gráficos Aceleração × Tempo (a × t) e Tradução Entre Gráficos"
                },
                {
                    "type": "paragraph",
                    "content": "Para fechar a trinca, temos o gráfico da Aceleração em função do Tempo (a × t). No MU, a aceleração é zero, então o gráfico fica grudado no eixo horizontal. No MUV, como a aceleração é constante e diferente de zero, o gráfico é uma reta horizontal acima ou abaixo do eixo do tempo. E qual é a mágica da área no gráfico a × t? Se no gráfico v × t a área dá ΔS, no gráfico a × t a área sob a curva entre dois instantes dá a VARIAÇÃO DA VELOCIDADE (Δv)! Lembre-se: variação de velocidade (v - v₀), e não a velocidade final direta — se o móvel não partiu do repouso, você soma Δv à velocidade inicial v₀."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: O Mapa das Traduções Gráficas",
                    "content": "O ENEM adora dar o gráfico S × t e pedir qual das 5 alternativas mostra o gráfico v × t correspondente (ou vice-versa). Use este tradutor instantâneo:\n• Reta horizontal no S × t (parado) → Reta em v = 0 no v × t.\n• Reta inclinada subindo no S × t (MU progressivo) → Reta horizontal acima de zero no v × t (e a = 0 no a × t).\n• Parábola para cima no S × t (MUV com a > 0) → Reta inclinada subindo no v × t → Reta horizontal positiva no a × t.\n• Parábola para baixo no S × t (MUV com a < 0) → Reta inclinada descendo no v × t → Reta horizontal negativa no a × t."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Área de Trapézio em Viagem Entre Estações de Metrô",
                    "content": "Enunciado: Um trem de metrô parte do repouso de uma estação, acelera uniformemente por 10 s até atingir 20 m/s, mantém essa velocidade constante por 30 s e depois freia uniformemente por 10 s até parar na estação seguinte. Qual é a distância entre as duas estações?\n\nResolução passo a passo:\n1. Desenhe mentalmente o gráfico v × t: ele sobe de 0 a 20 m/s em 10 s, fica plano em 20 m/s por 30 s e desce a 0 em 10 s. Isso forma um TRAPÉZIO perfeito!\n2. Base maior (tempo total) = 10 + 30 + 10 = 50 s.\n3. Base menor (tempo em velocidade constante) = 30 s.\n4. Altura (velocidade máxima) = 20 m/s.\n5. Área do trapézio = [(B + b) · h] / 2 = [(50 + 30) · 20] / 2 = 80 · 10 = 800 metros!"
                },
                {
                    "type": "quote",
                    "content": "Quem lê primeiro os eixos do gráfico nunca confunde um carro parado com um carro em velocidade constante; quem domina a área do trapézio resolve o MUV com geometria de 7º ano.",
                    "author": "Estratégia 800+ em Física no ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-20-leis-de-newton",
            "number": 20,
            "title": "20. Leis de Newton: Força, Massa, Peso, Atrito, Equilíbrio e Ação e Reação",
            "epigraph": {
                "text": "As três Leis de Newton explicam por que o cinto de segurança salva vidas, por que caminhar sem atrito é impossível e por que ação e reação nunca se anulam.",
                "author": "Aula Magna de Dinâmica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Força, Massa e Peso: Acabando Com a Confusão da Balança"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo à Dinâmica — a parte da Mecânica que não olha apenas para como os corpos se movem, mas investiga QUEM causa essas mudanças de movimento: as forças! Força é uma grandeza vetorial (tem intensidade em Newtons, direção e sentido) capaz de deformar um corpo ou alterar sua velocidade. E antes de irmos às três famosas Leis de Newton, precisamos corrigir um vício de linguagem do cotidiano que o ENEM adora testar: a diferença entre MASSA e PESO."
                },
                {
                    "type": "paragraph",
                    "content": "Quando você sobe na farmácia e diz 'estou pesando 70 kg', o físico sorri por dentro. Quilograma (kg) é a unidade de MASSA, uma propriedade escalar do corpo ligada à quantidade de matéria e à sua resistência em mudar de movimento (inércia). Se você viajar para a Lua, sua massa continua sendo exatamente 70 kg. Já o PESO é uma FORÇA — a força gravitacional com que o planeta puxa você para baixo! Calculamos o peso por P = m · g. Na Terra (g ≈ 10 m/s²), uma pessoa de 70 kg tem peso de 700 Newtons (N); na Lua (g ≈ 1,6 m/s²), a massa segue 70 kg, mas o peso cai para apenas 112 N!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "1ª Lei de Newton (Inércia): Cinto de Segurança, Encosto e Curvas"
                },
                {
                    "type": "paragraph",
                    "content": "A 1ª Lei de Newton, ou Princípio da Inércia, afirma que todo corpo tende a permanecer em seu estado natural de repouso ou de Movimento Retilíneo Uniforme (velocidade constante em linha reta), a menos que uma força resultante diferente de zero atue sobre ele. Quanto maior a massa de um corpo, maior a sua inércia — é muito mais difícil parar ou empurrar um caminhão carregado do que uma bicicleta."
                },
                {
                    "type": "paragraph",
                    "content": "Pense comigo em três cenas cotidianas de prova: primeiro, o ônibus freia bruscamente e você parece ser 'arremessado para frente'. Na verdade, ninguém empurrou você para frente! O ônibus parou pelos freios, e seu corpo, por inércia, apenas tentou continuar andando para frente na mesma velocidade em que estava. É o cinto de segurança que aplica a força para frear você junto com o banco! Segundo, quando o carro é batido por trás e arranca para frente, sua cabeça tende a ficar parada onde estava, jogando o pescoço para trás — função vital do encosto de cabeça! Terceiro, quando o carro faz uma curva fechada para a esquerda, você sente seu corpo ir para o lado direito porque ele tenta seguir em linha reta pela tangente da curva."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "2ª Lei de Newton e Condições de Equilíbrio"
                },
                {
                    "type": "paragraph",
                    "content": "Se a soma vetorial de todas as forças que agem sobre um corpo — chamada Força Resultante (F_R) — for ZERO, o corpo está em EQUILÍBRIO. Atenção máxima: equilíbrio não significa apenas estar parado (equilíbrio estático)! Um avião voando em linha reta com velocidade constante de 850 km/h também tem força resultante nula (equilíbrio dinâmico), pois o empuxo dos motores iguala o arrasto do ar e a sustentação iguala o peso!"
                },
                {
                    "type": "paragraph",
                    "content": "Quando a força resultante NÃO é zero, entra em cena a 2ª Lei de Newton (Princípio Fundamental da Dinâmica): F_R = m · a. A força resultante produz uma aceleração de mesma direção e mesmo sentido, proporcional à força e inversamente proporcional à massa. Se você empurra um bloco de 4 kg para a direita com 30 N enquanto o atrito puxa para a esquerda com 10 N, a força resultante é 30 - 10 = 20 N, gerando aceleração a = 20 / 4 = 5 m/s² para a direita."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "3ª Lei de Newton (Ação e Reação): Por Que Nunca Se Cancelam?"
                },
                {
                    "type": "paragraph",
                    "content": "A 3ª Lei de Newton diz que forças nunca existem sozinhas: se o corpo A aplica uma força sobre o corpo B (ação), o corpo B aplica instantaneamente sobre o corpo A uma força de mesmo módulo, mesma direção e sentido oposto (reação). Quando o foguete empurra os gases quentes para baixo, os gases empurram o foguete para cima; quando você empurra a água para trás na natação, a água empurra você para frente; quando a Terra puxa uma maçã para baixo (peso), a maçã puxa a Terra para cima com exatamente a mesma força!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Ação e Reação Nunca Se Anulam — e Normal ≠ Reação do Peso!",
                    "content": "Duas verdades absolutas para gabaritar Dinâmica:\n1. Por que ação e reação NUNCA se equilibram nem se cancelam? Porque elas atuam em CORPOS DIFERENTES! Para duas forças se anularem, ambas precisam agir no mesmo corpo. Como a ação age no corpo B e a reação age no corpo A, cada uma produz efeito em seu próprio corpo!\n2. Um livro parado sobre a mesa sofre Peso para baixo (feito pela Terra no livro) e Normal para cima (feita pela mesa no livro). Elas têm mesmo módulo e sentidos opostos, MAS NÃO SÃO PAR AÇÃO E REAÇÃO, pois ambas agem no mesmo corpo (o livro)! A reação do Peso está no centro da Terra; a reação da Normal é a força com que o livro empurra a mesa para baixo."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Força Normal e Atrito Estático vs. Atrito Dinâmico"
                },
                {
                    "type": "paragraph",
                    "content": "A Força Normal (N) é a força de contato que uma superfície faz sobre o corpo, sempre PERPENDICULAR (90°) à superfície. Em um chão plano horizontal sem forças verticais extras, N = P = m · g; em uma ladeira inclinada ou quando você aperta o bloco para baixo, a Normal muda! Já a Força de Atrito (f_at) aparece paralela à superfície, opondo-se à tendência de escorregamento entre duas superfícies."
                },
                {
                    "type": "paragraph",
                    "content": "Veja que distinção fantástica entre os dois tipos de atrito: enquanto o bloco NÃO escorrega (como um armário pesado que você empurra devagarinho e não sai do lugar, ou um pneu rolando sem derrapar), age o atrito estático. Ele é 'inteligente': vale exatamente o mesmo que você empurrar, até chegar ao seu limite máximo f_at,est,máx = μ_e · N. Se você vencer esse limite, o bloco começa a escorregar e passa a agir o atrito dinâmico (ou cinético), de valor fixo f_at,cin = μ_c · N. Na natureza, μ_e é sempre um pouco maior que μ_c — por isso é mais difícil tirar uma geladeira do lugar do que mantê-la deslizando, e é também por isso que os freios ABS impedem a roda de travar: manter o pneu girando sem derrapar garante o atrito estático máximo, que freia o carro em menor distância e mantém o volante controlável!"
                },
                {
                    "type": "paragraph",
                    "content": "E ao caminhar? Quando você dá um passo para frente, seu pé empurra o chão para TRÁS; pela 3ª Lei, o atrito estático do chão empurra seu pé para FRENTE! Sem atrito, como no gelo liso, você patina no mesmo lugar e não sai do canto."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Armário Pesado, Atrito Estático Máximo e Aceleração",
                    "content": "Enunciado: Uma caixa de massa 20 kg repousa sobre um piso horizontal (g = 10 m/s²). Os coeficientes de atrito entre a caixa e o piso são μ_e = 0,5 e μ_c = 0,4. Analise o que acontece se aplicarmos horizontalmente: (a) uma força de 80 N; e (b) uma força de 120 N.\n\nResolução passo a passo:\n1. Como o piso é horizontal sem outras forças verticais: N = P = m · g = 20 · 10 = 200 N.\n2. Calcule o limite máximo do atrito estático: f_at,est,máx = μ_e · N = 0,5 · 200 = 100 N.\n3. Caso (a) — Força aplicada de 80 N: como 80 N é menor que o limite de 100 N, a caixa NÃO se move! O atrito estático ajusta-se e vale exatamente 80 N (NUNCA responda 100 N aqui!).\n4. Caso (b) — Força aplicada de 120 N: como 120 N supera 100 N, a caixa entra em movimento! Agora vale o atrito cinético: f_at,cin = μ_c · N = 0,4 · 200 = 80 N.\n5. Pela 2ª Lei de Newton: F_R = 120 - 80 = 40 N → a = F_R / m = 40 / 20 = 2 m/s²!"
                },
                {
                    "type": "quote",
                    "content": "Sem a 1ª Lei não existiria o cinto de segurança; sem a 3ª Lei e o atrito, ninguém daria um único passo para frente.",
                    "author": "Aula Magna de Leis de Newton"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-21-trabalho-energia",
            "number": 21,
            "title": "21. Trabalho e Energia: Conservação da Energia Mecânica e Potência",
            "epigraph": {
                "text": "Na natureza, energia não nasce do nada nem desaparece no vazio: ela apenas muda de fantasia — de altura para velocidade, de mola comprimida para movimento, ou de atrito para calor.",
                "author": "Princípio da Conservação da Energia"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Trabalho Mecânico: Quando Fazer Força NÃO Realiza Trabalho"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao capítulo final deste módulo, onde tudo o que vimos em Cinemática e Dinâmica se une na ideia mais elegante da Física: a Energia! Começamos pelo Trabalho Mecânico (representado por W ou τ, medido em Joules, J). Na Física, trabalho não é cansaço muscular — é transferência de energia através de uma força atuando ao longo de um deslocamento. Para uma força constante F formando um ângulo θ com o deslocamento d, escrevemos: W = F · d · cosθ."
                },
                {
                    "type": "paragraph",
                    "content": "Olhe atentamente para esse cosθ porque ele explica três situações famosas de prova. Se a força está a favor do deslocamento (θ = 0°, cos 0° = +1), o trabalho é positivo ou motor (força entrega energia). Se está contra o deslocamento, como o atrito freando um carro (θ = 180°, cos 180° = -1), o trabalho é negativo ou resistente (força retira energia). E se a força é PERPENDICULAR ao movimento (θ = 90°, cos 90° = 0), o trabalho é ZERO! Exemplo clássico: um garçom caminhando em linha reta horizontal segurando uma bandeja exerce força normal vertical para cima enquanto anda para frente — o trabalho da normal e do peso nesse percurso horizontal é rigorosamente NULO! O mesmo vale para a força centrípeta em movimentos circulares."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Três Energias da Mecânica e o Teorema da Energia Cinética"
                },
                {
                    "type": "paragraph",
                    "content": "A Energia Mecânica (E_m) de um sistema é a soma de duas grandes famílias: a energia do movimento e as energias armazenadas (potenciais). A Energia Cinética depende da massa e do QUADRADO da velocidade: E_c = (m · v²) / 2. Muita atenção a esse v²! Se um motorista dobra a velocidade do carro de 40 km/h para 80 km/h, a energia cinética fica QUATRO vezes maior (2² = 4) — e, pelo Teorema da Energia Cinética (W_total = ΔE_c), o trabalho dos freios para parar o carro também quadruplica, multiplicando por 4 a distância de frenagem! Triplicar a velocidade exige 9 vezes mais distância para parar!"
                },
                {
                    "type": "paragraph",
                    "content": "Já as energias potenciais ficam guardadas prontas para virar movimento. A Energia Potencial Gravitacional nasce da altura h em relação a um nível de referência: E_pg = m · g · h (é assim que funciona uma usina hidrelétrica, armazenando água no alto da barragem). E a Energia Potencial Elástica fica guardada quando esticamos ou comprimimos uma mola, um elástico ou uma cama elástica de constante elástica k em uma deformação x: E_pe = (k · x²) / 2."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Conservação da Energia Mecânica e Dissipação por Atrito"
                },
                {
                    "type": "paragraph",
                    "content": "Chegamos ao coração do capítulo: em um sistema conservativo — isto é, livre de atrito e resistência do ar — a Energia Mecânica Total permanece constante o tempo todo: E_m,antes = E_m,depois! Pense em um carrinho de montanha-russa ou em um pêndulo oscilando sem atrito. No ponto mais alto, se o carrinho parte do repouso, toda a energia está na forma potencial gravitacional (m · g · h). Ao descer, a altura cai e a velocidade dispara: a energia potencial se transforma integralmente em energia cinética! Na base do trilho (h = 0), temos (m · g · H) = (m · v²) / 2. Perceba um detalhe lindo: a massa m corta dos dois lados! Logo v = √(2 · g · H) — sem atrito, uma pena e uma bola de boliche descem o escorregador chegando lá embaixo com exatamente a mesma velocidade!"
                },
                {
                    "type": "paragraph",
                    "content": "Mas e quando existe atrito ou resistência do ar no mundo real (sistemas dissipativos)? A energia total do universo continua conservada, mas parte da energia mecânica vira calor e som! Nesse caso, a energia mecânica final é menor que a inicial, e a diferença exata é a energia dissipada pelo trabalho do atrito: E_m,inicial = E_m,final + |W_atrito| (ou simplesmente E_dissipada = E_m,antes - E_m,depois). Se o carrinho solto a 20 m de altura só consegue subir até 15 m no morro seguinte, 25% da energia mecânica foi dissipada em calor no trilho!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Montanha-Russa com Atrito",
                    "content": "Enunciado: Um carrinho de montanha-russa de 400 kg parte do repouso do topo de uma rampa de 25 m de altura e atinge a base (h = 0) com velocidade de 20 m/s. Adote g = 10 m/s². Determine quanta energia mecânica foi dissipada pelo atrito durante a descida.\n\nResolução passo a passo:\n1. Energia mecânica inicial no topo (v = 0, logo só E_pg): E_m,i = m · g · h = 400 · 10 · 25 = 100.000 J (100 kJ).\n2. Energia mecânica final na base (h = 0, logo só E_c): E_m,f = (m · v²) / 2 = (400 · 20²) / 2 = (400 · 400) / 2 = 80.000 J (80 kJ).\n3. Energia dissipada pelo atrito: E_diss = 100.000 - 80.000 = 20.000 J (ou seja, 20% da energia virou calor nos trilhos e no ar)!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Potência Mecânica e Rendimento: Rapidez e Eficiência"
                },
                {
                    "type": "paragraph",
                    "content": "Imagine dois guindastes idênticos erguendo o mesmo contêiner de 2.000 kg até 10 metros de altura. Ambos realizam exatamente o mesmo trabalho contra a gravidade (W = m · g · h = 200.000 J). Porém, o guindaste A faz isso em 10 segundos e o guindaste B leva 50 segundos. Qual é mais potente? O A! Potência Mecânica (P) é o trabalho realizado dividido pelo tempo gasto: P = W / Δt (em Watts, W = J/s). E quando um veículo se move com velocidade constante v sob uma força motora F, vale também o atalho P = F · v."
                },
                {
                    "type": "paragraph",
                    "content": "Por fim, nenhuma máquina real aproveita 100% da energia que consome — sempre há perdas por atrito ou aquecimento. Medimos essa eficiência pelo Rendimento (η): η = P_útil / P_total = E_útil / E_total. Como a potência útil é sempre menor que a total recebida, o rendimento fica entre 0 e 1 (ou entre 0% e 100%). Se uma bomba hidráulica recebe 2.000 W da tomada e tem rendimento de 75% (0,75), a potência útil que realmente ergue a água vale P_útil = 0,75 · 2.000 = 1.500 W; os outros 500 W estão aquecendo o motor!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Potência e Rendimento de uma Bomba d'Água",
                    "content": "Enunciado: Uma bomba elétrica deve elevar 600 litros (600 kg) de água por minuto até uma caixa d'água situada a 12 m de altura (g = 10 m/s²). Sabendo que o rendimento do motor é de 80%, qual deve ser a potência elétrica total consumida pela bomba?\n\nResolução passo a passo:\n1. Trabalho útil em 1 minuto (Δt = 60 s): W_útil = m · g · h = 600 · 10 · 12 = 72.000 J.\n2. Potência útil entregue à água: P_útil = W_útil / Δt = 72.000 / 60 = 1.200 W.\n3. Pelo rendimento η = P_útil / P_total → 0,80 = 1.200 / P_total → P_total = 1.200 / 0,80 = 1.500 W!\nResposta: A bomba consome 1.500 W da rede elétrica para entregar 1.200 W erguendo a água."
                },
                {
                    "type": "quote",
                    "content": "Quando você enxerga um problema de mecânica através da energia e do rendimento, deixa de decorar dezenas de casos isolados e passa a ler a contabilidade universal da natureza.",
                    "author": "Encerramento do Módulo de Eletricidade e Mecânica"
                }
            ],
            "quiz": []
        }
    ]
