import express from 'express';
import cors from 'cors';
import path from 'path';
import { CONFIG } from './config.js';
import { booksRouter } from './routes/books.js';
import { aiRouter } from './routes/ai.js';

const app = express();

app.use(cors({
  origin: '*',
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-Requested-With']
}));

app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ extended: true, limit: '50mb' }));

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: 'leitor-monocromatico-api', timestamp: new Date().toISOString() });
});

// Static data serving
app.use('/data', express.static(CONFIG.DATA_DIR));

// API Routes
app.use('/api', booksRouter);
app.use('/api/ai', aiRouter);

app.listen(CONFIG.PORT, '0.0.0.0', () => {
  console.log(`[API] Servidor Backend do Leitor Monocromático rodando em http://localhost:${CONFIG.PORT}`);
  console.log(`[API] Diretório de dados: ${CONFIG.DATA_DIR}`);
});

export default app;
