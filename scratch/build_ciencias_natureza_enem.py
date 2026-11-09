# -*- coding: utf-8 -*-
"""Compilador Master do Curso Completo de Ciências da Natureza ENEM (2º Dia)"""

import json
import os
import nat_mod1_biologia
import nat_mod2_fisica
import nat_mod3_quimica

def build_book():
    all_chapters = []
    modules = [
        ("Biologia", nat_mod1_biologia),
        ("Física", nat_mod2_fisica),
        ("Química", nat_mod3_quimica)
    ]

    for area_name, m in modules:
        chapters = m.get_chapters()
        for ch in chapters:
            ch["area"] = area_name
        all_chapters.extend(chapters)

    # Re-index chapters correctly
    for idx, ch in enumerate(all_chapters):
        ch["number"] = idx + 1

    book_doc = {
        "meta": {
            "id": "ciencias-da-natureza-enem-completo",
            "title": "Manual Supremo de Ciências da Natureza e suas Tecnologias ENEM",
            "subtitle": "Grade Completa do 2º Dia: Biologia, Física e Química Integradas com Foco Máximo nas 45 Questões da Prova",
            "author": "Prof. Antigravity & Colegiado de Ciências da Natureza",
            "category": "Ciências da Natureza e suas Tecnologias · ENEM 2º Dia",
            "chaptersCount": len(all_chapters),
            "estimatedReadingTime": "Aprox. 7 horas de estudo detalhado",
            "description": "Curso completo e definitivo cobrindo 100% da Matriz de Referência do ENEM para Ciências da Natureza (45 questões do 2º dia). Abrange: BIOLOGIA (Ecologia, Meio Ambiente, Citologia, Metabolismo Energético, Divisão Celular, Genética/Biotecnologia, Evolução, Fisiologia Humana e Saúde Pública); FÍSICA (Cinemática, Leis de Newton, Trabalho e Energia, Hidrostática, Termologia, Termodinâmica, Circuitos Elétricos, Eletromagnetismo, Ondulatória e Doppler, Óptica e Física Moderna); e QUÍMICA (Estrutura Atômica, Tabela Periódica, Ligações e Forças Intermoleculares, Reações Químicas, Estequiometria, Soluções, Funções Inorgânicas, Termoquímica, Cinética, Equilíbrio Químico, Eletroquímica/Pilhas, Química Orgânica e Química Ambiental). Todas as teorias trazem aplicações práticas, esquemas de resolução e os distratores mais recorrentes do ENEM.",
            "isGeneratedByAI": True
        },
        "chapters": all_chapters
    }

    base_dir = "/home/thiagonox/leitor-monocromatico"
    path_data = os.path.join(base_dir, "data/ciencias-da-natureza-enem-completo.json")
    path_web = os.path.join(base_dir, "apps/web/public/data/ciencias-da-natureza-enem-completo.json")

    with open(path_data, "w", encoding="utf-8") as f:
        json.dump(book_doc, f, ensure_ascii=False, indent=2)

    with open(path_web, "w", encoding="utf-8") as f:
        json.dump(book_doc, f, ensure_ascii=False, indent=2)

    total_words = 0
    for ch in all_chapters:
        for sec in ch.get("sections", []):
            total_words += len(sec.get("content", "").split())

    print(f"Sucesso! Livro de Ciências da Natureza gerado:")
    print(f"- Total de capítulos: {len(all_chapters)}")
    print(f"- Total de seções de conteúdo: {sum(len(c.get('sections', [])) for c in all_chapters)}")
    print(f"- Total de palavras: {total_words}")
    print(f"- Salvo em: {path_data}")
    print(f"- Salvo em: {path_web}")

if __name__ == "__main__":
    build_book()
