import { Router, Request, Response } from 'express';
import fs from 'fs';
import path from 'path';
import { CONFIG } from '../config.js';
import { DEFAULT_CATALOG, CatalogItem, BookDoc } from '@mono-reader/shared';

export const booksRouter = Router();

booksRouter.get('/catalog', (req: Request, res: Response) => {
  try {
    const libraryPath = path.join(CONFIG.DATA_DIR, 'library.json');
    if (fs.existsSync(libraryPath)) {
      const data = JSON.parse(fs.readFileSync(libraryPath, 'utf-8'));
      return res.json({ status: 'ok', catalog: data });
    }
  } catch (err) {
    console.warn('Erro ao ler library.json, usando DEFAULT_CATALOG:', err);
  }
  return res.json({ status: 'ok', catalog: DEFAULT_CATALOG });
});

booksRouter.get('/books/:id', (req: Request, res: Response) => {
  let id = Array.isArray(req.params.id) ? req.params.id[0] : req.params.id;

  // Normalização de IDs de redação legada para o ID canônico
  if (id.startsWith('obra-17938') || (id.includes('redacao') && id !== 'redacao-enem')) {
    id = 'redacao-enem';
  }

  const filePath = path.join(CONFIG.DATA_DIR, `${id}.json`);
  if (fs.existsSync(filePath)) {
    try {
      const book = JSON.parse(fs.readFileSync(filePath, 'utf-8')) as BookDoc;
      return res.json({ status: 'ok', book });
    } catch (err: any) {
      return res.status(500).json({ status: 'error', message: `Erro ao processar livro: ${err.message}` });
    }
  }

  return res.status(404).json({ status: 'error', message: `Livro '${id}' não encontrado.` });
});

booksRouter.post('/books', (req: Request, res: Response) => {
  const { book } = req.body;
  if (!book || !book.meta || !book.meta.id) {
    return res.status(400).json({ status: 'error', message: 'Payload de livro inválido.' });
  }

  try {
    const bookId = book.meta.id;
    const filePath = path.join(CONFIG.DATA_DIR, `${bookId}.json`);
    fs.writeFileSync(filePath, JSON.stringify(book, null, 2), 'utf-8');

    // Atualiza library.json se necessário
    const libraryPath = path.join(CONFIG.DATA_DIR, 'library.json');
    let catalog: CatalogItem[] = [];
    if (fs.existsSync(libraryPath)) {
      try {
        catalog = JSON.parse(fs.readFileSync(libraryPath, 'utf-8'));
      } catch (e) {
        catalog = [...DEFAULT_CATALOG];
      }
    } else {
      catalog = [...DEFAULT_CATALOG];
    }

    const newEntry: CatalogItem = {
      id: bookId,
      title: book.meta.title,
      subtitle: book.meta.subtitle,
      author: book.meta.author || 'Manual Vivo · Leitura em Camadas',
      category: book.meta.category || 'Leitura em Camadas',
      chaptersCount: book.chapters?.length || 1,
      estimatedTime: book.meta.estimatedReadingTime || 'Leitura Didática',
      file: `/data/${bookId}.json`,
      description: book.meta.description,
      isPriority: false,
      isGeneratedByAI: true,
      createdAt: new Date().toISOString()
    };

    catalog = catalog.filter(c => c.id !== bookId);
    catalog.unshift(newEntry);
    fs.writeFileSync(libraryPath, JSON.stringify(catalog, null, 2), 'utf-8');

    return res.json({ status: 'ok', bookId, message: 'Livro salvo com sucesso.' });
  } catch (err: any) {
    return res.status(500).json({ status: 'error', message: `Erro ao salvar: ${err.message}` });
  }
});
