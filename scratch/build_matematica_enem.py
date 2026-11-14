# -*- coding: utf-8 -*-
"""Compilador Master do Curso Completo de Matemática ENEM (2º Dia) em Linguagem de Curso"""

import json
import os
import mat_curso_1_inaugural_basica_a
import mat_curso_2_basica_b
import mat_curso_3_financeira
import mat_curso_4_estatistica
import mat_curso_5_geom_plana
import mat_curso_6_geom_espacial
import mat_curso_7_algebra
import mat_curso_8_funcoes
import mat_curso_9_seq_trig_analitica
import mat_curso_10_prob_comb

ROMAN_NUMERALS = [
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
    "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX",
    "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL",
    "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L",
    "LI", "LII", "LIII", "LIV", "LV"
]

def build_book():
    all_chapters = []
    modules = [
        mat_curso_1_inaugural_basica_a,
        mat_curso_2_basica_b,
        mat_curso_3_financeira,
        mat_curso_4_estatistica,
        mat_curso_5_geom_plana,
        mat_curso_6_geom_espacial,
        mat_curso_7_algebra,
        mat_curso_8_funcoes,
        mat_curso_9_seq_trig_analitica,
        mat_curso_10_prob_comb,
    ]

    for m in modules:
        all_chapters.extend(m.get_chapters())

    for idx, ch in enumerate(all_chapters):
        ch["number"] = ROMAN_NUMERALS[idx] if idx < len(ROMAN_NUMERALS) else str(idx + 1)
        ch["id"] = f"mat-capitulo-{idx + 1}"
        # Normalize sections: guarantee content field and valid quote author
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
    est_hours = max(4, round(total_words / 7500))

    book_doc = {
        "meta": {
            "id": "matematica-enem-completo",
            "title": "Manual Supremo de Matemática e suas Tecnologias ENEM",
            "subtitle": "O Curso Completo do 2º Dia em Linguagem de Sala de Aula: Todos os 12 Módulos Ordenados por Prioridade TRI para Romper os 800+ Pontos",
            "author": "Prof. Antigravity & Colegiado de Matemática",
            "category": "Curso Completo ENEM · Matemática (45 Questões)",
            "chaptersCount": len(all_chapters),
            "estimatedReadingTime": f"Aprox. {est_hours} horas de imersão completa ({len(all_chapters)} Capítulos)",
            "description": "Curso completo, conversado e extremamente didático cobrindo 100% da Matriz de Referência do ENEM para Matemática e suas Tecnologias (45 questões do 2º dia). Estruturado por ordem de prioridade TRI para 800+: 1. Matemática Básica e Aritmética (operações, conjuntos, frações, decimais, potenciação, radiciação, notação científica, MMC/MDC, razão, proporção, divisão proporcional, regra de três simples e composta, escalas); 2. Porcentagem e Matemática Financeira (aumentos/descontos, variação percentual, juros simples e compostos, taxas, inflação, financiamentos, parcelamentos, investimentos, custo/receita/lucro); 3. Estatística (tabelas, gráficos, média aritmética e ponderada, moda, mediana, amplitude, variância e desvio padrão); 4. Geometria Plana e Espacial (ângulos, triângulos, semelhança, Pitágoras, relações métricas, quadriláteros, círculo, perímetro, área, planificação, prismas, pirâmides, cilindros, cones, esferas); 5. Álgebra, Funções (afim, quadrática, exponencial, logarítmica, crescimento/decrescimento e gráficos) e Sequências (PA e PG); 6. Trigonometria e Geometria Analítica; 7. Probabilidade e Análise Combinatória.",
            "isGeneratedByAI": True
        },
        "chapters": all_chapters
    }

    base_dir = "/home/thiagonox/leitor-monocromatico"
    path_data = os.path.join(base_dir, "data/matematica-enem-completo.json")
    path_web = os.path.join(base_dir, "apps/web/public/data/matematica-enem-completo.json")

    with open(path_data, "w", encoding="utf-8") as f:
        json.dump(book_doc, f, ensure_ascii=False, indent=2)

    with open(path_web, "w", encoding="utf-8") as f:
        json.dump(book_doc, f, ensure_ascii=False, indent=2)

    print(f"Sucesso! Livro de Matemática gerado:")
    print(f"- Total de capítulos: {len(all_chapters)}")
    print(f"- Total de seções: {total_secs}")
    print(f"- Total de palavras: {total_words}")
    print(f"- Média palavras/capítulo: {total_words // max(1, len(all_chapters))}")

if __name__ == "__main__":
    build_book()
