# -*- coding: utf-8 -*-
"""
Gerador da Obra 'Revisão Turbo ENEM: Linguagens em Flashcards & Gatilhos de Prova'
Cobre 100% dos tópicos do edital em formato rápido, focado e de alta retenção.
"""

import json
import os

BOOK = {
    "meta": {
        "id": "revisao-turbo-linguagens-enem",
        "title": "Revisão Turbo ENEM: Linguagens em Flashcards & Gatilhos de Prova",
        "subtitle": "O Raio-X Mais Rápido e Focado do Edital: 31 Estações de Alta Retenção, Pegadinhas da Banca e Resumos de Bolso",
        "author": "Prof. Antigravity & Revisão Estratégica ENEM",
        "date": "2026",
        "language": "pt-BR",
        "category": "Revisão Turbo · Tiro Curto & Alta Retenção",
        "chaptersCount": 31,
        "estimatedReadingTime": "Aprox. 70 min de revisão acelerada (31 Estações Flash)",
        "description": "A revisão definitiva de alta velocidade para Linguagens, Códigos e suas Tecnologias no ENEM. Estruturada em 31 estações de tiro curto organizadas do maior peso na TRI para o menor: cada capítulo traz o Raio-X em 30 segundos, como o INEP cobra a questão no enunciado, o distrator fatal que elimina candidatos desatentos, um exemplo relâmpago resolvido e o flashcard mental de bolso para memorização imediata. Cobre toda a interpretação, gêneros, gramática aplicada ao sentido, linha do tempo literária, autores canônicos, artes, línguas estrangeiras (inglês/espanhol) e cultura corporal.",
        "isPriority": True,
        "createdAt": "2026-11-07T23:15:00Z",
        "style": "editorial-flashcard-turbo"
    },
    "settings": {
        "defaultFont": "serif",
        "defaultTheme": "eink",
        "fontSize": 20
    },
    "chapters": []
}

def ch(num_str, title, ep_text, ep_author, sections):
    return {
        "id": f"cap-{len(BOOK['chapters']) + 1:02d}",
        "number": num_str,
        "title": title,
        "epigraph": {
            "text": ep_text,
            "author": ep_author
        },
        "sections": sections
    }

def sec_h(title, level=2):
    return {"type": "heading", "level": level, "title": None, "content": title}

def sec_p(content):
    return {"type": "paragraph", "content": content}

def sec_c(title, content):
    return {"type": "callout", "title": title, "content": content}

def sec_q(content, author):
    return {"type": "quote", "content": content, "author": author}

print("Iniciando montagem dos capítulos de revisão turbo...")
