"""
AI-Powered Website Generation Service using Groq LLM
Generates unique, context-aware HTML layouts and content
"""

import os
import json
from typing import Dict, List
from groq import Groq


class WebsiteGeneratorAI:
    """AI-powered website generator that creates unique, context-aware landing pages."""

    VIBES = {
        "premium": {
            "name": "Premium",
            "description": "Luxury, sophisticated, high-end aesthetic",
            "personality": "elegant, exclusive, refined",
            "layout_style": "spacious, cinematic, dramatic",
            "font_tier": "editorial",
        },
        "playful": {
            "name": "Playful",
            "description": "Fun, energetic, approachable design",
            "personality": "friendly, creative, dynamic",
            "layout_style": "bouncy, colorful, asymmetrical",
            "font_tier": "rounded",
        },
        "professional": {
            "name": "Professional",
            "description": "Trustworthy, corporate, reliable",
            "personality": "serious, dependable, expert",
            "layout_style": "structured, balanced, clean",
            "font_tier": "sans-serif",
        },
        "minimal": {
            "name": "Minimal",
            "description": "Clean, focused, modern simplicity",
            "personality": "pure, essential, contemporary",
            "layout_style": "bare, breathable, intentional",
            "font_tier": "geometric",
        },
        "bold": {
            "name": "Bold",
            "description": "Attention-grabbing, confident, memorable",
            "personality": "strong, assertive, distinctive",
            "layout_style": "striking, oversized, high-contrast",
            "font_tier": "display",
        },
    }

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    def generate_website(
        self,
        business_name: str,
        tagline: str,
        industry: str,
        vibe: str = "professional",
        num_vibes: int = 3,
    ) -> Dict[str, object]:
        """Generate a complete AI-powered website."""

        if num_vibes > 1:
            return self._generate_multiple_vibes(
                business_name, tagline, industry, num_vibes
            )

        return self._generate_single_vibe(business_name, tagline, industry, vibe)

    def _generate_multiple_vibes(
        self, business_name: str, tagline: str, industry: str, num_vibes: int = 3
    ) -> Dict[str, object]:
        """Generate multiple vibe variations using AI."""

        vibes_to_generate = list(self.VIBES.keys())[:num_vibes]
        variations = []

        for vibe_key in vibes_to_generate:
            try:
                variation = self._generate_single_vibe(
                    business_name, tagline, industry, vibe_key
                )
                variations.append(variation)
            except Exception as e:
                print(f"Error generating vibe {vibe_key}: {e}")
                continue

        if not variations:
            variations = [
                self._generate_fallback_variation(
                    business_name,
                    tagline,
                    industry,
                    self.VIBES["professional"],
                    "professional",
                )
            ]

        return {
            "multiple_vibes": True,
            "variations": variations,
            "html": variations[0]["html"] if variations else "",
            "palette": variations[0]["palette"] if variations else {},
            "vibe_name": variations[0]["vibe_name"] if variations else "Professional",
            "vibe_description": variations[0]["vibe_description"] if variations else "",
        }

    def _generate_single_vibe(
        self,
        business_name: str,
        tagline: str,
        industry: str,
        vibe: str = "professional",
    ) -> Dict[str, object]:
        """Generate a single vibe variation using AI."""

        vibe_config = self.VIBES.get(vibe, self.VIBES["professional"])

        prompt = self._build_generation_prompt(
            business_name, tagline, industry, vibe_config
        )

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._get_system_prompt()},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.8,
                max_tokens=4000,
            )

            response_text = completion.choices[0].message.content
            website_data = self._parse_ai_response(response_text, vibe_config)
            website_data["business_name"] = business_name

            return self._build_website_response(website_data, vibe_config, vibe)

        except Exception as e:
            print(f"Error generating website with AI: {e}")
            return self._generate_fallback_variation(
                business_name, tagline, industry, vibe_config, vibe
            )

    def _build_generation_prompt(
        self, business_name: str, tagline: str, industry: str, vibe_config: Dict
    ) -> str:
        """Build the prompt for website generation."""

        return f"""Generate a complete, unique landing page for {business_name}.

BUSINESS DETAILS:
- Name: {business_name}
- Tagline: {tagline}
- Industry: {industry}

DESIGN VIBE: {vibe_config["name"]}
- Description: {vibe_config["description"]}
- Personality: {vibe_config["personality"]}
- Layout Style: {vibe_config["layout_style"]}
- Font Tier: {vibe_config["font_tier"]}

Generate a complete landing page in JSON format with these exact fields:
{{
    "hero_headline": "Main headline (10-15 words, compelling)",
    "hero_subheadline": "Supporting text under headline (20-25 words)",
    "primary_color": "Hex color for main brand color",
    "secondary_color": "Hex color for supporting elements",
    "accent_color": "Hex color for CTAs and highlights",
    "background_color": "Hex color for page background",
    "text_color": "Hex color for body text",
    "features": [
        {{"title": "Feature name", "description": "2-sentence description", "icon": "star"}}
    ],
    "benefits": ["3 bullet points about key benefits"],
    "testimonial": {{"quote": "Customer quote", "author": "Customer Name", "role": "Title/Company"}},
    "cta_text": "Main call-to-action button text",
    "cta_secondary_text": "Secondary button text",
    "footer_tagline": "Short footer message",
    "layout_variant": "modern_grid OR full_width_hero OR split_screen OR centered_minimal OR card_based"
}}

Make the design feel authentic to the industry and business. No generic copy."""

    def _get_system_prompt(self) -> str:
        """Get the system prompt for the AI."""
        return """You are an expert web designer and brand strategist. Generate unique, professional landing page designs that are:
- Tailored to the specific business and industry
- Modern and visually striking
- Conversion-focused with clear CTAs
- Responsive and mobile-friendly
- Unique (not template-like)

Always respond with valid JSON only."""

    def _parse_ai_response(self, response_text: str, vibe_config: Dict) -> Dict:
        """Parse the AI response into structured data."""

        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            import re

            json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
            if json_match:
                try:
                    return json.loads(json_match.group())
                except json.JSONDecodeError:
                    pass

        return self._get_default_content(vibe_config)

    def _build_website_response(
        self, data: Dict, vibe_config: Dict, vibe_key: str
    ) -> Dict[str, object]:
        """Build the complete website response with HTML."""

        html = self._generate_html(
            business_name=data.get("business_name", ""),
            headline=data.get("hero_headline", ""),
            subheadline=data.get("hero_subheadline", ""),
            features=data.get("features", []),
            benefits=data.get("benefits", []),
            testimonial=data.get("testimonial", {}),
            cta_text=data.get("cta_text", "Get Started"),
            cta_secondary_text=data.get("cta_secondary_text", "Learn More"),
            footer_tagline=data.get("footer_tagline", ""),
            colors={
                "primary": data.get("primary_color", "#3B82F6"),
                "secondary": data.get("secondary_color", "#8B5CF6"),
                "accent": data.get("accent_color", "#10B981"),
                "background": data.get("background_color", "#FFFFFF"),
                "text": data.get("text_color", "#1F2937"),
            },
            layout_variant=data.get("layout_variant", "modern_grid"),
            vibe_config=vibe_config,
        )

        return {
            "html": html,
            "palette": {
                "primary": data.get("primary_color", "#3B82F6"),
                "secondary": data.get("secondary_color", "#8B5CF6"),
                "accent": data.get("accent_color", "#10B981"),
                "surface": data.get("background_color", "#FFFFFF"),
                "text": data.get("text_color", "#1F2937"),
            },
            "vibe_name": vibe_config["name"],
            "vibe_description": vibe_config["description"],
            "vibe_key": vibe_key,
            "headline": data.get("hero_headline", ""),
            "features": data.get("features", []),
            "benefits": data.get("benefits", []),
            "testimonial": data.get("testimonial", {}),
            "cta_text": data.get("cta_text", "Get Started"),
            "layout_variant": data.get("layout_variant", "modern_grid"),
        }

    def _generate_html(
        self,
        business_name: str,
        headline: str,
        subheadline: str,
        features: List[Dict],
        benefits: List[str],
        testimonial: Dict,
        cta_text: str,
        cta_secondary_text: str,
        footer_tagline: str,
        colors: Dict,
        layout_variant: str,
        vibe_config: Dict,
    ) -> str:
        """Generate the complete HTML page."""

        feature_cards = self._generate_feature_cards(features, colors)
        benefit_items = self._generate_benefit_items(benefits)
        testimonial_html = self._generate_testimonial(testimonial, colors)

        layout_css = self._get_layout_css(layout_variant)

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{business_name}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family={self._get_font_family(vibe_config["font_tier"])}" rel="stylesheet">
    <style>
        :root {{
            --primary: {colors["primary"]};
            --secondary: {colors["secondary"]};
            --accent: {colors["accent"]};
            --bg: {colors["background"]};
            --text: {colors["text"]};
            --font: {self._get_css_font(vibe_config["font_tier"])};
            --radius: {self._get_border_radius(vibe_config)};
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: var(--font);
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
        }}

        nav {{
            padding: 20px 0;
            display: flex;
            justify-content: space-between;
           _align-items: center;
        }}

        .logo {{
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary);
        }}

        .nav-links {{
            display: flex;
            gap: 32px;
        }}

        .nav-links a {{
            color: var(--text);
            text-decoration: none;
            font-weight: 500;
            opacity: 0.8;
            transition: opacity 0.2s;
        }}

        .nav-links a:hover {{ opacity: 1; }}

        {layout_css}

        .hero {{
            min-height: 80vh;
            display: flex;
            align-items: center;
            padding: 80px 0;
        }}

        .hero-content {{
            flex: 1;
            max-width: 700px;
        }}

        .hero h1 {{
            font-size: clamp(2.5rem, 5vw, 4rem);
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 24px;
            color: var(--text);
        }}

        .hero p {{
            font-size: 1.25rem;
            opacity: 0.8;
            margin-bottom: 40px;
            max-width: 540px;
        }}

        .cta-group {{
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
        }}

        .btn {{
            padding: 16px 32px;
            border-radius: var(--radius);
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            border: none;
        }}

        .btn-primary {{
            background: var(--primary);
            color: white;
        }}

        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }}

        .btn-secondary {{
            background: transparent;
            color: var(--text);
            border: 2px solid var(--text);
        }}

        .btn-secondary:hover {{
            background: var(--text);
            color: var(--bg);
        }}

        .features {{
            padding: 100px 0;
        }}

        .section-header {{
            text-align: center;
            margin-bottom: 60px;
        }}

        .section-header h2 {{
            font-size: 2.5rem;
            margin-bottom: 16px;
        }}

        .section-header p {{
            font-size: 1.1rem;
            opacity: 0.7;
            max-width: 600px;
            margin: 0 auto;
        }}

        .features-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 32px;
        }}

        .feature-card {{
            background: white;
            padding: 32px;
            border-radius: calc(var(--radius) * 1.5);
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
            transition: all 0.3s ease;
        }}

        .feature-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .feature-icon {{
            width: 56px;
            height: 56px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: var(--radius);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            color: white;
            font-size: 1.5rem;
        }}

        .feature-card h3 {{
            font-size: 1.25rem;
            margin-bottom: 12px;
        }}

        .feature-card p {{
            opacity: 0.7;
            line-height: 1.7;
        }}

        .benefits {{
            padding: 100px 0;
        }}

        .benefits-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
        }}

        .benefits-content h2 {{
            font-size: 2.5rem;
            margin-bottom: 24px;
        }}

        .benefits-list {{
            list-style: none;
        }}

        .benefits-list li {{
            padding: 16px 0;
            padding-left: 36px;
            position: relative;
            font-size: 1.1rem;
        }}

        .benefits-list li::before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--accent);
            font-weight: bold;
        }}

        .benefits-visual {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 24px;
            height: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2rem;
        }}

        .testimonial {{
            padding: 100px 0;
            background: var(--primary);
            color: white;
        }}

        .testimonial-content {{
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
        }}

        .testimonial blockquote {{
            font-size: 1.5rem;
            font-style: italic;
            margin-bottom: 32px;
            line-height: 1.6;
        }}

        .testimonial cite {{
            font-style: normal;
        }}

        .testimonial cite strong {{
            display: block;
            font-size: 1.1rem;
            margin-bottom: 4px;
        }}

        .testimonial cite span {{
            opacity: 0.8;
        }}

        .cta-section {{
            padding: 100px 0;
            text-align: center;
        }}

        .cta-section h2 {{
            font-size: 2.5rem;
            margin-bottom: 16px;
        }}

        .cta-section p {{
            font-size: 1.1rem;
            opacity: 0.7;
            margin-bottom: 32px;
        }}

        footer {{
            padding: 40px 0;
            border-top: 1px solid rgba(0,0,0,0.1);
            text-align: center;
            opacity: 0.6;
        }}

        @media (max-width: 768px) {{
            .hero {{ min-height: auto; padding: 60px 0; }}
            .benefits-grid {{ grid-template-columns: 1fr; }}
            .nav-links {{ display: none; }}
            .hero h1 {{ font-size: 2rem; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <nav>
            <div class="logo">{business_name}</div>
            <div class="nav-links">
                <a href="#features">Features</a>
                <a href="#benefits">Benefits</a>
                <a href="#testimonials">Testimonials</a>
            </div>
        </nav>

        <section class="hero">
            <div class="hero-content">
                <h1>{headline}</h1>
                <p>{subheadline}</p>
                <div class="cta-group">
                    <button class="btn btn-primary">{cta_text}</button>
                    <button class="btn btn-secondary">{cta_secondary_text}</button>
                </div>
            </div>
        </section>
    </div>

    <section class="features" id="features">
        <div class="container">
            <div class="section-header">
                <h2>Why Choose Us</h2>
                <p>Everything you need to succeed, all in one place</p>
            </div>
            <div class="features-grid">
                {feature_cards}
            </div>
        </div>
    </section>

    <section class="benefits" id="benefits">
        <div class="container">
            <div class="benefits-grid">
                <div class="benefits-content">
                    <h2>The {business_name} Advantage</h2>
                    <ul class="benefits-list">
                        {benefit_items}
                    </ul>
                </div>
                <div class="benefits-visual">
                    Visual Representation
                </div>
            </div>
        </div>
    </section>

    {testimonial_html}

    <section class="cta-section" id="cta">
        <div class="container">
            <h2>Ready to Get Started?</h2>
            <p>Join thousands of satisfied customers today</p>
            <button class="btn btn-primary">{cta_text}</button>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>{footer_tagline} | {business_name}</p>
        </div>
    </footer>
</body>
</html>"""

    def _generate_feature_cards(self, features: List[Dict], colors: Dict) -> str:
        """Generate HTML for feature cards."""
        icons = ["★", "⚡", "🎯", "💡", "🚀", "✦"]
        cards = []

        for i, feature in enumerate(features[:6]):
            icon = feature.get("icon", icons[i % len(icons)])
            cards.append(f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <h3>{feature.get("title", "Feature")}</h3>
                    <p>{feature.get("description", "")}</p>
                </div>
            """)

        return "".join(cards)

    def _generate_benefit_items(self, benefits: List[str]) -> str:
        """Generate HTML for benefit items."""
        return "".join([f"<li>{b}</li>" for b in benefits])

    def _generate_testimonial(self, testimonial: Dict, colors: Dict) -> str:
        """Generate HTML for testimonial section."""
        if not testimonial.get("quote"):
            return ""

        return f"""
    <section class="testimonial" id="testimonials">
        <div class="container">
            <div class="testimonial-content">
                <blockquote>"{testimonial.get("quote", "")}"</blockquote>
                <cite>
                    <strong>{testimonial.get("author", "Customer")}</strong>
                    <span>{testimonial.get("role", "")}</span>
                </cite>
            </div>
        </div>
    </section>
        """

    def _get_layout_css(self, variant: str) -> str:
        """Get layout-specific CSS based on variant."""
        layouts = {
            "modern_grid": """
        .hero { background: linear-gradient(135deg, var(--bg) 0%, color-mix(in srgb, var(--primary) 8%, var(--bg)) 100%); }
            """,
            "full_width_hero": """
        .hero { background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%); color: white; }
        .hero p { color: rgba(255,255,255,0.9); }
            """,
            "split_screen": """
        .hero { background: var(--bg); }
            """,
            "centered_minimal": """
        .hero { text-align: center; justify-content: center; }
        .hero-content { max-width: 800px; margin: 0 auto; }
        .cta-group { justify-content: center; }
            """,
            "card_based": """
        .hero { background: var(--bg); }
            """,
        }
        return layouts.get(variant, layouts["modern_grid"])

    def _get_font_family(self, font_tier: str) -> str:
        """Get Google Font name for the tier."""
        fonts = {
            "editorial": "Playfair+Display:wght@400;600;700",
            "rounded": "Nunito:wght@400;600;700",
            "sans-serif": "Inter:wght@400;500;600;700",
            "geometric": "Space+Grotesk:wght@400;500;600;700",
            "display": "Poppins:wght@400;500;600;700",
        }
        return fonts.get(font_tier, fonts["sans-serif"])

    def _get_css_font(self, font_tier: str) -> str:
        """Get CSS font stack for the tier."""
        fonts = {
            "editorial": "'Playfair Display', Georgia, serif",
            "rounded": "'Nunito', system-ui, sans-serif",
            "sans-serif": "'Inter', system-ui, sans-serif",
            "geometric": "'Space Grotesk', system-ui, sans-serif",
            "display": "'Poppins', system-ui, sans-serif",
        }
        return fonts.get(font_tier, fonts["sans-serif"])

    def _get_border_radius(self, vibe_config: Dict) -> str:
        """Get border radius based on vibe."""
        radius_map = {
            "premium": "8px",
            "playful": "24px",
            "professional": "12px",
            "minimal": "4px",
            "bold": "16px",
        }
        return radius_map.get(vibe_config.get("name", "").lower(), "12px")

    def _get_default_content(self, vibe_config: Dict) -> Dict:
        """Get default content structure."""
        return {
            "hero_headline": "Transform Your Vision Into Reality",
            "hero_subheadline": "A powerful platform designed to help you achieve your goals faster and more efficiently than ever before.",
            "features": [
                {
                    "title": "Intuitive Design",
                    "description": "Beautifully crafted interface that feels natural and easy to use from day one.",
                },
                {
                    "title": "Powerful Features",
                    "description": "Everything you need to succeed, built right in with no compromises.",
                },
                {
                    "title": "Dedicated Support",
                    "description": "Expert help whenever you need it, ensuring you're never stuck.",
                },
            ],
            "benefits": [
                "Save time with automated workflows",
                "Scale your business with confidence",
                "Join thousands of happy customers",
            ],
            "testimonial": {
                "quote": "This platform has completely transformed how we work.",
                "author": "Sarah Johnson",
                "role": "CEO, TechStartup",
            },
            "cta_text": "Get Started Free",
            "cta_secondary_text": "See How It Works",
            "footer_tagline": "Making great things happen every day",
        }

    def _generate_fallback_variation(
        self,
        business_name: str,
        tagline: str,
        industry: str,
        vibe_config: Dict,
        vibe_key: str,
    ) -> Dict:
        """Generate fallback variation when AI fails."""

        default_content = self._get_default_content(vibe_config)
        default_content["business_name"] = business_name

        return self._build_website_response(default_content, vibe_config, vibe_key)
