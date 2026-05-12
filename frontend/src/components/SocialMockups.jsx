import { motion } from 'framer-motion';

/**
 * Social media post mockups — each styled like the actual platform.
 */
export function SocialMockups({ posts, className = '' }) {
  const platforms = [
    {
      name: 'X (Twitter)',
      color: '#1DA1F2',
      text: posts?.twitter,
      icon: '𝕏',
    },
    {
      name: 'LinkedIn',
      color: '#0A66C2',
      text: posts?.linkedin,
      icon: 'in',
    },
    {
      name: 'Instagram',
      color: '#E1306C',
      text: posts?.instagram,
      icon: '📷',
    },
  ];

  return (
    <div className={`grid grid-cols-1 md:grid-cols-3 gap-4 ${className}`}>
      {platforms.map((p, i) => (
        <motion.div
          key={p.name}
          className="bg-card border-2 border-foreground rounded-xl p-4 shadow-pop-sm"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: i * 0.1, ease: [0.34, 1.56, 0.64, 1] }}
          whileHover={{ rotate: i === 0 ? -1 : i === 2 ? 1 : 0, scale: 1.02 }}
        >
          <div className="flex items-center gap-2 mb-3">
            <div
              className="w-8 h-8 rounded-full flex items-center justify-center text-white text-xs font-bold border-2 border-foreground"
              style={{ backgroundColor: p.color }}
            >
              {p.icon}
            </div>
            <span className="font-heading font-bold text-sm text-foreground">
              {p.name}
            </span>
          </div>
          <p className="text-sm text-muted-foreground leading-relaxed">
            {p.text || 'No content generated'}
          </p>
        </motion.div>
      ))}
    </div>
  );
}
