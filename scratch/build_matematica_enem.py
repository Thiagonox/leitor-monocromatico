# -*- coding: utf-8 -*-
"""Compilador Master do Curso Completo de Matemática ENEM (2º Dia)"""

import json
import os
import mat_mod1_aritmetica
import mat_mod2_financeira
import mat_mod3_algebra
import mat_mod4_funcoes
import mat_mod5_sequencias
import mat_mod6_geometria_plana
import mat_mod7_geometria_espacial
import mat_mod8_analitica_trig
import mat_mod9_estatistica
import mat_mod10_probabilidade_combinatoria

def build_book():
    all_chapters = []
    modules = [
        mat_mod1_aritmetica,
        mat_mod2_financeira,
        mat_mod3_algebra,
        mat_mod4_funcoes,
        mat_mod5_sequencias,
        mat_mod6_geometria_plana,
        mat_mod7_geometria_espacial,
        mat_mod8_analitica_trig,
        mat_mod9_estatistica,
        mat_mod10_probabilidade_combinatoria
    ]

    for m in modules:
        all_chapters.extend(m.get_chapters())

    # Re-index chapters correctly
    for idx, ch in enumerate(all_chapters):
        ch["number"] = idx + 1

    book_doc = {
        "meta": {
            "id": "matematica-enem-completo",
            "title": "Manual Supremo de Matemática e suas Tecnologias ENEM",
            "subtitle": "A Grade Completa do 2º Dia: Da Matemática Básica à Análise Combinatória e Probabilidade com Foco Máximo na TRI e 800+ Pontos",
            "author": "Prof. Antigravity & Mestres das Ciências Exatas",
            "category": "Matemática e suas Tecnologias · ENEM 2º Dia",
            "chaptersCount": len(all_chapters),
            "estimatedReadingTime": "Aprox. 6 horas de imersão completa",
            "description": "Curso completo, rigoroso e estruturado cobrindo 100% da Matriz de Referência de Matemática e suas Tecnologias do ENEM (45 questões do 2º dia). Dividido em 12 grandes áreas: 1. Matemática Básica e Aritmética; 2. Porcentagem e Matemática Financeira; 3. Álgebra Elementar; 4. Estudo Completo de Funções (Afim, Quadrática, Exponencial e Logarítmica); 5. Sequências Numéricas (PA e PG); 6. Geometria Plana e Relações Métricas; 7. Geometria Espacial e Capacidades; 8. Geometria Analítica; 9. Trigonometria; 10. Estatística Descritiva (Médias, Moda, Mediana e Desvio Padrão); 11. Teoria das Probabilidades; e 12. Análise Combinatória. Cada capítulo conta com formulações didáticas, atalhos mentais para a prova, resolução comentada e estratégias anti-distrator da TRI.",
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

    total_words = 0
    for ch in all_chapters:
        for sec in ch.get("sections", []):
            total_words += len(sec.get("content", "").split())

    print(f"Sucesso! Livro de Matemática gerado:")
    print(f"- Total de capítulos: {len(all_chapters)}")
    print(f"- Total de seções de conteúdo: {sum(len(c.get('sections', [])) for c in all_chapters)}")
    print(f"- Total de palavras: {total_words}")
    print(f"- Salvo em: {path_data}")
    print(f"- Salvo em: {path_web}")

if __name__ == "__main__":
    build_book()
