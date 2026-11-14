# -*- coding: utf-8 -*-
"""Compilador dos dois Resumões de 30 Minutos ENEM 2º Dia (Matemática e Ciências da Natureza)"""

import json
import os
import mat_resumao_30min
import nat_resumao_30min

ROMAN_NUMERALS = [
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"
]

def compile_book(module, book_id, ch_prefix, title, subtitle, author, category, description, filename):
    chapters = module.get_chapters()
    for idx, ch in enumerate(chapters):
        ch["number"] = ROMAN_NUMERALS[idx] if idx < len(ROMAN_NUMERALS) else str(idx + 1)
        ch["id"] = f"{ch_prefix}-{idx + 1}"
        clean_secs = []
        for s in ch.get("sections", []):
            sec = dict(s)
            if "citation" in sec and "author" not in sec:
                sec["author"] = sec.pop("citation")
            if sec.get("content", "").strip():
                clean_secs.append(sec)
        ch["sections"] = clean_secs
        ch["quiz"] = []

    total_words = sum(
        len(sec.get("content", "").split())
        for ch in chapters
        for sec in ch.get("sections", [])
    )
    total_secs = sum(len(ch.get("sections", [])) for ch in chapters)
    est_mins = max(25, min(35, round(total_words / 150)))

    book_doc = {
        "meta": {
            "id": book_id,
            "title": title,
            "subtitle": subtitle,
            "author": author,
            "category": category,
            "chaptersCount": len(chapters),
            "estimatedReadingTime": f"Aprox. {est_mins} min (Resumão Contido · {len(chapters)} Capítulos)",
            "description": description,
            "isGeneratedByAI": True
        },
        "chapters": chapters
    }

    base_dir = "/home/thiagonox/leitor-monocromatico"
    for rel in [f"data/{filename}", f"apps/web/public/data/{filename}"]:
        out_path = os.path.join(base_dir, rel)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(book_doc, f, ensure_ascii=False, indent=2)

    print(f"[{book_id}] caps={len(chapters)}, secs={total_secs}, words={total_words}, avg={total_words // len(chapters)}, est={est_mins}min")

if __name__ == "__main__":
    compile_book(
        module=mat_resumao_30min,
        book_id="matematica-enem-resumo-30min",
        ch_prefix="mat-res-cap",
        title="Resumão Relâmpago de Matemática ENEM (30 Min)",
        subtitle="Toda a Grade do 2º Dia em Linguagem de Curso Direta ao Ponto: Fórmulas Essenciais, Atalhos e Pegadinhas por Ordem de TRI",
        author="Prof. Antigravity & Colegiado de Matemática",
        category="Resumão 30 Min · Matemática ENEM",
        description="A revisão mais enxuta e cirúrgica de todo o edital de Matemática (45 questões) em ~30 minutos de leitura ou áudio. Cobre 100% dos 12 módulos em linguagem de curso sem enrolação: Aritmética e Conjuntos, Razão/Proporção/Escalas/Regra de Três, Porcentagem e Financeira, Estatística e Gráficos, Geometria Plana e Espacial, Álgebra, Funções (Afim, Quadrática, Exponencial e Logarítmica), Sequências (PA/PG), Trigonometria, Geometria Analítica, Probabilidade e Combinatória.",
        filename="matematica-enem-resumo-30min.json"
    )
    compile_book(
        module=nat_resumao_30min,
        book_id="ciencias-da-natureza-enem-resumo-30min",
        ch_prefix="nat-res-cap",
        title="Resumão Relâmpago de Ciências da Natureza ENEM (30 Min)",
        subtitle="Biologia, Física e Química Integradas em ~30 Minutos: O Coração das 45 Questões em Linguagem de Curso Direta ao Ponto",
        author="Prof. Antigravity & Colegiado de Ciências da Natureza",
        category="Resumão 30 Min · Ciências da Natureza ENEM",
        description="Revisão super contida de ~30 minutos cobrindo 100% dos 33 módulos do edital de Ciências da Natureza em linguagem de cursinho direto ao ponto, ordenada por peso TRI 800+: Ecologia, Meio Ambiente/Biomas, Genética/Evolução, Citologia/Metabolismo/Divisão Celular, Fisiologia e Saúde/ISTs; Eletricidade/Magnetismo, Mecânica/Newton/Energia, Hidrostática/Termologia/Termodinâmica, Ondulatória/Óptica/Moderna; Estrutura Atômica/Tabela/Ligações, Estequiometria/Soluções, Funções Inorgânicas/Termoquímica/Cinética/Equilíbrio, Eletroquímica, Orgânica e Ambiental.",
        filename="ciencias-da-natureza-enem-resumo-30min.json"
    )
