'use client';

import React, { useEffect, useRef, useState, useCallback } from 'react';
import { audioSyncBus, AudioSyncData, AcousticProfile } from '@/lib/audioSync';

interface TimedWord {
  index: number;
  word: string;
  startTime: number;
  vocalEndTime: number;
  endTime: number;
  relLeft: number;
  relRight: number;
  relBottom: number;
  width: number;
  lineIndex: number;
  isPunctuationPause: boolean;
}

export interface ReadingPencilGuideProps {
  containerRef?: React.RefObject<HTMLElement | null>;
  activeBlockId?: string;
  activeBlockKey?: string | number;
  isPlaying?: boolean;
  currentTime?: number;
  duration?: number;
  isLoading?: boolean;
  enabled?: boolean;
  playbackRate?: number;
}

/**
 * Ponderação fonética calibrada para fala contínua em português brasileiro
 */
function computePhoneticWeight(word: string): number {
  const cleaned = word.toLowerCase().replace(/[^a-z0-9áéíóúâêîôûãõç]/g, '');
  if (!cleaned) return 1.0;

  // Palavras funcionais / monossílabos átonos rápidos (~90-140ms)
  const rapidWords = new Set([
    'a', 'o', 'as', 'os', 'um', 'uma', 'uns', 'umas',
    'de', 'da', 'do', 'das', 'dos',
    'em', 'no', 'na', 'nos', 'nas',
    'e', 'ou', 'mas', 'se', 'que', 'por', 'com', 'sem', 'sob', 'sobre',
    'ja', 'já', 'ao', 'aos', 'me', 'te', 'lhe', 'nos', 'vos'
  ]);

  if (rapidWords.has(cleaned)) return 1.15;
  if (/^\d+/.test(cleaned)) return Math.max(4.0, cleaned.length * 2.5);
  if (/^[A-Z0-9]{2,}$/.test(word.replace(/[^A-Za-z0-9]/g, ''))) {
    return Math.max(3.8, cleaned.length * 2.0);
  }

  // Contagem aproximada de vogais (núcleos silábicos)
  const vowels = cleaned.match(/[aeiouyáéíóúâêîôûãõ]/gi);
  const syllableCount = vowels ? vowels.length : Math.max(1, Math.floor(cleaned.length / 3));

  return 1.4 + syllableCount * 1.55 + cleaned.length * 0.35;
}

/**
 * Mede com precisão sub-pixel todas as palavras visíveis do bloco no DOM,
 * tratando drop-caps (primeira letra gigante), quebras de linha e nós aninhados.
 */
function measureBlockWords(root: HTMLElement): {
  words: {
    word: string;
    relLeft: number;
    relRight: number;
    relBottom: number;
    width: number;
    lineIndex: number;
  }[];
} {
  const blockRect = root.getBoundingClientRect();
  if (blockRect.width === 0 || blockRect.height === 0) {
    return { words: [] };
  }

  const charRefs: { node: Node; offset: number; ch: string }[] = [];
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      const parent = node.parentElement;
      if (!parent) return NodeFilter.FILTER_REJECT;
      if (
        parent.closest('button') ||
        parent.closest('.no-reading-guide') ||
        parent.closest('nav') ||
        parent.closest('cite') ||
        parent.closest('.reader-epigraph-author')
      ) {
        return NodeFilter.FILTER_REJECT;
      }
      return NodeFilter.FILTER_ACCEPT;
    },
  });

  let tNode: Node | null;
  while ((tNode = walker.nextNode())) {
    const val = tNode.nodeValue || '';
    for (let i = 0; i < val.length; i++) {
      charRefs.push({ node: tNode, offset: i, ch: val[i] });
    }
  }

  if (charRefs.length === 0) return { words: [] };

  const rawWords: {
    startNode: Node;
    startOffset: number;
    endNode: Node;
    endOffset: number;
    word: string;
    isFirstWord: boolean;
  }[] = [];

  let i = 0;
  while (i < charRefs.length) {
    while (i < charRefs.length && /\s/.test(charRefs[i].ch)) i++;
    if (i >= charRefs.length) break;

    const startIdx = i;
    let word = '';
    while (i < charRefs.length && !/\s/.test(charRefs[i].ch)) {
      word += charRefs[i].ch;
      i++;
    }
    const endIdx = i - 1;

    rawWords.push({
      startNode: charRefs[startIdx].node,
      startOffset: charRefs[startIdx].offset,
      endNode: charRefs[endIdx].node,
      endOffset: charRefs[endIdx].offset + 1,
      word,
      isFirstWord: rawWords.length === 0,
    });
  }

  const measured: {
    word: string;
    relLeft: number;
    relRight: number;
    relBottom: number;
    width: number;
    lineIndex: number;
  }[] = [];

  let currentLineIndex = 0;
  let lastMeasuredBottom = -1;

  for (let idx = 0; idx < rawWords.length; idx++) {
    const rw = rawWords[idx];
    try {
      const range = document.createRange();
      range.setStart(rw.startNode, rw.startOffset);
      range.setEnd(rw.endNode, rw.endOffset);
      const rects = range.getClientRects();

      let targetRect: DOMRect | { left: number; right: number; bottom: number; width: number } | null = null;

      if (rects.length > 0) {
        if (rw.isFirstWord && rects.length > 1) {
          // Drop-cap detectado: combina o retângulo da capitular com o resto da palavra
          const left = Math.min(...Array.from(rects).map((r) => r.left));
          const right = Math.max(...Array.from(rects).map((r) => r.right));
          const bottom = Math.max(...Array.from(rects).map((r) => r.bottom));
          targetRect = { left, right, bottom, width: right - left };
        } else {
          targetRect = rects[0];
        }
      } else {
        const b = range.getBoundingClientRect();
        if (b && b.width > 0) targetRect = b;
      }

      if (targetRect && targetRect.width > 0) {
        const relBottom = targetRect.bottom - blockRect.top + 2;
        if (lastMeasuredBottom > 0 && Math.abs(relBottom - lastMeasuredBottom) > 13) {
          currentLineIndex++;
        }
        lastMeasuredBottom = relBottom;

        measured.push({
          word: rw.word,
          relLeft: targetRect.left - blockRect.left,
          relRight: targetRect.right - blockRect.left,
          relBottom,
          width: targetRect.width,
          lineIndex: currentLineIndex,
        });
      }
    } catch (e) {}
  }

  return { words: measured };
}

/**
 * Constrói o modelo de temporização estritamente contínuo e monotônico de palavras.
 * Cada palavra tem:
 * - Janela de vocalização (onde o lápis caminha suavemente sobre o texto)
 * - Janela de pausa pontuada (onde o lápis fica imóvel na pontuação enquanto a voz respira)
 */
function buildWordTimingModel(
  measuredWords: {
    word: string;
    relLeft: number;
    relRight: number;
    relBottom: number;
    width: number;
    lineIndex: number;
  }[],
  duration: number,
  acousticProfile?: AcousticProfile | null
): TimedWord[] {
  if (measuredWords.length === 0 || duration <= 0) return [];

  // Ponderações fonéticas e pesos de pausas
  interface WordScore {
    wordItem: (typeof measuredWords)[0];
    phoneticWeight: number;
    pauseWeight: number;
    isPunctuationPause: boolean;
  }

  const scores: WordScore[] = measuredWords.map((mw, idx) => {
    const isMajor = /[.!?…\n]+['"”’)]*$/.test(mw.word);
    const isMinor = /[,;:—–]+['"”’)]*$/.test(mw.word);
    const isLast = idx === measuredWords.length - 1;

    const pWeight = computePhoneticWeight(mw.word);
    let pauseW = 0;
    if (isMajor || isLast) {
      pauseW = isLast ? 7.5 : 8.5; // ~450ms a 700ms
    } else if (isMinor) {
      pauseW = 4.2; // ~250ms a 380ms
    }

    return {
      wordItem: mw,
      phoneticWeight: pWeight,
      pauseWeight: pauseW,
      isPunctuationPause: pauseW > 0,
    };
  });

  const totalScore = scores.reduce((sum, s) => sum + s.phoneticWeight + s.pauseWeight, 0);
  if (totalScore <= 0) return [];

  const timedWords: TimedWord[] = [];
  let currentAccumulator = 0;

  scores.forEach((s, idx) => {
    const vocalDuration = (s.phoneticWeight / totalScore) * duration;
    const pauseDuration = (s.pauseWeight / totalScore) * duration;

    const startTime = currentAccumulator;
    const vocalEndTime = startTime + vocalDuration;
    const endTime = vocalEndTime + pauseDuration;
    currentAccumulator = endTime;

    timedWords.push({
      index: idx,
      word: s.wordItem.word,
      startTime,
      vocalEndTime,
      endTime,
      relLeft: s.wordItem.relLeft,
      relRight: s.wordItem.relRight,
      relBottom: s.wordItem.relBottom,
      width: s.wordItem.width,
      lineIndex: s.wordItem.lineIndex,
      isPunctuationPause: s.isPunctuationPause,
    });
  });

  return timedWords;
}

export function ReadingPencilGuide({
  containerRef,
  activeBlockId,
  activeBlockKey = 0,
  enabled = true,
}: ReadingPencilGuideProps) {
  const cursorRef = useRef<HTMLDivElement | null>(null);
  const trailRef = useRef<HTMLDivElement | null>(null);

  const [isLifting, setIsLifting] = useState(false);
  const [isActiveLayer, setIsActiveLayer] = useState(false);

  const currentBlockIdRef = useRef<string>('');
  const targetElementRef = useRef<HTMLElement | null>(null);
  const timedWordsRef = useRef<TimedWord[]>([]);
  const lastSyncDataRef = useRef<AudioSyncData>(audioSyncBus.getCurrent());
  const pendingTargetIdRef = useRef<string>('');

  const stateRef = useRef({
    curX: 0,
    curY: 0,
    lineStartX: 0,
    lastLineIndex: -1,
    initializedPos: false,
    lastFrameTime: performance.now(),
    liftTimer: null as any,
  });

  // Mede e constrói o modelo do bloco ativo
  const measureTargetElement = useCallback((targetId: string, syncData: AudioSyncData): boolean => {
    if (!targetId) return false;
    const el = document.getElementById(targetId);
    if (!el) return false;

    const { words } = measureBlockWords(el);
    if (words.length === 0) return false;

    targetElementRef.current = el;
    currentBlockIdRef.current = targetId;

    const dur = syncData.duration > 0 ? syncData.duration : 10;
    const model = buildWordTimingModel(words, dur, syncData.acousticProfile);
    timedWordsRef.current = model;

    const s = stateRef.current;
    s.initializedPos = false;
    s.lastLineIndex = -1;
    s.lineStartX = 0;

    setIsLifting(true);
    clearTimeout(s.liftTimer);
    s.liftTimer = setTimeout(() => setIsLifting(false), 180);

    if (trailRef.current) {
      trailRef.current.style.width = '0px';
    }

    if (model.length > 0) {
      const blockRect = el.getBoundingClientRect();
      const first = model[0];
      s.curX = blockRect.left + first.relLeft;
      s.curY = blockRect.top + first.relBottom;
      s.lineStartX = s.curX;
      s.lastLineIndex = first.lineIndex;
      s.initializedPos = true;

      if (cursorRef.current) {
        cursorRef.current.style.transform = `translate3d(${s.curX.toFixed(1)}px, ${s.curY.toFixed(1)}px, 0)`;
      }
    }

    return true;
  }, []);

  // Monitora alterações imediatas do barramento de áudio
  useEffect(() => {
    if (!enabled) return;

    const unsubscribe = audioSyncBus.subscribe((data) => {
      lastSyncDataRef.current = data;
      setIsActiveLayer(data.isPlaying || data.currentTime > 0);

      const targetId = data.blockId || activeBlockId || '';
      if (targetId && targetId !== currentBlockIdRef.current) {
        pendingTargetIdRef.current = targetId;
        measureTargetElement(targetId, data);
      }
    });

    return () => {
      unsubscribe();
    };
  }, [enabled, activeBlockId, measureTargetElement]);

  // Recalcula coordenadas em caso de redimensionamento da janela
  useEffect(() => {
    const handleResize = () => {
      if (currentBlockIdRef.current) {
        measureTargetElement(currentBlockIdRef.current, lastSyncDataRef.current);
      }
    };
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [measureTargetElement]);

  // Loop de animação contínua a 60fps desacoplado do ciclo de render do React
  useEffect(() => {
    if (!enabled) return;

    let rafId: number;

    function tick() {
      const sync = lastSyncDataRef.current;
      const cursor = cursorRef.current;
      const trail = trailRef.current;

      // Verifica se há bloco pendente ou se o bloco mudou
      const desiredBlockId = sync.blockId || activeBlockId || '';
      if (desiredBlockId && desiredBlockId !== currentBlockIdRef.current) {
        measureTargetElement(desiredBlockId, sync);
      }

      const targetEl = targetElementRef.current;
      const words = timedWordsRef.current;

      if (!cursor || !targetEl || words.length === 0 || !sync.isPlaying) {
        rafId = requestAnimationFrame(tick);
        return;
      }

      const curTime = sync.currentTime;
      const blockRect = targetEl.getBoundingClientRect();

      // Localiza a palavra ativa correspondente ao timestamp exato da fala
      let activeWord = words[words.length - 1];
      if (curTime <= words[0].startTime) {
        activeWord = words[0];
      } else {
        for (let i = 0; i < words.length; i++) {
          if (curTime < words[i].endTime || i === words.length - 1) {
            activeWord = words[i];
            break;
          }
        }
      }

      let targetX = blockRect.left + activeWord.relLeft;
      let targetY = blockRect.top + activeWord.relBottom;

      // Fase de vocalização ativa vs repouso na pontuação
      if (curTime < activeWord.vocalEndTime) {
        const span = Math.max(0.001, activeWord.vocalEndTime - activeWord.startTime);
        const frac = Math.min(1, Math.max(0, (curTime - activeWord.startTime) / span));
        targetX = blockRect.left + activeWord.relLeft + activeWord.width * frac;
      } else {
        // Pausa no sinal de pontuação: o lápis repousa exatamente no ponto final/vírgula!
        targetX = blockRect.left + activeWord.relRight;
      }

      const s = stateRef.current;
      const now = performance.now();
      const dt = Math.min(0.1, (now - s.lastFrameTime) / 1000);
      s.lastFrameTime = now;

      if (!s.initializedPos) {
        s.curX = targetX;
        s.curY = targetY;
        s.lineStartX = blockRect.left + activeWord.relLeft;
        s.lastLineIndex = activeWord.lineIndex;
        s.initializedPos = true;
      } else {
        // Mudança de linha: levanta ponta suavemente e zera rastro
        if (activeWord.lineIndex !== s.lastLineIndex) {
          s.lineStartX = blockRect.left + activeWord.relLeft;
          s.lastLineIndex = activeWord.lineIndex;

          setIsLifting(true);
          clearTimeout(s.liftTimer);
          s.liftTimer = setTimeout(() => setIsLifting(false), 170);

          if (trail) {
            trail.style.width = '0px';
          }
        }

        const dist = Math.hypot(targetX - s.curX, targetY - s.curY);
        if (dist > 140) {
          // Salto de seek ou transição de bloco sem arrasto diagonal na página
          s.curX = targetX;
          s.curY = targetY;
          s.lineStartX = blockRect.left + activeWord.relLeft;
          s.lastLineIndex = activeWord.lineIndex;
          if (trail) trail.style.width = '0px';
        } else {
          // Interpolação suave respondendo diretamente à velocidade de reprodução
          const rate = sync.playbackRate || 1;
          const lerpFactor = 1 - Math.exp(-32 * dt * Math.max(0.8, rate));
          s.curX += (targetX - s.curX) * lerpFactor;
          s.curY += (targetY - s.curY) * lerpFactor;
        }
      }

      cursor.style.transform = `translate3d(${s.curX.toFixed(1)}px, ${s.curY.toFixed(1)}px, 0)`;

      if (trail) {
        const startX = Math.min(s.lineStartX, s.curX);
        const width = Math.max(0, s.curX - startX);
        trail.style.transform = `translate3d(${startX.toFixed(1)}px, ${(s.curY - 1).toFixed(1)}px, 0)`;
        trail.style.width = `${width.toFixed(1)}px`;
      }

      rafId = requestAnimationFrame(tick);
    }

    rafId = requestAnimationFrame(tick);

    return () => {
      cancelAnimationFrame(rafId);
    };
  }, [enabled, activeBlockId, measureTargetElement]);

  if (!enabled) return null;

  const isWriting = isActiveLayer && !isLifting;

  return (
    <div
      className={`tts-pencil-layer ${isActiveLayer ? 'is-active' : ''}`}
      aria-hidden="true"
    >
      {/* Rastro fino de grafite editorial sob o texto */}
      <div ref={trailRef} className="tts-pencil-trail" />

      {/* Cursor com o Lápis Animado Monocromático */}
      <div
        ref={cursorRef}
        className={`tts-pencil-cursor ${isWriting ? 'is-writing' : ''} ${isLifting ? 'is-lifting' : ''}`}
      >
        <div className="tts-pencil-rig">
          {/* Ponto de grafite de precisão */}
          <span className="tts-pencil-tip-dot" />

          {/* SVG Fiel do Lápis Editorial */}
          <svg
            className="tts-pencil-svg"
            viewBox="-4 -4 56 56"
            width="44"
            height="44"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g transform="rotate(38 0 0)">
              {/* Sombra de grafite no papel */}
              <path
                d="M 1 2 L 12 6.5 L 45 6.5 L 45 1.5 L 12 1.5 Z"
                fill="rgba(0,0,0,0.12)"
                transform="translate(1.5, 3.5)"
              />

              {/* Ponta de grafite */}
              <polygon
                points="0,0 4.5,-1.8 4.5,1.8"
                className="pencil-lead"
              />

              {/* Madeira apontada cônica */}
              <polygon
                points="4.5,-1.8 11.5,-4.2 11.5,4.2 4.5,1.8"
                className="pencil-wood"
              />
              <path
                d="M 11.5 -4.2 Q 10 -2.1 11.5 0 Q 10 2.1 11.5 4.2"
                className="pencil-wood-collar"
              />

              {/* Corpo hexagonal do lápis */}
              <rect
                x="11.5"
                y="-4.2"
                width="24"
                height="8.4"
                className="pencil-body"
              />

              {/* Facetas de reflexo da madeira/verniz */}
              <line
                x1="11.5"
                y1="-1.5"
                x2="35.5"
                y2="-1.5"
                className="pencil-facet"
              />
              <line
                x1="11.5"
                y1="1.5"
                x2="35.5"
                y2="1.5"
                className="pencil-facet"
              />

              {/* Virola metálica */}
              <rect
                x="35.5"
                y="-4.2"
                width="4.5"
                height="8.4"
                className="pencil-ferrule"
              />
              <line
                x1="37"
                y1="-4.2"
                x2="37"
                y2="4.2"
                className="pencil-ferrule-band"
              />
              <line
                x1="38.5"
                y1="-4.2"
                x2="38.5"
                y2="4.2"
                className="pencil-ferrule-band"
              />

              {/* Borracha editorial na ponta */}
              <path
                d="M 40 -4.2 H 43.5 A 2.2 2.2 0 0 1 45.7 -2 V 2 A 2.2 2.2 0 0 1 43.5 4.2 H 40 Z"
                className="pencil-eraser"
              />
            </g>
          </svg>
        </div>
      </div>
    </div>
  );
}
