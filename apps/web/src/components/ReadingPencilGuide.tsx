'use client';

import React, { useEffect, useRef, useState, useCallback } from 'react';

export interface WordEntry {
  startNode: Node;
  startOffset: number;
  endNode: Node;
  endOffset: number;
  wordStr: string;
  phoneticWeight: number;
  pauseWeight: number;
  startWeight: number;
  vocalEndWeight: number;
  endWeight: number;
}

export interface ReadingPencilGuideProps {
  containerRef?: React.RefObject<HTMLElement | null>;
  activeBlockId?: string;
  activeBlockKey?: string | number;
  isPlaying: boolean;
  currentTime: number;
  duration: number;
  isLoading?: boolean;
  enabled?: boolean;
  playbackRate?: number;
}

/**
 * Pondera a duração acústica de pronúncia e as pausas respiratórias da voz sintetizada HeyGen
 */
function computeWordWeights(
  wordStr: string,
  isLastWord: boolean
): { phoneticWeight: number; pauseWeight: number } {
  const cleaned = wordStr.toLowerCase().replace(/[^a-z0-9áéíóúâêîôûãõç]/g, '');

  // Palavras funcionais de transição rápida em português falado (~110-170ms)
  const rapidWords = new Set([
    'a', 'o', 'as', 'os', 'um', 'uma', 'uns', 'umas',
    'de', 'da', 'do', 'das', 'dos',
    'em', 'no', 'na', 'nos', 'nas',
    'e', 'ou', 'mas', 'se', 'que', 'por', 'com', 'sem', 'sob', 'sobre',
    'ja', 'já', 'ao', 'aos', 'me', 'te', 'lhe', 'nos', 'vos'
  ]);

  let phonetic = 2.4; // Piso de articulação da palavra

  if (rapidWords.has(cleaned)) {
    phonetic = 1.5;
  } else if (/^\d+/.test(cleaned)) {
    // Dígitos numéricos ("1º", "2025") levam mais tempo para pronúncia por extenso
    phonetic = Math.max(5.0, cleaned.length * 3.5);
  } else if (/^[A-Z0-9]{2,}$/.test(wordStr.replace(/[^A-Za-z0-9]/g, ''))) {
    // Siglas pronunciadas letra a letra ("ENEM", "MEC", "TRI")
    phonetic = Math.max(4.5, cleaned.length * 2.6);
  } else if (cleaned.length > 0) {
    // Palavra padrão: correlação com sílabas fonéticas
    phonetic = 1.6 + cleaned.length * 0.75;
  }

  // Ponderação das pausas respiratórias da fala
  let pause = 0.5; // Micro-silêncio natural entre palavras (~45ms)

  if (/[.!?…]+['"”’)]*$/.test(wordStr)) {
    // Ponto final, exclamação, interrogação: pausa longa (~750-850ms)
    pause = 10.5;
  } else if (/[,;:—–]+['"”’)]*$/.test(wordStr)) {
    // Vírgula, ponto e vírgula, travessão, dois pontos: pausa média (~380-450ms)
    pause = 5.2;
  } else if (/\.\.\./.test(wordStr)) {
    pause = 9.0;
  }

  if (isLastWord) {
    // Pausa de fechamento do bloco antes da costura com o próximo áudio
    pause += 5.5;
  }

  return { phoneticWeight: phonetic, pauseWeight: pause };
}

/**
 * Mapeia todos os nós de texto dentro do bloco ativo em palavras com nós DOM e pesos acústicos
 */
function parseBlockWords(root: HTMLElement): WordEntry[] {
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

  if (charRefs.length === 0) return [];

  const rawWords: {
    startNode: Node;
    startOffset: number;
    endNode: Node;
    endOffset: number;
    wordStr: string;
  }[] = [];

  let i = 0;
  while (i < charRefs.length) {
    while (i < charRefs.length && /\s/.test(charRefs[i].ch)) i++;
    if (i >= charRefs.length) break;

    const startIdx = i;
    let wordStr = '';
    while (i < charRefs.length && !/\s/.test(charRefs[i].ch)) {
      wordStr += charRefs[i].ch;
      i++;
    }
    const endIdx = i - 1;

    rawWords.push({
      startNode: charRefs[startIdx].node,
      startOffset: charRefs[startIdx].offset,
      endNode: charRefs[endIdx].node,
      endOffset: charRefs[endIdx].offset + 1,
      wordStr,
    });
  }

  if (rawWords.length === 0) return [];

  const LEAD_IN_WEIGHT = 1.2; // Breve respiração inicial antes da primeira sílaba (~80ms)
  let totalWeight = LEAD_IN_WEIGHT;

  const intermediate = rawWords.map((rw, idx) => {
    const isLast = idx === rawWords.length - 1;
    const { phoneticWeight, pauseWeight } = computeWordWeights(rw.wordStr, isLast);
    totalWeight += phoneticWeight + pauseWeight;
    return {
      ...rw,
      phoneticWeight,
      pauseWeight,
    };
  });

  let acc = LEAD_IN_WEIGHT;
  return intermediate.map((item) => {
    const startWeight = acc / totalWeight;
    const phoneticSpan = item.phoneticWeight / totalWeight;
    const vocalEndWeight = startWeight + phoneticSpan;
    acc += item.phoneticWeight + item.pauseWeight;
    const endWeight = acc / totalWeight;

    return {
      startNode: item.startNode,
      startOffset: item.startOffset,
      endNode: item.endNode,
      endOffset: item.endOffset,
      wordStr: item.wordStr,
      phoneticWeight: item.phoneticWeight,
      pauseWeight: item.pauseWeight,
      startWeight,
      vocalEndWeight,
      endWeight,
    };
  });
}

export function ReadingPencilGuide({
  containerRef,
  activeBlockId,
  activeBlockKey = 0,
  isPlaying,
  currentTime,
  duration,
  isLoading = false,
  enabled = true,
  playbackRate = 1,
}: ReadingPencilGuideProps) {
  const cursorRef = useRef<HTMLDivElement | null>(null);
  const trailRef = useRef<HTMLDivElement | null>(null);

  const [words, setWords] = useState<WordEntry[]>([]);
  const [isLifting, setIsLifting] = useState(false);

  // Armazena as propriedades ativas em um Ref para sincronização sem interrupções de rAF
  const livePropsRef = useRef({
    currentTime,
    duration,
    isPlaying,
    isLoading,
    playbackRate,
  });
  livePropsRef.current = {
    currentTime,
    duration,
    isPlaying,
    isLoading,
    playbackRate,
  };

  const wordsRef = useRef<WordEntry[]>([]);
  wordsRef.current = words;

  const targetBlockElementRef = useRef<HTMLElement | null>(null);

  // Posições interpoladas para renderização orgânica 60fps
  const stateRef = useRef({
    curX: 0,
    curY: 0,
    lineStartX: 0,
    lastLineY: -1,
    initializedPos: false,
    lastFrameTime: performance.now(),
    liftTimer: null as any,
  });

  // Localiza e sincroniza o elemento do bloco no DOM
  const resolveTargetBlock = useCallback((): HTMLElement | null => {
    if (activeBlockId) {
      const el = document.getElementById(activeBlockId);
      if (el) return el;
    }
    if (containerRef && containerRef.current) {
      return containerRef.current;
    }
    return null;
  }, [activeBlockId, containerRef]);

  // Atualiza as palavras e reseta coordenadas imediatamente quando o bloco ativo muda
  useEffect(() => {
    if (!enabled) return;

    let retryCount = 0;
    let cancelled = false;

    function scanBlock() {
      if (cancelled) return;
      const el = resolveTargetBlock();
      if (el) {
        targetBlockElementRef.current = el;
        const parsed = parseBlockWords(el);
        setWords(parsed);

        // Reset imediato das coordenadas e levantamento suave do lápis
        const s = stateRef.current;
        s.initializedPos = false;
        s.lastLineY = -1;
        s.lineStartX = 0;

        setIsLifting(true);
        clearTimeout(s.liftTimer);
        s.liftTimer = setTimeout(() => {
          if (!cancelled) setIsLifting(false);
        }, 220);

        if (trailRef.current) {
          trailRef.current.style.width = '0px';
        }
      } else if (retryCount < 5) {
        retryCount++;
        requestAnimationFrame(scanBlock);
      }
    }

    scanBlock();

    return () => {
      cancelled = true;
    };
  }, [activeBlockId, activeBlockKey, enabled, resolveTargetBlock]);

  // Observa mudanças de tamanho de tela ou redimensionamento do bloco para recalcular posições
  useEffect(() => {
    const handleResize = () => {
      const el = targetBlockElementRef.current;
      if (el) {
        const parsed = parseBlockWords(el);
        setWords(parsed);
      }
    };

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  // Loop contínuo de animação a 60fps usando o relógio de alta precisão
  useEffect(() => {
    if (!enabled) return;

    let rafId: number;

    function tick() {
      const {
        currentTime: curTime,
        duration: curDur,
        isPlaying: playing,
        isLoading: loading,
        playbackRate: pRate,
      } = livePropsRef.current;

      const currentWords = wordsRef.current;
      const targetEl = targetBlockElementRef.current;

      if (!cursorRef.current) {
        rafId = requestAnimationFrame(tick);
        return;
      }

      const progress = curDur > 0 ? Math.min(1, Math.max(0, curTime / curDur)) : 0;
      let target: { x: number; y: number; wordLeft: number } | null = null;

      if (currentWords.length > 0) {
        // Encontra a palavra alvo correspondente ao tempo da fala
        let targetWord = currentWords[currentWords.length - 1];

        if (progress < currentWords[0].startWeight) {
          targetWord = currentWords[0];
        } else {
          for (let i = 0; i < currentWords.length; i++) {
            if (progress <= currentWords[i].endWeight || i === currentWords.length - 1) {
              targetWord = currentWords[i];
              break;
            }
          }
        }

        try {
          const range = document.createRange();
          range.setStart(targetWord.startNode, targetWord.startOffset);
          range.setEnd(targetWord.endNode, targetWord.endOffset);
          const rects = range.getClientRects();

          let rect: DOMRect | null = null;
          let targetY = 0;

          if (rects.length > 0) {
            // Caso especial: letra capitular (drop cap) no primeiro parágrafo
            if (rects.length > 1 && rects[0].height > rects[1].height * 1.6) {
              rect = rects[1];
              targetY = rect.bottom + 3;
            } else {
              rect = rects[0];
              targetY = rect.bottom + 3;
            }
          } else {
            const b = range.getBoundingClientRect();
            if (b && b.width > 0) {
              rect = b;
              targetY = b.bottom + 3;
            }
          }

          if (rect && rect.width > 0) {
            // Verifica se a voz está na fase ativa de pronúncia ou na fase de pausa respiratória
            if (progress <= targetWord.vocalEndWeight) {
              const span = Math.max(0.0001, targetWord.vocalEndWeight - targetWord.startWeight);
              const frac = Math.min(1, Math.max(0, (progress - targetWord.startWeight) / span));

              // Se a palavra quebrar entre duas linhas no DOM
              if (rects.length > 1 && !(rects[0].height > rects[1].height * 1.6)) {
                if (frac < 0.5) {
                  rect = rects[0];
                  targetY = rects[0].bottom + 3;
                } else {
                  rect = rects[1];
                  targetY = rects[1].bottom + 3;
                }
              }

              target = {
                x: rect.left + rect.width * frac,
                y: targetY,
                wordLeft: rect.left,
              };
            } else {
              // A voz está em PAUSA no sinal de pontuação: o lápis repousa fixo no fim da palavra!
              if (rects.length > 1 && !(rects[0].height > rects[1].height * 1.6)) {
                rect = rects[rects.length - 1];
                targetY = rect.bottom + 3;
              }
              target = {
                x: rect.right,
                y: targetY,
                wordLeft: rect.left,
              };
            }
          }
        } catch (e) {}
      }

      // Fallback seguro caso o bloco não tenha palavras renderizadas
      if (!target && targetEl) {
        const r = targetEl.getBoundingClientRect();
        target = {
          x: r.left + r.width * progress,
          y: r.top + 28,
          wordLeft: r.left,
        };
      }

      if (target) {
        const s = stateRef.current;
        const now = performance.now();
        const dt = Math.min(0.1, (now - s.lastFrameTime) / 1000);
        s.lastFrameTime = now;

        if (!s.initializedPos) {
          s.curX = target.x;
          s.curY = target.y;
          s.lineStartX = target.wordLeft;
          s.lastLineY = target.y;
          s.initializedPos = true;
        } else {
          // Detecta quebra de linha: levanta suavemente a ponta do lápis
          if (Math.abs(target.y - s.lastLineY) > 12) {
            s.lineStartX = target.wordLeft;
            s.lastLineY = target.y;

            setIsLifting(true);
            clearTimeout(s.liftTimer);
            s.liftTimer = setTimeout(() => setIsLifting(false), 190);

            // Zera temporariamente o rastro para não cruzar linhas
            if (trailRef.current) {
              trailRef.current.style.width = '0px';
            }
          }

          // Se a distância for muito grande (mudança de bloco ou seek > 140px), salta direto sem arrastar
          const dist = Math.hypot(target.x - s.curX, target.y - s.curY);
          if (dist > 140) {
            s.curX = target.x;
            s.curY = target.y;
            s.lineStartX = target.wordLeft;
            s.lastLineY = target.y;
            if (trailRef.current) {
              trailRef.current.style.width = '0px';
            }
          } else {
            // Interpolação adaptativa que responde à velocidade de reprodução
            const rate = pRate || 1;
            const lerpFactor = 1 - Math.exp(-24 * dt * Math.max(0.8, rate));
            s.curX += (target.x - s.curX) * lerpFactor;
            s.curY += (target.y - s.curY) * lerpFactor;
          }
        }

        if (cursorRef.current) {
          cursorRef.current.style.transform = `translate3d(${s.curX.toFixed(1)}px, ${s.curY.toFixed(1)}px, 0)`;
        }

        if (trailRef.current) {
          const startX = Math.min(s.lineStartX, s.curX);
          const width = Math.max(0, s.curX - startX);
          trailRef.current.style.transform = `translate3d(${startX.toFixed(1)}px, ${(s.curY - 1).toFixed(1)}px, 0)`;
          trailRef.current.style.width = `${width.toFixed(1)}px`;
        }
      }

      rafId = requestAnimationFrame(tick);
    }

    rafId = requestAnimationFrame(tick);

    return () => {
      cancelAnimationFrame(rafId);
    };
  }, [enabled]);

  if (!enabled) return null;

  const isActive = isPlaying || isLoading || currentTime > 0;
  const isWriting = isPlaying && !isLoading;
  const isWaiting = (isLoading || !isPlaying) && isActive;

  return (
    <div
      className={`tts-pencil-layer ${isActive ? 'is-active' : ''}`}
      aria-hidden="true"
    >
      {/* Rastro de grafite editorial */}
      <div ref={trailRef} className="tts-pencil-trail" />

      {/* Cursor com o Lápis Animado */}
      <div
        ref={cursorRef}
        className={`tts-pencil-cursor ${isWriting ? 'is-writing' : ''} ${isWaiting ? 'is-waiting' : ''} ${isLifting ? 'is-lifting' : ''}`}
      >
        <div className="tts-pencil-rig">
          {/* Ponto de grafite exato (0,0) */}
          <span className="tts-pencil-tip-dot" />

          {/* SVG Fiel do Lápis Editorial Monocromático */}
          <svg
            className="tts-pencil-svg"
            viewBox="-4 -4 56 56"
            width="44"
            height="44"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g transform="rotate(38 0 0)">
              {/* Sombra projetada no papel */}
              <path
                d="M 1 2 L 12 6.5 L 45 6.5 L 45 1.5 L 12 1.5 Z"
                fill="rgba(0,0,0,0.12)"
                transform="translate(1.5, 3.5)"
              />
              {/* Ponta de grafite */}
              <polygon points="0,0 4.5,-1.8 4.5,1.8" className="pencil-lead" />
              {/* Cone de madeira apontada */}
              <polygon points="4.5,-1.8 11.5,-4.2 11.5,4.2 4.5,1.8" className="pencil-wood" />
              <path d="M 11.5 -4.2 Q 10 -2.1 11.5 0 Q 10 2.1 11.5 4.2" className="pencil-wood-collar" />
              {/* Corpo hexagonal */}
              <rect x="11.5" y="-4.2" width="24" height="8.4" className="pencil-body" />
              <line x1="11.5" y1="-1.5" x2="35.5" y2="-1.5" className="pencil-facet" />
              <line x1="11.5" y1="1.5" x2="35.5" y2="1.5" className="pencil-facet" />
              {/* Virola metálica */}
              <rect x="35.5" y="-4.2" width="4.5" height="8.4" className="pencil-ferrule" />
              <line x1="37" y1="-4.2" x2="37" y2="4.2" className="pencil-ferrule-band" />
              <line x1="38.5" y1="-4.2" x2="38.5" y2="4.2" className="pencil-ferrule-band" />
              {/* Borracha traseira */}
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
