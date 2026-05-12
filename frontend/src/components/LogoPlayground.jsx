import { useState } from 'react';
import { motion } from 'framer-motion';

/**
 * Interactive logo playground — resize, change background, copy SVG.
 */
export function LogoPlayground({ svg, className = '' }) {
  const [size, setSize] = useState(160);
  const [bg, setBg] = useState('light');
  const [copied, setCopied] = useState(false);

  const bgStyles = {
    light: '#ffffff',
    dark: '#1E293B',
    gradient: 'linear-gradient(135deg, #ffffff 50%, #1E293B 50%)',
  };

  const copySvg = async () => {
    if (svg) {
      await navigator.clipboard.writeText(svg);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  return (
    <div className={`space-y-5 ${className}`}>
      {/* Preview area */}
      <motion.div
        className="flex items-center justify-center rounded-xl border-2 border-dashed border-border p-8"
        style={{ background: bgStyles[bg], minHeight: 280 }}
        layout
      >
        {svg && (
          <motion.div
            dangerouslySetInnerHTML={{ __html: svg }}
            style={{ width: size, height: size }}
          />
        )}
      </motion.div>

      {/* Controls */}
      <div className="flex flex-wrap items-center gap-4">
        {/* Size slider */}
        <div className="flex items-center gap-2">
          <span className="label-sm">{size}px</span>
          <input
            type="range"
            min="40"
            max="240"
            value={size}
            onChange={(e) => setSize(parseInt(e.target.value))}
            className="w-28 h-2 bg-border rounded-full appearance-none cursor-pointer accent-accent"
          />
        </div>

        {/* Background toggles */}
        <div className="flex gap-1 border-2 border-foreground rounded-full p-0.5">
          {['light', 'dark', 'gradient'].map((b) => (
            <button
              key={b}
              type="button"
              onClick={() => setBg(b)}
              className={`px-3 py-1 text-xs font-heading font-bold rounded-full transition-all duration-200 ${
                bg === b
                  ? 'bg-foreground text-card'
                  : 'text-foreground hover:bg-muted'
              }`}
            >
              {b.charAt(0).toUpperCase() + b.slice(1)}
            </button>
          ))}
        </div>

        {/* Copy button */}
        <motion.button
          onClick={copySvg}
          className="btn-secondary text-sm py-1.5 px-4"
          whileTap={{ scale: 0.95 }}
        >
          {copied ? '✓ Copied!' : 'Copy SVG'}
        </motion.button>
      </div>
    </div>
  );
}
