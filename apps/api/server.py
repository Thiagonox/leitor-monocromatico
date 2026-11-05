#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor HTTP e Proxy de IA para o Leitor Monocromático.
Atende requisições de arquivos estáticos e endpoint de aprofundamento via NVIDIA NIM (z-ai/glm-5.3-flash).
Executa de forma assíncrona/multithread com fallback pedagógico de alta densidade intelectual.
"""

import http.server
import socketserver
import json
import os
import sys
import time
import urllib.request
import urllib.error
import wave
import io

try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

PORT = 8080
DIRECTORY = "/home/thiagonox/leitor-monocromatico"
DEFAULT_NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "")
DEFAULT_MODEL = "z-ai/glm-5.3-flash"
DEFAULT_BASE_URL = "https://integrate.api.nvidia.com/v1"

# Configurações de IA e Audiodescrição via OpenRouter
DEFAULT_HEYGEN_API_KEY = os.environ.get("HEYGEN_API_KEY", "")
DEFAULT_HEYGEN_MODEL = "heygen/heygen-voice-1-turbo:free"
DEFAULT_OPENROUTER_TTS_URL = "https://openrouter.ai/api/v1/audio/speech"
DEFAULT_OPENROUTER_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_TEXT_MODELS = [
    "nvidia/nemotron-3.5-lightning:free",
    "nvidia/nemotron-3.5-super-vl:free",
    "recursive/flint-v1.0:free"
]


def call_openrouter_llm(messages, max_tokens=4500, temperature=0.55, timeout_sec=18.0):
    """
    Conecta-se aos modelos gratuitos de alta velocidade na OpenRouter.
    Desativa tokens internos de reasoning para resposta direta, rápida e limpa.
    """
    last_err = None
    for model_name in OPENROUTER_TEXT_MODELS:
        try:
            payload = {
                "model": model_name,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "reasoning": {"effort": "none"}
            }
            req = urllib.request.Request(
                DEFAULT_OPENROUTER_CHAT_URL,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Authorization": f"Bearer {DEFAULT_HEYGEN_API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "http://localhost:8080",
                    "X-Title": "Leitor Monocromatico"
                }
            )
            with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                msg = data.get("choices", [{}])[0].get("message", {})
                content = (msg.get("content") or "").strip()
                if content:
                    return content, model_name, None
        except Exception as e:
            last_err = f"{model_name}: {type(e).__name__} ({str(e)[:120]})"
            print(f"[{time.strftime('%H:%M:%S')}] Tentativa com {model_name} falhou: {last_err}")
    return None, None, last_err


def pcm_to_wav(pcm_bytes, sample_rate=44100, channels=1, sample_width=2):
    """
    Converte bytes PCM lineares de 16-bit mono 44.1kHz em um arquivo de áudio WAV
    com cabeçalho RIFF padrão universal para reprodução imediata em qualquer navegador.
    """
    wav_io = io.BytesIO()
    with wave.open(wav_io, 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(pcm_bytes)
    return wav_io.getvalue()


PROMPT_STYLES = {
    "didatico": (
        "Explique de forma extremamente clara, acessível e intuitiva, usando analogias do cotidiano, "
        "metáforas visuais e linguagem simples, sem jargões desnecessários. Ajude o estudante a 'enxergar' o conceito."
    ),
    "academico": (
        "Apresente uma análise aprofundada, com rigor linguístico e conceitual, fundamentando-se em teóricos "
        "(como Mikhail Bakhtin, Ingedore Koch, Luiz Antônio Marcuschi, José Luiz Fiorin, Francisco Platão Savioli e Paul Grice). "
        "Use precisão semântica e gramatical."
    ),
    "concursos": (
        "Foque estritamente no padrão de cobrança de grandes bancas examinadoras (FGV, Cebraspe, FCC, Vunesp). "
        "Destaque pegadinhas clássicas, distratores recorrentes, palavras-chave e critérios para não cair em extrapolação ou redução."
    ),
    "mapa_mental": (
        "Estruture o conteúdo em formato de resumo esquemático, tópicos mnemônicos, listas hierárquicas e palavras-chave em negrito, "
        "focado em memorização rápida e revisão eficiente."
    ),
    "questoes": (
        "Crie 2 questões de múltipla escolha (A, B, C, D, E) inéditas e desafiadoras sobre este tópico específico, "
        "seguidas do GABARITO COMENTADO detalhando por que a correta é a certa e qual o erro de cada uma das outras alternativas."
    ),
    "socratico": (
        "Desenvolva a explicação no formato de um diálogo socrático instigante entre um mestre e um discípulo curioso, "
        "desmontando falsas certezas através de perguntas perspicazes e revelando as entrelinhas do conceito."
    )
}

class ReaderRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Habilita CORS para requisições locais e chamadas de API
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == '/api/ai/deepen':
            self.handle_deepen_request()
        elif self.path in ('/api/ai/tts', '/api/ai/audiodescricao'):
            self.handle_tts_request()
        elif self.path == '/api/ai/generate-layered':
            self.handle_generate_layered_request()
        else:
            self.send_error(404, "Endpoint não encontrado")

    def handle_tts_request(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception as e:
            self.send_json_response(400, {"status": "error", "message": f"JSON inválido: {str(e)}"})
            return

        text = req_json.get('text', '').strip()
        voice = req_json.get('voice', 'nadine').strip() or 'nadine'
        api_key = req_json.get('apiKey', '').strip() or DEFAULT_HEYGEN_API_KEY
        model = req_json.get('model', '').strip() or DEFAULT_HEYGEN_MODEL

        if not text:
            self.send_json_response(400, {"status": "error", "message": "O campo 'text' é obrigatório."})
            return

        clean_text = text[:4000]

        t0 = time.time()
        print(f"[{time.strftime('%H:%M:%S')}] Gerando audiodescrição TTS via OpenRouter ({model}, voz: {voice}, {len(clean_text)} chars)...")

        try:
            payload = {
                "model": model,
                "input": clean_text,
                "voice": voice,
                "response_format": "pcm"
            }
            req = urllib.request.Request(
                DEFAULT_OPENROUTER_TTS_URL,
                data=json.dumps(payload).encode('utf-8'),
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "http://localhost:8080",
                    "X-Title": "Leitor Monocromatico"
                }
            )
            with urllib.request.urlopen(req, timeout=25.0) as resp:
                pcm_bytes = resp.read()

            wav_bytes = pcm_to_wav(pcm_bytes, sample_rate=44100, channels=1, sample_width=2)
            elapsed = time.time() - t0
            print(f"[{time.strftime('%H:%M:%S')}] Audiodescrição HeyGen gerada com sucesso em {elapsed:.2f}s ({len(wav_bytes)} bytes WAV)!")

            self.send_response(200)
            self.send_header('Content-Type', 'audio/wav')
            self.send_header('Content-Length', str(len(wav_bytes)))
            self.send_header('X-Voice', voice)
            self.send_header('X-Model', model)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(wav_bytes)

        except urllib.error.HTTPError as e:
            err_body = e.read().decode('utf-8', errors='replace')
            print(f"[{time.strftime('%H:%M:%S')}] Erro HTTP OpenRouter TTS ({e.code}): {err_body}")
            self.send_json_response(e.code, {"status": "error", "message": f"Erro do provedor TTS ({e.code}): {err_body}"})
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] Erro ao gerar TTS: {str(e)}")
            self.send_json_response(500, {"status": "error", "message": f"Erro interno TTS: {str(e)}"})

    def handle_deepen_request(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception as e:
            self.send_json_response(400, {"status": "error", "message": f"JSON inválido: {str(e)}"})
            return

        topic = req_json.get('topic', '').strip()
        context = req_json.get('context', '').strip()
        style = req_json.get('style', 'didatico')
        level = int(req_json.get('level', 1))
        history = req_json.get('history', [])
        user_api_key = req_json.get('apiKey', '').strip() or DEFAULT_NVIDIA_API_KEY
        user_model = req_json.get('model', '').strip() or DEFAULT_MODEL
        user_base_url = req_json.get('baseUrl', '').strip() or DEFAULT_BASE_URL

        if not topic:
            self.send_json_response(400, {"status": "error", "message": "O campo 'topic' é obrigatório."})
            return

        style_instruction = PROMPT_STYLES.get(style, PROMPT_STYLES["didatico"])

        system_prompt = (
            "Você é um tutor acadêmico e especialista em Língua Portuguesa e Linguística do Leitor Monocromático. "
            "Sua missão é aprofundar tópicos de estudo de forma viva, estimulante, didática e estruturada. "
            f"\n\nInstrução de estilo selecionada pelo usuário:\n{style_instruction}\n\n"
            "Diretrizes obrigatórias de formatação:\n"
            "1. Use Markdown limpo (títulos com ## e ###, negrito, listas e citações em > quando relevante).\n"
            "2. Não economize na qualidade analítica; seja denso e pedagógico.\n"
            f"3. Este é o Nível de Aprofundamento {level} da trilha de estudo do usuário.\n"
            "4. AO FINAL da sua resposta, adicione OBRIGATORIAMENTE uma seção com o título exato: "
            "'### ✦ Subtópicos para Continuar Aprofundando'\n"
            "Contendo 3 sugestões de sub-temas em lista, cada um entre colchetes no formato: "
            "`- [[Nome do Subtópico]] — breve frase sobre o que será explorado`. "
            "Esses colchetes serão convertidos em botões clicáveis para o estudante continuar aprofundando indefinidamente!"
        )

        user_content = f"TÓPICO PARA APROFUNDAMENTO (Nível {level}):\n{topic}\n\n"
        if context:
            user_content += f"CONTEXTO DO TEXTO ORIGINAL:\n\"{context}\"\n\n"
        if history and len(history) > 0:
            user_content += f"TRILHA ANTERIOR DE APROFUNDAMENTOS:\n{' > '.join(history)}\n\n"
        user_content += "Por favor, elabore a explicação aprofundada conforme o estilo e as diretrizes solicitadas."

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]

        t0 = time.time()
        print(f"[{time.strftime('%H:%M:%S')}] Requisição de IA para '{topic}' [{style}, Nível {level}]...")

        content, used_model, error_msg = call_openrouter_llm(messages, max_tokens=2200, temperature=0.6, timeout_sec=15.0)
        if content:
            print(f"[{time.strftime('%H:%M:%S')}] Concluído com sucesso pela IA ({used_model}) em {time.time()-t0:.2f}s!")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] Fallback local ativado ({error_msg}).")
            content = generate_pedagogical_fallback(topic, context, style, level)
            used_model = "Núcleo Didático Monocromático"

        self.send_json_response(200, {
            "status": "ok",
            "content": content,
            "topic": topic,
            "style": style,
            "level": level,
            "model": used_model,
            "elapsed": round(time.time() - t0, 2),
            "usedFallback": bool(error_msg),
            "notice": f"Conectado ao modelo {used_model}" if not error_msg else f"Formulado pelo Núcleo de Estudos Monocromático (estilo: {style})."
        })

    def send_json_response(self, code, data):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def handle_generate_layered_request(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            req_json = json.loads(post_data.decode('utf-8'))
        except Exception as e:
            self.send_json_response(400, {"status": "error", "message": f"JSON inválido: {str(e)}"})
            return

        topic = req_json.get('topic', '').strip()
        depth = req_json.get('depth', 'enem_elite')
        chapters_count = int(req_json.get('chaptersCount', 3))

        if not topic:
            self.send_json_response(400, {"status": "error", "message": "O campo 'topic' é obrigatório."})
            return

        clean_topic = topic.replace("[[", "").replace("]]", "").strip()
        lower_topic = clean_topic.lower()

        # Se for o tema prioritário de redação / dissertativo / enem, entrega imediatamente o master oficial de alta densidade
        if any(k in lower_topic for k in ["redação", "redacao", "dissertativo", "enem", "competências", "competencias", "repertório", "repertorio"]):
            master_file = os.path.join(DIRECTORY, "data", "redacao-enem.json")
            if os.path.exists(master_file):
                try:
                    with open(master_file, "r", encoding="utf-8") as f:
                        master_doc = json.load(f)
                    print(f"[{time.strftime('%H:%M:%S')}] Entregando Acervo Mestre Oficial de Redação ENEM ({len(master_doc.get('chapters', []))} capítulos)...")
                    self.send_json_response(200, {
                        "status": "ok",
                        "model": "Manual Vivo Oficial (Redação ENEM Nota 1000)",
                        "book": master_doc,
                        "usedFallback": False
                    })
                    return
                except Exception as e:
                    print(f"Erro ao ler data/redacao-enem.json: {e}")

        t0 = time.time()
        print(f"[{time.strftime('%H:%M:%S')}] Gerando Obra em Camadas para '{clean_topic[:80]}' ({chapters_count} caps, profundidade: {depth})...")

        book_data = None
        used_model = None
        error_msg = None

        system_prompt = (
            "Você é um professor e autor didático de excelência (no mesmo estilo claro, fluido e direto do 'Manual Vivo de Interpretação'). "
            "Sua missão é gerar um livro de estudo completo, bem feito e FÁCIL DE DIGERIR para o leitor padrão, "
            "usando EXCLUSIVAMENTE estas duas estratégias pedagógicas modernas:\n"
            "1. LEITURA EM CAMADAS (Layered Reading):\n"
            "   - Capítulo I: Camada 1 — Resumo Rápido: Panorama direto, simples e cristalino de todo o tema para reduzir a resistência inicial.\n"
            "   - Capítulo II: Camada 2 — Versão Intermediária com PROGRESSIVE DISCLOSURE.\n"
            "   - Capítulo III (e seguintes): Camada 3 — Texto Completo e Aprofundado: Explicação completa, conversada, detalhada e fluida de todos os pontos pedidos pelo usuário.\n"
            "2. PROGRESSIVE DISCLOSURE (Revelação Progressiva):\n"
            "   - Em vez de blocos pesados ou jargão acadêmico artificial, revele cada subtópico em pequenas partes fáceis de digerir seguindo SEMPRE a sequência:\n"
            "     • O Conceito (o que é, de forma simples e direta)\n"
            "     • O Exemplo (um caso concreto ou modelo prático real)\n"
            "     • A Aplicação (como usar na prática, na redação ou na prova)\n"
            "     • Depois o próximo conceito.\n"
            "REGRAS CRÍTICAS DE ESTILO:\n"
            "- NUNCA inclua indicações de tempo ou contagem de minutos em títulos, subtítulos ou capítulos (ex: NUNCA escreva '(2 a 5 min)', '(10 a 15 min)', '2 min (Resumo)', etc.). Use títulos limpos, elegantes e didáticos.\n"
            "- PROIBIDO usar títulos rebuscados vazios como 'Gênese, Premissas Epistemológicas'. Escreva com clareza, profundidade real e didática impecável.\n"
            "Responda APENAS com um objeto JSON válido, sem markdown antes ou depois."
        )

        user_prompt = (
            f"Gere uma obra completa em JSON sobre o tema/pauta abaixo:\n\n{clean_topic}\n\n"
            "Use exatamente esta estrutura JSON (NUNCA inclua contagem de minutos em títulos ou subtítulos):\n"
            "{\n"
            '  "title": "Título Claro, Direto e Didático da Obra",\n'
            '  "subtitle": "Guia Prático em Camadas & Progressive Disclosure",\n'
            '  "category": "Área do Conhecimento",\n'
            '  "description": "Resumo claro de 2 frases sobre o que o leitor vai aprender.",\n'
            '  "chapters": [\n'
            "    {\n"
            '      "number": "I",\n'
            '      "title": "Camada 1 — Resumo Rápido: Visão Geral Direta",\n'
            '      "epigraph": {"text": "Frase síntese inspiradora e clara sobre o tema.", "author": "Autor ou Referência"},\n'
            '      "sections": [\n'
            '        {"type": "heading", "level": 3, "content": "1. O Panorama Essencial"},\n'
            '        {"type": "paragraph", "content": "Explicação curta, clara e direta..."},\n'
            '        {"type": "callout", "title": "Ideia Central", "content": "Resumo prático fácil de guardar..."}\n'
            "      ]\n"
            "    },\n"
            "    {\n"
            '      "number": "II",\n'
            '      "title": "Camada 2 — Versão Intermediária: Conceito, Exemplo e Aplicação",\n'
            '      "epigraph": {"text": "Dividir para compreender sem esforço.", "author": "Progressive Disclosure"},\n'
            '      "sections": [\n'
            '        {"type": "heading", "level": 3, "content": "Bloco 1: [Nome do 1º Tópico]"},\n'
            '        {"type": "paragraph", "content": "O CONCEITO: explicação direta. O EXEMPLO: caso concreto. A APLICAÇÃO: como usar na prática."},\n'
            '        {"type": "callout", "title": "Aplicação Prática", "content": "Passo a passo direto..."}\n'
            "      ]\n"
            "    },\n"
            "    {\n"
            '      "number": "III",\n'
            '      "title": "Camada 3 — Texto Completo: Domínio Aprofundado Passo a Passo",\n'
            '      "epigraph": {"text": "Depois da base construída, a leitura profunda flui naturalmente.", "author": "Leitura em Camadas"},\n'
            '      "sections": [\n'
            '        {"type": "heading", "level": 3, "content": "1. Aprofundamento Completo"},\n'
            '        {"type": "paragraph", "content": "Desenvolvimento completo, claro, conversado e detalhado de todos os pontos..."}\n'
            "      ]\n"
            "    }\n"
            "  ]\n"
            "}"
        )

        raw_response, used_model, error_msg = call_openrouter_llm(
            [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=5500,
            temperature=0.5,
            timeout_sec=20.0
        )

        if raw_response:
            try:
                cleaned = raw_response.strip()
                if cleaned.startswith("```"):
                    cleaned = cleaned.split("\n", 1)[1]
                    if "```" in cleaned:
                        cleaned = cleaned.rsplit("```", 1)[0]
                start_idx = cleaned.find("{")
                end_idx = cleaned.rfind("}")
                if start_idx != -1 and end_idx != -1:
                    cleaned = cleaned[start_idx:end_idx + 1]
                parsed = json.loads(cleaned)
                if isinstance(parsed.get("chapters"), list) and len(parsed["chapters"]) >= 2:
                    book_data = parsed
                    print(f"[{time.strftime('%H:%M:%S')}] Obra gerada com sucesso via OpenRouter ({used_model}) em {time.time()-t0:.2f}s!")
            except Exception as e:
                error_msg = f"JSON parse error: {str(e)}"
                print(f"[{time.strftime('%H:%M:%S')}] Falha ao validar JSON da IA ({error_msg}). Usando gerador estruturado em camadas.")

        if not book_data:
            book_data = generate_layered_fallback_payload(topic, depth, chapters_count)
            used_model = "Motor Editorial em Camadas"

        book_id = f"obra-{int(time.time())}"
        chapters = []
        roman = ["I", "II", "III", "IV", "V", "VI"]

        for i, ch in enumerate(book_data.get('chapters', [])):
            ch_num = ch.get('number', roman[i] if i < len(roman) else str(i + 1))
            ch_id = f"capitulo-{i + 1}"
            chapters.append({
                "id": ch_id,
                "number": ch_num,
                "title": ch.get('title', f'Capítulo {ch_num}'),
                "epigraph": ch.get('epigraph', {"text": "Do resumo rápido ao texto completo, um conceito por vez.", "author": "Leitura em Camadas"}),
                "sections": ch.get('sections', [])
            })

        formatted_book = {
            "meta": {
                "id": book_id,
                "title": book_data.get('title', "Manual de Estudo em Camadas"),
                "subtitle": book_data.get('subtitle', "Leitura em Camadas & Progressive Disclosure"),
                "author": "Manual Vivo · Leitura em Camadas",
                "date": "Edição Didática Progressiva",
                "category": book_data.get('category', "Leitura em Camadas & Progressive Disclosure"),
                "chaptersCount": len(chapters),
                "estimatedReadingTime": book_data.get('estimatedReadingTime', f"Aprox. {len(chapters) * 8} min de leitura"),
                "description": book_data.get('description', "Conteúdo estruturado em camadas progressivas para assimilação natural e profunda."),
                "isGeneratedByAI": True,
                "createdAt": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            },
            "settings": {"defaultFont": "serif", "defaultTheme": "eink", "defaultWidth": "680px"},
            "chapters": chapters,
            "quiz": book_data.get("quiz", [])
        }

        self.send_json_response(200, {
            "status": "ok",
            "book": formatted_book,
            "layeredData": [],
            "model": used_model,
            "usedFallback": book_data.get("_isFallback", False),
            "elapsed": round(time.time() - t0, 2)
        })


def generate_pedagogical_fallback(topic, context, style, level):
    """
    Gera síntese pedagógica especializada de altíssimo nível para cada um dos 6 estilos de estudo,
    garantindo que o usuário tenha resposta imediata, sem telas travadas ou mensagens de erro.
    """
    clean_topic = topic.replace("[[", "").replace("]]", "").strip()

    if style == "didatico":
        return (
            f"## Compreendendo {clean_topic} com Clareza Total\n\n"
            f"*(Aprofundamento • Nível {level} • Abordagem Didática e Acessível)*\n\n"
            f"### 1. A Grande Metáfora: Como Enxergar Este Conceito\n"
            f"Imagine a leitura de um texto como a observação de um iceberg ou de uma pintura a óleo. "
            f"Na superfície, temos as palavras impressas no papel (o que está dito explicitamente). "
            f"Mas por trás de **{clean_topic}**, existe toda uma engrenagem que conecta o que o autor escreveu "
            f"àquilo que ele esperava que você já soubesse.\n\n"
            f"> **Regra de Ouro:** Ler não é engolir letras passivamente; ler é participar de um jogo de pistas onde "
            f"**{clean_topic}** funciona como a lente que ajusta o foco do leitor.\n\n"
            f"### 2. O Erro Mais Comum de Quem Lê com Pressa\n"
            f"A maioria das pessoas falha ao interpretar passagens envolvendo {clean_topic} porque confunde "
            f"**opinião pessoal do leitor** com **tese sustentada pelo texto**. O bom intérprete é como um detetive: "
            f"não inventa suspeitos por intuição, só aponta o que tem prova material nas entrelinhas.\n\n"
            f"### 3. Exemplo Prático de Aplicação\n"
            f"Considere a diferença entre simplesmente notar a presença de um termo e entender a sua força discursiva: "
            f"quando o autor escolhe falar em *'persistência'* em vez de *'teimosia'*, ou quando estrutura uma oração "
            f"para criar suspense, ele está operando as regras de {clean_topic}.\n\n"
            f"### ✦ Subtópicos para Continuar Aprofundando\n"
            f"- [[Aplicações Práticas em Textos Jornalísticos]] — Como {clean_topic} aparece em editoriais e artigos de opinião.\n"
            f"- [[Pistas Formais e Marcas Textuais]] — Os elementos gramaticais concretos que revelam {clean_topic}.\n"
            f"- [[Diferença Entre Sentido Literal e Figurativo]] — A fronteira sutil entre o dito e o sugerido."
        )

    elif style == "academico":
        return (
            f"## Tratado Teórico: {clean_topic}\n\n"
            f"*(Nível Epistemológico {level} • Linguística Textual e Análise do Discurso)*\n\n"
            f"### 1. Enquadramento Teórico Seminal\n"
            f"Na tradição dos estudos linguísticos contemporâneos — notadamente em **Ingedore Koch**, **Luiz Antônio Marcuschi** "
            f"e **José Luiz Fiorin** —, o fenômeno de **{clean_topic}** não pode ser reduzido a um mero artifício estilístico. "
            f"Trata-se de uma propriedade constitutiva da textualidade e da interação verbal.\n\n"
            f"Conforme preconizou **Mikhail Bakhtin**, todo enunciado é dialógico e povoado pelas vozes de outrem. "
            f"Em **{clean_topic}**, a polifonia se manifesta no choque de pontos de vista e nas condições de produção do discurso.\n\n"
            f"### 2. Mecanismos de Articulação Semântica\n"
            f"- **Operações de Co-enunciação:** A construção do sentido exige a partilha de conhecimentos enciclopédicos.\n"
            f"- **Princípio da Relevância e Máximas Conversacionais:** Sob a ótica de Paul Grice, a interpretação eficiente "
            f"depende do reconhecimento da cooperação comunicativa e da quebra intencional das máximas de modo e quantidade.\n"
            f"- **Cadeia Anafórica e Coesão:** Como {clean_topic} afeta a progressão tópica e a continuidade referencial.\n\n"
            f"### 3. Síntese Epistemológica\n"
            f"> *\"O texto não é um produto acabado e autônomo, mas uma partitura cuja execução depende da cooperação ativa do leitor.\"* — Koch & Elias\n\n"
            f"### ✦ Subtópicos para Continuar Aprofundando\n"
            f"- [[A Teoria dos Atos de Fala em Austin e Searle]] — Força ilocucionária e efeitos de sentido em {clean_topic}.\n"
            f"- [[Polifonia Discursiva e Heterogeneidade Mostrada]] — A coexistência de múltiplas vozes no mesmo enunciado.\n"
            f"- [[Argumentação na Língua segundo Anscombre e Ducrot]] — Os conectores argumentativos como direcionadores de conclusão."
        )

    elif style == "concursos":
        return (
            f"## Padrão de Cobrança em Concursos: {clean_topic}\n\n"
            f"*(Foco de Alto Rendimento • Nível {level} • FGV, Cebraspe, FCC, Vunesp)*\n\n"
            f"### 1. O Raio-X das Bancas Examinadoras\n"
            f"Em provas de alto nível, itens sobre **{clean_topic}** costumam responder por 25% a 35% das questões de Língua Portuguesa. "
            f"A banca não cobra definições decoradas; ela testa sua capacidade de **rastrear a pista no texto sem extrapolar**.\n\n"
            f"### 2. A Tríade Mortal de Distratores (Como as Bancas Fabricam as Erradas)\n"
            f"1. **Extrapolação:** A alternativa traz uma afirmação verdadeira no mundo real, mas que NÃO tem amparo no texto sob análise.\n"
            f"2. **Redução:** A alternativa pega um detalhe secundário de um único parágrafo e o eleva a tese central de todo o artigo.\n"
            f"3. **Inversão de Causa e Efeito:** A banca inverte a relação lógica indicada pelos conectivos de {clean_topic}.\n\n"
            f"### 3. Macete Mnemônico de Prova\n"
            f"> **Regra do Dedo no Texto:** Para marcar a alternativa correta em questões de {clean_topic}, você precisa ser capaz "
            f"de colocar o dedo físico na linha do texto que comprova rigorosamente a assertiva. Se depender de 'eu acho que o autor quis dizer', é distrator!\n\n"
            f"### ✦ Subtópicos para Continuar Aprofundando\n"
            f"- [[Distratores Clássicos da FGV em Interpretação]] — Como identificar o padrão sofisticado da Fundação Getulio Vargas.\n"
            f"- [[Itens Certo ou Errado do Cebraspe]] — Análise de pressuposição e reescritura com manutenção de sentido.\n"
            f"- [[Guia de Sobrevivência a Textos Longos]] — Técnicas de escaneamento e identificação da tese no primeiro minuto."
        )

    elif style == "mapa_mental":
        return (
            f"## Mapa Mental & Esquema de Revisão: {clean_topic}\n\n"
            f"*(Nível {level} • Estrutura Sintética de Rápida Memorização)*\n\n"
            f"```\n"
            f"┌────────────────────────────────────────────────────────┐\n"
            f"│                 ✦ {clean_topic.upper()} ✦              │\n"
            f"└──────────────┬──────────────────────────┬──────────────┘\n"
            f"               │                          │\n"
            f"        [ DEFINIÇÃO ]              [ MECANISMO ]\n"
            f"        • Sentido partilhado       • Pistas do texto\n"
            f"        • Além da superfície       • Contexto situacional\n"
            f"               │                          │\n"
            f"        [ ARMADILHA ]              [ REGRA DE OURO ]\n"
            f"        • Extrapolação mental      • Comprovação formal\n"
            f"        • Leitura apressada        • Fidelidade ao autor\n"
            f"```\n\n"
            f"### 1. Núcleos Essenciais\n"
            f"- **O que É:** Processamento inferencial e relacional sobre {clean_topic}.\n"
            f"- **O que NÃO É:** Adivinhação mágica ou subjetivismo sem limites.\n"
            f"- **Gatilho de Memória (Mnemonia):** *P-A-R-T* (Pistas $\\rightarrow$ Análise $\\rightarrow$ Relação $\\rightarrow$ Tese).\n\n"
            f"### 2. Checklist Rápido de 30 Segundos\n"
            f"- [x] Localizei o sujeito e o predicador central?\n"
            f"- [x] Verifiquei se há conjunções adversativas mudando o rumo do argumento?\n"
            f"- [x] Diferenciei fato objetivo de julgamento de valor do articulista?\n\n"
            f"### ✦ Subtópicos para Continuar Aprofundando\n"
            f"- [[Fluxograma de Resolução Rápida]] — Algoritmo passo a passo para destrinchar parágrafos complexos.\n"
            f"- [[Quadro Comparativo de Conceitos Próximos]] — Diferenciando termos parecidos que confundem o leitor.\n"
            f"- [[Fichamento Mnemônico Completo]] — Tabela esquemática com todas as variáveis deste assunto."
        )

    elif style == "questoes":
        return (
            f"## Questões Desafiadoras com Gabarito Comentado: {clean_topic}\n\n"
            f"*(Simulado Prático • Nível {level} • Padrão Prova Difícil)*\n\n"
            f"---\n\n"
            f"### Questão 01 (Inédita — Raciocínio Analítico)\n"
            f"Considere o fragmento hipotético a seguir:\n"
            f"> *\"Ele não hesitou em classificar o projeto como 'audacioso', embora os números preliminares ainda dormissem sob o manto do sigilo burocrático.\"*\n\n"
            f"Em relação aos mecanismos de **{clean_topic}** e à construção dos sentidos do texto, é correto afirmar:\n\n"
            f"- (A) O emprego de aspas na palavra *'audacioso'* possui função meramente decorativa, sem alterar a conotação do adjetivo.\n"
            f"- (B) A oração subordinada introduzida por *'embora'* instaura uma concessão que ironiza a certeza manifestada na oração principal.\n"
            f"- (C) O texto atesta de forma incontestável que o projeto era financeiramente inviável.\n"
            f"- (D) O adjetivo *'audacioso'* foi empregado em sentido puramente denotativo e laudatório.\n"
            f"- (E) O narrador concorda expressamente com a classificação positiva conferida ao projeto.\n\n"
            f"**GABARITO COMENTADO DA QUESTÃO 01:**\n"
            f"- **Alternativa Correta: (B)**. O conectivo 'embora' estabelece quebra de expectativa concessiva, e o contraste entre 'classificar como audacioso' e o fato de os números estarem 'em sigilo' revela uma crítica ou ironia subjacente.\n"
            f"- **Distratores:** (A) Errada: aspas em adjetivos frequentemente demarcam distanciamento irônico. (C) Errada: extrapolação, o texto não diz que é inviável, apenas que os dados eram sigilosos. (D) Errada: não é puramente denotativo. (E) Errada: o narrador mantém postura crítica distante.\n\n"
            f"---\n\n"
            f"### Questão 02 (Interpretação e Inferência)\n"
            f"Quando um autor articula o tópico de **{clean_topic}**, a identificação do pressuposto textual exige:\n\n"
            f"- (A) Conhecimento exclusivo de dados biográficos do autor do texto.\n"
            f"- (B) Reconhecimento de pistas gramaticais e marcas lexicais que tornam a informação indiscutível para o leitor.\n"
            f"- (C) Aceitação cega da tese defendida sem questionar seus argumentos.\n"
            f"- (D) Eliminação de todos os conectivos para facilitar a leitura linear.\n"
            f"- (E) Suposição livre baseada nas experiências individuais de quem lê.\n\n"
            f"**GABARITO COMENTADO DA QUESTÃO 02:**\n"
            f"- **Alternativa Correta: (B)**. Pressupostos linguísticos apoiam-se rigorosamente em marcas formais explícitas (verbos que indicam mudança de estado, advérbios temporais, orações adjetivas explicativas).\n"
            f"- **Distratores:** (A), (C), (D) e (E) incorrem em concepções errôneas ou absurdas sobre leitura analítica.\n\n"
            f"### ✦ Subtópicos para Continuar Aprofundando\n"
            f"- [[Bateria Complementar de 5 Questões FGV]] — Exercícios práticos com textos de enunciados longos.\n"
            f"- [[Análise de Recursos e Itens Anulados]] — Onde as bancas costumam errar na formulação de gabaritos.\n"
            f"- [[Método de Resolução por Eliminação Ativa]] — Como garantir 100% de acerto nas alternativas restantes."
        )

    else: # socratico
        return (
            f"## Diálogo Socrático: As Entrelinhas de {clean_topic}\n\n"
            f"*(Investigação Dialética • Nível {level} • Filosofia da Linguagem)*\n\n"
            f"**Personagens:** *Sócrates* (o mestre questionador) e *Teeteto* (o estudante perspicaz).\n\n"
            f"---\n\n"
            f"**Sócrates:** Diga-me, meu jovem Teeteto: quando você lê uma frase e diz 'eu entendi o que o autor quis dizer', "
            f"onde exatamente reside esse entendimento? Nas letras pintadas sobre o papel, ou na sua própria mente?\n\n"
            f"**Teeteto:** Ora, Sócrates, creio que esteja nas palavras! Se eu abrir um livro e ler as palavras em grego ou em português, "
            f"o sentido está lá, empilhado nas linhas.\n\n"
            f"**Sócrates:** Curioso. Se estivesse nas palavras como a água está em uma ânfora, por que dois homens sensatos, lendo exatamente "
            f"o mesmo parágrafo acerca de **{clean_topic}**, retiram dele conclusões diametralmente opostas?\n\n"
            f"**Teeteto:** Talvez porque um deles seja tolo, Sócrates?\n\n"
            f"**Sócrates:** *(sorrindo)* Ou talvez porque ler não seja recolher pedras no chão, mas decifrar um enigma onde o autor deixou pegadas intencionais. "
            f"Se você ignora essas pegadas — a ironia, a pressuposição, os conectivos —, você não lê o texto; lê apenas a si mesmo refletido na página!\n\n"
            f"**Teeteto:** Então, para verdadeiramente dominar **{clean_topic}**, preciso calar meus próprios preconceitos e rastrear o pacto que o autor propôs?\n\n"
            f"**Sócrates:** Você tocou no coração da questão. Examinemos agora como as palavras disfarçam as intenções...\n\n"
            f"### ✦ Subtópicos para Continuar Aprofundando\n"
            f"- [[O Paradoxo da Intencionalidade do Autor]] — O autor ainda é dono do sentido após publicar sua obra?\n"
            f"- [[A Ironia Como Desmascaramento da Verdade]] — Quando dizer o oposto é a única forma de dizer o real.\n"
            f"- [[A Linguagem Como Jogo em Ludwig Wittgenstein]] — As regras tácitas que regem a comunicação humana."
        )


def generate_layered_fallback_payload(topic, depth="enem_elite", chapters_count=3):
    """
    Gera um livro claro, fluido e fácil de digerir para o leitor padrão (#view-reader),
    estruturado estritamente em:
    1. Leitura em Camadas (Resumo 2-5 min -> Intermediário 10-15 min -> Texto Completo)
    2. Progressive Disclosure (Conceito -> Exemplo -> Aplicação -> Próximo Conceito)
    """
    clean_topic = topic.replace("[[", "").replace("]]", "").strip()
    lower_topic = clean_topic.lower()

    if any(k in lower_topic for k in ["redação", "redacao", "dissertativo", "competências", "competencias", "repertório", "repertorio"]):
        master_file = os.path.join(DIRECTORY, "data", "redacao-enem.json")
        if os.path.exists(master_file):
            try:
                with open(master_file, "r", encoding="utf-8") as f:
                    master_doc = json.load(f)
                    master_doc["_isFallback"] = False
                    return master_doc
            except Exception as e:
                print(f"Erro ao ler master de redação no fallback: {e}")

    # Caso o usuário tenha enviado uma lista de tópicos ou um tema qualquer:
    raw_lines = [ln.strip(" -•*\t") for ln in clean_topic.splitlines() if ln.strip(" -•*\t")]
    main_title = raw_lines[0] if raw_lines else clean_topic[:70]
    sub_items = [ln for ln in raw_lines[1:] if len(ln) > 2][:10]
    if not sub_items:
        sub_items = [
            f"Conceito essencial e definição clara de {main_title}",
            f"Como {main_title} funciona na prática e causas principais",
            f"Exemplos concretos e aplicações reais de {main_title}",
            f"Como esse tema é cobrado em provas, redações e no dia a dia"
        ]

    progressive_sections = []
    for idx, item in enumerate(sub_items, 1):
        progressive_sections.extend([
            {"type": "heading", "level": 3, "content": f"Bloco {idx}: {item}"},
            {
                "type": "paragraph",
                "content": (
                    f"• O CONCEITO: {item} representa um dos pontos-chave para compreender {main_title} sem confusão. "
                    f"Em linguagem simples, trata-se de identificar a regra central que explica por que esse fenômeno acontece.\n"
                    f"• O EXEMPLO: Na prática cotidiana, você enxerga {item} sempre que observa a diferença entre uma explicação superficial "
                    f"e uma análise baseada em fatos, causas e consequências reais.\n"
                    f"• A APLICAÇÃO: Ao estudar ou resolver questões sobre {item}, pergunte sempre: qual é a causa principal, "
                    f"qual é o efeito concreto e como usar esse argumento com clareza."
                )
            }
        ])

    deep_sections = []
    for idx, item in enumerate(sub_items, 1):
        deep_sections.extend([
            {"type": "heading", "level": 3, "content": f"{idx}. Aprofundamento Completo: {item}"},
            {
                "type": "paragraph",
                "content": (
                    f"Agora que você já conhece o resumo geral e os blocos de conceito, exemplo e aplicação, vamos aprofundar {item}. "
                    f"Dentro do estudo de {main_title}, este ponto conecta a teoria à realidade prática: compreender suas causas "
                    f"permite evitar memorizações mecânicas e construir um raciocínio sólido, fluido e seguro."
                )
            }
        ])

    return {
        "_isFallback": True,
        "title": f"Guia Claro e Progressivo: {main_title[:65]}",
        "subtitle": "Guia Prático em Camadas & Progressive Disclosure",
        "category": "Leitura em Camadas & Progressive Disclosure",
        "description": f"Estudo estruturado em camadas progressivas sobre {main_title}, revelando cada tópico em pequenas partes (Conceito, Exemplo e Aplicação) até o texto completo.",
        "chapters": [
            {
                "number": "I",
                "title": "Camada 1 — Resumo Rápido: Visão Geral Direta",
                "epigraph": {
                    "text": "Comece pelo mapa simples: entender o todo sem pressa elimina a resistência inicial da leitura.",
                    "author": "Leitura em Camadas (Layered Reading)"
                },
                "sections": [
                    {"type": "heading", "level": 3, "content": f"1. O Que Você Precisa Saber de Imediato sobre {main_title}"},
                    {
                        "type": "paragraph",
                        "content": (
                            f"Esta primeira camada oferece a visão panorâmica essencial "
                            f"de {main_title} antes de entrarmos nos detalhes. Em vez de encarar um texto denso de uma vez, "
                            f"veja os pontos essenciais que formam a espinha dorsal deste tema:"
                        )
                    },
                    {
                        "type": "callout",
                        "title": "Roteiro Rápido dos Pontos Principais",
                        "content": "\n".join([f"• {it}" for it in sub_items])
                    }
                ]
            },
            {
                "number": "II",
                "title": "Camada 2 — Versão Intermediária: Conceito, Exemplo e Aplicação",
                "epigraph": {
                    "text": "Um conceito. Um exemplo. Uma aplicação. Depois o próximo conceito.",
                    "author": "Progressive Disclosure"
                },
                "sections": progressive_sections
            },
            {
                "number": "III",
                "title": "Camada 3 — Texto Completo: Domínio Aprofundado e Integrado",
                "epigraph": {
                    "text": "Com a base construída em blocos curtos, o texto completo torna-se leve, claro e natural.",
                    "author": "Leitura Profunda"
                },
                "sections": deep_sections
            }
        ]
    }


class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def run_server():
    server = ThreadedHTTPServer(("", PORT), ReaderRequestHandler)
    print(f"Servidor Multithread do Leitor Monocromático rodando em http://localhost:{PORT}")
    print("API de IA ativa em /api/ai/deepen (NVIDIA NIM z-ai/glm-5.3-flash com failover ativo)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nEncerrando servidor...")
        server.server_close()


if __name__ == '__main__':
    run_server()
