# -*- coding: utf-8 -*-
"""Curso de Ciências da Natureza ENEM - Módulo 8: Química (Termoquímica, Cinética, Equilíbrio, Eletroquímica e Química Ambiental - Capítulos 38 a 42)"""


def get_chapters():
    return [
        {
            "id": "nat-cap-38-termoquimica",
            "number": 38,
            "title": "38. Termoquímica: Energia nas Reações, Entalpia e Combustão",
            "epigraph": {
                "text": "Toda reação química é uma negociação energética: primeiro paga-se o preço para quebrar ligações antigas; depois recebe-se o troco ao formar ligações novas.",
                "author": "Aula Magna de Físico-Química Aplicada"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-vindas à Química do Calor: Por que o Mundo Esquenta e Esfria?"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao Módulo 8 de Ciências da Natureza. Pense comigo em duas cenas comuns do cotidiano: ao acender a boca do fogão, a chama azul aquece a água do café em segundos; já ao sair do banho ou segurar um cubo de gelo, você sente um frio imediato na pele conforme a água evapora ou o gelo derrete. Nos dois casos, há matéria se transformando e calor mudando de endereço!"
                },
                {
                    "type": "paragraph",
                    "content": "A Termoquímica estuda exatamente as trocas de energia térmica nas reações químicas e mudanças de estado físico. No ENEM, esse tema aparece todo ano ligado a combustíveis, alimentos, bolsas térmicas e gráficos. Para nunca errar, pergunte sempre quem é o sistema (a reação) e quem é a vizinhança (sua mão, o copo, o ambiente)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Processos Endotérmicos e Exotérmicos no Cotidiano"
                },
                {
                    "type": "paragraph",
                    "content": "No processo exotérmico ('exo' = para fora), o sistema libera calor para o ambiente. Como perdeu energia, sua entalpia final diminui: variação de entalpia negativa (ΔH < 0), e ao encostar a mão você sente quente! Exemplos clássicos: queima do gás de cozinha, solidificação da água no congelador, respiração celular e bolsas térmicas quentes usadas em fisioterapia (dissolução exotérmica de cloreto de cálcio ou cristalização do acetato de sódio)."
                },
                {
                    "type": "paragraph",
                    "content": "No processo endotérmico ('endo' = para dentro), o sistema absorve calor do ambiente. Sua entalpia final fica maior que a inicial: ΔH > 0. Como ele rouba calor da vizinhança, a sensação ao toque é de frio! Por isso, uma bolsa térmica fria instantânea (nitrato de amônio + água) gela na hora; e por isso gelo derretendo, suor evaporando da pele e fotossíntese (absorvendo luz solar) são processos endotérmicos."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Leitura de Gráficos de Entalpia e Equações Termoquímicas"
                },
                {
                    "type": "paragraph",
                    "content": "Nos gráficos de entalpia (H), lemos dois patamares: reagentes (H_reagentes) e produtos (H_produtos), com a fórmula ΔH = H_produtos - H_reagentes. Produtos abaixo dos reagentes indicam seta para baixo, perda de energia e processo exotérmico (ΔH < 0). Produtos acima dos reagentes indicam seta para cima, ganho de energia e processo endotérmico (ΔH > 0). Na equação termoquímica, estado físico importa muito: formar 1 mol de H₂O(l) libera 286 kJ, enquanto formar H₂O(g) libera 242 kJ, pois parte da energia mantém o vapor. Além disso, dobrar a equação dobra o ΔH, e inverter a reação inverte o sinal de ΔH."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Três Caminhos para Calcular ΔH na Prova"
                },
                {
                    "type": "paragraph",
                    "content": "Primeiro método — Entalpia de Formação (ΔH°_f): a banca fornece a entalpia padrão de formação das substâncias (lembrando que substâncias simples estáveis no estado padrão, como O₂(g), N₂(g), H₂(g) e C(grafite), têm ΔH°_f = ZERO!). Aplicamos ΔH = Σ ΔH°_f(produtos) - Σ ΔH°_f(reagentes), multiplicando cada valor pelo seu coeficiente estequiométrico."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Entalpia de Formação na Combustão do Etanol",
                    "content": "Enunciado: Calcule o ΔH da combustão de 1 mol de etanol líquido: C₂H₅OH(l) + 3 O₂(g) → 2 CO₂(g) + 3 H₂O(l), dados ΔH°_f(C₂H₅OH(l)) = -278 kJ/mol, ΔH°_f(CO₂(g)) = -394 kJ/mol e ΔH°_f(H₂O(l)) = -286 kJ/mol.\n\nResolução passo a passo:\n1. Substância simples O₂(g) tem ΔH°_f = 0.\n2. Produtos: 2 × (-394) + 3 × (-286) = -788 - 858 = -1.646 kJ.\n3. Reagentes: 1 × (-278) + 3 × 0 = -278 kJ.\n4. ΔH = -1.646 - (-278) = -1.368 kJ/mol (reação fortemente exotérmica)."
                },
                {
                    "type": "paragraph",
                    "content": "Segundo método — Energia de Ligação: cuidado com a inversão de sinal! Quebrar ligações nos reagentes consome energia (endotérmico, +); formar novas ligações nos produtos libera energia (exotérmico, -). Logo: ΔH = Σ E_quebradas(reagentes) - Σ E_formadas(produtos)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Energia de Ligação na Síntese do HCl",
                    "content": "Enunciado: Em H₂(g) + Cl₂(g) → 2 HCl(g), calcule o ΔH usando as energias de ligação: H–H = 436 kJ/mol, Cl–Cl = 242 kJ/mol e H–Cl = 431 kJ/mol.\n\nResolução passo a passo:\n1. Quebradas nos reagentes (+): 436 + 242 = +678 kJ.\n2. Formadas nos produtos (-): 2 × 431 = 862 kJ liberados (-862 kJ).\n3. Saldo energético: ΔH = +678 - 862 = -184 kJ para 2 mols de HCl (-92 kJ/mol de HCl)."
                },
                {
                    "type": "paragraph",
                    "content": "Terceiro método — Lei de Hess: a variação de entalpia depende apenas dos estados inicial e final, não do caminho intermediário. Funciona como um quebra-cabeça algébrico: manipulamos equações auxiliares (invertendo sinais ou multiplicando coeficientes) até que sua soma gere exatamente a equação-alvo."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 3: Lei de Hess Passo a Passo",
                    "content": "Enunciado: Calcule o ΔH de C(grafite) + 1/2 O₂(g) → CO(g), sabendo que:\n(I) C(grafite) + O₂(g) → CO₂(g)   ΔH₁ = -394 kJ\n(II) CO(g) + 1/2 O₂(g) → CO₂(g)   ΔH₂ = -283 kJ\n\nResolução passo a passo:\n1. Mantemos (I) intacta para ter C(grafite) na esquerda (ΔH₁ = -394 kJ).\n2. Invertemos (II) para jogar CO(g) para a direita, trocando o sinal: CO₂ → CO + 1/2 O₂ (ΔH₂' = +283 kJ).\n3. Somando (I) + (II'), cancelamos CO₂ e 1/2 O₂ e obtemos C + 1/2 O₂ → CO.\n4. ΔH = -394 + 283 = -111 kJ/mol!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Poder Calorífico: Etanol, Gasolina e Hidrogênio na Balança"
                },
                {
                    "type": "paragraph",
                    "content": "No ENEM, poder calorífico mede a energia liberada por massa de combustível (kJ/g ou kcal/g). O etanol (C₂H₅OH, 46 g/mol) libera 1.368 kJ/mol, dando ~29,7 kJ/g. A gasolina (octano, C₈H₁₈, 114 g/mol) libera ~5.470 kJ/mol, resultando em ~48 kJ/g — por isso rende mais km/litro, embora seja fóssil. Já o gás hidrogênio (H₂, apenas 2 g/mol) libera 286 kJ/mol formando água líquida, atingindo impressionantes 143 kJ/g! Além de entregar quase três vezes mais energia por grama que a gasolina, sua queima gera apenas água (H₂O), sem emitir CO₂."
                },
                {
                    "type": "quote",
                    "content": "Em Termoquímica, quem olha o sinal vê o fluxo: ΔH negativo aquece a vizinhança; ΔH positivo rouba calor ao redor. E pela Lei de Hess, todo atalho leva ao mesmo ΔH.",
                    "author": "Síntese de Termoquímica ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-39-cinetica-quimica",
            "number": 39,
            "title": "39. Cinética Química: Velocidade das Reações, Catalisadores e Fatores de Controle",
            "epigraph": {
                "text": "A Termodinâmica diz se uma reação pode acontecer; a Cinética Química decide se ela acontece em um piscar de olhos ou se levará séculos.",
                "author": "Aula Magna de Cinética e Catálise"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Nem Tudo que É Espontâneo É Rápido: Bem-Vindo à Cinética!"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao Capítulo 39. Um diamante tem os mesmos átomos de carbono que o grafite do seu lápis e, termodinamicamente, tende a virar grafite. Por que sua joia nunca vira pó de lápis na gaveta? Porque a velocidade dessa reação é absurdamente lenta! A Cinética Química estuda exatamente a velocidade das reações e os fatores que a controlam — tema campeão no ENEM em contextos de geladeira, panela de pressão, comprimidos efervescentes e enzimas."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Calculando a Velocidade Média das Reações"
                },
                {
                    "type": "paragraph",
                    "content": "A velocidade média (v_m) mede o quanto a quantidade de um participante varia por unidade de tempo: v_m = |Δquantidade| / Δt (em mol/s, mol/L·min ou g/s). Como substâncias diferentes participam na proporção de seus coeficientes estequiométricos, suas velocidades individuais também obedecem exatamente a essa proporção."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Velocidade e Estequiometria na Produção de Amônia",
                    "content": "Enunciado: Na reação N₂(g) + 3 H₂(g) → 2 NH₃(g), consumiram-se 6 mols de H₂ em 2 minutos. Qual a velocidade média de consumo de H₂ e de formação de NH₃?\n\nResolução passo a passo:\n1. Para H₂: v(H₂) = 6 mol / 2 min = 3 mol/min.\n2. Pela proporção 3 H₂ : 2 NH₃, temos v(H₂) / 3 = v(NH₃) / 2 → 3 / 3 = v(NH₃) / 2 → v(NH₃) = 2 mol/min."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Teoria das Colisões Efetivas e Energia de Ativação"
                },
                {
                    "type": "paragraph",
                    "content": "Pela Teoria das Colisões, para reagir, as moléculas precisam se chocar — mas nem toda batida funciona! Uma colisão efetiva exige duas condições simultâneas: orientação geométrica favorável (bater no ângulo certo para que os átomos certos se encontrem) e energia cinética suficiente para vencer uma barreira energética mínima chamada Energia de Ativação (E_a). Imagine empurrar um carro morro acima antes de ele descer: mesmo que a reação seja exotérmica e desça bastante depois, você precisa fazer força inicial para cruzar o topo do morro. Esse pico no gráfico de energia chama-se Complexo Ativado (estado intermediário instável com ligações se rompendo e formando), e a altura dos reagentes até o pico é a E_a. Quanto menor a E_a, maior a fração de choques eficazes e mais rápida é a reação!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Catalisadores e Enzimas: O Atalho Genial Sem Alterar o ΔH"
                },
                {
                    "type": "paragraph",
                    "content": "Quer acelerar uma reação sem torrar combustível? Use um catalisador! Ele aumenta a velocidade abrindo um caminho reacional alternativo de MENOR energia de ativação (como cavar um túnel através da montanha). No corpo humano, nossas enzimas são catalisadores biológicos espetaculares: a amilase salivar quebra o amido do pão em segundos e a catalase decompõe água oxigenada instantaneamente. Nos carros, catalisadores de platina e paládio aceleram a conversão de gases tóxicos (CO e NOₓ) em gases menos nocivos."
                },
                {
                    "type": "callout",
                    "title": "Pegadinha Clássica da TRI: O Que o Catalisador NÃO Faz",
                    "content": "O catalisador abaixa a energia de ativação (E_a) e acelera TANTO a reação direta quanto a inversa na mesma proporção. Porém:\n1. Ele NÃO é consumido (regenera-se intacto ao final).\n2. Ele NÃO altera o ΔH (reagentes e produtos continuam nos mesmos patamares!).\n3. Ele NÃO aumenta o rendimento final de produto nem desloca o equilíbrio químico!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Os Quatro Fatores de Controle no Dia a Dia e na Prova"
                },
                {
                    "type": "paragraph",
                    "content": "Primeiro fator — Temperatura: aquecer aumenta a agitação molecular e, principalmente, eleva a fração de moléculas com energia igual ou superior à E_a. Por isso, a panela de pressão (água fervendo a ~120 °C) cozinha o feijão bem mais depressa, enquanto a geladeira retarda as reações de apodrecimento dos alimentos."
                },
                {
                    "type": "paragraph",
                    "content": "Segundo e terceiro fatores — Concentração e Pressão: aumentar a concentração coloca mais moléculas por volume, multiplicando o número de colisões por segundo (uma brasa queima muito mais forte em O₂ puro do que no ar com 21% de O₂). Em gases, aumentar a pressão reduz o volume e aproxima as moléculas, produzindo o mesmo efeito acelerador."
                },
                {
                    "type": "paragraph",
                    "content": "Quarto fator — Superfície de Contato: decisivo para sólidos! Triturar um sólido expõe muito mais átomos ao ataque simultâneo. No famoso experimento do comprimido efervescente em água na mesma temperatura, o comprimido triturado em pó termina de efervescer muito antes do comprimido inteiro; pelo mesmo motivo, serragem pega fogo muito mais rápido que uma tora de madeira."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Questão Integrada de Cinética Estilo ENEM",
                    "content": "Enunciado: Testou-se a reação de 1 g de zinco com excesso de HCl em quatro frascos: (1) Zn em barra, HCl 1 mol/L, 25 °C; (2) Zn em pó, HCl 1 mol/L, 25 °C; (3) Zn em pó, HCl 2 mol/L, 25 °C; (4) Zn em pó, HCl 2 mol/L, 45 °C. Em qual o gás H₂ sai mais rápido, e em qual o volume total final de H₂ é maior?\n\nResolução passo a passo:\n1. Rapidez: O Frasco 4 soma três aceleradores (maior superfície de contato do pó, maior concentração 2 mol/L e maior temperatura 45 °C) → é o mais rápido!\n2. Volume final: Cuidado com a armadilha! A massa do reagente limitante (1 g de Zn) é idêntica em todos os frascos. Fatores cinéticos mudam apenas o tempo, nunca a estequiometria final → o volume total final de H₂ será IGUAL nos quatro frascos!"
                },
                {
                    "type": "quote",
                    "content": "Quer acelerar uma reação? Multiplique choques com temperatura, concentração, pressão ou superfície de contato — ou abra um túnel energético com um catalisador.",
                    "author": "Síntese de Cinética Química ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-40-equilibrio-quimico",
            "number": 40,
            "title": "40. Equilíbrio Químico e Princípio de Le Chatelier: A Gangorra Molecular",
            "epigraph": {
                "text": "O equilíbrio químico não é um estado de repouso morto, mas uma dança frenética em que a ida e a volta acontecem exatamente no mesmo compasso.",
                "author": "Aula Magna de Equilíbrios Moleculares"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Reações Reversíveis e o Equilíbrio Dinâmico"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao Capítulo 40. Em sistemas fechados, muitas reações são reversíveis (⇄): os reagentes formam produtos (sentido direto) ao mesmo tempo em que os produtos se regeneram em reagentes (sentido inverso). Imagine uma loja cheia em que entram 5 clientes por minuto e saem 5 clientes por minuto: o movimento continua intenso, mas a lotação lá dentro permanece constante. Isso é o Equilíbrio Dinâmico, atingido no exato instante em que v_direta = v_inversa > 0!"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Constante NÃO Significa Igual!",
                    "content": "Ao atingir o equilíbrio, as concentrações de reagentes e produtos tornam-se CONSTANTES (linhas horizontais no gráfico concentração × tempo), mas NÃO precisam ser iguais entre si! Podemos ter 0,8 mol/L de produto e 0,2 mol/L de reagente estáveis para sempre enquanto nada perturbar o sistema."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "A Constante de Equilíbrio (Kc e Kp)"
                },
                {
                    "type": "paragraph",
                    "content": "Para medir quem domina no equilíbrio, usamos Kc (concentrações em mol/L) ou Kp (pressões parciais de gases). A regra de ouro é: PRODUTOS no numerador sobre REAGENTES no denominador, elevados aos coeficientes da equação balanceada: Kc = ([C]^c · [D]^d) / ([A]^a · [B]^b). Atenção vital: sólidos puros e líquidos puros (como a água solvente) NÃO entram na expressão de Kc nem de Kp! Se Kc >> 1, os produtos dominam; se Kc << 1, os reagentes dominam. E grave bem: somente a TEMPERATURA altera o valor numérico de Kc!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Calculando o Kc Passo a Passo",
                    "content": "Enunciado: Num recipiente de 2 L, o equilíbrio N₂O₄(g) ⇄ 2 NO₂(g) apresenta 0,4 mol de N₂O₄ e 0,8 mol de NO₂. Calcule Kc.\n\nResolução passo a passo:\n1. Converta mols em mol/L dividindo pelos 2 L: [N₂O₄] = 0,4 / 2 = 0,2 mol/L; [NO₂] = 0,8 / 2 = 0,4 mol/L.\n2. Monte a expressão: Kc = [NO₂]² / [N₂O₄].\n3. Calcule: Kc = (0,4)² / 0,2 = 0,16 / 0,2 = 0,8 mol/L."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Princípio de Le Chatelier: A Gangorra Molecular"
                },
                {
                    "type": "paragraph",
                    "content": "O Princípio de Le Chatelier afirma que, quando perturbamos um sistema em equilíbrio, ele desloca-se no sentido que minimiza a perturbação imposta. Com prática, você prevê qualquer deslocamento em segundos:"
                },
                {
                    "type": "paragraph",
                    "content": "1) Concentração: adicionou uma substância gasosa ou aquosa? O equilíbrio foge para o lado OPOSTO para consumi-la. Removeu uma substância? O equilíbrio corre para o MESMO lado para repô-la. (Sólidos puros não deslocam!)"
                },
                {
                    "type": "paragraph",
                    "content": "2) Pressão em gases: aumentar a pressão (comprimindo o volume do recipiente) aperta os gases e desloca o equilíbrio para o lado de MENOR número de mols gasosos; diminuir a pressão (expandindo o volume) desloca para o lado de MAIOR volume gasoso. Se os dois lados somarem exatamente a mesma quantidade de mols de gás, ou se você apenas injetar um gás inerte a volume constante, a pressão não desloca o equilíbrio."
                },
                {
                    "type": "paragraph",
                    "content": "3) Temperatura (único fator físico que altera o valor numérico de Kc e Kp!): pense no calor como um ingrediente da equação. Aumentar a temperatura fornece calor e favorece sempre o sentido ENDOTÉRMICO (ΔH > 0, que absorve o excesso); diminuir a temperatura favorece o sentido EXOTÉRMICO (ΔH < 0, que libera calor). E atenção à clássica pegadinha de prova: adicionar um catalisador NUNCA desloca o equilíbrio químico — ele acelera igualmente as duas setas, fazendo o sistema atingir o equilíbrio mais depressa!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Aplicações Reais que o ENEM Ama: Haber-Bosch, Sangue e Cascas de Ovo"
                },
                {
                    "type": "paragraph",
                    "content": "Na síntese industrial da amônia (Processo Haber-Bosch), N₂(g) + 3 H₂(g) ⇄ 2 NH₃(g) (ΔH = -92 kJ, exotérmica), temos 4 mols gasosos à esquerda e 2 mols à direita. Alta pressão desloca para a direita (menor volume gasoso), aumentando a produção de NH₃. Como é exotérmica, baixa temperatura daria maior rendimento, mas deixaria a reação lenta demais; a indústria usa temperatura moderada (~450 °C) com catalisador de ferro para equilibrar velocidade e rendimento!"
                },
                {
                    "type": "paragraph",
                    "content": "No seu sangue e nas galinhas poedeiras no verão, atua o tampão bicarbonato: CO₂(g) + H₂O(l) ⇄ H₂CO₃(aq) ⇄ H⁺(aq) + HCO₃⁻(aq). Quando uma pessoa hiperventila por ansiedade, exala muito CO₂; o equilíbrio recua para a esquerda para repor o CO₂, consumindo H⁺ e elevando o pH sanguíneo (alcalose respiratória). Nas galinhas, ofegar no calor intenso elimina CO₂ em excesso, recuando o equilíbrio e reduzindo os íons carbonato (CO₃²⁻) disponíveis para formar a casca de CaCO₃ — deixando os ovos com casca fina e quebradiça!"
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Previsão Completa de Deslocamento",
                    "content": "Enunciado: Em 2 SO₂(g) + O₂(g) ⇄ 2 SO₃(g), ΔH = -198 kJ, o que aumenta o rendimento de SO₃?\n\nResolução passo a passo:\n1. Injetar O₂ (reagente) → desloca para a DIREITA (+ SO₃).\n2. Aumentar a pressão → esquerda tem 3 mols de gás e direita tem 2 mols → desloca para o menor volume gasoso (DIREITA, + SO₃).\n3. Diminuir a temperatura → como ΔH < 0, a direta é exotérmica → esfriar favorece o sentido exotérmico (DIREITA, + SO₃), compensando a lentidão com catalisador V₂O₅."
                },
                {
                    "type": "quote",
                    "content": "Para domar o equilíbrio de Le Chatelier, pense como a natureza: se você aperta, ela encolhe; se você aquece, ela absorve; se você tira, ela corre para repor.",
                    "author": "Síntese de Equilíbrio Químico ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-41-eletroquimica",
            "number": 41,
            "title": "41. Eletroquímica: Oxirredução, Pilhas e Eletrólise",
            "epigraph": {
                "text": "Na ponte invisível entre a Química e a Eletricidade, elétrons viajam espontaneamente nas pilhas e são empurrados à força nas eletrólises.",
                "author": "Aula Magna de Eletroquímica Aplicada"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "NOX e Oxirredução: Quem Perde e Quem Ganha Elétrons?"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao Capítulo 41. Sua bateria de celular só funciona longe da tomada graças à Eletroquímica, que conecta reações de transferência de elétrons à corrente elétrica. Para começar firme, domine o Número de Oxidação (NOX): substância simples (Fe, O₂, Zn) tem NOX = 0; metais do grupo 1 (Li, Na, K) valem +1; grupo 2 (Mg, Ca) valem +2; Al vale +3; H geralmente +1 e O geralmente -2; e a soma dos NOX numa molécula neutra é sempre 0 (ou igual à carga total, num íon)."
                },
                {
                    "type": "paragraph",
                    "content": "Quem perde elétrons tem o NOX aumentado e sofre OXIDAÇÃO (atuando como agente redutor). Quem ganha elétrons tem o NOX diminuído e sofre REDUÇÃO (atuando como agente oxidante)."
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: O Mnemônico CRAO / OXIDANO",
                    "content": "Vale tanto para PILHAS quanto para ELETRÓLISE, sem nenhuma exceção:\n- CRAO: Cátodo = Redução | Ânodo = Oxidação (consoante com consoante C-R; vogal com vogal A-O).\n- Fluxo externo de elétrons: Sempre saem do ÂNODO e correm pelo fio até o CÁTODO (de A para C!)."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Pilhas: Reações Espontâneas Gerando Corrente e a Pilha de Daniell"
                },
                {
                    "type": "paragraph",
                    "content": "Na pilha (célula galvânica), uma reação de oxirredução espontânea (ΔE° > 0) gera eletricidade. Na clássica Pilha de Daniell, temos uma placa de zinco em ZnSO₄ conectada por fio metálico a uma placa de cobre em CuSO₄, com uma ponte salina (íons K⁺ e NO₃⁻ ou Cl⁻) fechando o circuito ao manter a neutralidade elétrica das soluções. Regra da tabela de potenciais padrão de redução (E°_red): quem tem MAIOR E°_red reduz (Cátodo, polo +); quem tem MENOR E°_red oxida (Ânodo, polo -). A ddp espontânea é ΔE° = E°_red(maior) - E°_red(menor)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 1: Pilha de Daniell na Ponta do Lápis",
                    "content": "Enunciado: Dados Zn²⁺ + 2 e⁻ → Zn (E° = -0,76 V) e Cu²⁺ + 2 e⁻ → Cu (E° = +0,34 V), determine ânodo, cátodo, variação de massa das placas e a ddp.\n\nResolução passo a passo:\n1. Como +0,34 V > -0,76 V, o Cu²⁺ REDUZ (Cátodo, polo +) e o Zn OXIDA (Ânodo, polo -).\n2. Ânodo: Zn(s) → Zn²⁺(aq) + 2 e⁻ (a barra de zinco CORRÓI e perde massa).\n3. Cátodo: Cu²⁺(aq) + 2 e⁻ → Cu(s) (a barra de cobre ENGORDA e ganha massa).\n4. Equação global: Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s).\n5. ddp = +0,34 - (-0,76) = +1,10 V!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Baterias de Íon-Lítio e Metal de Sacrifício contra a Corrosão"
                },
                {
                    "type": "paragraph",
                    "content": "As baterias recarregáveis de íon-lítio dominam celulares e veículos elétricos porque o lítio é levíssimo e tem baixíssimo potencial de redução (-3,04 V), entregando alta tensão (~3,7 V por célula) com peso mínimo. Na descarga, íons Li⁺ migram do ânodo de grafite até o cátodo de óxido metálico por um eletrólito não aquoso; ao recarregar na tomada, o fluxo inverte. Já para evitar a ferrugem do ferro (E° = -0,44 V) em cascos de navios e tubulações, usamos metal de sacrifício (proteção catódica): acoplamos blocos de magnésio (-2,37 V) ou zinco (-0,76 V, como no aço galvanizado). Tendo menor potencial de redução, eles oxidam no lugar do ferro!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Eletrólise Ígnea e Aquosa: Forçando a Química com Eletricidade"
                },
                {
                    "type": "paragraph",
                    "content": "Na Eletrólise, uma fonte externa de corrente contínua (como uma bateria ou tomada retificada) força uma reação de oxirredução NÃO espontânea (ΔE° < 0). Fique atento a uma inversão clássica: na eletrólise, os sinais dos polos invertem em relação à pilha (o Cátodo passa a ser o polo negativo, ligado ao polo negativo da fonte, e o Ânodo passa a ser o polo positivo), mas a definição CRAO continua sagrada e inabalável: no Cátodo sempre ocorre redução e no Ânodo sempre ocorre oxidação!"
                },
                {
                    "type": "paragraph",
                    "content": "Na eletrólise ígnea (sem água, apenas com o sal ou óxido derretido em alta temperatura), produzimos metais muito reativos como sódio (a partir de NaCl fundido) e alumínio metálico no famoso processo Hall-Héroult: funde-se a alumina (Al₂O₃, purificada da bauxita) misturada com criolita para abaixar o ponto de fusão de mais de 2.000 °C para cerca de 960 °C, reduzindo Al³⁺ a alumínio líquido puríssimo com gigantesco consumo elétrico. Já na eletrólise aquosa, a água entra na disputa pelas descargas: o H⁺ da água vence cátions alcalinos (1A), alcalino-terrosos (2A) e Al³⁺ (liberando gás H₂ no cátodo), enquanto metais nobres e de transição (Cu²⁺, Ag⁺, Ni²⁺, Cr³⁺) vencem o H⁺ e se depositam sobre a peça ligada ao CÁTODO — base da galvanoplastia (cromagem, prateação e niquelagem)."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido 2: Estequiometria da Eletrólise (Leis de Faraday)",
                    "content": "Enunciado: Uma peça recebe banho de prata (Ag⁺ + 1 e⁻ → Ag) sob corrente de 10 A durante 965 s. Qual a massa de prata depositada? (Dados: M(Ag) = 108 g/mol; 1 F = 96.500 C/mol de e⁻).\n\nResolução passo a passo:\n1. Carga elétrica: Q = i × t = 10 A × 965 s = 9.650 C.\n2. Pela equação, 1 mol de elétrons (96.500 C) deposita 1 mol de Ag (108 g).\n3. Regra de três: 96.500 C → 108 g; logo 9.650 C (um décimo!) → 10,8 g de prata depositada no cátodo!"
                },
                {
                    "type": "quote",
                    "content": "Na pilha, a natureza empurra elétrons e acende a lâmpada; na eletrólise, a tomada força o processo e fabrica alumínio ou banha de prata. Em ambas, CRAO nunca falha.",
                    "author": "Síntese de Eletroquímica ENEM"
                }
            ],
            "quiz": []
        },
        {
            "id": "nat-cap-42-quimica-ambiental",
            "number": 42,
            "title": "42. Química Ambiental: Tratamento de Água, Poluição, Combustíveis, Chuva Ácida, Efeito Estufa e Reciclagem",
            "epigraph": {
                "text": "Entender a Química Ambiental é enxergar como cada átomo que lançamos no ar, no rio ou no solo sempre encontra um caminho de volta para nossas vidas.",
                "author": "Aula Magna de Química e Sustentabilidade"
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Capítulo Mais Frequente da Prova: Química com Consciência Planetária"
                },
                {
                    "type": "paragraph",
                    "content": "Olá! Seja muito bem-vindo ao último capítulo deste módulo — e talvez o mais transversal de toda a prova de Ciências da Natureza do ENEM! A Química Ambiental une reações inorgânicas, equilíbrios, termoquímica, eletroquímica e ecologia para analisar problemas reais das cidades e do planeta. Vamos percorrer juntos, passo a passo, da torneira da sua casa até a estratosfera."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Da Represa à Torneira: Etapas da Estação de Tratamento de Água (ETA)"
                },
                {
                    "type": "paragraph",
                    "content": "Como água barrenta de um rio vira água límpida e potável na sua torneira? Em uma ETA convencional, o roteiro segue uma sequência física e química precisa. Após a captação e o gradeamento (que segura folhas e plásticos grandes), a água vai para a coagulação e floculação: adicionam-se sulfato de alumínio, Al₂(SO₄)₃, e cal hidratada, Ca(OH)₂, que reagem formando flocos gelatinosos e insolúveis de hidróxido de alumínio, Al(OH)₃. Esses flocos agregam partículas finas de barro e bactérias em suspensão, deixando-as pesadas!"
                },
                {
                    "type": "paragraph",
                    "content": "Em seguida vem a decantação: em tanques calmos, os flocos pesados afundam pela ação da gravidade. A água clara passa então para a filtração, atravessando camadas de areia, cascalho e carvão ativado (que adsorve odores e sabores). Atenção: até aqui, ela está limpa a olho nu, mas ainda pode conter microrganismos! Por isso ocorrem a desinfecção/cloração (adição de cloro ou hipoclorito para matar patógenos), a fluoretação (adição de fluoretos para prevenir cáries) e a correção final do pH antes da distribuição."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Poluição Hídrica: Eutrofização e Metais Pesados"
                },
                {
                    "type": "paragraph",
                    "content": "Nos rios e lagos, dois vilões dominam o ENEM. O primeiro é a eutrofização: esgoto não tratado ou excesso de fertilizantes despejam muitos nutrientes (nitratos e fosfatos) na água, disparando uma floração de algas na superfície. Essa camada verde bloqueia a luz solar, matando plantas submersas; depois as algas morrem e bactérias aeróbias se multiplicam decompondo essa matéria orgânica — consumindo o oxigênio dissolvido (elevando a DBO, Demanda Bioquímica de Oxigênio) e matando os peixes por asfixia!"
                },
                {
                    "type": "paragraph",
                    "content": "O segundo vilão são os metais pesados, como mercúrio (Hg, de garimpos ilegais), chumbo (Pb) e cádmio (Cd). Como não são biodegradáveis, sofrem bioacumulação nos organismos e magnificação trófica — aumentando de concentração ao longo da cadeia alimentar até chegar ao ser humano."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Combustíveis Fósseis vs Biocombustíveis e a Química da Chuva Ácida"
                },
                {
                    "type": "paragraph",
                    "content": "Queimar combustíveis fósseis (carvão mineral, gasolina, diesel, gás natural) devolve à atmosfera carbono aprisionado há milhões de anos, elevando o CO₂ líquido. Já biocombustíveis renováveis — como o etanol da cana-de-açúcar e o biodiesel (produzido por transesterificação de óleos vegetais ou gorduras animais com álcool, formando ésteres + glicerol) — integram o ciclo curto do carbono, pois o CO₂ emitido é reabsorvido pela fotossíntese da safra seguinte!"
                },
                {
                    "type": "paragraph",
                    "content": "Além do CO₂, combustíveis fósseis com enxofre (diesel e carvão) e motores quentes provocam a Chuva Ácida. A chuva natural já é levemente ácida (pH ~5,6) pelo CO₂ dissolvido formando H₂CO₃. Porém, a chuva ácida antrópica (pH < 5,0) vem de óxidos de enxofre (SO₂ → SO₃ + H₂O → H₂SO₄, ácido sulfúrico) e óxidos de nitrogênio (NOₓ + H₂O → HNO₃, ácido nítrico). Ela corrói estátuas de mármore (CaCO₃ + 2 H⁺ → Ca²⁺ + H₂O + CO₂) e acidifica solos e lagos."
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Não Confunda Mais: Efeito Estufa vs Camada de Ozônio"
                },
                {
                    "type": "callout",
                    "title": "Pegadinha Número 1 da TRI: Dois Fenômenos Totalmente Diferentes!",
                    "content": "Nunca misture os gases nem as radiações no ENEM:\n1. EFEITO ESTUFA (Troposfera): Fenômeno natural vital agravado por CO₂, CH₄ (pecuária/aterros) e N₂O, que absorvem radiação INFRAVERMELHA (calor) emitida pela Terra → Aquecimento Global.\n2. CAMADA DE OZÔNIO (Estratosfera): O O₃ filtra radiação ULTRAVIOLETA (UV-B/UV-C) do Sol. Foi destruída por clorofluorcarbonos (CFCs): sob luz UV, liberam radicais cloro (•Cl) que catalisam a destruição de O₃ em O₂!"
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Reciclagem e os Princípios da Química Verde"
                },
                {
                    "type": "paragraph",
                    "content": "Reciclar reduz extração mineral e gasto energético! Plásticos como PET, PEAD e PVC precisam ser separados para reciclagem mecânica (derretimento) ou química (despolimerização). Já o alumínio das latinhas é imbatível: reciclar alumínio consome cerca de 95% MENOS energia elétrica do que produzi-lo do zero pela eletrólise ígnea da bauxita, além de evitar rejeitos industriais!"
                },
                {
                    "type": "paragraph",
                    "content": "Tudo isso converge para a Química Verde: prevenir resíduos na origem, buscar máxima economia atômica, substituir solventes tóxicos por água ou CO₂ supercrítico, usar matérias-primas renováveis, projetar substâncias biodegradáveis e preferir processos catalíticos eficientes."
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Questão Integrada de Química Ambiental Estilo ENEM",
                    "content": "Enunciado: Uma prefeitura substituiu o diesel comum por biodiesel com baixo enxofre (medida I) e implantou coleta seletiva de latinhas de alumínio (medida II). Quais impactos químicos diretos correspondem a (I) e (II)?\n\nResolução passo a passo:\n1. Medida (I): Reduzir enxofre na queima corta a emissão de SO₂/SO₃, combatendo a CHUVA ÁCIDA (além de diminuir emissões líquidas de CO₂ fóssil).\n2. Medida (II): Reciclar alumínio evita nova eletrólise ígnea da alumina (Al₂O₃), economizando ~95% de energia elétrica!"
                },
                {
                    "type": "quote",
                    "content": "A Química Verde nos ensina a frase mais inteligente do século XXI: o resíduo mais fácil e barato de tratar é aquele que você nunca chegou a produzir.",
                    "author": "Síntese de Química Ambiental ENEM"
                }
            ],
            "quiz": []
        }
    ]
