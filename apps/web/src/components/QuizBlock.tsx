'use client';

import React, { useState } from 'react';
import { CheckCircle2, XCircle, HelpCircle } from 'lucide-react';
import { QuizItem } from '@mono-reader/shared';

interface QuizBlockProps {
  quiz: QuizItem;
  index?: number;
}

export function QuizBlock({ quiz, index = 1 }: QuizBlockProps) {
  const [selectedLetter, setSelectedLetter] = useState<string | null>(null);
  const [revealed, setRevealed] = useState(false);

  const correctLetter = quiz.correctLetter || quiz.options.find(o => o.isCorrect)?.letter || 'A';
  const isCorrect = selectedLetter === correctLetter;

  const handleSelect = (letter: string) => {
    if (revealed) return;
    setSelectedLetter(letter);
    setRevealed(true);
  };

  const handleReset = () => {
    setSelectedLetter(null);
    setRevealed(false);
  };

  return (
    <div className="my-8 p-6 rounded border border-[var(--border-strong)] bg-[var(--bg-card)]">
      <div className="flex items-center gap-2 mb-3 text-xs font-mono uppercase tracking-wider text-[var(--text-muted)]">
        <HelpCircle className="w-4 h-4" />
        <span>Checagem de Fixação & Recuperação Ativa #{index}</span>
      </div>

      <h4 className="font-serif text-base font-bold text-[var(--text-primary)] mb-4 leading-snug">
        {quiz.questionText || quiz.prompt}
      </h4>

      <div className="space-y-2 mb-4">
        {quiz.options.map((opt) => {
          let btnStyle = "border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-primary)] hover:border-[var(--border-strong)]";

          if (revealed) {
            if (opt.letter === correctLetter) {
              btnStyle = "border-black dark:border-white bg-black dark:bg-white text-white dark:text-black font-semibold";
            } else if (opt.letter === selectedLetter && !isCorrect) {
              btnStyle = "border-red-500 bg-red-50 dark:bg-red-950/40 text-red-700 dark:text-red-300 opacity-80";
            } else {
              btnStyle = "border-[var(--border-light)] opacity-50";
            }
          }

          return (
            <button
              key={opt.letter}
              onClick={() => handleSelect(opt.letter)}
              disabled={revealed}
              className={`w-full text-left p-3 rounded border text-sm font-sans flex items-start gap-3 transition-colors ${btnStyle}`}
            >
              <span className="font-mono text-xs font-bold px-1.5 py-0.5 rounded border border-current shrink-0">
                {opt.letter}
              </span>
              <span className="flex-1">{opt.text}</span>
            </button>
          );
        })}
      </div>

      {revealed && (
        <div className="pt-4 border-t border-[var(--border-color)] mt-4">
          <div className="flex items-center gap-2 text-sm font-mono font-bold mb-2">
            {isCorrect ? (
              <span className="flex items-center gap-1.5 text-black dark:text-white">
                <CheckCircle2 className="w-4 h-4" /> Resposta Correta!
              </span>
            ) : (
              <span className="flex items-center gap-1.5 text-red-600 dark:text-red-400">
                <XCircle className="w-4 h-4" /> Alternativa Incorreta
              </span>
            )}
          </div>

          {(quiz.explanation || quiz.feedback) && (
            <p className="text-xs text-[var(--text-secondary)] font-sans leading-relaxed mb-3">
              {quiz.explanation || quiz.feedback}
            </p>
          )}

          <button
            onClick={handleReset}
            className="text-xs font-mono underline hover:no-underline text-[var(--text-muted)]"
          >
            Refazer pergunta
          </button>
        </div>
      )}
    </div>
  );
}
