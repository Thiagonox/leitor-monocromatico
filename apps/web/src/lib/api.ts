import { BookDoc, CatalogItem, GenerateLayeredRequest, DeepenRequest, TTSRequest, DEFAULT_CATALOG } from '@mono-reader/shared';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || '';

export async function fetchCatalog(): Promise<CatalogItem[]> {
  try {
    const res = await fetch(`${API_BASE}/api/catalog`, { cache: 'no-store' });
    if (res.ok) {
      const data = await res.json();
      if (data.status === 'ok' && Array.isArray(data.catalog) && data.catalog.length > 0) {
        return data.catalog;
      }
    }
  } catch (err) {
    console.warn('API catalog fetch falhou, tentando fallback estático:', err);
  }

  // Fallback para arquivo estático
  try {
    const res = await fetch('/data/library.json');
    if (res.ok) {
      return await res.json();
    }
  } catch (e) {
    console.warn('Fallback estático falhou:', e);
  }

  return DEFAULT_CATALOG;
}

export async function fetchBook(id: string): Promise<BookDoc | null> {
  // Normalização de IDs de redação legada
  const canonicalId = (id.startsWith('obra-17938') || (id.includes('redacao') && id !== 'redacao-enem'))
    ? 'redacao-enem'
    : id;

  try {
    const res = await fetch(`${API_BASE}/api/books/${canonicalId}`, { cache: 'no-store' });
    if (res.ok) {
      const data = await res.json();
      if (data.status === 'ok' && data.book) {
        return data.book;
      }
    }
  } catch (err) {
    console.warn(`API fetch para ${canonicalId} falhou, tentando estático:`, err);
  }

  // Fallback para arquivo estático no Next.js public
  try {
    const res = await fetch(`/data/${canonicalId}.json`);
    if (res.ok) {
      return await res.json();
    }
  } catch (e) {
    console.warn(`Estático /data/${canonicalId}.json falhou:`, e);
  }

  // Fallback para localStorage
  if (typeof window !== 'undefined') {
    try {
      const local = localStorage.getItem(`book_json_${canonicalId}`);
      if (local) return JSON.parse(local);
    } catch (e) {}
  }

  return null;
}

export async function generateLayeredBook(payload: GenerateLayeredRequest): Promise<{ book: BookDoc; model: string }> {
  const res = await fetch(`${API_BASE}/api/ai/generate-layered`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (!res.ok) {
    throw new Error(`Falha na geração de obra: HTTP ${res.status}`);
  }

  const data = await res.json();
  if (data.status !== 'ok' || !data.book) {
    throw new Error(data.message || 'Resposta de geração inválida.');
  }

  return { book: data.book, model: data.model || 'Motor Editorial' };
}

export async function deepenTopic(payload: DeepenRequest): Promise<{ content: string; model?: string }> {
  const res = await fetch(`${API_BASE}/api/ai/deepen`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (!res.ok) {
    throw new Error(`Falha no aprofundamento: HTTP ${res.status}`);
  }

  const data = await res.json();
  return { content: data.content || '', model: data.model };
}

export interface TTSResponse {
  status: string;
  cached?: boolean;
  cacheKey?: string;
  audioUrl?: string;
  script?: string;
  durationEstimateSec?: number;
  mode?: string;
  message?: string;
}

export async function requestTTS(payload: {
  text: string;
  chapterTitle?: string;
  chapterId?: string;
  mode?: 'audiodescricao' | 'direct';
}): Promise<TTSResponse> {
  const res = await fetch(`${API_BASE}/api/ai/tts`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  return await res.json();
}
