import { motion } from 'framer-motion';

/**
 * Animated donut chart for brand score.
 */
export function BrandScore({ score = 75, size = 120, className = '' }) {
  const radius = 45;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (score / 100) * circumference;

  const getColor = (s) => {
    if (s >= 80) return '#34D399'; // emerald
    if (s >= 60) return '#FBBF24'; // yellow
    if (s >= 40) return '#F472B6'; // pink
    return '#EF4444'; // red
  };

  const color = getColor(score);

  return (
    <div className={`flex flex-col items-center ${className}`}>
      <svg width={size} height={size} viewBox="0 0 120 120" className="drop-shadow-sm">
        {/* Background track */}
        <circle
          cx="60"
          cy="60"
          r={radius}
          fill="none"
          stroke="currentColor"
          strokeWidth="8"
          className="text-border"
        />
        {/* Score arc */}
        <motion.circle
          cx="60"
          cy="60"
          r={radius}
          fill="none"
          stroke={color}
          strokeWidth="8"
          strokeLinecap="round"
          strokeDasharray={circumference}
          initial={{ strokeDashoffset: circumference }}
          animate={{ strokeDashoffset: offset }}
          transition={{ duration: 1.5, ease: [0.34, 1.56, 0.64, 1] }}
          transform="rotate(-90 60 60)"
        />
        {/* Score text */}
        <text
          x="60"
          y="56"
          textAnchor="middle"
          className="fill-foreground text-2xl font-heading font-extrabold"
          fontFamily="'Outfit', system-ui, sans-serif"
        >
          {score}
        </text>
        <text
          x="60"
          y="74"
          textAnchor="middle"
          className="fill-muted-foreground text-[10px] font-heading font-bold"
          fontFamily="'Outfit', system-ui, sans-serif"
        >
          /100
        </text>
      </svg>
      <p className="label-sm mt-2">Brand Score</p>
    </div>
  );
}
