/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Playful Geometric Palette
        bg: {
          DEFAULT: '#FFFDF5',
          dark: '#1A1625',
        },
        fg: {
          DEFAULT: '#1E293B',
          dark: '#E2E8F0',
        },
        muted: {
          DEFAULT: '#F1F5F9',
          foreground: '#64748B',
          dark: '#2D2640',
          'foreground-dark': '#94A3B8',
        },
        accent: {
          DEFAULT: '#8B5CF6',
          foreground: '#FFFFFF',
          dark: '#A78BFA',
        },
        secondary: {
          DEFAULT: '#F472B6',
          dark: '#F472B6',
        },
        tertiary: {
          DEFAULT: '#FBBF24',
          dark: '#FBBF24',
        },
        quaternary: {
          DEFAULT: '#34D399',
          dark: '#34D399',
        },
        border: {
          DEFAULT: '#E2E8F0',
          dark: '#374151',
        },
        card: {
          DEFAULT: '#FFFFFF',
          dark: '#251E35',
        },
        ring: '#8B5CF6',
        danger: {
          DEFAULT: '#EF4444',
          foreground: '#FFFFFF',
        },
      },
      fontFamily: {
        heading: ['"Outfit"', 'system-ui', 'sans-serif'],
        body: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        sm: '8px',
        md: '16px',
        lg: '24px',
        full: '9999px',
      },
      boxShadow: {
        pop: '4px 4px 0px 0px #1E293B',
        'pop-hover': '6px 6px 0px 0px #1E293B',
        'pop-active': '2px 2px 0px 0px #1E293B',
        'pop-sm': '2px 2px 0px 0px #1E293B',
        'pop-pink': '4px 4px 0px 0px #F472B6',
        'pop-yellow': '4px 4px 0px 0px #FBBF24',
        'pop-green': '4px 4px 0px 0px #34D399',
        'pop-lg': '8px 8px 0px 0px #E2E8F0',
        'pop-dark': '4px 4px 0px 0px #E2E8F0',
      },
      animation: {
        'fade-in': 'fadeIn 0.4s ease-[cubic-bezier(0.34,1.56,0.64,1)] forwards',
        'pop-in': 'popIn 0.4s ease-[cubic-bezier(0.34,1.56,0.64,1)] forwards',
        'slide-up': 'slideUp 0.4s ease-[cubic-bezier(0.34,1.56,0.64,1)] forwards',
        'wiggle': 'wiggle 0.5s ease-in-out',
        'spin-slow': 'spin 3s linear infinite',
        'bounce-in': 'bounceIn 0.6s ease-[cubic-bezier(0.34,1.56,0.64,1)] forwards',
        'marquee': 'marquee 25s linear infinite',
        'float': 'float 3s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        popIn: {
          '0%': { opacity: '0', transform: 'scale(0.5)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(24px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        wiggle: {
          '0%, 100%': { transform: 'rotate(0deg)' },
          '25%': { transform: 'rotate(3deg)' },
          '75%': { transform: 'rotate(-3deg)' },
        },
        bounceIn: {
          '0%': { opacity: '0', transform: 'scale(0.3)' },
          '50%': { transform: 'scale(1.05)' },
          '70%': { transform: 'scale(0.95)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
        marquee: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-12px)' },
        },
      },
      transitionTimingFunction: {
        bounce: 'cubic-bezier(0.34, 1.56, 0.64, 1)',
      },
      backgroundImage: {
        'dot-grid': "radial-gradient(circle, #CBD5E1 1px, transparent 1px)",
      },
      backgroundSize: {
        'dot-grid': '24px 24px',
      },
    },
  },
  plugins: [],
};
