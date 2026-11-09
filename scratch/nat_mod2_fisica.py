# -*- coding: utf-8 -*-
"""Eixo 2: Física Completa ENEM (Capítulos 10 a 20)"""

def get_chapters():
    return [
        {
            "id": "nat-fis-10-mecanica-cinematica",
            "number": 10,
            "title": "10. Mecânica e Cinemática: Movimento, Velocidade e Gráficos",
            "epigraph": {
                "text": "O movimento é sempre relativo ao referencial adotado. No ENEM, a interpretação de gráficos s x t e v x t resolve metade das questões de cinemática sem necessidade de cálculos extensos.",
                "author": "Guia de Cinemática no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Movimento Retilíneo Uniforme (MRU) e Uniformemente Variado (MUV)"
                },
                {
                    "type": "paragraph",
                    "content": "• MRU (Velocidade constante, aceleração nula): S = S0 + v * t. O gráfico da posição em função do tempo é uma RETA cuja inclinação é numericamente igual à velocidade escalar.\n• MUV (Aceleração constante diferente de zero):\n1. Função Horária da Velocidade: v = v0 + a * t (reta no gráfico v x t; a inclinação da reta é a aceleração).\n2. Função Horária da Posição: S = S0 + v0 * t + (a * t²) / 2 (parábola no gráfico s x t).\n3. Equação de Torricelli (quando o tempo NÃO foi informado nem pedido!): v² = v0² + 2 * a * delta_s."
                },
                {
                    "type": "callout",
                    "title": "O Atalho de Ouro dos Gráficos de Cinemática no ENEM",
                    "content": "• No gráfico Velocidade versus Tempo (v x t): A ÁREA sob a curva entre dois instantes de tempo é NUMERICAMENTE IGUAL AO DESLOCAMENTO ESCALAR (delta_s)!\nEm vez de aplicar fórmulas complexas de aceleração em gráficos com formato de trapézio ou triângulo, basta calcular a área geométrica da figura!"
                }
            ],
            "quiz": [
                {
                    "question": "Um automóvel trafega a uma velocidade constante de 72 km/h quando o motorista avista um obstáculo e aciona os freios, parando completamente o veículo em 4 segundos com desaceleração constante. Qual foi a distância percorrida pelo carro durante a frenagem?",
                    "options": [
                        "40 metros",
                        "80 metros",
                        "20 metros",
                        "144 metros"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Primeiro, converta 72 km/h para m/s dividindo por 3,6: v0 = 72 / 3,6 = 20 m/s. Pelo método da área do gráfico v x t (triângulo retângulo com base = 4 s e altura = 20 m/s): delta_s = (base * altura) / 2 = (4 * 20) / 2 = 40 metros."
                }
            ]
        },
        {
            "id": "nat-fis-11-leis-de-newton-dinamica",
            "number": 11,
            "title": "11. Dinâmica e Leis de Newton: Forças, Inércia, Atrito e Equilíbrio",
            "epigraph": {
                "text": "Força é uma interação entre dois corpos capaz de alterar a velocidade ou deformar a matéria. As Três Leis de Newton governam da caminhada humana ao lançamento de satélites.",
                "author": "Mecânica Newtoniana no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Três Leis Fundamentais de Newton"
                },
                {
                    "type": "paragraph",
                    "content": "1. 1ª Lei (Princípio da Inércia): Todo corpo tende a permanecer em repouso ou em movimento retilíneo uniforme a menos que seja obrigado a mudar seu estado por forças externas aplicadas sobre ele. A massa de um corpo é a medida quantitativa de sua inércia (cinto de segurança e encosto de cabeça salvam vidas pela 1ª Lei).\n2. 2ª Lei (Princípio Fundamental da Dinâmica): A resultante das forças que atuam sobre uma partícula de massa m produz uma aceleração na mesma direção e sentido: F_res = m * a (unidade no SI: Newtons = kg * m/s²).\n3. 3ª Lei (Princípio da Ação e Reação): Toda ação de um corpo A sobre um corpo B gera uma reação de B sobre A de MESMA intensidade, MESMA direção e SENTIDOS OPOSTOS. Atenção vital: Forças de ação e reação NUNCA se equilibram nem se anulam, pois ATUAM EM CORPOS DIFERENTES!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Forças de Atrito e Condições de Equilíbrio"
                },
                {
                    "type": "paragraph",
                    "content": "• Força Peso: P = m * g (direcionada sempre para o centro gravitacional da Terra; massa é invariável, peso varia com a gravidade local).\n• Força de Atrito Estático e Cinético: Fat = mu * N (onde mu é o coeficiente de atrito e N é a força normal). O atrito estático máximo é SEMPRE maior do que o atrito cinético (é mais difícil iniciar o movimento de uma caixa pesada do que mantê-la deslizando).\n• O atrito é propulsor: quando você anda ou quando um carro traciona as rodas, o chão EMPURRA o pé ou o pneu para a FRENTE por atrito estático!"
                }
            ],
            "quiz": [
                {
                    "question": "Um cavalo puxa uma carroça aplicando sobre ela uma força de tração para a frente. Pela Terceira Lei de Newton, a carroça exerce sobre o cavalo uma força de mesma intensidade, mesma direção e sentido para trás. Por que, afinal, o cavalo consegue acelerar o conjunto para a frente?",
                    "options": [
                        "Porque a força horizontal de atrito que o chão exerce sobre os cascos do cavalo para a frente é maior do que as forças resistivas que atuam sobre a carroça.",
                        "Porque a força do cavalo sobre a carroça é ligeiramente maior do que a reação da carroça sobre o cavalo.",
                        "Porque as forças de ação e reação se anulam no ponto de engate liberando energia cinética.",
                        "Porque a inércia do cavalo é menor do que a inércia da carroça acelerando o sistema."
                    ],
                    "correctAnswer": 0,
                    "explanation": "Ação e reação têm módulos rigorosamente iguais, mas atuam em corpos diferentes. O cavalo acelera porque empurra o solo para trás com suas patas, e o solo empurra o cavalo para a FRENTE (força externa de atrito). Se essa força externa para a frente for maior que o atrito das rodas da carroça, o sistema todo acelera."
                }
            ]
        },
        {
            "id": "nat-fis-12-trabalho-energia-potencia",
            "number": 12,
            "title": "12. Trabalho, Energia e Potência: O Princípio Universal da Conservação",
            "epigraph": {
                "text": "A energia não pode ser criada nem destruída, apenas transformada de uma forma em outra. O ENEM foca nas transformações entre energia mecânica, elétrica, térmica e química.",
                "author": "Conservação da Energia no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Tipos de Energia Mecânica e Trabalho"
                },
                {
                    "type": "paragraph",
                    "content": "• Trabalho de uma Força Constante (W ou Tau): W = F * d * cos(theta). Medido em Joules (J = N * m).\n• Energia Cinética (associada ao movimento): Ec = (m * v²) / 2.\n• Energia Potencial Gravitacional (associada à altura em um campo gravitacional): Epg = m * g * h.\n• Energia Potencial Elástica (associada a molas e elásticos deformados): Epe = (k * x²) / 2 (onde k é a constante elástica em N/m e x é a deformação em metros).\n• Energia Mecânica Total: Em = Ec + Ep."
                },
                {
                    "type": "callout",
                    "title": "Sistemas Conservativos vs Dissipativos",
                    "content": "• Sistema Conservativo (sem atrito nem resistência do ar): A energia mecânica total se conserva intacta em qualquer ponto da trajetória: Em_inicial = Em_final (ex: montanha-russa sem atrito; no topo toda energia é potencial, no ponto mais baixo toda energia é cinética: m*g*h = m*v²/2 => v = raiz(2*g*h)).\n• Sistema Dissipativo: Há atrito ou resistência do ar. Parte da energia mecânica é degradada em calor e som: W_atrito = Em_final - Em_inicial."
                }
            ],
            "quiz": [
                {
                    "question": "Um carrinho de montanha-russa de massa 400 kg parte do repouso do topo de uma pista a 20 metros de altura em relação ao solo. Desprezando todas as forças dissipativas e adotando g = 10 m/s², qual é a velocidade do carrinho ao atingir o ponto mais baixo da pista?",
                    "options": [
                        "20 m/s (72 km/h)",
                        "15 m/s (54 km/h)",
                        "25 m/s (90 km/h)",
                        "10 m/s (36 km/h)"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Por conservação da energia mecânica: Em_topo = Em_base => m * g * h = (m * v²) / 2 => v = raiz(2 * g * h) = raiz(2 * 10 * 20) = raiz(400) = 20 m/s."
                }
            ]
        },
        {
            "id": "nat-fis-13-hidrostatica-pressao-empuxo",
            "number": 13,
            "title": "13. Hidrostática: Pressão, Princípio de Pascal e Empuxo de Arquimedes",
            "epigraph": {
                "text": "A pressão em um líquido aumenta linearmente com a profundidade (Stevin). Todo corpo submerso recebe um empuxo vertical para cima igual ao peso do líquido deslocado (Arquimedes).",
                "author": "Física de Fluidos no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Pressão e o Teorema de Stevin"
                },
                {
                    "type": "paragraph",
                    "content": "• Pressão: P = Força / Área (P = F / A, unidade no SI: Pascal = N/m²; 1 atm ~= 10^5 Pa ~= 10 m de coluna de água).\n• Teorema Fundamental da Hidrostática (Stevin): delta_P = d * g * h (onde d é a densidade do fluido, g é a gravidade e h é a profundidade). Pontos situados na mesma profundidade em um mesmo líquido em equilíbrio possuem exatamente a MESMA pressão hidrostática!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Princípio de Pascal e Prensa Hidráulica"
                },
                {
                    "type": "paragraph",
                    "content": "O acréscimo de pressão aplicado a um ponto de um líquido incompressível em equilíbrio transmite-se integralmente a todos os pontos do líquido:\nF1 / A1 = F2 / A2 (Princípio da Prensa Hidráulica, elevador de oficina mecânica e freios hidráulicos de automóveis: aplicando uma força pequena em um êmbolo de área pequena, gera-se uma força gigantesca no êmbolo de área grande!)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Princípio de Arquimedes e Força de Empuxo"
                },
                {
                    "type": "paragraph",
                    "content": "Todo corpo imerso em um fluido sofre a ação de uma força vertical dirigida para cima chamada Empuxo (E):\nE = d_liquido * V_submerso * g.\n• Se Peso > Empuxo (densidade do corpo > densidade do fluido): o corpo AFUNDA.\n• Se Peso = Empuxo (densidade do corpo < densidade do fluido): o corpo FLUTUA em equilíbrio na superfície com apenas uma fração do seu volume submerso: V_submerso / V_total = d_corpo / d_fluido (como um iceberg ou navio cargueiro de aço oco)!"
                }
            ],
            "quiz": [
                {
                    "question": "Um iceberg de gelo puro de densidade 0,9 g/cm³ flutua na água do mar de densidade 1,0 g/cm³. Qual é a porcentagem do volume total do iceberg que permanece submersa abaixo da linha d'água?",
                    "options": [
                        "90%",
                        "10%",
                        "80%",
                        "95%"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Na flutuação em equilíbrio, Peso = Empuxo: m_corpo * g = d_fluido * V_submerso * g => d_corpo * V_total = d_fluido * V_submerso => V_submerso / V_total = d_corpo / d_fluido = 0,9 / 1,0 = 0,90 = 90%."
                }
            ]
        },
        {
            "id": "nat-fis-14-termologia-calorimetria",
            "number": 14,
            "title": "14. Termologia e Calorimetria: Calor Sensível, Latente e Propagação",
            "epigraph": {
                "text": "Temperatura é a medida do grau de agitação térmica molecular. Calor é energia térmica em trânsito motivada espontaneamente pela diferença de temperatura.",
                "author": "Termofísica no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Calor Sensível vs Calor Latente"
                },
                {
                    "type": "paragraph",
                    "content": "• Calor Sensível (Provoca alteração de temperatura sem mudança de estado físico):\nQ = m * c * delta_theta ('Que Macete!'). O calor específico 'c' mede a inércia térmica da substância (a água tem calor específico elevadíssimo de 1 cal/g°C, por isso demora a esquentar e a esfriar, atuando como moderador climático global).\n• Calor Latente (Provoca mudança de estado físico à temperatura rigorosamente constante):\nQ = m * L ('Que Moleza!'). Durante a fusão ou ebulição de uma substância pura, o calor recebido rompe ligações intermoleculares sem alterar a energia cinética média (temperatura permanece fixa)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Processos de Propagação do Calor"
                },
                {
                    "type": "paragraph",
                    "content": "1. Condução: Propagação de molécula a molécula por contato direto em sólidos (metais são ótimos condutores térmicos; madeira, ar e lã são isolantes).\n2. Convecção: Propagação pelo movimento real de massas fluidas (líquidos e gases) impulsionadas por diferenças de densidade: ar quente sobe (menos denso), ar frio desce (mais denso). Por isso o ar-condicionado é instalado no alto e o aquecedor no chão; explica as brisas marítimas diurna e noturna.\n3. Irradiação (Radiação Térmica): Propagação por ondas eletromagnéticas (infravermelho). O ÚNICO processo que ocorre no VÁCUO (é como o calor do Sol chega à Terra e como funciona a garrafa térmica com paredes espelhadas)."
                }
            ],
            "quiz": [
                {
                    "question": "Durante o dia na praia, sopra uma brisa do mar para o continente (brisa marítima). À noite, a direção do vento se inverte, soprando da terra para o mar (brisa terrestre). Esse fenômeno térmico periódico decorre diretamente de:",
                    "options": [
                        "A água ter maior calor específico que a areia, aquecendo e resfriando mais lentamente e gerando correntes de convecção.",
                        "A areia emitir mais radiação no vácuo do que a superfície oceânica.",
                        "A condução térmica no ar ser bloqueada pela salinidade marítima.",
                        "A força de Coriolis acelerar o movimento do vento durante o período noturno."
                    ],
                    "correctAnswer": 0,
                    "explanation": "A água tem calor específico elevado (c = 1 cal/g°C) e a areia tem calor específico baixo (~0,2 cal/g°C). Durante o dia, a terra esquenta rápido, o ar sobre ela sobe e o ar mais frio do mar ocupa o lugar (brisa marítima). À noite, a terra resfria rápido e o mar permanece morno, invertendo o fluxo de convecção (brisa terrestre)."
                }
            ]
        },
        {
            "id": "nat-fis-15-termodinamica-maquinas",
            "number": 15,
            "title": "15. Termodinâmica e Máquinas Térmicas: 1ª e 2ª Leis e Ciclo de Carnot",
            "epigraph": {
                "text": "É impossível construir uma máquina térmica que, operando em ciclos, converta integralmente todo o calor recebido de uma fonte em trabalho útil. O rendimento de 100% é proibido pela 2ª Lei.",
                "author": "Enunciado de Kelvin-Planck da Termodinâmica"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A 1ª Lei da Termodinâmica: Balanço de Energia"
                },
                {
                    "type": "paragraph",
                    "content": "A 1ª Lei é a conservação de energia aplicada a sistemas gasosos: delta_U = Q - W.\n• delta_U (Variação de Energia Interna): Depende EXCLUSIVAMENTE da temperatura do gás. Se a temperatura sobe, delta_U > 0; se é isotérmica, delta_U = 0.\n• Q: Calor trocado. Se o gás recebe calor, Q > 0; se cede calor, Q < 0; se a transformação for adiabática (muito rápida ou isolada), Q = 0.\n• W: Trabalho realizado pelo gás: W = P * delta_V. Se o gás expande (volume aumenta), W > 0; se o gás é comprimido, W < 0."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Máquinas Térmicas, Refrigeradores e o Ciclo de Carnot"
                },
                {
                    "type": "paragraph",
                    "content": "Uma máquina térmica opera entre uma Fonte Quente (T_quente) e uma Fonte Fria (T_fria):\n• Conservação: Q_quente = Trabalho (W) + Q_fria\n• Rendimento Real (eta): eta = W / Q_quente = (Q_quente - Q_fria) / Q_quente = 1 - (Q_fria / Q_quente).\n• Rendimento Máximo Teórico de Carnot (o limite absoluto da natureza):\neta_Carnot = 1 - (T_fria / T_quente) [As temperaturas DEVEM estar OBRIGATORIAMENTE em KELVIN: K = °C + 273]!"
                }
            ],
            "quiz": [
                {
                    "question": "Uma máquina térmica de Carnot ideal opera entre uma fonte quente a 500 K e uma fonte fria a 300 K. Se em cada ciclo ela absorve 1.000 Joules de calor da fonte quente, qual é o trabalho útil realizado por essa máquina?",
                    "options": [
                        "400 Joules",
                        "600 Joules",
                        "200 Joules",
                        "500 Joules"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Rendimento de Carnot: eta = 1 - (T_fria / T_quente) = 1 - (300 / 500) = 1 - 0,60 = 0,40 (40%). O trabalho útil realizado é W = eta * Q_quente = 0,40 * 1.000 J = 400 Joules."
                }
            ]
        },
        {
            "id": "nat-fis-16-eletrodinamica-circuitos",
            "number": 16,
            "title": "16. Eletrodinâmica e Circuitos: Leis de Ohm, Potência e Consumo em kWh",
            "epigraph": {
                "text": "Eletrodinâmica é o conteúdo de Física mais recorrente do ENEM. Toda prova tem de 2 a 4 questões sobre resistores, chuveiro elétrico e cálculo de conta de luz.",
                "author": "Estatística Oficial do ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "As Leis de Ohm e Grandezas Elétricas"
                },
                {
                    "type": "paragraph",
                    "content": "• Corrente Elétrica (i): Taxa de fluxo de carga líquida pelo condutor: i = delta_q / delta_t (Amperes = Coulomb/segundo).\n• 1ª Lei de Ohm: U = R * i (Tensão em Volts, Resistência em Ohms, Corrente em Amperes).\n• 2ª Lei de Ohm (Resistência de um fio): R = rho * L / A (onde rho é a resistividade do material, L é o comprimento do fio e A é a área de seção transversal). Para diminuir a resistência de um fio de chuveiro ou extensão, use fios mais grossos (maior área A) e mais curtos (menor L)!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Associação de Resistores em Série vs Paralelo"
                },
                {
                    "type": "paragraph",
                    "content": "• Em Série: Os resistores estão no mesmo caminho contínuo. A CORRENTE É A MESMA em todos eles. Req = R1 + R2 + ... Se uma lâmpada queimar, todo o circuito apaga.\n• Em Paralelo (padrão de toda instalação residencial!): Os resistores compartilham os mesmos nós elétricos. A TENSÃO (VOLTAGEM U) É A MESMA em todas as tomadas e lâmpadas (127 V ou 220 V). 1/Req = 1/R1 + 1/R2. Para dois resistores: Req = (R1 * R2) / (R1 + R2). Se uma lâmpada queimar, as outras continuam funcionando normalmente!"
                },
                {
                    "type": "callout",
                    "title": "Cálculo de Consumo de Energia Elétrica em kWh (Questão Certa!)",
                    "content": "• Potência: P = U * i = R * i² = U² / R (em Watts).\n• Energia Elétrica: E = P * delta_t (se P estiver em kW e o tempo em horas h, a energia resulta diretamente em kWh!).\n• Custo na Conta de Luz = Energia (em kWh) * Preço do kWh (em R$).\nExemplo do Chuveiro: Na posição INVERNO, precisamos de MAIOR potência para esquentar a água. Como a tensão U da rede é fixa (127V ou 220V) e P = U² / R, para AUMENTAR a potência devemos DIMINUIR A RESISTÊNCIA R (fio mais curto)!"
                }
            ],
            "quiz": [
                {
                    "question": "Um chuveiro elétrico de potência 5.500 W é utilizado diariamente por uma família durante 1 hora por dia ao longo de um mês de 30 dias. Sabendo que a tarifa cobrada pela concessionária de energia é de R$ 0,80 por kWh consumido, qual é o custo mensal gerado exclusivamente pelo banho?",
                    "options": [
                        "R$ 132,00",
                        "R$ 165,00",
                        "R$ 110,00",
                        "R$ 144,00"
                    ],
                    "correctAnswer": 0,
                    "explanation": "Potência em kW = 5.500 W / 1.000 = 5,5 kW. Tempo total no mês = 1 h/dia * 30 dias = 30 horas. Energia consumida = P * t = 5,5 kW * 30 h = 165 kWh. Custo = 165 kWh * R$ 0,80 = R$ 132,00."
                }
            ]
        },
        {
            "id": "nat-fis-17-magnetismo-inducao",
            "number": 17,
            "title": "17. Magnetismo e Eletromagnetismo: Campo, Força Magnética e Indução de Faraday",
            "epigraph": {
                "text": "Corrente elétrica gera campo magnético (Oersted); variação de fluxo magnético gera corrente elétrica induzida (Faraday). É o princípio de usinas hidrelétricas, turbinas eólicas e carregadores sem fio.",
                "author": "Eletromagnetismo Unificado"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Polos Magnéticos e Experiência de Oersted"
                },
                {
                    "type": "paragraph",
                    "content": "• Ímãs: Possuem polo Norte e polo Sul. Polos de mesmo nome se repelem; polos de nomes diferentes se atraem. Princípio da Inseparabilidade dos Polos Magnéticos: se você quebrar um ímã ao meio, você obtém dois novos ímãs completos, cada um com polo Norte e Sul próprios; NUNCA existe monopolo magnético isolado na natureza!\n• Campo Magnético da Terra: O polo Norte geográfico da Terra atua como um polo Sul magnético (por isso atrai o polo Norte magnético da agulha da bússola!).\n• Experimento de Oersted: Uma corrente elétrica passando por um condutor desvia a agulha de uma bússola, provando que CARGAS ELÉTRICAS EM MOVIMENTO GERAM CAMPO MAGNÉTICO."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Força Magnética e Lei da Indução de Faraday-Lenz"
                },
                {
                    "type": "paragraph",
                    "content": "• Força Magnética sobre Carga em Movimento: Fmag = |q| * v * B * sen(theta) (Regra da Mão Direita: polegar na velocidade v, dedos indicadores no campo B, a palma da mão empurra a força Fmag para carga positiva). Se a carga estiver em repouso (v = 0) ou se mover paralelamente ao campo (theta = 0°), a força magnética é NULA!\n• Indução Eletromagnética de Faraday: fem = - delta_Phi / delta_t. Para gerar eletricidade em uma espira condutora, é OBRIGATÓRIO haver VARIAÇÃO DO FLUXO MAGNÉTICO ao longo do tempo (movimentando um ímã perto da espira ou girando a espira dentro do campo)."
                }
            ],
            "quiz": [
                {
                    "question": "Uma pessoa move um ímã em barra aproximando-o rapidamente de uma bobina condutora ligada a um galvanômetro sensível, observando uma deflexão no ponteiro que indica passagem de corrente. Quando o ímã é mantido completamente parado no interior da bobina, o ponteiro volta a marcar zero. Esse fenômeno é explicado por:",
                    "options": [
                        "A corrente induzida só existe enquanto houver variação no fluxo magnético que atravessa a bobina.",
                        "O campo magnético do ímã se anula quando ele atinge o centro geométrico da bobina.",
                        "A resistência elétrica do condutor cresce instantaneamente ao infinito em repouso.",
                        "A temperatura da bobina dissipa a carga elétrica quando cessa o movimento mecânico."
                    ],
                    "correctAnswer": 0,
                    "explanation": "Pela Lei da Indução Eletromagnética de Faraday-Lenz, a força eletromotriz induzida é diretamente proporcional à taxa de VARIAÇÃO do fluxo magnético no tempo (delta_Phi / delta_t). Quando o ímã para de se mover, o fluxo torna-se constante, delta_Phi / delta_t = 0 e a corrente cessa imediatamente."
                }
            ]
        },
        {
            "id": "nat-fis-18-ondulatoria-acustica",
            "number": 18,
            "title": "18. Ondulatória e Acústica: Fenômenos Ondulatórios e Efeito Doppler",
            "epigraph": {
                "text": "v = lambda * f. A Equação Fundamental da Ondulatória é a chave mestra. Ondas transportam energia e quantidade de movimento, NUNCA transportam matéria.",
                "author": "Ondas e Acústica no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Classificação e Equação Fundamental das Ondas"
                },
                {
                    "type": "paragraph",
                    "content": "• Mecânicas vs Eletromagnéticas: Ondas mecânicas (som, ondas no mar, terremotos) EXIGEM meio material para se propagar e NÃO se propagam no vácuo; ondas eletromagnéticas (luz visível, ondas de rádio, micro-ondas, raio X) propagam-se no vácuo com velocidade c = 3 * 10^8 m/s.\n• Equação Fundamental: v = lambda * f (onde v é a velocidade de propagação, lambda é o comprimento de onda e f é a frequência em Hertz = 1/s; Período T = 1/f).\nImportante: A FREQUÊNCIA depende exclusivamente da FONTE emissora e NUNCA muda quando a onda muda de meio (na refração)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Fenômenos Ondulatórios e Qualidades Fisiológicas do Som"
                },
                {
                    "type": "paragraph",
                    "content": "• Difração: Capacidade da onda de contornar obstáculos ou frestas de tamanho comparável ao seu comprimento de onda (é por isso que você escuta alguém falando atrás de um muro: o som contorna o muro por difração, mas a luz, com lambda minúsculo, não contorna).\n• Ressonância: Transferência máxima de energia quando um sistema é estimulado por uma frequência externa igual à sua frequência natural de vibração (ponte balançando com vento, taça de cristal quebrando com voz de tenor).\n• Qualidades do Som: ALTURA (som agudo = alta frequência; som grave = baixa frequência), INTENSIDADE (volume alto/forte = grande amplitude; som fraco = baixa amplitude) e TIMBRE (formato da onda que permite distinguir instrumentos tocando a mesma nota).\n• Efeito Doppler: Alteração aparente da frequência percebida devido ao movimento relativo entre fonte e observador (aproximação = som mais agudo/frequência maior; afastamento = som mais grave/frequência menor)."
                }
            ],
            "quiz": [
                {
                    "question": "Uma ambulância com a sirene ligada se aproxima em alta velocidade de um pedestre parado na calçada e, em seguida, ultrapassa-o e se afasta. O que o pedestre percebe em relação ao som da sirene?",
                    "options": [
                        "O som é percebido mais agudo (frequência aparente maior) durante a aproximação e mais grave (frequência menor) durante o afastamento.",
                        "A velocidade de propagação do som no ar aumenta continuamente com a aproximação.",
                        "O som é percebido mais grave durante a aproximação e mais agudo no afastamento.",
                        "A frequência do som emitido pela sirene na ambulância se altera com a velocidade do carro."
                    ],
                    "correctAnswer": 0,
                    "explanation": "Pelo Efeito Doppler acústico, quando a fonte se aproxima do observador, as frentes de onda são comprimidas, reduzindo o comprimento de onda aparente e aumentando a frequência percebida (som mais agudo). No afastamento, as frentes de onda se espaçam, diminuindo a frequência aparente (som mais grave). A frequência real da sirene e a velocidade do som no ar permanecem inalteradas."
                }
            ]
        },
        {
            "id": "nat-fis-19-optica-geometrica",
            "number": 19,
            "title": "19. Óptica Geométrica: Reflexão, Refração, Espelhos, Lentes e Olho Humano",
            "epigraph": {
                "text": "A luz viaja em linha reta em meios homogêneos e transparentes. Espelhos refletem; lentes refratam. Na miopia a imagem forma-se antes da retina (corrige-se com lentes divergentes).",
                "author": "Óptica da Visão no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Reflexão da Luz e Espelhos Esféricos"
                },
                {
                    "type": "paragraph",
                    "content": "• Espelho Plano: Imagem sempre VIRTUAL, DIREITA, de MESMO TAMANHO do objeto e simétrica em relação ao plano do espelho (enantiomorfa: inverte esquerda e direita).\n• Espelho Côncavo: Capaz de formar imagens reais e invertidas ou, quando o objeto está entre o foco e o vértice, forma imagem VIRTUAL, DIREITA e MAIOR (espelhos de maquiagem e dentista).\n• Espelho Convexo: SEMPRE forma imagem VIRTUAL, DIREITA e MENOR, proporcionando um campo de visão muito mais AMPLO (retrovisores de ônibus, garagens e esquinas de lojas)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Refração, Lei de Snell e Correção das Ametropias Oculares"
                },
                {
                    "type": "paragraph",
                    "content": "• Índice de Refração Absoluto: n = c / v (meio mais refringente tem maior n e menor velocidade da luz).\n• Lei de Snell-Descartes: n1 * sen(theta1) = n2 * sen(theta2).\n• Reflexão Total e Fibras Ópticas: Ocorre quando a luz tenta passar do meio MAIS refringente para o MENOS refringente com ângulo de incidência superior ao ângulo limite (sen L = n_menor / n_maior).\n• Defeitos da Visão no ENEM:\n- Miopia: Globo ocular muito longo; a imagem foca ANTES da retina. Dificuldade para ver de longe. Correção: LENTES DIVERGENTES (grau negativo).\n- Hipermetropia: Globo ocular curto; a imagem foca DEPOIS da retina. Dificuldade para ver de perto. Correção: LENTES CONVERGENTES (grau positivo)."
                }
            ],
            "quiz": [
                {
                    "question": "Um jovem queixa-se de dificuldade para ler o conteúdo da lousa na escola, embora consiga ler livros e telas de celular perfeitamente a curta distância. O oftalmologista diagnostica miopia. Que tipo de lente deve ser receitada para corrigir sua visão?",
                    "options": [
                        "Lente divergente, para atrasar a convergência e deslocar o foco para cima da retina.",
                        "Lente convergente, para adiantar o ponto de encontro dos raios de luz.",
                        "Lente cilíndrica bifocal, para eliminar a curvatura irregular da córnea.",
                        "Lente prismática de reflexão total, para inverter a imagem retiniana."
                    ],
                    "correctAnswer": 0,
                    "explanation": "Na miopia, o sistema óptico do olho converge em excesso, formando a imagem antes da retina. Para corrigir, usam-se lentes DIVERGENTES (côncavas), que abrem ligeiramente os feixes de luz incidentes, fazendo com que o ponto focal se desloque para trás, exatamente sobre a fóvea da retina."
                }
            ]
        },
        {
            "id": "nat-fis-20-fisica-moderna-radiacao",
            "number": 20,
            "title": "20. Física Moderna: Efeito Fotoelétrico, Dualidade Onda-Partícula e Radiações",
            "epigraph": {
                "text": "A luz possui natureza dual: comporta-se como onda eletromagnética na propagação e como feixe de partículas (fótons de energia E = h*f) na interação com a matéria. Einstein ganhou o Nobel pelo Efeito Fotoelétrico.",
                "author": "Revolução Quântica no ENEM"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Efeito Fotoelétrico e os Painéis Solares"
                },
                {
                    "type": "paragraph",
                    "content": "O Efeito Fotoelétrico consiste na ejeção de elétrons (fotoelétrons) de uma placa metálica iluminada por radiação eletromagnética:\n• Cada fóton incidente carrega um quantum de energia discreto proporcional à frequência da luz: E = h * f (onde h é a Constante de Planck).\n• Para que haja emissão de elétrons, a frequência da luz incidente deve ser superior a uma Frequência de Corte (f0) mínima característica da Função Trabalho (Phi) do metal: E_cinetica_max = h*f - Phi.\n• Aumentar o brilho (intensidade) da luz abaixo da frequência de corte NÃO ejeta nenhum elétron; aumentar o brilho acima da frequência de corte aumenta o NÚMERO de elétrons ejetados por segundo (corrente elétrica), mas não a energia individual deles!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Radioatividade e Energia Nuclear: Fissão vs Fusão"
                },
                {
                    "type": "paragraph",
                    "content": "• Emissões Nucleares: Alfa (alfa: núcleo de Hélio com 2 prótons e 2 nêutrons; baixa penetração, retida por folha de papel); Beta (beta: elétron de alta velocidade ejetado do núcleo pela desintegração de um nêutron); Gama (gama: onda eletromagnética pura de alta energia e altíssimo poder de penetração, retida apenas por grossas placas de chumbo ou concreto).\n• Fissão Nuclear: Quebra de um núcleo atômico pesado e instável (Urânio-235) bombardeado por nêutrons, liberando grande quantidade de energia, fragmentos radioativos e mais nêutrons que sustentam uma reação em cadeia (reatores nucleares de Angra dos Reis).\n• Fusão Nuclear: União de núcleos atômicos leves (Isótopos de Hidrogênio: Deutério e Trítio) sob temperaturas extremas, gerando Hélio e liberando quantidades colossais de energia limpa sem rejeitos radioativos pesados (processo que alimenta o Sol e as estrelas)!"
                }
            ],
            "quiz": [
                {
                    "question": "Os painéis solares fotovoltaicos convertem diretamente a luz solar em energia elétrica. O princípio físico fundamental que rege esse funcionamento é:",
                    "options": [
                        "O efeito fotoelétrico, no qual fótons de luz incidente com energia suficiente arrancam elétrons do material semicondutor gerando corrente.",
                        "A convecção térmica da radiação infravermelha que movimenta microturbinas no silício.",
                        "A fissão nuclear espontânea dos átomos de silício sob bombardeamento solar.",
                        "A reflexão total dos raios ultravioleta no interior de fibras condutoras."
                    ],
                    "correctAnswer": 0,
                    "explanation": "As células fotovoltaicas operam com base no efeito fotoelétrico em materiais semicondutores (como o silício dopado). Fótons da luz solar com energia superior ao gap de banda do semicondutor excitam elétrons da banda de valência para a banda de condução, estabelecendo uma corrente elétrica contínua."
                }
            ]
        }
    ]
