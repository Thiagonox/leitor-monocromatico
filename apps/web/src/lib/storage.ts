import { CatalogItem } from '@mono-reader/shared';

export type ThemeMode = 'eink' | 'dark' | 'light';
export type FontMode = 'serif' | 'sans' | 'mono';

const THEME_KEY = 'mono_reader_theme';
const FONT_KEY = 'mono_reader_font';
const FONT_SIZE_KEY = 'mono_reader_fontsize';
const CUSTOM_CATALOG_KEY = 'mono_library_custom_catalog';

export function getStoredTheme(): ThemeMode {
  if (typeof window === 'undefined') return 'eink';
  const val = localStorage.getItem(THEME_KEY);
  if (val === 'dark' || val === 'light' || val === 'eink') return val;
  return 'eink';
}

export function setStoredTheme(theme: ThemeMode) {
  if (typeof window === 'undefined') return;
  localStorage.setItem(THEME_KEY, theme);
  document.documentElement.setAttribute('data-theme', theme);
}

export function getStoredFont(): FontMode {
  if (typeof window === 'undefined') return 'serif';
  const val = localStorage.getItem(FONT_KEY);
  if (val === 'sans' || val === 'mono' || val === 'serif') return val;
  return 'serif';
}

export function setStoredFont(font: FontMode) {
  if (typeof window === 'undefined') return;
  localStorage.setItem(FONT_KEY, font);
  document.documentElement.setAttribute('data-font', font);
}

export function getStoredFontSize(): number {
  if (typeof window === 'undefined') return 20;
  const val = localStorage.getItem(FONT_SIZE_KEY);
  const num = parseInt(val || '20', 10);
  return isNaN(num) ? 20 : Math.min(32, Math.max(14, num));
}

export function setStoredFontSize(size: number) {
  if (typeof window === 'undefined') return;
  localStorage.setItem(FONT_SIZE_KEY, size.toString());
  document.documentElement.style.setProperty('--font-size', `${size}px`);
}

const REMOVED_BOOK_IDS = new Set([
  'elogio-da-tinta',
  'generos-textuais',
  'gramatica-aplicada',
  'historia-da-arte-e-cultura',
  'interpretacao-de-texto',
  'lingua-estrangeira-ingles-espanhol',
  'linguagens-enem-completo',
  'linguagens-enem-essencial',
  'literatura-e-autores',
  'redacao-enem',
  'revisao-turbo-linguagens-enem',
]);

export function purgeLegacyRedacaoBooks(): void {
  if (typeof window === 'undefined') return;
  try {
    // Purga obras legadas ou removidas do catálogo local
    const stored = localStorage.getItem(CUSTOM_CATALOG_KEY);
    if (stored) {
      let list = JSON.parse(stored);
      if (Array.isArray(list)) {
        list = list.filter((item: any) => {
          const isRemoved = item.id && (REMOVED_BOOK_IDS.has(item.id) || item.id.startsWith('obra-17938'));
          return !isRemoved;
        });
        localStorage.setItem(CUSTOM_CATALOG_KEY, JSON.stringify(list));
      }
    }

    // Varredura de chaves órfãs ou cacheadas de obras antigas
    const toRemove: string[] = [];
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (!k) continue;
      const isRemovedKey =
        k.startsWith('book_json_obra-17938') ||
        k.startsWith('book_layered_obra-17938') ||
        k.startsWith('book_generations_obra-17938') ||
        Array.from(REMOVED_BOOK_IDS).some(
          id => k === `book_json_${id}` || k === `book_layered_${id}` || k === `book_generations_${id}`
        );
      if (isRemovedKey) {
        toRemove.push(k);
      }
    }
    toRemove.forEach(k => localStorage.removeItem(k));
  } catch (e) {
    console.warn('Erro ao purgar obras legadas:', e);
  }
}

export function getCustomCatalog(): CatalogItem[] {
  if (typeof window === 'undefined') return [];
  purgeLegacyRedacaoBooks();
  try {
    const raw = localStorage.getItem(CUSTOM_CATALOG_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch (e) {
    return [];
  }
}

export function addCustomCatalogBook(entry: CatalogItem): void {
  if (typeof window === 'undefined') return;
  try {
    let list = getCustomCatalog();
    list = list.filter(item => item.id !== entry.id);
    list.unshift(entry);
    localStorage.setItem(CUSTOM_CATALOG_KEY, JSON.stringify(list));
  } catch (e) {}
}

export function getBookProgress(bookId: string): { chapterIndex: number; scrollRatio: number } {
  if (typeof window === 'undefined') return { chapterIndex: 0, scrollRatio: 0 };
  try {
    const raw = localStorage.getItem(`book_progress_${bookId}`);
    return raw ? JSON.parse(raw) : { chapterIndex: 0, scrollRatio: 0 };
  } catch (e) {
    return { chapterIndex: 0, scrollRatio: 0 };
  }
}

export function setBookProgress(bookId: string, chapterIndex: number, scrollRatio: number): void {
  if (typeof window === 'undefined') return;
  try {
    localStorage.setItem(`book_progress_${bookId}`, JSON.stringify({
      chapterIndex,
      scrollRatio,
      updatedAt: new Date().toISOString()
    }));
  } catch (e) {}
}
