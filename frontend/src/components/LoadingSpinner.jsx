import { motion } from 'framer-motion';

/**
 * Playful loading spinner — bouncing shapes instead of a boring circle.
 */
export function LoadingSpinner({ message = 'Generating your brand...', className = '' }) {
  const shapes = [
    { color: '#8B5CF6', delay: 0 },
    { color: '#F472B6', delay: 0.15 },
    { color: '#FBBF24', delay: 0.3 },
    { color: '#34D399', delay: 0.45 },
  ];

  return (
    <div className={`flex flex-col items-center justify-center gap-6 ${className}`}>
      {/* Bouncing dots */}
      <div className="flex items-end gap-2 h-12">
        {shapes.map((s, i) => (
          <motion.div
            key={i}
            className="w-4 h-4 rounded-full border-2 border-foreground"
            style={{ backgroundColor: s.color }}
            animate={{
              y: [0, -24, 0],
              scale: [1, 1.2, 1],
            }}
            transition={{
              duration: 0.8,
              repeat: Infinity,
              delay: s.delay,
              ease: [0.34, 1.56, 0.64, 1],
            }}
          />
        ))}
      </div>

      {/* Message */}
      <div className="text-center">
        <motion.p
          className="text-lg font-heading font-bold text-foreground"
          animate={{ opacity: [0.5, 1, 0.5] }}
          transition={{ duration: 2, repeat: Infinity }}
        >
          {message}
        </motion.p>
        <p className="text-sm text-muted-foreground mt-1">This may take up to 30 seconds</p>
      </div>
    </div>
  );
}
