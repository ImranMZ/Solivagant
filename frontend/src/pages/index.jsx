import { useState, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useTheme } from './_app';
import { generateBrand, twistBrand, downloadBrandKit } from '../utils/api';
import {
  StepIndicator, BrandScore, LoadingSpinner, CollapsibleSection,
  SocialMockups, LogoPlayground, ColorPaletteEditor, ConfettiBackground, DecorativeShape,
} from '../components';

const BRAND_VIBES = [
  { label: 'Bold & Energetic', emoji: '⚡', desc: 'High-impact, dynamic, action-oriented' },
  { label: 'Calm & Trustworthy', emoji: '🌿', desc: 'Serene, reliable, professional' },
  { label: 'Playful & Fun', emoji: '🎉', desc: 'Cheerful, approachable, creative' },
  { label: 'Luxury & Premium', emoji: '💎', desc: 'Elegant, exclusive, refined' },
  { label: 'Earthy & Natural', emoji: '🌍', desc: 'Organic, grounded, sustainable' },
];
const LOGO_STYLES = [
  { label: 'Minimalist', emoji: '◯', desc: 'Clean lines, lots of whitespace' },
  { label: 'Modern', emoji: '△', desc: 'Bold shapes, contemporary feel' },
  { label: 'Playful', emoji: '★', desc: 'Rounded, bright, fun character' },
  { label: 'Professional', emoji: '▢', desc: 'Symmetrical, balanced, trustworthy' },
  { label: 'Bold', emoji: '⬡', desc: 'Thick strokes, strong contrast' },
  { label: 'Elegant', emoji: '◇', desc: 'Thin lines, refined, graceful' },
];
const COLOR_MOODS = [
  { name: 'Ocean Blue', emoji: '🌊', colors: ['#1e3a5f', '#4a90d9', '#7ab8f5', '#e8f4f8', '#0d1b2a'] },
  { name: 'Forest Green', emoji: '🌲', colors: ['#1b4332', '#2d6a4f', '#40916c', '#d8f3dc', '#081c15'] },
  { name: 'Sunset Orange', emoji: '🌅', colors: ['#7f2d0f', '#e85d04', '#f48c06', '#fff3e0', '#370617'] },
  { name: 'Royal Purple', emoji: '👑', colors: ['#3c096c', '#5a189a', '#7b2cbf', '#f3e8ff', '#10002b'] },
  { name: 'Warm Earth', emoji: '🏔️', colors: ['#5c3a21', '#8b5e34', '#c49a6c', '#fef3e2', '#2c1810'] },
  { name: 'Cool Gray', emoji: '🪨', colors: ['#1e293b', '#475569', '#94a3b8', '#f1f5f9', '#0f172a'] },
  { name: 'Cherry Red', emoji: '🍒', colors: ['#800f2f', '#c9184a', '#ff4d6d', '#fff0f3', '#2b0000'] },
  { name: 'Midnight', emoji: '🌙', colors: ['#0a0a1a', '#1a1a3e', '#3a3a7e', '#e0e0ff', '#050510'] },
  { name: 'Coral Pink', emoji: '🪸', colors: ['#9f1239', '#fb7185', '#fda4af', '#fff1f2', '#4c0519'] },
  { name: 'Teal Wave', emoji: '🐚', colors: ['#134e4a', '#14b8a6', '#5eead4', '#f0fdfa', '#042f2e'] },
  { name: 'Golden Hour', emoji: '✨', colors: ['#78350f', '#f59e0b', '#fcd34d', '#fffbeb', '#451a03'] },
  { name: 'Lavender Mist', emoji: '💜', colors: ['#4c1d95', '#8b5cf6', '#c4b5fd', '#f5f3ff', '#2e1065'] },
];
const FONT_STYLES = [
  { label: 'Modern Sans-Serif', emoji: 'Aa', desc: 'Clean, geometric, highly readable' },
  { label: 'Classic Serif', emoji: 'Aa', desc: 'Timeless, authoritative, elegant' },
  { label: 'Playful Display', emoji: 'Aa', desc: 'Rounded, friendly, personality-driven' },
  { label: 'Minimalist', emoji: 'Aa', desc: 'Ultra-clean, spacious, refined' },
];
const BRAND_VALUES_LIST = [
  { label: 'Innovation', emoji: '💡' },
  { label: 'Quality', emoji: '⭐' },
  { label: 'Sustainability', emoji: '🌱' },
  { label: 'Community', emoji: '🤝' },
  { label: 'Authenticity', emoji: '💎' },
  { label: 'Simplicity', emoji: '◯' },
  { label: 'Creativity', emoji: '🎨' },
  { label: 'Reliability', emoji: '🛡️' },
];

function CopyButton({ text, label = 'Copy' }) {
  const [copied, setCopied] = useState(false);
  const handleCopy = useCallback(async () => {
    if (!text) return;
    try { await navigator.clipboard.writeText(text); } catch { /* fallback ignored */ }
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }, [text]);
  return (
    <button onClick={handleCopy} title={`Copy ${label.toLowerCase()}`}
      className="inline-flex items-center gap-1 px-2.5 py-1 text-[10px] font-heading font-bold rounded-full border-2 border-foreground/15 bg-card hover:bg-accent/10 hover:border-accent/30 transition-all duration-200">
      {copied ? '✓ Copied' : `📋 ${label}`}
    </button>
  );
}

function Step1({ data, onChange }) {
  return (
    <motion.div className="card-step max-w-xl mx-auto" initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ ease: [0.34, 1.56, 0.64, 1] }}>
      <div className="flex items-center gap-3 mb-2"><span className="text-3xl">✨</span><h2 className="text-2xl font-heading font-extrabold text-foreground">Brand Identity</h2></div>
      <p className="text-sm text-muted-foreground mb-6 ml-12">Tell us about your business.</p>
      <div className="space-y-5">
        <div><label className="input-label">Business Name *</label><input className="input-field text-lg font-heading font-bold" placeholder="e.g., TechStart" value={data.business_name} onChange={(e) => onChange('business_name', e.target.value)} /></div>
        <div><label className="input-label">Tagline *</label><input className="input-field" placeholder="e.g., Innovating the Future" value={data.tagline} onChange={(e) => onChange('tagline', e.target.value)} /></div>
        <div><label className="input-label">Industry *</label><input className="input-field" placeholder="e.g., Software Development, Healthcare" value={data.industry} onChange={(e) => onChange('industry', e.target.value)} /></div>
      </div>
    </motion.div>
  );
}

function Step2({ data, onChange }) {
  const toggleValue = (key, val) => {
    const arr = data[key] || [];
    onChange(key, arr.includes(val) ? arr.filter((v) => v !== val) : [...arr, val]);
  };
  return (
    <motion.div className="card-step max-w-xl mx-auto" initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ ease: [0.34, 1.56, 0.64, 1] }}>
      <div className="flex items-center gap-3 mb-2"><span className="text-3xl">🎯</span><h2 className="text-2xl font-heading font-extrabold text-foreground">Audience & Goals</h2></div>
      <p className="text-sm text-muted-foreground mb-6 ml-12">Who are you talking to, and what do you want to achieve?</p>
      <div className="space-y-5">
        <div><label className="input-label">Target Audience *</label><input className="input-field" placeholder="e.g., Startup founders aged 25-40" value={data.target_audience} onChange={(e) => onChange('target_audience', e.target.value)} /></div>
        <div>
          <label className="input-label">Brand Values (select 2-4) *</label>
          <div className="flex flex-wrap gap-2">
            {BRAND_VALUES_LIST.map((v) => {
              const sel = (data.brand_values || []).includes(v.label);
              return (<button key={v.label} type="button" onClick={() => toggleValue('brand_values', v.label)} className={`inline-flex items-center gap-1.5 px-4 py-2.5 rounded-full text-sm font-heading font-bold border-2 transition-all duration-300 ease-bounce tap-target ${sel ? 'bg-accent text-white border-foreground shadow-pop-sm' : 'bg-card text-foreground border-border hover:border-accent hover:bg-accent/5'}`}><span>{v.emoji}</span>{v.label}</button>);
            })}
          </div>
          <p className="text-xs text-muted-foreground mt-2">{(data.brand_values || []).length}/4 selected{(data.brand_values || []).length < 2 ? ' — pick at least 2' : ''}</p>
        </div>
        <div>
          <label className="input-label">Primary Goal *</label>
          <select className="input-field" value={data.primary_goal} onChange={(e) => onChange('primary_goal', e.target.value)}>
            <option value="">Select your primary goal</option>
            <option value="brand-awareness">📣 Brand Awareness</option>
            <option value="lead-generation">🎣 Lead Generation</option>
            <option value="customer-engagement">💬 Customer Engagement</option>
            <option value="sales-conversion">💰 Sales Conversion</option>
            <option value="community-building">🤝 Community Building</option>
          </select>
        </div>
        <div>
          <label className="input-label">Brand Tone: <span className="text-foreground capitalize font-extrabold text-base">{data.tone}</span></label>
          <input type="range" min="0" max="4" value={['formal', 'professional', 'friendly', 'playful', 'humorous'].indexOf(data.tone)} onChange={(e) => { const t = ['formal', 'professional', 'friendly', 'playful', 'humorous']; onChange('tone', t[parseInt(e.target.value)]); }} className="w-full h-2 bg-border rounded-full appearance-none cursor-pointer accent-accent" />
          <div className="flex justify-between text-[10px] text-muted-foreground mt-1.5 font-heading font-bold uppercase tracking-wider"><span>Formal</span><span>Professional</span><span>Friendly</span><span>Playful</span><span>Humorous</span></div>
        </div>
      </div>
    </motion.div>
  );
}

function Step3({ data, onChange }) {
  return (
    <motion.div className="card-step max-w-xl mx-auto" initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ ease: [0.34, 1.56, 0.64, 1] }}>
      <div className="flex items-center gap-3 mb-2"><span className="text-3xl">🎨</span><h2 className="text-2xl font-heading font-extrabold text-foreground">Visual Vibe</h2></div>
      <p className="text-sm text-muted-foreground mb-6 ml-12">How should your brand feel at a glance?</p>
      <div className="space-y-6">
        <div>
          <label className="input-label">Brand Vibe *</label>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {BRAND_VIBES.map((v) => (
              <button key={v.label} type="button" onClick={() => onChange('brand_vibe', v.label)} className={`p-4 rounded-xl border-2 text-left transition-all duration-300 ease-bounce tap-target ${data.brand_vibe === v.label ? 'border-accent bg-accent/5 shadow-pop-sm' : 'border-border hover:border-accent/40 bg-card'}`}>
                <div className="flex items-center gap-2.5 mb-1"><span className="text-xl">{v.emoji}</span><span className={`font-heading font-bold text-sm ${data.brand_vibe === v.label ? 'text-accent' : 'text-foreground'}`}>{v.label}</span></div>
                <p className="text-xs text-muted-foreground ml-8">{v.desc}</p>
              </button>
            ))}
          </div>
        </div>
        <div>
          <label className="input-label">Logo Style *</label>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {LOGO_STYLES.map((s) => (
              <button key={s.label} type="button" onClick={() => onChange('logo_style', s.label)} className={`p-3 rounded-xl border-2 text-center transition-all duration-300 ease-bounce tap-target ${data.logo_style === s.label ? 'border-accent bg-accent/5 shadow-pop-sm' : 'border-border hover:border-accent/40 bg-card'}`}>
                <span className="text-xl block mb-1">{s.emoji}</span>
                <span className={`font-heading font-bold text-sm block ${data.logo_style === s.label ? 'text-accent' : 'text-foreground'}`}>{s.label}</span>
                <span className="text-[10px] text-muted-foreground block mt-0.5 leading-tight">{s.desc}</span>
              </button>
            ))}
          </div>
        </div>
      </div>
    </motion.div>
  );
}

function Step4({ data, onChange }) {
  return (
    <motion.div className="card-step max-w-xl mx-auto" initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ ease: [0.34, 1.56, 0.64, 1] }}>
      <div className="flex items-center gap-3 mb-2"><span className="text-3xl">🌈</span><h2 className="text-2xl font-heading font-extrabold text-foreground">Color & Style</h2></div>
      <p className="text-sm text-muted-foreground mb-6 ml-12">Choose your visual direction.</p>
      <div className="space-y-6">
        <div>
          <label className="input-label">Color Mood *</label>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {COLOR_MOODS.map((m) => (
              <button key={m.name} type="button" onClick={() => onChange('color_mood', m.name)} className={`p-3 rounded-xl border-2 transition-all duration-300 ease-bounce ${data.color_mood === m.name ? 'border-accent ring-2 ring-accent/20 shadow-pop-sm' : 'border-border hover:border-accent/40 bg-card'}`}>
                <div className="flex gap-1 mb-2 justify-center">{m.colors.map((c, i) => (<div key={i} className="w-5 h-5 rounded-full border border-foreground/10" style={{ backgroundColor: c }} />))}</div>
                <div className="flex items-center justify-center gap-1.5"><span className="text-sm">{m.emoji}</span><span className={`text-xs font-heading font-bold ${data.color_mood === m.name ? 'text-accent' : 'text-foreground'}`}>{m.name}</span></div>
              </button>
            ))}
          </div>
        </div>
        <div>
          <label className="input-label">Font Personality *</label>
          <div className="grid grid-cols-2 gap-3">
            {FONT_STYLES.map((f) => (
              <button key={f.label} type="button" onClick={() => onChange('font_personality', f.label)} className={`p-4 rounded-xl border-2 text-left transition-all duration-300 ease-bounce tap-target ${data.font_personality === f.label ? 'border-accent bg-accent/5 shadow-pop-sm' : 'border-border hover:border-accent/40 bg-card'}`}>
                <span className="text-lg block mb-1">{f.emoji}</span>
                <span className={`font-heading font-bold text-sm block ${data.font_personality === f.label ? 'text-accent' : 'text-foreground'}`}>{f.label}</span>
                <span className="text-[10px] text-muted-foreground block mt-0.5">{f.desc}</span>
              </button>
            ))}
          </div>
        </div>
        <div><label className="input-label">Inspiration (optional)</label><textarea className="input-field h-24 resize-none" placeholder="Any references, competitors you admire, specific ideas..." value={data.inspiration} onChange={(e) => onChange('inspiration', e.target.value)} /></div>
      </div>
    </motion.div>
  );
}

function Step5({ data }) {
  const items = [
    { label: 'Business', value: data.business_name, emoji: '🏢' },
    { label: 'Tagline', value: data.tagline, emoji: '💬' },
    { label: 'Industry', value: data.industry, emoji: '🏭' },
    { label: 'Audience', value: data.target_audience, emoji: '👥' },
    { label: 'Values', value: (data.brand_values || []).join(', '), emoji: '💎' },
    { label: 'Vibe', value: data.brand_vibe, emoji: '🎭' },
    { label: 'Colors', value: data.color_mood, emoji: '🎨' },
    { label: 'Font', value: data.font_personality, emoji: '✏️' },
  ];
  return (
    <motion.div className="card-step max-w-xl mx-auto" initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ ease: [0.34, 1.56, 0.64, 1] }}>
      <motion.div initial={{ scale: 0.8 }} animate={{ scale: 1 }} transition={{ ease: [0.34, 1.56, 0.64, 1] }} className="text-center mb-6">
        <span className="text-5xl block mb-3">🚀</span>
        <h2 className="text-2xl font-heading font-extrabold text-foreground mb-1">Ready to Launch!</h2>
        <p className="text-muted-foreground text-sm">Review everything below, then hit generate.</p>
      </motion.div>
      <div className="border-2 border-foreground rounded-xl overflow-hidden">
        {items.map((item, i) => (
          <div key={item.label} className={`flex items-center justify-between px-5 py-3.5 ${i % 2 === 0 ? 'bg-card' : 'bg-muted/30'} ${i < items.length - 1 ? 'border-b border-border' : ''}`}>
            <div className="flex items-center gap-2"><span className="text-sm">{item.emoji}</span><span className="text-sm text-muted-foreground font-heading font-bold">{item.label}</span></div>
            <span className="font-heading font-bold text-sm text-foreground text-right max-w-[60%] truncate">{item.value || '—'}</span>
          </div>
        ))}
      </div>
    </motion.div>
  );
}

function extractErrorMessage(err) {
  const data = err?.response?.data;
  if (!data) return 'Something went wrong. Please try again.';
  if (Array.isArray(data.errors) && data.errors.length > 0) {
    return data.errors.join('. ');
  }
  if (typeof data.detail === 'string') {
    return data.detail;
  }
  if (Array.isArray(data.detail)) {
    return data.detail.map(d => d.msg || String(d)).join('. ');
  }
  return 'Something went wrong. Please try again.';
}

export default function Home() {
  const { dark, toggleTheme } = useTheme();
  const [step, setStep] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);
  const [formData, setFormData] = useState({ business_name: '', tagline: '', industry: '', target_audience: '', brand_values: [], primary_goal: '', tone: 'friendly', brand_vibe: '', logo_style: '', color_mood: '', font_personality: '', inspiration: '' });

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
    setLoading(true); setError(null);
    try { const data = await generateBrand(formData); setResult(data); }
    catch (err) { setError(extractErrorMessage(err)); }
    finally { setLoading(false); }
  };
  const handleTwist = async () => {
    setLoading(true); setError(null);
    try { const data = await twistBrand(formData); setResult(data); }
    catch (err) { setError(extractErrorMessage(err)); }
    finally { setLoading(false); }
  };
  const handleDownload = () => { downloadBrandKit(formData); };

  if (loading) {
    return (<div className="min-h-screen flex items-center justify-center bg-bg relative overflow-hidden"><ConfettiBackground density={10} /><div className="relative z-10"><LoadingSpinner /></div></div>);
  }

  if (result) {
    return (
      <div className="min-h-screen bg-bg relative">
        <DecorativeShape variant="circle" color="#FBBF24" size={90} className="top-24 left-[4%] hidden lg:block" />
        <DecorativeShape variant="triangle" color="#F472B6" size={55} className="top-48 right-[6%] hidden lg:block" />
        <DecorativeShape variant="ring" color="#8B5CF6" size={70} className="bottom-24 left-[8%] hidden lg:block" />
        <DecorativeShape variant="square" color="#34D399" size={45} className="bottom-48 right-[4%] hidden lg:block" />
        <DecorativeShape variant="dot" color="#F472B6" size={20} className="top-[60%] right-[15%] hidden xl:block" />
        <DecorativeShape variant="dot" color="#FBBF24" size={16} className="top-[30%] left-[15%] hidden xl:block" />
        <header className="bg-card/90 backdrop-blur-md border-b-2 border-foreground sticky top-0 z-20">
          <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-heading font-extrabold text-foreground">{result.business_name}</h1>
              <div className="flex items-center gap-2 mt-0.5">
                <span className="text-sm text-muted-foreground font-heading font-bold">Brand Score:</span>
                <span className={`text-sm font-heading font-extrabold px-2 py-0.5 rounded-full ${result.brand_score >= 80 ? 'bg-quaternary/20 text-quaternary' : result.brand_score >= 60 ? 'bg-tertiary/20 text-tertiary' : 'bg-secondary/20 text-secondary'}`}>{result.brand_score}/100</span>
              </div>
            </div>
            <div className="flex gap-2">
              <button onClick={handleTwist} className="btn-secondary text-sm !px-4" disabled={loading}>🔀 Twist</button>
              <button onClick={handleDownload} className="btn-primary text-sm !px-4">📦 Download</button>
              <button onClick={() => setResult(null)} className="btn-icon !w-10 !h-10 !p-0 text-sm" title="Start Over">✕</button>
              <button onClick={toggleTheme} className="btn-icon !w-10 !h-10 !p-0 text-sm" title="Toggle Theme">{dark ? '☀️' : '🌙'}</button>
            </div>
          </div>
        </header>
        <main className="max-w-6xl mx-auto px-4 py-8 space-y-6 relative z-10">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2 space-y-6">
              <CollapsibleSection title="Logo Preview" defaultOpen={true} icon="🎨"><LogoPlayground svg={result.logo?.svg} /></CollapsibleSection>
              <CollapsibleSection title="Website Preview" defaultOpen={false} icon="🌐"><iframe srcDoc={result.website_content?.html} title="Website Preview" className="w-full h-[500px] border-2 border-foreground rounded-xl bg-white" sandbox="allow-scripts" /></CollapsibleSection>
              <CollapsibleSection title="Social Media Posts" defaultOpen={false} icon="📱"><SocialMockups posts={result.social_posts} /></CollapsibleSection>
            </div>
            <div className="space-y-6">
              <div className="bg-card border-2 border-foreground rounded-xl p-6 shadow-pop-lg flex flex-col items-center">
                <BrandScore score={result.brand_score} />
                <p className="text-xs text-muted-foreground mt-2">{result.brand_score >= 85 ? '🌟 Exceptional' : result.brand_score >= 70 ? '✨ Strong identity' : result.brand_score >= 55 ? '👍 Solid foundation' : '🔧 Room to grow'}</p>
              </div>
              <CollapsibleSection title="Color Palette" defaultOpen={true} icon="🎨"><ColorPaletteEditor colors={result.colors} onChange={(next) => setResult((prev) => ({ ...prev, colors: next }))} /></CollapsibleSection>
              <CollapsibleSection title="SEO Metadata" defaultOpen={false} icon="🔍">
                <div className="space-y-4">
                  <div><div className="flex items-center justify-between mb-1"><p className="label-sm">Title</p><CopyButton text={result.seo_tags?.title} label="Title" /></div><p className="text-sm font-heading font-bold text-foreground bg-muted/30 rounded-lg px-3 py-2">{result.seo_tags?.title}</p><p className="text-[10px] text-muted-foreground mt-1">{(result.seo_tags?.title || '').length}/60 chars</p></div>
                  <div><div className="flex items-center justify-between mb-1"><p className="label-sm">Description</p><CopyButton text={result.seo_tags?.description} label="Desc" /></div><p className="text-sm text-muted-foreground bg-muted/30 rounded-lg px-3 py-2 leading-relaxed">{result.seo_tags?.description}</p><p className="text-[10px] text-muted-foreground mt-1">{(result.seo_tags?.description || '').length}/160 chars</p></div>
                  <div><p className="label-sm mb-2">Keywords</p><div className="flex flex-wrap gap-1.5">{(result.seo_tags?.keywords || []).map((kw, i) => (<span key={i} className="tag bg-accent/10 text-accent border-accent/20 text-[11px]">{kw}</span>))}</div></div>
                </div>
              </CollapsibleSection>
              <CollapsibleSection title="Brand Guide" defaultOpen={false} icon="📖">
                <div className="flex items-center justify-between mb-3"><p className="label-sm mb-0">Full Guide</p><CopyButton text={result.brand_guide} label="Guide" /></div>
                <pre className="whitespace-pre-wrap text-sm text-muted-foreground font-sans leading-relaxed bg-muted/20 rounded-lg p-4 border border-border">{result.brand_guide}</pre>
              </CollapsibleSection>
            </div>
          </div>
        </main>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-bg relative overflow-hidden">
      <ConfettiBackground density={4} />
      <DecorativeShape variant="circle" color="#FBBF24" size={110} className="top-8 right-[8%] opacity-20 hidden lg:block" />
      <DecorativeShape variant="triangle" color="#F472B6" size={65} className="bottom-16 left-[4%] opacity-20 hidden lg:block" />
      <DecorativeShape variant="ring" color="#8B5CF6" size={85} className="top-[40%] left-[2%] opacity-15 hidden xl:block" />
      <header className="bg-card/80 backdrop-blur-sm border-b-2 border-foreground sticky top-0 z-20">
        <div className="max-w-4xl mx-auto px-4 py-4 flex items-center justify-between">
          <div><h1 className="text-2xl font-heading font-extrabold text-foreground"><span className="text-accent">S</span>olivagant</h1><p className="text-xs text-muted-foreground font-heading font-bold tracking-wide">AI BRAND DESIGNER</p></div>
          <button onClick={toggleTheme} className="btn-icon !w-10 !h-10 !p-0 text-sm" title="Toggle Theme">{dark ? '☀️' : '🌙'}</button>
        </div>
      </header>
      <main className="max-w-4xl mx-auto px-4 py-8 relative z-10">
        <StepIndicator current={step} onSelect={setStep} />
        <AnimatePresence mode="wait">
          <motion.div key={step} initial={{ opacity: 0, x: 60 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -60 }} transition={{ ease: [0.34, 1.56, 0.64, 1], duration: 0.35 }}>
            {step === 0 && <Step1 data={formData} onChange={updateField} />}
            {step === 1 && <Step2 data={formData} onChange={updateField} />}
            {step === 2 && <Step3 data={formData} onChange={updateField} />}
            {step === 3 && <Step4 data={formData} onChange={updateField} />}
            {step === 4 && <Step5 data={formData} />}
          </motion.div>
        </AnimatePresence>
        <AnimatePresence>{error && (<motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: 10 }} className="mt-4 p-4 bg-danger/10 border-2 border-danger rounded-xl"><p className="text-danger text-sm font-heading font-bold">{error}</p></motion.div>)}</AnimatePresence>
        <div className="flex justify-between mt-8 max-w-xl mx-auto">
          <button onClick={() => setStep((s) => Math.max(0, s - 1))} disabled={step === 0} className="btn-secondary">← Back</button>
          {step < 4 ? (
            <button onClick={() => canProceed() && setStep((s) => s + 1)} disabled={!canProceed()} className="btn-primary">Next →</button>
          ) : (
            <motion.button onClick={handleGenerate} className="btn-primary !px-8" whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>🚀 Generate My Brand</motion.button>
          )}
        </div>
      </main>
    </div>
  );
}
