'use client';

import React, { useEffect, useState } from 'react';

interface ReadingRulerProps {
  isActive: boolean;
  rulerHeight?: number;
}

export function ReadingRuler({ isActive, rulerHeight = 84 }: ReadingRulerProps) {
  const [windowY, setWindowY] = useState(250);

  useEffect(() => {
    if (!isActive) return;

    const handleMouseMove = (e: MouseEvent) => {
      const top = Math.max(0, e.clientY - rulerHeight / 2);
      setWindowY(top);
    };

    window.addEventListener('mousemove', handleMouseMove, { passive: true });
    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
    };
  }, [isActive, rulerHeight]);

  if (!isActive) return null;

  const topHeight = windowY;
  const bottomTop = windowY + rulerHeight;

  return (
    <div className="reading-ruler-overlay" aria-hidden="true">
      <div className="reading-ruler-mask-top" style={{ height: `${topHeight}px` }} />
      <div
        className="reading-ruler-window"
        style={{ top: `${topHeight}px`, height: `${rulerHeight}px` }}
      />
      <div className="reading-ruler-mask-bottom" style={{ top: `${bottomTop}px` }} />
    </div>
  );
}
