"""
Website Generation Service for brand landing pages
Generates stable, modern HTML and color palette recommendations
"""

import hashlib
import json
from typing import Dict, List


class WebsiteGenerator:
    """Stable local website generator that creates unique, professional landing pages."""

    def __init__(self):
        self.palettes = {
            "modern": {
                "name": "Modern Blue",
                "primary": "#1E40AF",
                "secondary": "#0EA5E9",
                "accent": "#F59E0B",
                "surface": "#F8FAFC",
                "text": "#111827"
            },
            "professional": {
                "name": "Professional Slate",
                "primary": "#111827",
                "secondary": "#4B5563",
                "accent": "#2563EB",
                "surface": "#F3F4F6",
                "text": "#111827"
            },
            "vibrant": {
                "name": "Vibrant Bloom",
                "primary": "#EC4899",
                "secondary": "#8B5CF6",
                "accent": "#10B981",
                "surface": "#F8FAFC",
                "text": "#0F172A"
            },
            "elegant": {
                "name": "Elegant Violet",
                "primary": "#7C3AED",
                "secondary": "#A78BFA",
                "accent": "#FBBF24",
                "surface": "#F9FAFB",
                "text": "#111827"
            }
        }

        self.templates = {
            "modern": {
                "name": "Modern Launchpad",
                "description": "A bright, polished layout built for startups and digital brands.",
                "preview_label": "Contemporary launch page with bold headings and fresh gradients.",
                "cta_label": "Launch your product"
            },
            "classic": {
                "name": "Classic Corporate",
                "description": "A refined layout for trusted professional services and enterprise brands.",
                "preview_label": "Clean structure with elegant typography and reassuring messaging.",
                "cta_label": "Request a consultation"
            },
            "creative": {
                "name": "Creative Studio",
                "description": "An expressive layout with vibrant accents and attention-grabbing storytelling.",
                "preview_label": "Bold, artistic sections for design-forward brands.",
                "cta_label": "View our work"
            },
            "minimal": {
                "name": "Minimal Showcase",
                "description": "A simple, focused layout that highlights your message with clarity.",
                "preview_label": "Low-clutter landing page with refined spacing and strong hierarchy.",
                "cta_label": "Start a project"
            }
        }

    def generate_website(
        self,
        business_name: str,
        tagline: str,
        color_scheme: str = "modern",
        industry: str = "general",
        website_template: str = "modern"
    ) -> Dict[str, object]:
        """Generate a complete website payload with HTML and palette info."""
        palette = self._get_color_palette(color_scheme)
        template_meta = self._get_template_meta(website_template)
        theme_key = self._choose_theme(business_name, industry, color_scheme, website_template)
        headline = self._build_headline(business_name, tagline, website_template)
        features = self._get_features(industry, website_template)
        sections = self._get_sections(industry, website_template)
        font_family = self._get_font_family(theme_key)

        html = self._render_html(
            business_name=business_name,
            tagline=tagline,
            headline=headline,
            features=features,
            sections=sections,
            palette=palette,
            font_family=font_family,
            industry=industry,
            template_meta=template_meta
        )

        return {
            "html": html,
            "palette": palette,
            "theme_name": palette["name"],
            "font_family": font_family,
            "features": features,
            "sections": sections,
            "template_style": website_template,
            "template_name": template_meta["name"],
            "template_description": template_meta["description"],
            "palette_suggestions": self._get_palette_suggestions(color_scheme)
        }

    def _get_color_palette(self, scheme: str) -> Dict[str, str]:
        return self.palettes.get(scheme, self.palettes["modern"])

    def _get_template_meta(self, template: str) -> Dict[str, str]:
        return self.templates.get(template, self.templates["modern"])

    def _choose_theme(
        self,
        business_name: str,
        industry: str,
        color_scheme: str,
        website_template: str
    ) -> str:
        key_string = f"{business_name.lower()}-{industry.lower()}-{color_scheme}-{website_template}"
        digest = hashlib.sha256(key_string.encode("utf-8")).hexdigest()
        return "professional" if int(digest[:2], 16) % 2 == 0 else "modern"

    def _build_headline(self, business_name: str, tagline: str, website_template: str) -> str:
        prefix = {
            "modern": "Build",
            "classic": "Elevate",
            "creative": "Create",
            "minimal": "Focus"
        }.get(website_template, "Build")
        return f"{prefix} {business_name} — {tagline}"

    def _get_features(self, industry: str, website_template: str) -> List[Dict[str, str]]:
        industry = industry.lower()
        if "tech" in industry or "software" in industry:
            features = [
                {"title": "Fast innovation", "description": "Launch modern digital products with reliable performance.", "template": website_template},
                {"title": "Scalable systems", "description": "Engineered to grow with your customers and products.", "template": website_template},
                {"title": "Secure infrastructure", "description": "Built with trust, privacy and uptime in mind.", "template": website_template}
            ]
        elif "creative" in industry or "design" in industry:
            features = [
                {"title": "Bold visual systems", "description": "Beautiful branding that captivates and converts.", "template": website_template},
                {"title": "Digital storytelling", "description": "Elegant experiences that feel crafted and intuitive.", "template": website_template},
                {"title": "Consistent identity", "description": "Every touchpoint feels polished and memorable.", "template": website_template}
            ]
        elif "finance" in industry or "consult" in industry:
            features = [
                {"title": "Strategic clarity", "description": "Trustworthy messaging built for intelligent audiences.", "template": website_template},
                {"title": "Data-led decisions", "description": "Reports and insights designed to move stakeholders.", "template": website_template},
                {"title": "Reliable support", "description": "Professional services with a modern digital presence.", "template": website_template}
            ]
        else:
            features = [
                {"title": "Smart solutions", "description": "Clear, modern design built for real results.", "template": website_template},
                {"title": "Customer focus", "description": "Every detail is designed to improve engagement.", "template": website_template},
                {"title": "Brand consistency", "description": "A polished identity across web and marketing.", "template": website_template}
            ]

        if website_template == "creative":
            features.append({"title": "Eye-catching moments", "description": "Design details that make your brand memorable and distinct.", "template": website_template})

        return features

    def _get_sections(self, industry: str, website_template: str) -> List[Dict[str, str]]:
        if website_template == "classic":
            return [
                {"headline": "Trusted services", "text": "Present your experience, processes, and client outcomes with authority.", "template": "classic"},
                {"headline": "Proven approach", "text": "Define how your strategy works in a clear, professional way.", "template": "classic"},
                {"headline": "Partner with confidence", "text": "Encourage action with a dependable, results-driven message.", "template": "classic"}
            ]

        if website_template == "creative":
            return [
                {"headline": "Creative direction", "text": "Express your visual language with bold storytelling and curated design systems.", "template": "creative"},
                {"headline": "Studio process", "text": "Bring ideas to life with purposeful concepts, prototypes, and brand experiences.", "template": "creative"},
                {"headline": "Signature projects", "text": "Highlight standout work with clarity, emotion, and modern layout.", "template": "creative"}
            ]

        if website_template == "minimal":
            return [
                {"headline": "Clear value", "text": "Focus on the most important benefit with crisp messaging and clean structure.", "template": "minimal"},
                {"headline": "Fast decisions", "text": "Reduce friction with a direct, easy-to-navigate experience.", "template": "minimal"},
                {"headline": "Lean brand presentation", "text": "A pared-back website that supports confident business decisions.", "template": "minimal"}
            ]

        return [
            {"headline": "What we do", "text": "Deliver modern brand systems, digital experiences, and web solutions tailored to your audience.", "template": "modern"},
            {"headline": "How it helps", "text": "Increase trust, drive conversions, and present your business like a modern leader.", "template": "modern"},
            {"headline": "Ready to launch", "text": "Create a polished online presence with one professional package.", "template": "modern"}
        ]

    def _get_font_family(self, theme_key: str) -> str:
        families = {
            "professional": "Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
            "modern": "Plus Jakarta Sans, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
            "classic": "Georgia, 'Times New Roman', serif",
            "creative": "'Poppins', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
            "minimal": "Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
        }
        return families.get(theme_key, families["modern"])

    def _get_palette_suggestions(self, chosen_scheme: str) -> List[Dict[str, object]]:
        variations = ["modern", "professional", "vibrant", "elegant"]
        return [
            {"scheme": key, "palette": self.palettes[key]} for key in variations if key != chosen_scheme
        ]

    def _render_html(
        self,
        business_name: str,
        tagline: str,
        headline: str,
        features: List[Dict[str, str]],
        sections: List[Dict[str, str]],
        palette: Dict[str, str],
        font_family: str,
        industry: str,
        template_meta: Dict[str, str]
    ) -> str:
        feature_cards = "\n".join([
            f"<div class=\"feature-card\"><h3>{item['title']}</h3><p>{item['description']}</p></div>"
            for item in features
        ])

        section_cards = "\n".join([
            f"<div class=\"section-card\"><h3>{item['headline']}</h3><p>{item['text']}</p></div>"
            for item in sections
        ])

        return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <meta name=\"theme-color\" content=\"{palette['primary']}\">
    <title>{business_name}</title>
    <style>
        :root {{
            color-scheme: light;
            font-family: {font_family};
            --primary: {palette['primary']};
            --secondary: {palette['secondary']};
            --accent: {palette['accent']};
            --surface: {palette['surface']};
            --text: {palette['text']};
            --shadow: 0 30px 80px rgba(15, 23, 42, 0.12);
        }}
        * {{ box-sizing: border-box; }}
        html, body {{ margin: 0; padding: 0; background: #F8FAFC; color: var(--text); }}
        body {{ font-family: {font_family}; line-height: 1.65; }}
        a {{ color: inherit; text-decoration: none; }}
        .page {{ max-width: 1200px; margin: 0 auto; padding: 24px; }}
        header {{ display: flex; align-items: center; justify-content: space-between; gap: 24px; padding: 20px 0; }}
        .brand-mark {{ font-weight: 800; letter-spacing: -.04em; color: var(--primary); font-size: 1.2rem; }}
        .top-nav {{ display: flex; gap: 24px; font-size: 0.95rem; color: #475569; }}
        .top-nav a:hover {{ color: var(--primary); }}
        .hero {{ background: white; border-radius: 30px; box-shadow: var(--shadow); padding: 60px 50px; overflow: hidden; }}
        .hero::before {{ content: ''; position: absolute; inset: 0; background: radial-gradient(circle at top right, rgba(59,130,246,0.15), transparent 32%); pointer-events: none; }}
        .hero-grid {{ display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(340px, 1fr); gap: 32px; align-items: center; position: relative; }}
        .hero-copy h1 {{ font-size: clamp(2.8rem, 4vw, 4.4rem); margin: 0 0 24px; line-height: 1.02; }}
        .hero-copy p {{ margin: 0 0 30px; max-width: 600px; color: #475569; font-size: 1.05rem; }}
        .hero-actions {{ display: flex; flex-wrap: wrap; gap: 16px; }}
        .button-primary {{ background: linear-gradient(135deg, var(--primary), var(--secondary)); color: white; border: none; padding: 16px 28px; border-radius: 999px; font-size: 1rem; cursor: pointer; transition: transform .2s ease, box-shadow .2s ease; box-shadow: 0 18px 40px rgba(59, 130, 246, 0.18); }}
        .button-primary:hover {{ transform: translateY(-2px); }}
        .button-secondary {{ background: rgba(15, 23, 42, 0.04); color: #0F172A; border: none; padding: 16px 28px; border-radius: 999px; }}
        .hero-visual {{ background: linear-gradient(180deg, var(--secondary), transparent); border-radius: 24px; min-height: 360px; display: grid; place-items: center; position: relative; overflow: hidden; }}
        .hero-visual::after {{ content: ''; position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(255,255,255,0.35), transparent 45%); }}
        .hero-visual span {{ position: relative; z-index: 1; color: white; font-size: 1.1rem; text-align: center; max-width: 240px; }}
        .swatches {{ display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px; margin-top: 24px; }}
        .swatch {{ height: 80px; border-radius: 18px; display: flex; align-items: flex-end; justify-content: center; color: white; padding: 12px; font-size: 0.85rem; font-weight: 700; text-shadow: 0 10px 30px rgba(0,0,0,.15); }}
        .content-grid {{ display: grid; gap: 24px; margin: 48px 0; }}
        .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; }}
        .feature-card, .section-card {{ background: white; border: 1px solid rgba(15, 23, 42, 0.08); border-radius: 24px; padding: 26px; box-shadow: 0 18px 40px rgba(15, 23, 42, 0.04); transition: transform .2s ease, box-shadow .2s ease; }}
        .feature-card:hover, .section-card:hover {{ transform: translateY(-3px); box-shadow: 0 24px 50px rgba(15, 23, 42, 0.09); }}
        .feature-card h3, .section-card h3 {{ margin-top: 0; color: var(--primary); }}
        .section-card p {{ color: #475569; }}
        footer {{ padding: 60px 0 20px; text-align: center; color: #64748B; }}
        footer p {{ margin: 0; }}
        .palette-panel {{ display: grid; gap: 18px; background: white; padding: 28px; border-radius: 28px; box-shadow: var(--shadow); }}
        .palette-row {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }}
        .palette-chip {{ width: 42px; height: 42px; border-radius: 12px; display: inline-flex; align-items: center; justify-content: center; color: white; font-size: 0.8rem; font-weight: 700; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.18); }}
        .meta-list {{ display: grid; gap: 12px; }}
        .meta-item {{ background: #F8FAFC; border-radius: 16px; padding: 18px; border: 1px solid rgba(15,23,42,0.06); }}
        .meta-item strong {{ display: block; margin-bottom: 6px; color: #0F172A; }}
        .summary-bar {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }}
        .summary-pill {{ background: rgba(59, 130, 246, 0.12); color: #1D4ED8; font-size: 0.85rem; padding: 8px 14px; border-radius: 999px; }}
        .comparison-card {{ display: grid; gap: 14px; }}
        .comparison-card h3 {{ margin-bottom: 8px; }}
        .palette-suggestion {{ display: flex; gap: 10px; align-items: center; margin-bottom: 10px; }}
        .palette-swatch-small {{ width: 48px; height: 48px; border-radius: 16px; }}
        @media (max-width: 960px) {{ .hero-grid {{ grid-template-columns: 1fr; }} }}
        @media (max-width: 720px) {{ .page {{ padding: 20px; }} .hero {{ padding: 36px 24px; }} .hero-copy h1 {{ font-size: 2.5rem; }} }}
    </style>
</head>
<body>
    <div class="page">
        <header>
            <div class="brand-mark">{business_name}</div>
            <nav class="top-nav">
                <a href="#features">Features</a>
                <a href="#palette">Palette</a>
                <a href="#mission">Mission</a>
            </nav>
        </header>

        <section class="hero">
            <div class="hero-grid">
                <div class="hero-copy">
                    <h1>{headline}</h1>
                    <p>{tagline}</p>
                    <div class="hero-actions">
                        <button class="button-primary">{template_meta['cta_label']}</button>
                        <button class="button-secondary">View portfolio</button>
                    </div>
                    <div class="template-info">
                        <span class="template-chip">Template: {template_meta['name']}</span>
                        <div class="template-meta">{template_meta['preview_label']}</div>
                    </div>
                    <div class="swatches">
                        <div class="swatch" style="background:{palette['primary']}">{palette['primary']}</div>
                        <div class="swatch" style="background:{palette['secondary']}">{palette['secondary']}</div>
                        <div class="swatch" style="background:{palette['accent']}">{palette['accent']}</div>
                        <div class="swatch" style="background:{palette['surface']}; color:{palette['text']};">BG</div>
                        <div class="swatch" style="background:{palette['text']}">TXT</div>
                    </div>
                </div>
                <div class="hero-visual">
                    <span>{template_meta['preview_label']}</span>
                </div>
            </div>
        </section>

        <section class="content-grid" id="features">
            <div class="palette-panel">
                <div class="summary-bar">
                    <span class="summary-pill">Template: {template_meta['name']}</span>
                    <span class="summary-pill">Font: {font_family.split(',')[0]}</span>
                    <span class="summary-pill">Industry: {industry}</span>
                </div>
                <div class="comparison-card">
                    <h3>Brand design system</h3>
                    <div>Primary color, secondary color, accent, surface and text tones are configured for a clean, polished brand experience.</div>
                </div>
            </div>
            <div class="cards">
                {feature_cards}
            </div>
        </section>

        <section class="content-grid" id="mission">
            {section_cards}
        </section>

        <footer>
            <p>{business_name} is designed to make your brand stand out online with confidence, clarity, and conversion-ready design.</p>
        </footer>
    </div>
</body>
</html>"""
