import { useState, useEffect, createContext, useContext } from 'react';
import '../styles/globals.css';

const ThemeContext = createContext();

export function useTheme() {
  return useContext(ThemeContext);
}

export default function App({ Component, pageProps }) {
  const [dark, setDark] = useState(false);

  useEffect(() => {
    const stored = localStorage.getItem('solivagant-theme');
    if (stored === 'dark' || (!stored && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      setDark(true);
      document.documentElement.classList.add('dark');
    }
  }, []);

  const toggleTheme = () => {
    setDark((prev) => {
      const next = !prev;
      localStorage.setItem('solivagant-theme', next ? 'dark' : 'light');
      document.documentElement.classList.toggle('dark', next);
      return next;
    });
  };

  return (
    <ThemeContext.Provider value={{ dark, toggleTheme }}>
      <Component {...pageProps} />
    </ThemeContext.Provider>
  );
}
