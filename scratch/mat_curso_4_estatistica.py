# -*- coding: utf-8 -*-
"""Curso Completo de Matemática ENEM - Módulo 4: Estatística Descritiva (Capítulos 14 a 17)."""


def get_chapters():
    return [
        {
            "id": "mat-curso-cap-14-tabelas-graficos",
            "number": 14,
            "title": "14. Leitura Cirúrgica de Tabelas e Gráficos no ENEM",
            "epigraph": {
                "text": "Os números não mentem, mas quem apresenta um gráfico sem critério pode fazer os seus olhos acreditarem em qualquer história.",
                "author": "Lição de Ouro da Estatística Aplicada",
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Boas-Vindas à Mina de Ouro da Estatística no ENEM",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Olá! Seja muito bem-vindo ao nosso módulo de Estatística Descritiva. Se existe um assunto "
                        "essencial para conquistar mais de 800 pontos em Matemática no ENEM, é este aqui. Em "
                        "praticamente toda edição, de seis a oito questões envolvem tabelas, gráficos ou medidas "
                        "estatísticas. E há uma vantagem estratégica enorme: muitas delas são classificadas pela "
                        "TRI como fáceis ou médias, protegendo sua nota inteira e garantindo base sólida para a "
                        "aprovação. Hoje, vamos treinar o seu olhar para ler qualquer gráfico como um cirurgião, "
                        "sem cair nas armadilhas visuais que derrubam milhares de candidatos apressados."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Gráficos de Barras, Colunas e a Armadilha do Eixo Truncado",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Os gráficos de colunas (verticais) e de barras (horizontais) são velhos conhecidos nossos. "
                        "Eles servem para comparar categorias separadas, como a produção de soja por estado, o número "
                        "de medalhas por país ou as vendas de cinco modelos de celular. A leitura parece óbvia: "
                        "barra maior significa valor maior. Mas atenção redobrada! Existe um truque clássico de "
                        "diagramação chamado eixo truncado. Imagine uma pesquisa eleitoral ou uma tabela de vendas "
                        "em que o Produto A tem 52% e o Produto B tem 50%. Se o eixo vertical começar no zero, as "
                        "duas barras ficam praticamente da mesma altura. Porém, se o autor do gráfico começar o eixo "
                        "vertical em 49%, a barra do Produto A terá altura equivalente a 3 unidades (de 49 a 52) e "
                        "a do Produto B terá altura de apenas 1 unidade (de 49 a 50). Aos olhos desatentos, parece "
                        "que o Produto A vendeu o triplo do Produto B!"
                    ),
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: O Eixo que Engana os Olhos",
                    "content": (
                        "Nunca compare duas barras apenas pelo tamanho do desenho! Antes de afirmar que um valor é "
                        "o dobro ou o triplo do outro, olhe imediatamente para a base do eixo numérico. Se o eixo "
                        "não começar no zero, o desenho está fora de proporção visual. Faça a conta usando os "
                        "números escritos no topo das barras ou no eixo, nunca medindo a altura no olho."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Gráficos de Linhas e Pictogramas: Lendo Tendências e Símbolos",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Quando a questão quer mostrar a evolução de um fenômeno ao longo do tempo — como a variação "
                        "do dólar durante doze meses ou a curva de casos de uma doença — o protagonista é o gráfico "
                        "de linhas. Pense comigo na leitura da inclinação dessa linha: quanto mais íngreme for a "
                        "subida entre dois anos, maior foi a velocidade de crescimento naquele intervalo. Se a linha "
                        "ficou perfeitamente horizontal, houve estabilidade; se caiu, houve redução. Já nos "
                        "pictogramas, os números são substituídos por ícones temáticos, como bonequinhos, carros ou "
                        "sacos de grãos. O segredo aqui mora na legenda: se cada desenho de árvore representa "
                        "500 mil mudas plantadas, então três árvores e meia significam 3,5 vezes 500 mil, ou seja, "
                        "1.750.000 mudas. Esquecer a escala da legenda ou ignorar um ícone cortado ao meio é erro "
                        "garantido na conta final."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Gráficos de Setores (Pizza): A Ponte Entre Porcentagem e Ângulo",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "O gráfico de setores, popularmente chamado de gráfico de pizza, mostra como um todo de 100% "
                        "está fatiado entre diferentes partes. Além de ler porcentagens diretas, o ENEM adora cobrar "
                        "a conversão entre o ângulo central da fatia e a porcentagem correspondente. Veja que sacada "
                        "simples: uma volta completa no círculo tem 360 graus e representa 100% do total. Logo, se "
                        "dividirmos 360 por 100, descobrimos que cada 1% equivale exatamente a 3,6 graus! Memorizar "
                        "algumas fatias clássicas acelera muito a sua prova: metade da pizza são 180 graus (50%), "
                        "um quarto são 90 graus (25%), um quinto são 72 graus (20%) e um décimo são 36 graus (10%). "
                        "Se aparecer um ângulo diferente, como 108 graus, basta fazer a regra de três: 108 dividido "
                        "por 360 dá 0,30, ou seja, exatos 30%."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Histogramas: Colunas Coladas que Contam Intervalos",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Muita atenção aqui porque este gráfico costuma assustar quem só conhece barras comuns. "
                        "O histograma parece um gráfico de colunas, mas tem uma característica visual marcante: as "
                        "colunas ficam completamente coladas umas nas outras, sem espaço entre elas. Por quê? Porque "
                        "no eixo horizontal não temos categorias isoladas, mas sim intervalos numéricos contínuos, "
                        "como faixas de idade (de 10 a 20 anos, de 20 a 30 anos) ou faixas de tempo de espera em "
                        "uma fila (de 0 a 5 minutos, de 5 a 10 minutos). A altura de cada bloco mostra quantas "
                        "pessoas ou objetos caíram dentro daquela faixa. Por exemplo, se o bloco de 10 a 15 minutos "
                        "tem altura 18 e o bloco de 15 a 20 minutos tem altura 12, sabemos que 30 clientes "
                        "esperaram entre 10 e 20 minutos."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Protocolo de 4 Passos Para Não Cair em Distratores",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Antes de sair fazendo conta, respire fundo e aplique sempre o mesmo roteiro cirúrgico em "
                        "qualquer tabela ou gráfico do ENEM. Primeiro passo: leia o título e a fonte, pois eles "
                        "dizem exatamente o que está sendo medido e em qual período. Segundo passo: examine as "
                        "unidades dos eixos e os cabeçalhos das colunas. Um número 42 pode significar 42 pessoas, "
                        "42 mil toneladas ou 42% — ignorar a palavra 'em milhares' no canto do gráfico é uma das "
                        "armadilhas mais cruéis da prova. Terceiro passo: identifique se a pergunta pede um valor "
                        "absoluto (quantos reais aumentou), uma variação relativa (quantos por cento aumentou) ou "
                        "apenas uma comparação direta. Quarto passo: confira se sua resposta faz sentido lógico "
                        "com a escala apresentada antes de marcar o gabarito."
                    ),
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo (Nível ENEM)",
                    "content": (
                        "Enunciado adaptado: Uma prefeitura pesquisou o meio de transporte principal de 2.000 "
                        "moradores e exibiu os dados em um gráfico de setores. O setor 'Bicicleta' possui um ângulo "
                        "central de 54 graus, e o setor 'Ônibus' corresponde a 45% dos entrevistados. Quantos "
                        "moradores usam bicicleta e quantos graus tem o setor dos usuários de ônibus?\n\n"
                        "Resolução passo a passo:\n"
                        "1) Para descobrir a porcentagem de quem usa bicicleta, relacionamos o ângulo de 54° com a "
                        "volta inteira de 360°: fração = 54 / 360. Simplificando por 18, temos 3 / 20 = 0,15 = 15%.\n"
                        "2) Agora calculamos 15% do total de 2.000 moradores: 10% de 2.000 é 200, e 5% é 100. "
                        "Somando, temos 300 moradores que usam bicicleta.\n"
                        "3) Para o setor 'Ônibus', queremos transformar 45% em graus. Como 100% equivale a 360°, "
                        "fazemos 0,45 × 360° = 162°. (Atalho mental: 50% seria 180° e 5% é metade de 36°, ou seja, "
                        "18°; logo 180° - 18° = 162°!). Resposta: 300 moradores e 162°."
                    ),
                },
                {
                    "type": "quote",
                    "content": "Ler bem um gráfico não é questão de sorte: é olhar para o eixo antes de olhar para o desenho.",
                    "author": "Regra de Ouro da Sala de Aula",
                },
            ],
            "quiz": [],
        },
        {
            "id": "mat-curso-cap-15-medias",
            "number": 15,
            "title": "15. Média Aritmética Simples e Média Ponderada: O Ponto de Equilíbrio",
            "epigraph": {
                "text": "A média aritmética é o ponto onde todos os excessos e todas as faltas de um grupo finalmente se compensam.",
                "author": "Caderno de Estatística do ENEM",
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Afinal, O Que é Média de Verdade? A Ideia da Divisão Justa",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Pense comigo em uma cena bem comum de fim de semana. Quatro amigos vão a uma lanchonete e "
                        "cada um pede o que quer: o primeiro gasta R$ 20, o segundo gasta R$ 30, o terceiro gasta "
                        "R$ 24 e o quarto gasta R$ 46. Na hora de pagar, eles decidem dividir tudo igualmente. "
                        "Qual é o total da conta? Somamos 20 + 30 + 24 + 46 e encontramos R$ 120. Dividindo esses "
                        "R$ 120 igualmente pelas 4 pessoas, cada um paga R$ 30. Pronto! Você acabou de calcular "
                        "uma média aritmética simples. Na essência, a média representa uma divisão justa, um "
                        "nivelamento: se pegássemos o excesso de quem gastou mais (R$ 46 deu R$ 16 acima de 30) e "
                        "entregássemos para quem gastou menos (R$ 20 precisava de R$ 10 e R$ 24 precisava de R$ 6, "
                        "somando exatos R$ 16), todo mundo ficaria exatamente com o mesmo valor!"
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Média Aritmética Simples e o Poder Oculto da Soma Total",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Matematicamente, a média aritmética simples é a soma de todos os valores dividida pela "
                        "quantidade total de elementos: Média = Soma / n. Mas aqui mora uma sacada poderosa: "
                        "passando 'n' multiplicando, descobrimos que Soma Total = n × Média. Grave isso! Sempre "
                        "que o enunciado informar a média de um grupo e a quantidade de elementos, seu primeiro "
                        "reflexo deve ser multiplicar os dois números para achar o total antes da divisão. Se a "
                        "média de idade de 11 jogadores é 24 anos, a soma das idades deles é 11 × 24 = 264 anos."
                    ),
                },
                {
                    "type": "callout",
                    "title": "Dica de Ouro do Professor: O Truque do Elemento Faltante",
                    "content": (
                        "Imagine que Laura fez 4 simulados e está com média 7,5. Qual nota ela precisa tirar no 5º "
                        "simulado para que sua média suba para 8,0?\n"
                        "Passo 1 (Soma atual): Com 4 simulados e média 7,5, Laura já acumulou 4 × 7,5 = 30 pontos.\n"
                        "Passo 2 (Soma desejada): Ao final de 5 simulados com média 8,0, ela precisará ter um total "
                        "de 5 × 8,0 = 40 pontos.\n"
                        "Passo 3 (Diferença): Se ela já tem 30 e precisa chegar a 40, no 5º simulado ela precisa "
                        "tirar exatamente 40 - 30 = 10,0! Sem montar equação feia, em dez segundos você matou a questão."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Média em Tabelas de Frequência: Quando os Dados se Repetem",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Agora preste muita atenção num erro que derruba metade dos candidatos quando os dados "
                        "aparecem organizados em uma tabela. Suponha que uma pequena oficina tenha 10 funcionários "
                        "distribuídos assim: 5 recebem salário de R$ 2.000, 3 recebem R$ 3.000 e 2 recebem R$ 5.500. "
                        "Qual é o salário médio dessa oficina? O candidato distraído soma 2.000 + 3.000 + 5.500 e "
                        "divide por 3 linhas! Isso está completamente errado porque não há apenas três funcionários, "
                        "há dez! Precisamos multiplicar cada salário pela sua frequência (quantas pessoas o recebem) "
                        "e dividir pelo total de funcionários: (5 × 2.000 + 3 × 3.000 + 2 × 5.500) dividido por "
                        "(5 + 3 + 2). Temos (10.000 + 9.000 + 11.000) / 10 = 30.000 / 10 = R$ 3.000 por pessoa."
                    ),
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Dividir Pela Quantidade de Linhas",
                    "content": (
                        "Em tabelas de frequência, o denominador da média NUNCA é o número de linhas ou categorias "
                        "da tabela, e sim a soma total das frequências! Sempre some a coluna da quantidade de "
                        "pessoas, dias ou itens para garantir que você está dividindo pelo universo real da amostra."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Média Ponderada: Nem Todo Número Tem o Mesmo Peso",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Você acabou de perceber, sem nem notar o nome formal, como funciona a média ponderada! "
                        "Na média ponderada, alguns valores influenciam o resultado final mais do que outros porque "
                        "possuem pesos diferentes. Você convive com isso no próprio SISU: se uma universidade dá "
                        "peso 3 para Matemática, peso 2 para Natureza e peso 1 para Humanas, tirar 800 em Matemática "
                        "puxa sua média muito mais para cima do que tirar 800 em Humanas. A fórmula é idêntica à "
                        "da tabela de frequência: multiplicamos cada valor pelo seu respectivo peso, somamos tudo "
                        "e dividimos pela soma dos pesos. Outro campeão absoluto do ENEM com essa mesma lógica é o "
                        "preço médio de misturas ou compras em lotes diferentes."
                    ),
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Veja esse exemplo cotidiano de preço médio: um comerciante mistura 20 kg de um café especial "
                        "que custa R$ 40,00 o quilo com 30 kg de um café tradicional que custa R$ 25,00 o quilo. "
                        "Qual é o preço médio por quilo dessa mistura? Quem chuta a média simples entre 40 e 25 "
                        "(que daria R$ 32,50) cai direto no distrator, porque há muito mais quilos do café barato "
                        "do que do café caro! Fazendo a conta ponderada pelas quantidades: o gasto total foi "
                        "(20 × 40) + (30 × 25) = 800 + 750 = R$ 1.550. A quantidade total de café na saca agora é "
                        "20 + 30 = 50 kg. Dividindo R$ 1.550 por 50 kg, encontramos exatamente R$ 31,00 por quilo."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Questão Estilo ENEM 800+ Resolvida na Íntegra",
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido: Média Ponderada com Meta de Aprovação",
                    "content": (
                        "Enunciado: Em um processo seletivo, a nota final é a média ponderada de três etapas: Prova "
                        "Objetiva (peso 4), Redação (peso 3) e Entrevista (peso 3). Para ser aprovado, o candidato "
                        "precisa obter média final mínima 7,0. Sabendo que Bruno tirou 6,5 na Prova Objetiva e "
                        "8,0 na Redação, qual é a nota mínima que ele precisa tirar na Entrevista?\n\n"
                        "Resolução passo a passo:\n"
                        "1) Somamos os pesos para saber o tamanho do denominador: 4 + 3 + 3 = 10.\n"
                        "2) Aplicamos o truque da soma ponderada total: para que a divisão por 10 dê média 7,0, "
                        "o numerador (soma das notas multiplicadas pelos pesos) precisa ser pelo menos 10 × 7,0 = 70 pontos.\n"
                        "3) Calculamos o que Bruno já conquistou: na Objetiva, 6,5 × 4 = 26 pontos. Na Redação, "
                        "8,0 × 3 = 24 pontos. Somando os dois, ele já tem 26 + 24 = 50 pontos.\n"
                        "4) Quanto falta para 70? Faltam 70 - 50 = 20 pontos! Como a Entrevista tem peso 3, "
                        "precisamos de 3 × Nota >= 20, logo Nota >= 20 / 3 = 6,66... Ou seja, no mínimo 6,7."
                    ),
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Viu como fica leve quando pensamos em pontos acumulados? Mas antes de encerrarmos este "
                        "capítulo, deixe-me fazer uma provocação: e se um único valor gigantesco — muito fora da "
                        "curva — entrar no nosso conjunto de dados? A média é extremamente sensível a extremos! "
                        "Para lidar com esses casos e descobrir o valor mais popular ou o verdadeiro centro da fila, "
                        "vamos agora para o Capítulo 16 aprender Moda e Mediana."
                    ),
                },
                {
                    "type": "quote",
                    "content": "Na média ponderada, o denominador nunca mente: some todos os pesos antes de dividir.",
                    "author": "Bússola da Matemática ENEM",
                },
            ],
            "quiz": [],
        },
        {
            "id": "mat-curso-cap-16-moda-mediana",
            "number": 16,
            "title": "16. Moda e Mediana: Os Segredos da Frequência e da Ordenação",
            "epigraph": {
                "text": "Se um bilionário entra em um ônibus com trinta trabalhadores, todos ficam ricos na média, mas ninguém muda de vida na mediana.",
                "author": "Parábola Clássica da Estatística",
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Quando a Média Mente: A Chegada do Bilionário na Sala",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Seja muito bem-vindo ao Capítulo 16! Imagine 9 estudantes em que cada um recebe mesada "
                        "de R$ 500; a média do grupo é, claro, R$ 500. De repente, entra na sala um jovem "
                        "empreendedor que ganha R$ 95.500 por mês. A soma das dez rendas vai a R$ 100.000, "
                        "elevando a média salarial da sala para R$ 10.000! Faz sentido dizer que esse grupo ganha "
                        "R$ 10.000? Nenhum, pois nove em dez pessoas seguem ganhando R$ 500. Isso prova como a "
                        "média sofre com valores extremos (outliers) e por que o ENEM cobra tanto a Moda e a Mediana."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Moda: O Valor Mais Popular do Conjunto",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "O nome já entrega tudo: estar na moda significa ser o que todo mundo está usando ou o que "
                        "mais aparece! Em Estatística, a Moda (Mo) é simplesmente o valor que apresenta a maior "
                        "frequência absoluta em um conjunto de dados. Não precisa ordenar nada e não precisa fazer "
                        "nenhuma conta complexa — basta bater o olho e contar quem se repete mais vezes. Em um "
                        "gráfico de colunas, a moda é a categoria da barra mais alta. Em uma tabela de frequências, "
                        "é o valor correspondente à linha com maior número de ocorrências. Ah, e vale um detalhe "
                        "importante: um conjunto pode ter duas modas empatadas na liderança (chamamos de bimodal), "
                        "ou pode até não ter moda nenhuma se todos os valores aparecerem apenas uma vez (amodal)."
                    ),
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Confundir a Moda com a Frequência",
                    "content": (
                        "Muita atenção aqui porque essa distração derruba muita gente boa! Suponha que uma tabela "
                        "mostre as notas de uma turma: 4 alunos tiraram nota 5; 18 alunos tiraram nota 7; e 6 alunos "
                        "tiraram nota 9. Qual é a moda das notas? A moda é 7, e NÃO 18! O número 18 é apenas a "
                        "quantidade de repetições (a frequência). A moda é o DADO observado (a nota 7) que venceu "
                        "em popularidade."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Mediana: O Verdadeiro Meio do Caminho (E Seu Perigo Número 1)",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Agora chegamos à estrela favorita das provas recentes do ENEM: a Mediana (Md). Pense na "
                        "mediana como o valor que ocupa exatamente o meio de uma fila organizada por tamanho, "
                        "deixando metade dos elementos para um lado e metade para o outro. E é justamente nessa "
                        "palavra — ORGANIZADA — que mora o perigo número 1 do ENEM! Na maioria das questões, a "
                        "banca apresenta uma tabela em ordem cronológica (janeiro, fevereiro, março, abril...) ou "
                        "em ordem alfabética de cidades, e pede a mediana das vendas ou das temperaturas. Se você "
                        "pegar o valor que está no meio da tabela sem ordenar os números do menor para o maior (ou "
                        "do maior para o menor), você erra na hora — e pode ter certeza de que o número errado "
                        "estará lá na alternativa A esperando por você!"
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Quantidade Ímpar vs. Quantidade Par de Dados",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Depois de colocar todos os números em ordem crescente, temos apenas dois cenários possíveis. "
                        "Cenário 1: a quantidade N de dados é ÍMPAR. Aqui existe um único termo solitário bem no "
                        "meio da fila. Por exemplo, com 7 números ordenados (10, 12, 15, 18, 22, 30, 95), o centro "
                        "é o 4º número, pois sobram 3 à esquerda e 3 à direita. Logo, a mediana é 18. Perceba como "
                        "o 95 lá na ponta não mexeu em nada no 18! Cenário 2: a quantidade N de dados é PAR, como "
                        "nos 12 meses do ano. Nesse caso, não há um elemento sozinho no centro, e sim uma dupla "
                        "central (o 6º e o 7º elementos de uma fila de 12). Para achar a mediana, tiramos a média "
                        "aritmética simples desses dois termos centrais: somamos o 6º com o 7º e dividimos por 2."
                    ),
                },
                {
                    "type": "callout",
                    "title": "Quadro de Bolso: Fórmula Rápida da Posição Central",
                    "content": (
                        "Com os dados SEMPRE ordenados:\n"
                        "• Se N é ímpar: a mediana está exatamente na posição (N + 1) / 2. Exemplo: para N = 25 "
                        "dados, a mediana é o (25 + 1) / 2 = 13º valor.\n"
                        "• Se N é par: a mediana é a média entre o valor da posição N / 2 e o da posição (N / 2) + 1. "
                        "Exemplo: para N = 20 dados, tiramos a média entre o 10º e o 11º valores."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Mediana em Tabelas de Frequência Acumulada (Nível 800+)",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "E quando o ENEM dá uma tabela com 40, 50 ou 100 pessoas? Você não vai escrever cem "
                        "números no seu rascunho da prova! É aqui que usamos a Frequência Acumulada. Como a tabela "
                        "normalmente já lista os valores em ordem crescente (por exemplo, idades de 15, 16, 17, 18 "
                        "anos), nós vamos somando as frequências linha por linha para descobrir qual posição cada "
                        "valor ocupa na fila imaginária. Depois, basta identificar onde estão as posições centrais "
                        "e ler o valor correspondente na tabela. Vamos treinar isso agora mesmo num exemplo completo."
                    ),
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido Passo a Passo: Mediana na Tabela de Notas",
                    "content": (
                        "Enunciado: Uma pesquisa registrou o número de livros lidos no ano por 40 estudantes:\n"
                        "• 0 livros: 6 alunos\n"
                        "• 1 livro: 10 alunos\n"
                        "• 2 livros: 9 alunos\n"
                        "• 3 livros: 11 alunos\n"
                        "• 4 livros: 4 alunos\n"
                        "Determine a moda e a mediana dessa amostra.\n\n"
                        "Resolução passo a passo:\n"
                        "1) Moda: A maior frequência é 11 alunos, que corresponde a 3 livros. Logo, Moda = 3 livros.\n"
                        "2) Mediana: Como o total é N = 40 (número par), a mediana será a média entre o 20º e o 21º "
                        "estudantes da fila ordenada do menor para o maior.\n"
                        "3) Frequência acumulada:\n"
                        "• Quem leu 0 livros ocupa da 1ª até a 6ª posição.\n"
                        "• Somando os 10 alunos de 1 livro (6 + 10 = 16), eles ocupam da 7ª até a 16ª posição.\n"
                        "• Somando os 9 alunos de 2 livros (16 + 9 = 25), eles ocupam da 17ª até a 25ª posição!\n"
                        "4) Opa! Tanto o 20º quanto o 21º estudante caíram dentro do grupo entre a 17ª e a 25ª posição, "
                        "ou seja, ambos leram 2 livros. Logo, a média entre 2 e 2 é 2. Mediana = 2 livros!"
                    ),
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Para fechar com chave de ouro, guarde também a aplicação interpretativa: se uma loja de "
                        "sapatos quer saber qual numeração comprar em maior quantidade para o estoque, ela olha "
                        "para a Moda. Se um economista quer analisar a renda típica de um bairro sem deixar os "
                        "milionários distorcerem o retrato, ele escolhe a Mediana. Se o objetivo é calcular o total "
                        "distribuído igualmente, a ferramenta certa é a Média."
                    ),
                },
                {
                    "type": "quote",
                    "content": "Antes de procurar o meio do caminho, coloque a fila em ordem. A pressa é a única inimiga da mediana.",
                    "author": "Manual de Sobrevivência no ENEM",
                },
            ],
            "quiz": [],
        },
        {
            "id": "mat-curso-cap-17-dispersao",
            "number": 17,
            "title": "17. Medidas de Dispersão: Amplitude, Variância e Desvio Padrão Sem Sofrimento",
            "epigraph": {
                "text": "Duas equipes podem ter exatamente a mesma média e viver realidades completamente opostas: uma caminha em paz pela regularidade, a outra vive numa montanha-russa.",
                "author": "Lição Final de Estatística",
            },
            "sections": [
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Paradoxo das Duas Turmas de Média 7,0",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Bem-vindo ao último capítulo do nosso módulo de Estatística! Vamos começar com um enigma "
                        "clássico de sala de aula. Imagine duas turmas de quatro alunos cada uma. Na Turma A, as "
                        "notas da prova foram 7, 7, 7 e 7. A média, claro, é 7,0. Na Turma B, as notas foram "
                        "2, 2, 12 e 12 (numa prova que valia até 12) ou, pensando numa escala até 10, foram "
                        "4, 4, 10 e 10. Some 4 + 4 + 10 + 10 = 28 e divida por 4: a média da Turma B também é "
                        "exatamente 7,0! Agora olhe para as duas realidades: a Turma A é perfeitamente equilibrada, "
                        "todo mundo sabe o mesmo tanto; já a Turma B tem metade da sala com nota excelente e metade "
                        "sofrendo muito. A média sozinha foi cega para essa diferença! É para medir o quanto os "
                        "dados se espalham ou se afastam da média que existem as Medidas de Dispersão."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "O Vocabulário Secreto do ENEM: Regularidade e Homogeneidade",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Antes de fazer qualquer conta, você precisa dominar a tradução das palavras que o ENEM usa "
                        "nos enunciados. Quando uma questão pedir para escolher o jogador mais 'regular', a máquina "
                        "mais 'constante', a turma mais 'homogênea', o investimento de menor 'risco' ou a produção "
                        "mais 'estável', ela está falando diretamente de dispersão! Pense num atirador de arco e "
                        "flecha: o atirador com MENOR dispersão é aquele cujas flechas caem todas juntinhas, bem "
                        "perto umas das outras. Portanto, memorize essa equivalência de ouro: quanto MENOR a "
                        "variância ou o desvio padrão, MAIOR é a regularidade e a homogeneidade do grupo."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Amplitude: A Medida Mais Rápida (E Sua Limitação)",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "A primeira e mais simples medida de dispersão é a Amplitude Total. Para calculá-la, basta "
                        "subtrair o menor valor do maior valor do conjunto: Amplitude = Máximo - Mínimo. Veja como "
                        "isso é útil no clima: duas cidades têm temperatura média anual de 22 °C. Porém, na Cidade X, "
                        "a mínima do ano é 19 °C e a máxima é 25 °C (amplitude de 6 °C). Na Cidade Y, faz 4 °C no "
                        "inverno e 40 °C no verão (amplitude térmica de 36 °C!). A amplitude revela na hora qual "
                        "cidade tem clima mais extremo. Sua única limitação é que ela olha apenas para os dois "
                        "extremos e ignora como os valores intermediários se distribuem."
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Desvios em Relação à Média: Por Que a Soma Sempre Dá Zero?",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Para medir o espalhamento de TODOS os dados, a ideia natural seria calcular a distância de "
                        "cada elemento até a média (chamamos isso de desvio) e tirar a média dessas distâncias. "
                        "Vamos testar com os números 4, 6, 8 e 10, cuja média é 7. Os desvios são: 4 - 7 = -3; "
                        "6 - 7 = -1; 8 - 7 = +1; e 10 - 7 = +3. Quando tentamos somar esses desvios, veja o que "
                        "acontece: (-3) + (-1) + (+1) + (+3) = 0! Isso sempre acontece porque a média é o ponto de "
                        "equilíbrio. Como os sinais negativos e positivos se anulam, os matemáticos tiveram uma "
                        "ideia genial para eliminar os sinais negativos: elevar cada desvio ao quadrado!"
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Variância e Desvio Padrão: Passo a Passo Sem Trauma",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "É daí que nascem a Variância e o Desvio Padrão — nada de fórmulas assustadoras, apenas uma "
                        "receita em quatro passos lógicos. Passo 1: calcule a média aritmética do conjunto. "
                        "Passo 2: calcule os desvios (cada valor menos a média). Passo 3: eleve cada desvio ao "
                        "quadrado para tudo ficar positivo e tire a média desses quadrados — esse resultado já é a "
                        "Variância! Passo 4: como elevamos tudo ao quadrado no passo anterior (por exemplo, metros "
                        "viraram metros quadrados), tiramos a raiz quadrada da variância para voltar à unidade "
                        "original. Essa raiz quadrada da variância é o famoso Desvio Padrão!"
                    ),
                },
                {
                    "type": "callout",
                    "title": "Exemplo Resolvido na Prática: Calculando Variância e Desvio Padrão",
                    "content": (
                        "Suponha que uma fábrica testou a espessura (em mm) de três peças produzidas pela Máquina A: "
                        "9 mm, 10 mm e 11 mm.\n"
                        "• Passo 1 (Média): (9 + 10 + 11) / 3 = 30 / 3 = 10 mm.\n"
                        "• Passo 2 (Desvios): 9 - 10 = -1; 10 - 10 = 0; 11 - 10 = +1.\n"
                        "• Passo 3 (Variância = média dos quadrados dos desvios): [(-1)² + 0² + 1²] / 3 = "
                        "(1 + 0 + 1) / 3 = 2/3 ≈ 0,67 mm².\n"
                        "• Passo 4 (Desvio Padrão = raiz da variância): √(2/3) ≈ 0,82 mm.\n\n"
                        "Agora compare com a Máquina B, que produziu peças de 6 mm, 10 mm e 14 mm (também com "
                        "média 10 mm). Os desvios são -4, 0 e +4. A variância vira (16 + 0 + 16) / 3 = 32/3 ≈ 10,67, "
                        "e o desvio padrão é √(10,67) ≈ 3,27 mm. Conclusão cristalina: a Máquina A tem desvio "
                        "padrão quatro vezes menor, logo é muito mais regular e precisa!"
                    ),
                },
                {
                    "type": "heading",
                    "level": 2,
                    "content": "Como o ENEM Cobra Dispersão Sem Pedir Conta Gigante",
                },
                {
                    "type": "paragraph",
                    "content": (
                        "Aqui vai uma notícia libertadora: na maioria esmagadora das questões do ENEM, você não "
                        "precisa fazer raiz quadrada decimal na mão! A prova costuma cobrar dispersão de duas "
                        "maneiras muito inteligentes. Na primeira, ela apresenta uma tabela pronta contendo a média "
                        "e o desvio padrão de cinco opções (atletas, ações da bolsa, máquinas ou turmas) e pergunta "
                        "qual opção atende a dois critérios: atingir um desempenho mínimo e ser a mais regular. Na "
                        "segunda, ela mostra os dados brutos de conjuntos com a mesma média e pede apenas para "
                        "identificar qual tem menor desvio padrão — basta olhar qual lista tem os números mais "
                        "agrupados, bem coladinhos uns nos outros!"
                    ),
                },
                {
                    "type": "callout",
                    "title": "Pegadinha da TRI: Maior Média vs. Menor Desvio Padrão",
                    "content": (
                        "Enunciado típico: Um técnico precisa convocar um arremessador que tenha média de acertos "
                        "pelo menos igual a 80% e que seja o mais regular possível entre os classificados.\n"
                        "• Candidato 1: Média 88%, Desvio Padrão 6,2%\n"
                        "• Candidato 2: Média 82%, Desvio Padrão 1,8%\n"
                        "• Candidato 3: Média 78%, Desvio Padrão 0,9%\n\n"
                        "Cuidado com o distrator! O Candidato 3 tem o menor desvio padrão de todos (0,9%), mas foi "
                        "eliminado pelo filtro inicial porque sua média (78%) não atingiu os 80% exigidos! Entre os "
                        "classificados (Candidatos 1 e 2), o mais regular é o Candidato 2 (Desvio Padrão 1,8%). "
                        "Sempre verifique primeiro o critério de corte antes de escolher o menor desvio padrão."
                    ),
                },
                {
                    "type": "quote",
                    "content": "Média diz para onde você vai na maioria das vezes; desvio padrão diz se você vai chegar lá tranquilo ou aos trancos e barrancos.",
                    "author": "Fechamento do Módulo de Estatística",
                },
            ],
            "quiz": [],
        },
    ]
