# -*- coding: utf-8 -*-
"""Montador do Livro 'Revisão Turbo ENEM: Linguagens em Flashcards & Gatilhos de Prova'"""

import json
import os
import sys

# Importa os módulos com os capítulos
sys.path.insert(0, os.path.dirname(__file__))
import mod1_interpretacao
import mod2_generos
import mod3_gramatica
import mod4_literatura
import mod5_artes_corpo
import mod6_linguas

all_raw_chapters = (
    mod1_interpretacao.get_chapters() +
    mod2_generos.get_chapters() +
    mod3_gramatica.get_chapters() +
    mod4_literatura.get_chapters() +
    mod5_artes_corpo.get_chapters() +
    mod6_linguas.get_chapters()
)

print(f"Total de capítulos brutos carregados: {len(all_raw_chapters)}")

formatted_chapters = []
for idx, ch in enumerate(all_raw_chapters):
    cap_id = f"cap-{idx + 1:02d}"
    formatted_chapters.append({
        "id": cap_id,
        "number": ch["number"],
        "title": ch["title"],
        "epigraph": ch.get("epigraph"),
        "sections": ch["sections"]
    })

BOOK = {
    "meta": {
        "id": "revisao-turbo-linguagens-enem",
        "title": "Revisão Turbo ENEM: Linguagens em Flashcards & Gatilhos de Prova",
        "subtitle": "O Raio-X Mais Rápido e Focado do Edital: 31 Estações de Alta Retenção, Pegadinhas da Banca e Resumos de Bolso",
        "author": "Prof. Antigravity & Revisão Estratégica ENEM",
        "date": "2026",
        "language": "pt-BR",
        "category": "Revisão Turbo · Tiro Curto & Alta Retenção",
        "chaptersCount": len(formatted_chapters),
        "estimatedReadingTime": "Aprox. 70 min de revisão acelerada (31 Estações Flash)",
        "description": "A revisão definitiva de alta velocidade para Linguagens, Códigos e suas Tecnologias no ENEM. Estruturada em 31 estações de tiro curto organizadas do maior peso na TRI para o menor: cada capítulo traz o Raio-X em 30 segundos, como o INEP cobra a questão no enunciado, o distrator fatal que elimina candidatos desatentos, um exemplo relâmpago resolvido e o flashcard mental de bolso para memorização imediata. Cobre toda a interpretação, gêneros, gramática aplicada ao sentido, linha do tempo literária, autores canônicos, artes, línguas estrangeiras (inglês/espanhol) e cultura corporal.",
        "isPriority": True,
        "createdAt": "2026-11-07T23:20:00Z",
        "style": "editorial-flashcard-turbo"
    },
    "settings": {
        "defaultFont": "serif",
        "defaultTheme": "eink",
        "fontSize": 20
    },
    "chapters": formatted_chapters
}

# Salva nos dois destinos do projeto
dest1 = "data/revisao-turbo-linguagens-enem.json"
dest2 = "apps/web/public/data/revisao-turbo-linguagens-enem.json"

for dest in [dest1, dest2]:
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(BOOK, f, ensure_ascii=False, indent=2)
    print(f"Arquivo gerado com sucesso em: {dest} ({len(formatted_chapters)} capítulos)")

# Estatísticas
total_words = 0
total_sections = 0
for ch in formatted_chapters:
    total_sections += len(ch["sections"])
    for sec in ch["sections"]:
        text = sec.get("content") or ""
        total_words += len(text.split())

print(f"Estatísticas da Obra:")
print(f" - Total de Capítulos/Estações: {len(formatted_chapters)}")
print(f" - Total de Seções: {total_sections}")
print(f" - Total de Palavras: {total_words}")
print(f" - Média de palavras por capítulo: {total_words / len(formatted_chapters):.1f}")
