'use client';

import React, { useEffect, useState } from 'react';
import { Sun, Moon, BookOpen } from 'lucide-react';
import { getStoredTheme, setStoredTheme, ThemeMode } from '@/lib/storage';

export function ThemeToggle() {
  const [theme, setTheme] = useState<ThemeMode>('eink');

  useEffect(() => {
    const current = getStoredTheme();
    setTheme(current);
    document.documentElement.setAttribute('data-theme', current);
  }, []);

  const toggleTheme = () => {
    let next: ThemeMode = 'eink';
    if (theme === 'eink') next = 'dark';
    else if (theme === 'dark') next = 'light';
    else next = 'eink';

    setTheme(next);
    setStoredTheme(next);
  };

  return (
    <button
      onClick={toggleTheme}
      className="p-2 border border-[var(--border-color)] bg-[var(--bg-surface)] hover:bg-[var(--bg-secondary)] rounded transition-colors text-[var(--text-primary)] flex items-center gap-1.5 text-xs font-mono"
      title={`Tema atual: ${theme}. Clique para alternar (E-Ink → Dark → Light)`}
    >
      {theme === 'eink' && <BookOpen className="w-4 h-4" />}
      {theme === 'dark' && <Moon className="w-4 h-4" />}
      {theme === 'light' && <Sun className="w-4 h-4" />}
      <span className="capitalize">{theme}</span>
    </button>
  );
}
