def get_system_prompt() -> str:
    return """You are an expert brand strategist, logo designer, copywriter, and web developer.
You create complete brand identities. Always respond with valid JSON.
Be creative, professional, and consistent across all brand elements."""


def get_brand_generation_prompt(
    business_name: str,
    tagline: str,
    industry: str,
    target_audience: str,
    brand_values: list[str],
    primary_goal: str,
    tone: str,
    brand_vibe: str,
    logo_style: str,
    color_mood: str,
    font_personality: str,
    inspiration: str | None = None,
) -> str:
    values_str = ", ".join(brand_values)
    prompt = f"""Create a complete brand identity with these details:
- Business Name: {business_name}
- Tagline: {tagline}
- Industry: {industry}
- Target Audience: {target_audience}
- Brand Values: {values_str}
- Primary Goal: {primary_goal}
- Tone: {tone}
- Brand Vibe: {brand_vibe}
- Logo Style: {logo_style}
- Color Mood: {color_mood}
- Font Personality: {font_personality}
"""
    if inspiration:
        prompt += f"- Inspiration: {inspiration}\n"

    prompt += """
Return valid JSON with this EXACT structure:
{
  "logo_svg": "<svg>...</svg>",
  "colors": {
    "primary": "#HEX",
    "secondary": "#HEX",
    "accent": "#HEX",
    "background": "#HEX",
    "text": "#HEX"
  },
  "website_html": "<!DOCTYPE html>...full landing page html...</html>",
  "social_posts": {
    "twitter": "post text under 280 chars",
    "linkedin": "professional post text",
    "instagram": "post with hashtags"
  },
  "seo_tags": {
    "title": "under 60 chars",
    "description": "under 160 chars",
    "keywords": ["kw1", "kw2", "kw3"],
    "og_title": "og title",
    "og_description": "og description"
  },
  "brand_guide": "# Brand Guide\\n\\n## Colors... full markdown guide...",
  "brand_score": 85
}

Requirements:
1. logo_svg: Generate a valid, clean SVG logo (inline SVG element). Must use the color palette. Must include the business name.
2. website_html: Complete responsive HTML page with hero, features section, about, footer. Use the brand colors. Must be a full valid HTML document.
3. social_posts: Platform-appropriate copy with character limits.
4. seo_tags: Title ≤60 chars, description ≤160 chars.
5. brand_guide: Full markdown with color palette, typography, usage guidelines.
6. brand_score: Integer 0-100 rating the brand completeness.
"""
    return prompt


def get_twist_prompt(
    business_name: str,
    tagline: str,
    industry: str,
    target_audience: str,
    brand_values: list[str],
    primary_goal: str,
    tone: str,
    brand_vibe: str,
    logo_style: str,
    font_personality: str,
    inspiration: str | None = None,
) -> str:
    values_str = ", ".join(brand_values)
    prompt = f"""Reimagine this brand with a RANDOM, SURPRISING color mood twist:
- Business Name: {business_name}
- Tagline: {tagline}
- Industry: {industry}
- Target Audience: {target_audience}
- Brand Values: {values_str}
- Primary Goal: {primary_goal}
- Tone: {tone}
- Brand Vibe: {brand_vibe}
- Logo Style: {logo_style}
- Font Personality: {font_personality}
"""
    if inspiration:
        prompt += f"- Previous Inspiration: {inspiration}\n"

    prompt += """
Pick a completely different color direction (unexpected palette).
Return valid JSON with this EXACT structure:
{
  "logo_svg": "<svg>...</svg>",
  "colors": { "primary": "#HEX", "secondary": "#HEX", "accent": "#HEX", "background": "#HEX", "text": "#HEX" },
  "website_html": "<!DOCTYPE html>...</html>",
  "social_posts": { "twitter": "...", "linkedin": "...", "instagram": "..." },
  "seo_tags": { "title": "...", "description": "...", "keywords": [...], "og_title": "...", "og_description": "..." },
  "brand_guide": "# Brand Guide...",
  "brand_score": 85
}
"""
    return prompt
