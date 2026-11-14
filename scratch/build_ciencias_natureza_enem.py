# -*- coding: utf-8 -*-
"""Compilador Master do Curso Completo de Ciências da Natureza ENEM (2º Dia) em Linguagem de Curso"""

import json
import os
import nat_curso_1_inaugural_bio_eco
import nat_curso_2_bio_gen_cito_metab
import nat_curso_3_bio_evol_fisio_saude
import nat_curso_4_fis_eletr_mec
import nat_curso_5_fis_hidro_termo_ond_opt_mod
import nat_curso_6_quim_esteq_org
import nat_curso_7_quim_atom_tab_lig_reac_sol_inorg
import nat_curso_8_quim_termo_cin_eq_eletro_amb

ROMAN_NUMERALS = [
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
    "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX",
    "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL",
    "XLI", "XLII", "XLIII", "XLIV", "XLV"
]

def build_book():
    all_chapters = []
    modules = [
        nat_curso_1_inaugural_bio_eco,
        nat_curso_2_bio_gen_cito_metab,
        nat_curso_3_bio_evol_fisio_saude,
        nat_curso_4_fis_eletr_mec,
        nat_curso_5_fis_hidro_termo_ond_opt_mod,
        nat_curso_6_quim_esteq_org,
        nat_curso_7_quim_atom_tab_lig_reac_sol_inorg,
        nat_curso_8_quim_termo_cin_eq_eletro_amb,
    ]

    for m in modules:
        all_chapters.extend(m.get_chapters())

    for idx, ch in enumerate(all_chapters):
        ch["number"] = ROMAN_NUMERALS[idx] if idx < len(ROMAN_NUMERALS) else str(idx + 1)
        ch["id"] = f"nat-capitulo-{idx + 1}"
        clean_secs = []
        for s in ch.get("sections", []):
            sec = dict(s)
            if "citation" in sec and "author" not in sec:
                sec["author"] = sec.pop("citation")
            if sec.get("content", "").strip():
                clean_secs.append(sec)
        ch["sections"] = clean_secs

    total_words = sum(
        len(sec.get("content", "").split())
        for ch in all_chapters
        for sec in ch.get("sections", [])
    )
    total_secs = sum(len(ch.get("sections", [])) for ch in all_chapters)
    est_hours = max(5, round(total_words / 7500))

    book_doc = {
        "meta": {
            "id": "ciencias-da-natureza-enem-completo",
            "title": "Manual Supremo de Ciências da Natureza e suas Tecnologias ENEM",
            "subtitle": "O Curso Completo do 2º Dia em Linguagem de Sala de Aula: Biologia, Física e Química Integradas com Prioridade Máxima para 800+",
            "author": "Prof. Antigravity & Colegiado de Ciências da Natureza",
            "category": "Curso Completo ENEM · Ciências da Natureza (45 Questões)",
            "chaptersCount": len(all_chapters),
            "estimatedReadingTime": f"Aprox. {est_hours} horas de imersão completa ({len(all_chapters)} Capítulos)",
            "description": "Curso completo, conversado e altamente didático cobrindo 100% do edital oficial de Ciências da Natureza para o ENEM (45 questões do 2º dia). BIOLOGIA (9 módulos): Ecologia (Prioridade 800+), Meio Ambiente e Biomas, Genética e Biotecnologia (Prioridade 800+), Citologia, Metabolismo Celular, Divisão Celular, Evolução, Fisiologia Humana e Saúde Pública/ISTs. FÍSICA (11 módulos): Eletricidade e Circuitos (Prioridade 800+), Mecânica e Gráficos (Prioridade 800+), Leis de Newton, Trabalho e Energia, Hidrostática, Termologia, Termodinâmica, Magnetismo, Ondulatória e Efeito Doppler, Óptica e Física Moderna. QUÍMICA (13 módulos): Estequiometria (Prioridade 800+), Química Orgânica (Prioridade 800+), Estrutura da Matéria, Tabela Periódica, Ligações e Forças Intermoleculares, Reações, Soluções, Funções Inorgânicas e pH, Termoquímica, Cinética, Equilíbrio Químico, Eletroquímica e Química Ambiental.",
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

    print(f"Sucesso! Livro de Ciências da Natureza gerado:")
    print(f"- Total de capítulos: {len(all_chapters)}")
    print(f"- Total de seções: {total_secs}")
    print(f"- Total de palavras: {total_words}")
    print(f"- Média palavras/capítulo: {total_words // max(1, len(all_chapters))}")

if __name__ == "__main__":
    build_book()
