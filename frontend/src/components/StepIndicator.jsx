import { motion } from 'framer-motion';

const STEPS = [
  { id: 1, label: 'Identity', emoji: '✨' },
  { id: 2, label: 'Audience', emoji: '🎯' },
  { id: 3, label: 'Vibe', emoji: '🎨' },
  { id: 4, label: 'Colors', emoji: '🌈' },
  { id: 5, label: 'Launch', emoji: '🚀' },
];

export function StepIndicator({ current, total = 5, onSelect, className = '' }) {
  return (
    <div className={`flex items-center justify-center gap-1 sm:gap-2 mb-10 ${className}`}>
      {STEPS.map((step, i) => (
        <div key={step.id} className="flex items-center gap-1 sm:gap-2">
          {/* Dot + label */}
          <button
            onClick={() => i < current && onSelect && onSelect(i)}
            disabled={!(i < current && onSelect)}
            className={`flex items-center gap-1.5 transition-all duration-300 ease-bounce ${
              i < current ? 'cursor-pointer hover:scale-110' : ''
            }`}
          >
            <motion.div
              className={`step-dot flex items-center justify-center text-white text-[10px] font-bold
                ${i === current ? 'active' : ''}
                ${i < current ? 'completed' : ''}
                ${i > current ? 'pending' : ''}
              `}
              whileHover={i < current ? { scale: 1.3 } : {}}
              animate={i === current ? { scale: [1, 1.15, 1] } : {}}
              transition={i === current ? { duration: 1.5, repeat: Infinity } : {}}
            >
              {i < current ? '✓' : step.emoji}
            </motion.div>
            <span
              className={`hidden sm:inline text-xs font-heading font-bold transition-colors duration-300 ${
                i === current
                  ? 'text-accent'
                  : i < current
                  ? 'text-quaternary'
                  : 'text-muted-foreground'
              }`}
            >
              {step.label}
            </span>
          </button>

          {/* Connector line */}
          {i < total - 1 && (
            <div
              className={`step-line w-6 sm:w-10 ${
                i < current ? 'completed' : 'pending'
              }`}
            />
          )}
        </div>
      ))}
    </div>
  );
}
