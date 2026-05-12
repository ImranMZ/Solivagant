import { motion } from 'framer-motion';

/**
 * Floating decorative shapes for section backgrounds.
 * Use absolutely positioned behind content (z-0).
 *
 * Variants: 'circle' | 'triangle' | 'square' | 'ring' | 'cross'
 * Colors: maps to theme tokens via inline style.
 */
export function DecorativeShape({
  variant = 'circle',
  color = '#FBBF24',
  size = 40,
  className = '',
  animate = true,
  style = {},
}) {
  const baseClass = className;
  const animationProps = animate
    ? {
        animate: { y: [0, -12, 0] },
        transition: {
          duration: 3,
          repeat: Infinity,
          ease: 'easeInOut',
          delay: Math.random() * 2,
        },
      }
    : {};

  const shapeContent = {
    circle: (
      <div
        className="rounded-full border-2 border-foreground"
        style={{
          width: size,
          height: size,
          backgroundColor: color,
        }}
      />
    ),
    triangle: (
      <svg width={size} height={size} viewBox="0 0 40 40">
        <polygon
          points="20,2 38,38 2,38"
          fill={color}
          stroke="currentColor"
          strokeWidth="2"
          className="text-foreground"
        />
      </svg>
    ),
    square: (
      <div
        className="border-2 border-foreground"
        style={{
          width: size,
          height: size,
          backgroundColor: color,
        }}
      />
    ),
    ring: (
      <div
        className="rounded-full border-[3px] border-foreground bg-transparent"
        style={{
          width: size,
          height: size,
          backgroundColor: 'transparent',
          borderColor: color,
        }}
      />
    ),
    cross: (
      <svg width={size} height={size} viewBox="0 0 40 40">
        <rect x="16" y="2" width="8" height="36" rx="2" fill={color} stroke="currentColor" strokeWidth="1.5" className="text-foreground" />
        <rect x="2" y="16" width="36" height="8" rx="2" fill={color} stroke="currentColor" strokeWidth="1.5" className="text-foreground" />
      </svg>
    ),
    dot: (
      <div
        className="rounded-full"
        style={{
          width: size * 0.4,
          height: size * 0.4,
          backgroundColor: color,
        }}
      />
    ),
  };

  return (
    <motion.div
      className={`absolute pointer-events-none ${baseClass}`}
      style={{ zIndex: 0, ...style }}
      {...animationProps}
    >
      {shapeContent[variant]}
    </motion.div>
  );
}

/**
 * A decorative scatter of confetti shapes for large background areas.
 * Position the parent container as relative + overflow-hidden.
 */
export function ConfettiBackground({ density = 6, className = '' }) {
  const shapes = ['circle', 'triangle', 'square', 'ring', 'cross', 'dot'];
  const colors = ['#8B5CF6', '#F472B6', '#FBBF24', '#34D399'];

  const items = Array.from({ length: density }, (_, i) => ({
    id: i,
    shape: shapes[i % shapes.length],
    color: colors[i % colors.length],
    size: 16 + (i % 5) * 8,
    top: `${(i * 17 + 5) % 90}%`,
    left: `${(i * 23 + 3) % 92}%`,
    delay: i * 0.4,
  }));

  return (
    <div className={`absolute inset-0 overflow-hidden pointer-events-none ${className}`}>
      {items.map((item) => (
        <motion.div
          key={item.id}
          className="absolute"
          style={{ top: item.top, left: item.left }}
          animate={{ y: [0, -12, 0], rotate: [0, item.shape === 'triangle' ? 360 : 0, 0] }}
          transition={{
            duration: 3 + (item.id % 3),
            repeat: Infinity,
            ease: 'easeInOut',
            delay: item.delay,
          }}
        >
          <DecorativeShape
            variant={item.shape}
            color={item.color}
            size={item.size}
            animate={false}
          />
        </motion.div>
      ))}
    </div>
  );
}

/**
 * Squiggly SVG divider — use between sections.
 */
export function SquiggleDivider({ color = '#F472B6', className = '' }) {
  return (
    <div className={`w-full overflow-hidden leading-[0] ${className}`}>
      <svg
        viewBox="0 0 1200 60"
        preserveAspectRatio="none"
        className="w-full h-6"
      >
        <path
          d="M0,30 Q50,0 100,30 T200,30 T300,30 T400,30 T500,30 T600,30 T700,30 T800,30 T900,30 T1000,30 T1100,30 T1200,30"
          fill="none"
          stroke={color}
          strokeWidth="3"
          strokeLinecap="round"
        />
      </svg>
    </div>
  );
}

/**
 * Polka dot pattern as a section background accent.
 */
export function DotPattern({ color = '#F1F5F9', darkColor = '#2D2640', className = '' }) {
  return (
    <div
      className={`absolute inset-0 overflow-hidden pointer-events-none opacity-40 ${className}`}
      style={{
        backgroundImage: `radial-gradient(circle, ${color} 1.5px, transparent 1.5px)`,
        backgroundSize: '20px 20px',
      }}
    />
  );
}
