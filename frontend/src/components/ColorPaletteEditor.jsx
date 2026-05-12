import { motion } from 'framer-motion';

/**
 * Editable color palette display — click a swatch to pick a new color.
 */
export function ColorPaletteEditor({ colors = {}, onChange, className = '' }) {
  const entries = Object.entries(colors).filter(
    ([k]) => k !== 'background' && k !== 'text'
  );

  return (
    <div className={`grid grid-cols-2 sm:grid-cols-3 gap-4 ${className}`}>
      {entries.map(([name, hex], i) => (
        <motion.div
          key={name}
          className="text-center"
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: i * 0.08, ease: [0.34, 1.56, 0.64, 1] }}
        >
          <div className="relative inline-block group">
            <div
              className="color-swatch cursor-pointer"
              style={{ backgroundColor: hex }}
            />
            <input
              type="color"
              value={hex}
              onChange={(e) => {
                if (onChange) onChange({ ...colors, [name]: e.target.value });
              }}
              className="absolute inset-0 w-16 h-16 opacity-0 cursor-pointer"
              title={`Change ${name} color`}
            />
          </div>
          <p className="label-sm mt-2 capitalize">{name}</p>
          <p className="text-xs font-mono text-muted-foreground">{hex}</p>
        </motion.div>
      ))}
    </div>
  );
}
