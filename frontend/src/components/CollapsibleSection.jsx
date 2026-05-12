import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

/**
 * Collapsible section with bouncy animation.
 */
export function CollapsibleSection({
  title,
  children,
  defaultOpen = false,
  icon = null,
  className = '',
}) {
  const [open, setOpen] = useState(defaultOpen);

  return (
    <div className={`section-collapsible ${className}`}>
      <button
        onClick={() => setOpen(!open)}
        className="section-header w-full tap-target"
      >
        <div className="flex items-center gap-2">
          {icon && <span className="text-lg">{icon}</span>}
          <h3 className="text-lg font-heading font-bold text-foreground">
            {title}
          </h3>
        </div>
        <motion.svg
          animate={{ rotate: open ? 180 : 0 }}
          transition={{ ease: [0.34, 1.56, 0.64, 1], duration: 0.3 }}
          className="w-5 h-5 text-muted-foreground"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2.5}
            d="M19 9l-7 7-7-7"
          />
        </motion.svg>
      </button>
      <AnimatePresence initial={false}>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ ease: [0.34, 1.56, 0.64, 1], duration: 0.35 }}
            className="overflow-hidden"
          >
            <div className="p-4 pt-0">{children}</div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
