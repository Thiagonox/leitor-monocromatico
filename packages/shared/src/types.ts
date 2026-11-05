export type ThemeType = 'eink' | 'dark' | 'white' | 'sepia';
export type FontType = 'serif' | 'sans' | 'mono';

export interface Epigraph {
  text: string;
  author?: string;
  source?: string;
}

export interface Section {
  type: 'heading' | 'paragraph' | 'callout' | 'quote' | 'list' | 'divider' | 'quiz';
  level?: number;
  title?: string;
  content?: string;
  author?: string;
  items?: string[];
}

export interface QuizOption {
  letter: string;
  text: string;
  isCorrect?: boolean;
}

export interface QuizItem {
  prompt?: string;
  questionText?: string;
  options: QuizOption[];
  correctLetter?: string;
  explanation?: string;
  feedback?: string;
}

export interface Chapter {
  id: string;
  number: string;
  title: string;
  epigraph?: Epigraph;
  sections: Section[];
  quiz?: QuizItem[];
}

export interface BookMeta {
  id: string;
  title: string;
  subtitle?: string;
  author: string;
  date?: string;
  language?: string;
  category?: string;
  chaptersCount?: number;
  estimatedReadingTime?: string;
  description?: string;
  isGeneratedByAI?: boolean;
  createdAt?: string;
  style?: string;
}

export interface BookSettings {
  defaultFont?: FontType;
  defaultTheme?: ThemeType;
  defaultWidth?: string;
  fontSize?: number;
}

export interface BookDoc {
  meta: BookMeta;
  settings?: BookSettings;
  chapters: Chapter[];
  quiz?: QuizItem[];
  _isFallback?: boolean;
}

export interface CatalogItem {
  id: string;
  title: string;
  subtitle?: string;
  author: string;
  category: string;
  chaptersCount: number;
  estimatedTime?: string;
  file?: string;
  description?: string;
  isPriority?: boolean;
  isGeneratedByAI?: boolean;
  createdAt?: string;
}

export interface ChallengeOption {
  letter: string;
  text: string;
}

export interface Layer0Challenge {
  questionText: string;
  options: ChallengeOption[];
  correctLetter: string;
  explanation: string;
}

export interface Layer1Flash {
  title: string;
  goldenTakeaway: string;
  text: string;
}

export interface Layer2Concept {
  title: string;
  analogyTitle?: string;
  analogyText?: string;
  conceptText: string;
}

export interface Layer3Mechanism {
  title: string;
  mechanismText: string;
  traps?: string[];
  authorities?: string;
}

export interface Layer4Deep {
  chapterId: string;
  totalWordCount?: number;
  estimatedMinutes?: number;
}

export interface Layer5Recall {
  title: string;
  subtitle?: string;
  questions: QuizItem[];
}

export interface LayeredChapterData {
  chapterIndex: number;
  chapterNumber: string;
  chapterTitle: string;
  readingGoal?: string;
  layer0Challenge?: Layer0Challenge;
  layer1Flash30s?: Layer1Flash;
  layer2Concept1m?: Layer2Concept;
  layer3Mechanism3m?: Layer3Mechanism;
  layer4DeepChapter?: Layer4Deep;
  layer5ActiveRecall?: Layer5Recall;
}

export interface ReadingProgress {
  bookId: string;
  chapterIndex: number;
  scrollRatio: number;
  lastReadAt: string;
  completedChapters: number[];
}

export interface GenerateLayeredRequest {
  topic: string;
  depth?: string;
  chaptersCount?: number;
  apiKey?: string;
  model?: string;
  baseUrl?: string;
}

export interface DeepenRequest {
  topic: string;
  contextText?: string;
  style?: string;
  level?: number;
  apiKey?: string;
  model?: string;
}

export interface TTSRequest {
  text: string;
  voice?: string;
  apiKey?: string;
  model?: string;
}
