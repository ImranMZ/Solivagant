import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useTheme } from './_app';
import { generateBrand, twistBrand, downloadBrandKit } from '../utils/api';

const STEPS = [
  { id: 1, label: 'Brand Identity' },
  { id: 2, label: 'Audience & Goals' },
  { id: 3, label: 'Visual Vibe' },
  { id: 4, label: 'Color & Style' },
  { id: 5, label: 'Review & Generate' },
];

const BRAND_VIBES = ['Bold & Energetic', 'Calm & Trustworthy', 'Playful & Fun', 'Luxury & Premium', 'Earthy & Natural'];
const LOGO_STYLES = ['Minimalist', 'Modern', 'Playful', 'Professional', 'Bold', 'Elegant'];
const COLOR_MOODS = [
  { name: 'Ocean Blue', colors: ['#1e3a5f', '#4a90d9', '#7ab8f5', '#e8f4f8', '#0d1b2a'] },
  { name: 'Forest Green', colors: ['#1b4332', '#2d6a4f', '#40916c', '#d8f3dc', '#081c15'] },
  { name: 'Sunset Orange', colors: ['#7f2d0f', '#e85d04', '#f48c06', '#fff3e0', '#370617'] },
  { name: 'Royal Purple', colors: ['#3c096c', '#5a189a', '#7b2cbf', '#f3e8ff', '#10002b'] },
  { name: 'Warm Earth', colors: ['#5c3a21', '#8b5e34', '#c49a6c', '#fef3e2', '#2c1810'] },
  { name: 'Cool Gray', colors: ['#1e293b', '#475569', '#94a3b8', '#f1f5f9', '#0f172a'] },
  { name: 'Cherry Red', colors: ['#800f2f', '#c9184a', '#ff4d6d', '#fff0f3', '#2b0000'] },
  { name: 'Midnight', colors: ['#0a0a1a', '#1a1a3e', '#3a3a7e', '#e0e0ff', '#050510'] },
];
const FONT_STYLES = ['Modern Sans-Serif', 'Classic Serif', 'Playful Display', 'Minimalist'];
const BRAND_VALUES = ['Innovation', 'Quality', 'Sustainability', 'Community', 'Authenticity', 'Simplicity', 'Creativity', 'Reliability'];

function StepIndicator({ current, onSelect }) {
  return (
    <div className="flex items-center justify-center gap-2 mb-8">
      {STEPS.map((step, i) => (
        <button
          key={step.id}
          onClick={() => i < current && onSelect(i)}
          className="flex items-center gap-2"
        >
          <div
            className={`progress-dot ${i === current ? 'active' : ''} ${i < current ? 'completed' : ''}`}
          />
          <span className={`text-sm hidden sm:inline ${i === current ? 'text-brand-600 dark:text-brand-400 font-semibold' : i < current ? 'text-green-600 dark:text-green-400' : 'text-gray-400'}`}>
            {step.label}
          </span>
          {i < STEPS.length - 1 && (
            <div className={`w-8 h-0.5 ${i < current ? 'bg-green-500' : 'bg-gray-300 dark:bg-slate-600'}`} />
          )}
        </button>
      ))}
    </div>
  );
}

function Step1({ data, onChange }) {
  return (
    <div className="step-card max-w-xl mx-auto">
      <h2 className="text-2xl font-bold mb-6 text-gray-900 dark:text-gray-100">Brand Identity</h2>
      <div className="space-y-5">
        <div>
          <label className="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-300">Business Name *</label>
          <input
            className="input-field"
            placeholder="e.g., TechStart"
            value={data.business_name}
            onChange={(e) => onChange('business_name', e.target.value)}
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-300">Tagline *</label>
          <input
            className="input-field"
            placeholder="e.g., Innovating the Future"
            value={data.tagline}
            onChange={(e) => onChange('tagline', e.target.value)}
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-300">Industry *</label>
          <input
            className="input-field"
            placeholder="e.g., Software Development"
            value={data.industry}
            onChange={(e) => onChange('industry', e.target.value)}
            required
          />
        </div>
      </div>
    </div>
  );
}

function Step2({ data, onChange }) {
  const toggleValue = (key, val) => {
    const arr = data[key] || [];
    const next = arr.includes(val) ? arr.filter((v) => v !== val) : [...arr, val];
    onChange(key, next);
  };

  return (
    <div className="step-card max-w-xl mx-auto">
      <h2 className="text-2xl font-bold mb-6 text-gray-900 dark:text-gray-100">Audience & Goals</h2>
      <div className="space-y-5">
        <div>
          <label className="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-300">Target Audience *</label>
          <input
            className="input-field"
            placeholder="e.g., Startup founders aged 25-40"
            value={data.target_audience}
            onChange={(e) => onChange('target_audience', e.target.value)}
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Brand Values (select 2-4) *</label>
          <div className="flex flex-wrap gap-2">
            {BRAND_VALUES.map((v) => (
              <button
                key={v}
                type="button"
                onClick={() => toggleValue('brand_values', v)}
                className={`px-4 py-2 rounded-full text-sm font-medium border transition-all tap-target ${
                  (data.brand_values || []).includes(v)
                    ? 'bg-brand-600 text-white border-brand-600'
                    : 'bg-white dark:bg-slate-700 text-gray-700 dark:text-gray-300 border-gray-300 dark:border-slate-600 hover:border-brand-400'
                }`}
              >
                {v}
              </button>
            ))}
          </div>
        </div>
        <div>
          <label className="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-300">Primary Goal *</label>
          <select
            className="input-field"
            value={data.primary_goal}
            onChange={(e) => onChange('primary_goal', e.target.value)}
            required
          >
            <option value="">Select a goal</option>
            <option value="brand-awareness">Brand Awareness</option>
            <option value="lead-generation">Lead Generation</option>
            <option value="customer-engagement">Customer Engagement</option>
            <option value="sales-conversion">Sales Conversion</option>
            <option value="community-building">Community Building</option>
          </select>
        </div>
        <div>
          <label className="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-300">
            Tone: <span className="font-semibold capitalize">{data.tone}</span>
          </label>
          <input
            type="range"
            min="0"
            max="4"
            value={['formal', 'professional', 'friendly', 'playful', 'humorous'].indexOf(data.tone)}
            onChange={(e) => {
              const tones = ['formal', 'professional', 'friendly', 'playful', 'humorous'];
              onChange('tone', tones[parseInt(e.target.value)]);
            }}
            className="w-full"
          />
          <div className="flex justify-between text-xs text-gray-500 mt-1">
            <span>Formal</span>
            <span>Humorous</span>
          </div>
        </div>
      </div>
    </div>
  );
}

function Step3({ data, onChange }) {
  return (
    <div className="step-card max-w-xl mx-auto">
      <h2 className="text-2xl font-bold mb-6 text-gray-900 dark:text-gray-100">Visual Vibe</h2>
      <div className="space-y-6">
        <div>
          <label className="block text-sm font-medium mb-3 text-gray-700 dark:text-gray-300">Brand Vibe *</label>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {BRAND_VIBES.map((v) => (
              <button
                key={v}
                type="button"
                onClick={() => onChange('brand_vibe', v)}
                className={`p-4 rounded-xl border-2 text-left transition-all tap-target ${
                  data.brand_vibe === v
                    ? 'border-brand-600 bg-brand-50 dark:bg-brand-900/20'
                    : 'border-gray-200 dark:border-slate-600 hover:border-brand-300'
                }`}
              >
                <span className={`font-medium ${data.brand_vibe === v ? 'text-brand-700 dark:text-brand-300' : 'text-gray-800 dark:text-gray-200'}`}>
                  {v}
                </span>
              </button>
            ))}
          </div>
        </div>
        <div>
          <label className="block text-sm font-medium mb-3 text-gray-700 dark:text-gray-300">Logo Style *</label>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {LOGO_STYLES.map((s) => (
              <button
                key={s}
                type="button"
                onClick={() => onChange('logo_style', s)}
                className={`p-3 rounded-xl border-2 text-center transition-all tap-target ${
                  data.logo_style === s
                    ? 'border-brand-600 bg-brand-50 dark:bg-brand-900/20'
                    : 'border-gray-200 dark:border-slate-600 hover:border-brand-300'
                }`}
              >
                <span className={`font-medium text-sm ${data.logo_style === s ? 'text-brand-700 dark:text-brand-300' : 'text-gray-800 dark:text-gray-200'}`}>
                  {s}
                </span>
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function Step4({ data, onChange }) {
  return (
    <div className="step-card max-w-xl mx-auto">
      <h2 className="text-2xl font-bold mb-6 text-gray-900 dark:text-gray-100">Color & Style</h2>
      <div className="space-y-6">
        <div>
          <label className="block text-sm font-medium mb-3 text-gray-700 dark:text-gray-300">Color Mood *</label>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            {COLOR_MOODS.map((m) => (
              <button
                key={m.name}
                type="button"
                onClick={() => onChange('color_mood', m.name)}
                className={`p-4 rounded-xl border-2 transition-all ${
                  data.color_mood === m.name
                    ? 'border-brand-600 ring-2 ring-brand-400'
                    : 'border-gray-200 dark:border-slate-600 hover:border-brand-300'
                }`}
              >
                <div className="flex gap-1 mb-2">
                  {m.colors.map((c, i) => (
                    <div key={i} className="w-4 h-4 rounded-full" style={{ backgroundColor: c }} />
                  ))}
                </div>
                <span className={`text-xs font-medium ${data.color_mood === m.name ? 'text-brand-700 dark:text-brand-300' : 'text-gray-600 dark:text-gray-400'}`}>
                  {m.name}
                </span>
              </button>
            ))}
          </div>
        </div>
        <div>
          <label className="block text-sm font-medium mb-3 text-gray-700 dark:text-gray-300">Font Personality *</label>
          <div className="grid grid-cols-2 gap-3">
            {FONT_STYLES.map((f) => (
              <button
                key={f}
                type="button"
                onClick={() => onChange('font_personality', f)}
                className={`p-4 rounded-xl border-2 text-center transition-all tap-target ${
                  data.font_personality === f
                    ? 'border-brand-600 bg-brand-50 dark:bg-brand-900/20'
                    : 'border-gray-200 dark:border-slate-600 hover:border-brand-300'
                }`}
              >
                <span className={`font-medium text-sm ${data.font_personality === f ? 'text-brand-700 dark:text-brand-300' : 'text-gray-800 dark:text-gray-200'}`}>
                  {f}
                </span>
              </button>
            ))}
          </div>
        </div>
        <div>
          <label className="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-300">Inspiration (optional)</label>
          <textarea
            className="input-field h-24 resize-none"
            placeholder="Describe any inspiration, references, or specific ideas..."
            value={data.inspiration}
            onChange={(e) => onChange('inspiration', e.target.value)}
          />
        </div>
      </div>
    </div>
  );
}

function Step5({ data }) {
  return (
    <div className="step-card max-w-xl mx-auto text-center">
      <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} transition={{ type: 'spring', stiffness: 200 }}>
        <h2 className="text-2xl font-bold mb-2 text-gray-900 dark:text-gray-100">Ready to Generate!</h2>
        <p className="text-gray-500 dark:text-gray-400 mb-6">Review your brand identity summary below</p>
        <div className="text-left space-y-3 bg-gray-50 dark:bg-slate-700/50 rounded-xl p-6">
          <div className="flex justify-between"><span className="text-gray-500">Business:</span><span className="font-semibold">{data.business_name}</span></div>
          <div className="flex justify-between"><span className="text-gray-500">Tagline:</span><span className="font-semibold">{data.tagline}</span></div>
          <div className="flex justify-between"><span className="text-gray-500">Industry:</span><span className="font-semibold">{data.industry}</span></div>
          <div className="flex justify-between"><span className="text-gray-500">Audience:</span><span className="font-semibold">{data.target_audience}</span></div>
          <div className="flex justify-between"><span className="text-gray-500">Values:</span><span className="font-semibold">{(data.brand_values || []).join(', ')}</span></div>
          <div className="flex justify-between"><span className="text-gray-500">Vibe:</span><span className="font-semibold">{data.brand_vibe}</span></div>
          <div className="flex justify-between"><span className="text-gray-500">Colors:</span><span className="font-semibold">{data.color_mood}</span></div>
          <div className="flex justify-between"><span className="text-gray-500">Font:</span><span className="font-semibold">{data.font_personality}</span></div>
        </div>
      </motion.div>
    </div>
  );
}

function BrandScore({ score }) {
  const radius = 45;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (score / 100) * circumference;

  return (
    <div className="flex flex-col items-center">
      <svg width="120" height="120" viewBox="0 0 120 120">
        <circle cx="60" cy="60" r={radius} fill="none" stroke="#e2e8f0" strokeWidth="8" className="dark:stroke-slate-600" />
        <motion.circle
          cx="60" cy="60" r={radius}
          fill="none" stroke="#4c6ef5" strokeWidth="8"
          strokeLinecap="round"
          strokeDasharray={circumference}
          initial={{ strokeDashoffset: circumference }}
          animate={{ strokeDashoffset: offset }}
          transition={{ duration: 1.5, ease: 'easeOut' }}
          transform="rotate(-90 60 60)"
          className="dark:stroke-brand-400"
        />
        <text x="60" y="60" textAnchor="middle" dominantBaseline="central"
          className="fill-gray-900 dark:fill-gray-100 text-2xl font-bold"
        >
          {score}
        </text>
      </svg>
      <p className="text-sm text-gray-500 mt-1 font-medium">Brand Score</p>
    </div>
  );
}

function CollapsibleSection({ title, children, defaultOpen }) {
  const [open, setOpen] = useState(defaultOpen);
  return (
    <div className="section-collapsible">
      <button onClick={() => setOpen(!open)} className="section-header w-full tap-target">
        <h3 className="text-lg font-bold text-gray-900 dark:text-gray-100">{title}</h3>
        <motion.svg animate={{ rotate: open ? 180 : 0 }} className="w-5 h-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </motion.svg>
      </button>
      <AnimatePresence>
        {open && (
          <motion.div initial={{ height: 0, opacity: 0 }} animate={{ height: 'auto', opacity: 1 }} exit={{ height: 0, opacity: 0 }} className="overflow-hidden">
            <div className="p-4 pt-0">{children}</div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

function SocialMockups({ posts }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div className="bg-white dark:bg-slate-700 rounded-xl p-4 border border-gray-200 dark:border-slate-600">
        <div className="flex items-center gap-2 mb-3">
          <div className="w-8 h-8 rounded-full bg-blue-400" />
          <span className="font-semibold text-sm">X (Twitter)</span>
        </div>
        <p className="text-sm text-gray-700 dark:text-gray-300">{posts.twitter}</p>
      </div>
      <div className="bg-white dark:bg-slate-700 rounded-xl p-4 border border-gray-200 dark:border-slate-600">
        <div className="flex items-center gap-2 mb-3">
          <div className="w-8 h-8 rounded-full bg-blue-700" />
          <span className="font-semibold text-sm">LinkedIn</span>
        </div>
        <p className="text-sm text-gray-700 dark:text-gray-300">{posts.linkedin}</p>
      </div>
      <div className="bg-white dark:bg-slate-700 rounded-xl p-4 border border-gray-200 dark:border-slate-600">
        <div className="flex items-center gap-2 mb-3">
          <div className="w-8 h-8 rounded-full bg-pink-500" />
          <span className="font-semibold text-sm">Instagram</span>
        </div>
        <p className="text-sm text-gray-700 dark:text-gray-300">{posts.instagram}</p>
      </div>
    </div>
  );
}

function LogoPlayground({ svg }) {
  const [size, setSize] = useState(160);
  const [bg, setBg] = useState('light');
  const bgColor = bg === 'light' ? '#ffffff' : bg === 'dark' ? '#1e293b' : 'linear-gradient(135deg, #ffffff 50%, #1e293b 50%)';

  const copySvg = () => {
    navigator.clipboard.writeText(svg);
  };

  return (
    <div>
      <div
        className="flex items-center justify-center rounded-xl border-2 border-dashed border-gray-300 dark:border-slate-600 mb-4 transition-all"
        style={{ background: bgColor, minHeight: '280px' }}
      >
        <div
          dangerouslySetInnerHTML={{ __html: svg }}
          style={{ width: size, height: size }}
        />
      </div>
      <div className="flex flex-wrap items-center gap-4">
        <div className="flex items-center gap-2">
          <span className="text-sm text-gray-500">{size}px</span>
          <input
            type="range" min="40" max="240"
            value={size}
            onChange={(e) => setSize(parseInt(e.target.value))}
            className="w-24"
          />
        </div>
        <div className="flex gap-1">
          {['light', 'dark', 'split'].map((b) => (
            <button
              key={b}
              type="button"
              onClick={() => setBg(b)}
              className={`px-3 py-1 text-xs rounded-lg border tap-target ${
                bg === b ? 'bg-brand-600 text-white border-brand-600' : 'bg-white dark:bg-slate-700 text-gray-700 dark:text-gray-300 border-gray-300 dark:border-slate-600'
              }`}
            >
              {b}
            </button>
          ))}
        </div>
        <button onClick={copySvg} className="btn-secondary text-sm py-1 px-3">
          Copy SVG
        </button>
      </div>
    </div>
  );
}

function ColorPaletteEditor({ colors, onChange }) {
  const entries = Object.entries(colors).filter(([k]) => k !== 'background' && k !== 'text');

  return (
    <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
      {entries.map(([name, hex]) => (
        <div key={name} className="text-center">
          <div className="relative inline-block">
            <div
              className="w-16 h-16 rounded-xl shadow-md mx-auto mb-2 border-2 border-gray-200 dark:border-slate-600"
              style={{ backgroundColor: hex }}
            />
            <input
              type="color"
              value={hex}
              onChange={(e) => {
                const next = { ...colors, [name]: e.target.value };
                if (onChange) onChange(next);
              }}
              className="absolute inset-0 w-16 h-16 opacity-0 cursor-pointer mx-auto"
            />
          </div>
          <p className="text-xs text-gray-600 dark:text-gray-400 capitalize">{name}</p>
          <p className="text-xs font-mono text-gray-500">{hex}</p>
        </div>
      ))}
    </div>
  );
}

export default function Home() {
  const { dark, toggleTheme } = useTheme();
  const [step, setStep] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);
  const [formData, setFormData] = useState({
    business_name: '',
    tagline: '',
    industry: '',
    target_audience: '',
    brand_values: [],
    primary_goal: '',
    tone: 'friendly',
    brand_vibe: '',
    logo_style: '',
    color_mood: '',
    font_personality: '',
    inspiration: '',
  });

  const updateField = (key, value) => setFormData((prev) => ({ ...prev, [key]: value }));

  const canProceed = () => {
    switch (step) {
      case 0: return formData.business_name && formData.tagline && formData.industry;
      case 1: return formData.target_audience && formData.brand_values.length >= 2 && formData.brand_values.length <= 4 && formData.primary_goal;
      case 2: return formData.brand_vibe && formData.logo_style;
      case 3: return formData.color_mood && formData.font_personality;
      case 4: return true;
      default: return false;
    }
  };

  const handleGenerate = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await generateBrand(formData);
      setResult(data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Generation failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleTwist = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await twistBrand(formData);
      setResult(data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Twist failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = () => {
    downloadBrandKit(formData);
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-slate-900">
        <div className="text-center">
          <div className="w-16 h-16 border-4 border-brand-600 border-t-transparent rounded-full animate-spin mx-auto" />
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-400 font-medium">Generating your brand...</p>
          <p className="text-sm text-gray-500">This may take up to 30 seconds</p>
        </div>
      </div>
    );
  }

  if (result) {
    return (
      <div className="min-h-screen bg-gray-50 dark:bg-slate-900">
        <header className="bg-white dark:bg-slate-800 shadow-sm border-b border-gray-200 dark:border-slate-700">
          <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">{result.business_name}</h1>
              <p className="text-sm text-gray-500">Brand Score: {result.brand_score}/100</p>
            </div>
            <div className="flex gap-3">
              <button onClick={handleTwist} className="btn-secondary text-sm" disabled={loading}>
                Twist It
              </button>
              <button onClick={handleDownload} className="btn-primary text-sm">
                Download Kit
              </button>
              <button onClick={() => setResult(null)} className="btn-secondary text-sm">
                New Brand
              </button>
              <button onClick={toggleTheme} className="btn-secondary p-2 tap-target">
                {dark ? '☀️' : '🌙'}
              </button>
            </div>
          </div>
        </header>

        <main className="max-w-6xl mx-auto px-4 py-8 space-y-6">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
              <CollapsibleSection title="Logo Preview" defaultOpen={true}>
                <LogoPlayground svg={result.logo?.svg} />
              </CollapsibleSection>

              <div className="mt-6">
                <CollapsibleSection title="Website Preview" defaultOpen={false}>
                  <iframe
                    srcDoc={result.website_content?.html}
                    title="Website Preview"
                    className="w-full h-[500px] border-0 rounded-lg"
                    sandbox="allow-scripts"
                  />
                </CollapsibleSection>
              </div>

              <div className="mt-6">
                <CollapsibleSection title="Social Media Posts" defaultOpen={false}>
                  <SocialMockups posts={result.social_posts} />
                </CollapsibleSection>
              </div>
            </div>

            <div className="space-y-6">
              <div className="card p-6">
                <BrandScore score={result.brand_score} />
              </div>

              <CollapsibleSection title="Color Palette" defaultOpen={true}>
                <ColorPaletteEditor
                  colors={result.colors}
                  onChange={(next) => setResult((prev) => ({ ...prev, colors: next }))}
                />
              </CollapsibleSection>

              <CollapsibleSection title="SEO Metadata" defaultOpen={false}>
                <div className="space-y-3">
                  <div>
                    <label className="block text-xs font-medium text-gray-500 mb-1">Title</label>
                    <p className="text-sm font-medium text-gray-900 dark:text-gray-100">{result.seo_tags?.title}</p>
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-gray-500 mb-1">Description</label>
                    <p className="text-sm text-gray-700 dark:text-gray-300">{result.seo_tags?.description}</p>
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-gray-500 mb-1">Keywords</label>
                    <div className="flex flex-wrap gap-1">
                      {(result.seo_tags?.keywords || []).map((kw, i) => (
                        <span key={i} className="px-2 py-0.5 bg-brand-100 dark:bg-brand-900/30 text-brand-700 dark:text-brand-300 rounded-full text-xs">
                          {kw}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              </CollapsibleSection>

              <CollapsibleSection title="Brand Guide" defaultOpen={false}>
                <div className="prose prose-sm dark:prose-invert max-w-none">
                  <pre className="whitespace-pre-wrap text-sm text-gray-700 dark:text-gray-300 font-sans">
                    {result.brand_guide}
                  </pre>
                </div>
              </CollapsibleSection>
            </div>
          </div>
        </main>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-slate-900">
      <header className="bg-white dark:bg-slate-800 shadow-sm border-b border-gray-200 dark:border-slate-700">
        <div className="max-w-4xl mx-auto px-4 py-4 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">Solivagant</h1>
            <p className="text-sm text-gray-500 dark:text-gray-400">AI Brand Designer</p>
          </div>
          <button onClick={toggleTheme} className="btn-secondary p-2 tap-target">
            {dark ? '☀️' : '🌙'}
          </button>
        </div>
      </header>

      <main className="max-w-4xl mx-auto px-4 py-8">
        <StepIndicator current={step} onSelect={setStep} />

        <AnimatePresence mode="wait">
          <motion.div
            key={step}
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -50 }}
            transition={{ type: 'spring', stiffness: 200, damping: 25 }}
          >
            {step === 0 && <Step1 data={formData} onChange={updateField} />}
            {step === 1 && <Step2 data={formData} onChange={updateField} />}
            {step === 2 && <Step3 data={formData} onChange={updateField} />}
            {step === 3 && <Step4 data={formData} onChange={updateField} />}
            {step === 4 && <Step5 data={formData} />}
          </motion.div>
        </AnimatePresence>

        {error && (
          <div className="mt-4 p-4 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-xl">
            <p className="text-red-600 dark:text-red-400 text-sm">{error}</p>
          </div>
        )}

        <div className="flex justify-between mt-8 max-w-xl mx-auto">
          <button
            onClick={() => setStep((s) => Math.max(0, s - 1))}
            disabled={step === 0}
            className="btn-secondary"
          >
            ← Back
          </button>
          {step < 4 ? (
            <button
              onClick={() => canProceed() && setStep((s) => s + 1)}
              disabled={!canProceed()}
              className="btn-primary"
            >
              Next →
            </button>
          ) : (
            <button onClick={handleGenerate} className="btn-primary">
              Generate My Brand
            </button>
          )}
        </div>
      </main>
    </div>
  );
}
