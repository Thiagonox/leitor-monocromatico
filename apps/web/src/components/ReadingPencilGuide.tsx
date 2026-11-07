'use client';

import React, { useEffect, useRef, useState } from 'react';

interface WordEntry {
  startNode: Node;
  startOffset: number;
  endNode: Node;
  endOffset: number;
  weight: number;
  startWeight: number;
  endWeight: number;
}

interface ReadingPencilGuideProps {
  containerRef: React.RefObject<HTMLElement | null>;
  isPlaying: boolean;
  currentTime: number;
  duration: number;
  isLoading?: boolean;
  enabled?: boolean;
  activeBlockKey?: string | number;
}

export function ReadingPencilGuide({
  containerRef,
  isPlaying,
  currentTime,
  duration,
  isLoading = false,
  enabled = true,
  activeBlockKey = 0,
}: ReadingPencilGuideProps) {
  const cursorRef = useRef<HTMLDivElement | null>(null);
  const trailRef = useRef<HTMLDivElement | null>(null);

  const [words, setWords] = useState<WordEntry[]>([]);
  const [isLifting, setIsLifting] = useState(false);

  // Posições interpoladas para renderização orgânica 60fps
  const stateRef = useRef({
    curX: 0,
    curY: 0,
    lineStartX: 0,
    lastLineY: -1,
    initializedPos: false,
    lastAutoScrollAt: 0,
    liftTimer: null as any,
  });

  // Mapeia o texto do container em palavras com ponderação temporal
  useEffect(() => {
    if (!containerRef.current) return;

    const root = containerRef.current;
    const charRefs: { node: Node; offset: number; ch: string }[] = [];

    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        const parent = node.parentElement;
        if (!parent) return NodeFilter.FILTER_REJECT;
        if (
          parent.closest('button') ||
          parent.closest('.no-reading-guide') ||
          parent.closest('nav')
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

    const wordList: WordEntry[] = [];
    let i = 0;
    let totalWeight = 0;

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

      // Pondera a duração da fala e pontuações
      let weight = Math.max(1, wordStr.length) + 0.8;
      if (/[,;:—–]$/.test(wordStr)) weight += 3.2;
      else if (/[.!?…]$/.test(wordStr)) weight += 5.5;

      wordList.push({
        startNode: charRefs[startIdx].node,
        startOffset: charRefs[startIdx].offset,
        endNode: charRefs[endIdx].node,
        endOffset: charRefs[endIdx].offset + 1,
        weight,
        startWeight: 0,
        endWeight: 1,
      });
      totalWeight += weight;
    }

    if (totalWeight > 0) {
      let acc = 0;
      for (const w of wordList) {
        w.startWeight = acc / totalWeight;
        acc += w.weight;
        w.endWeight = acc / totalWeight;
      }
    }

    setWords(wordList);
  }, [containerRef, activeBlockKey]);

  // Loop de Animação contínua (rAF) para suavidade máxima
  useEffect(() => {
    if (!enabled) return;

    let rafId: number;

    const progress = duration > 0 ? Math.min(1, Math.max(0, currentTime / duration)) : 0;

    function tick() {
      if (!cursorRef.current) return;

      let target: { x: number; y: number; wordLeft: number } | null = null;

      if (words.length > 0) {
        let targetWord = words[words.length - 1];
        for (let i = 0; i < words.length; i++) {
          if (progress <= words[i].endWeight) {
            targetWord = words[i];
            break;
          }
        }

        try {
          const range = document.createRange();
          range.setStart(targetWord.startNode, targetWord.startOffset);
          range.setEnd(targetWord.endNode, targetWord.endOffset);
          const rects = range.getClientRects();
          const rect = rects.length > 0 ? rects[0] : range.getBoundingClientRect();

          if (rect && rect.width > 0) {
            const span = Math.max(0.0001, targetWord.endWeight - targetWord.startWeight);
            const wordFrac = Math.min(1, Math.max(0, (progress - targetWord.startWeight) / span));
            target = {
              x: rect.left + rect.width * wordFrac,
              y: rect.bottom + 3,
              wordLeft: rect.left,
            };
          }
        } catch (e) {}
      }

      if (!target && containerRef.current) {
        const r = containerRef.current.getBoundingClientRect();
        target = {
          x: r.left + r.width * progress,
          y: r.top + 28,
          wordLeft: r.left,
        };
      }

      if (target) {
        const s = stateRef.current;
        if (!s.initializedPos) {
          s.curX = target.x;
          s.curY = target.y;
          s.lineStartX = target.wordLeft;
          s.lastLineY = target.y;
          s.initializedPos = true;
        } else {
          // Detecta quebra de linha: levanta suavemente a ponta do lápis
          if (Math.abs(target.y - s.lastLineY) > 10) {
            s.lineStartX = target.wordLeft;
            s.lastLineY = target.y;

            setIsLifting(true);
            clearTimeout(s.liftTimer);
            s.liftTimer = setTimeout(() => setIsLifting(false), 190);

            // Auto-scroll para manter a linha lida centralizada
            const now = performance.now();
            if (now - s.lastAutoScrollAt > 700) {
              const viewH = window.innerHeight;
              if (target.y > viewH - 145 || target.y < 105) {
                s.lastAutoScrollAt = now;
                window.scrollBy({
                  top: target.y - viewH * 0.42,
                  behavior: 'smooth',
                });
              }
            }
          }

          // Interpolação suave simulando mão humana acompanhando a leitura
          s.curX += (target.x - s.curX) * 0.28;
          s.curY += (target.y - s.curY) * 0.25;
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
  }, [enabled, words, currentTime, duration, containerRef]);

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
