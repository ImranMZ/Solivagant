def get_system_prompt() -> str:
    return """You are Solivagant — an elite brand strategist, visual designer, copywriter, and front-end developer with 20 years of experience working with top-tier brands.

Your expertise spans:
- Brand strategy & positioning
- Visual identity & logo design (especially SVG-based marks)
- Brand voice & tone development
- Landing page design & copywriting
- Social media content strategy
- SEO optimization

You think in systems. Every element you create — colors, words, layouts — must work together as a cohesive whole. You are creative but strategic, bold but professional.

CRITICAL RULES:
1. Always return valid, parseable JSON — no markdown wrappers, no code blocks, no trailing commas
2. Every field in the requested structure must be populated — never return empty strings for required fields
3. All copy must be original, specific, and compelling — never generic filler text
4. Colors must be carefully chosen with proper contrast ratios and color theory
5. SVG logos must be clean, scalable, and use proper SVG syntax
6. HTML must be complete, valid, and self-contained (inline CSS ok)
7. Brand score must be honest and reflect actual quality of the generated identity"""


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

    prompt = f"""Create a complete, production-ready brand identity for:

BUSINESS PROFILE:
- Name: {business_name}
- Tagline: {tagline}
- Industry: {industry}
- Target Audience: {target_audience}
- Core Values: {values_str}
- Primary Goal: {primary_goal}
- Brand Tone: {tone} (how the brand "speaks" — e.g., formal, friendly, playful)
- Brand Vibe: {brand_vibe} (the emotional feeling — e.g., bold, calm, playful)
- Logo Style: {logo_style} (visual approach — e.g., minimalist, modern, playful)
- Color Mood: {color_mood} (the emotional color direction)
- Font Personality: {font_personality} (typography character)
"""
    if inspiration:
        prompt += f"- Inspiration/References: {inspiration}\n"

    prompt += """
═══════════════════════════════════════════════════════════════
DESIGN DIRECTION
═══════════════════════════════════════════════════════════════

COLORS — Create a harmonious 5-color palette:
- Primary: The dominant brand color (used for CTAs, key elements)
- Secondary: Supporting color (complements primary, used for accents)
- Accent: Highlight color (for badges, highlights, interactive states)
- Background: Page/surface color (light for light mode)
- Text: Body text color (high contrast against background)

Use color theory: analogous, complementary, or triadic relationships. Consider the color_mood as emotional direction, then pick specific hex values that embody it. Ensure WCAG AA contrast between text and background.

LOGO SVG — Create a distinctive, scalable SVG logo:
- Use viewBox="0 0 400 400"
- Include the business name as text element
- Use geometric shapes, icons, or lettermarks that reflect the industry
- Apply the brand colors from the palette
- Style must match the requested logo_style (minimalist = clean lines, playful = rounded shapes, etc.)
- Must look good at 32px, 64px, and 256px sizes
- Use proper SVG elements: <svg>, <path>, <circle>, <rect>, <text>, <g>
- Include xmlns="http://www.w3.org/2000/svg"

WEBSITE HTML — Create a complete, beautiful landing page:
- Full HTML5 document with <!DOCTYPE html>
- Inline <style> block (no external dependencies)
- Sections: Hero with headline + CTA, Features/Services (3 cards), About, Testimonials (2-3), Footer
- Use the brand colors throughout via CSS custom properties
- Responsive design with mobile breakpoints
- Modern CSS: flexbox/grid, smooth transitions, hover effects
- Hero headline must be compelling and specific (not generic)
- Feature cards should have icons (use inline SVG or Unicode symbols)
- Include the business name and tagline prominently
- Font stack should match font_personality (e.g., "Playful Display" → rounded fonts)

SOCIAL MEDIA — Platform-native copy:
- Twitter/X: Under 280 chars, punchy, may include 1-2 relevant hashtags
- LinkedIn: Professional tone, 2-3 paragraphs, thought-leadership angle
- Instagram: Engaging, visual-first caption, 5-10 relevant hashtags, emoji-friendly
- All posts should sound like a real human wrote them, not a bot

SEO — Optimized metadata:
- Title: Under 60 chars, includes business name + primary keyword
- Description: Under 160 chars, compelling call-to-action, includes keywords naturally
- Keywords: 5-8 relevant search terms (not stuffed)
- OG Title/Description: Social-media optimized versions

BRAND GUIDE — Professional markdown document:
- Color palette with hex codes and usage guidelines
- Typography recommendations (font pairings, sizes, weights)
- Logo usage rules (clear space, minimum size, do's and don'ts)
- Brand voice guidelines (tone examples, words to use/avoid)
- Visual style notes (photography style, iconography, patterns)

BRAND SCORE — Honest assessment (0-100):
Consider: color harmony, copy quality, visual consistency, uniqueness, completeness, and overall brand strength. Be critical — a score of 70-85 is typical for a good identity. Reserve 90+ for exceptional work.

═══════════════════════════════════════════════════════════════
OUTPUT FORMAT — Return ONLY this JSON structure, nothing else:
═══════════════════════════════════════════════════════════════

{
  "colors": {
    "primary": "#HEXCODE",
    "secondary": "#HEXCODE",
    "accent": "#HEXCODE",
    "background": "#HEXCODE",
    "text": "#HEXCODE"
  },
  "website_html": "<!DOCTYPE html>...complete HTML document...</html>",
  "social_posts": {
    "twitter": "Punchy tweet under 280 chars with hashtags",
    "linkedin": "Professional 2-3 paragraph post",
    "instagram": "Engaging caption with hashtags and emojis"
  },
  "seo_tags": {
    "title": "Under 60 chars with business name + keyword",
    "description": "Under 160 chars, compelling CTA",
    "keywords": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"],
    "og_title": "Social-optimized title",
    "og_description": "Social-optimized description"
  },
  "brand_guide": "# Brand Guide\\n\\n## Color Palette\\n...full markdown...\\n\\n## Typography\\n...\\n\\n## Logo Usage\\n...\\n\\n## Brand Voice\\n...\\n\\n## Visual Style\\n...",
  "brand_score": 82
}

IMPORTANT: Do NOT include logo_svg in the JSON — that is generated separately. Focus all your energy on making every other element exceptional.
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

    prompt = f"""REIMAGINE this brand with a completely unexpected creative twist:

ORIGINAL BRAND:
- Name: {business_name}
- Tagline: {tagline}
- Industry: {industry}
- Target Audience: {target_audience}
- Core Values: {values_str}
- Primary Goal: {primary_goal}
- Tone: {tone}
- Vibe: {brand_vibe}
- Logo Style: {logo_style}
- Font: {font_personality}
"""
    if inspiration:
        prompt += f"- Previous Inspiration: {inspiration}\n"

    prompt += """
═══════════════════════════════════════════════════════════════
THE TWIST CHALLENGE
═══════════════════════════════════════════════════════════════

Your job is to SURPRISE. Take this brand in a completely different creative direction while keeping it appropriate for the industry and audience.

RULES FOR THE TWIST:
1. COLOR MOOD: Pick a completely different color direction. If the original was "calm blues", go "energetic oranges". If it was "earthy greens", try "bold purples". The twist should feel like a different personality for the same business.
2. VOICE: Shift the tone. If it was formal, make it playful. If it was playful, make it sophisticated. Keep it appropriate but unexpected.
3. VISUAL STYLE: Evolve the logo style. If minimalist, try bold. If professional, try creative.
4. COPY: Rewrite everything with the new voice. Same message, different personality.
5. WEBSITE: Redesign the landing page with the new colors and voice. Different layout energy.

The twist should feel like: "Wow, I never thought of this brand THAT way — but it works!"

═══════════════════════════════════════════════════════════════
OUTPUT FORMAT — Same structure as brand generation:
═══════════════════════════════════════════════════════════════

{
  "colors": {
    "primary": "#HEXCODE (DIFFERENT from original)",
    "secondary": "#HEXCODE",
    "accent": "#HEXCODE",
    "background": "#HEXCODE",
    "text": "#HEXCODE"
  },
  "website_html": "<!DOCTYPE html>...complete redesigned HTML...</html>",
  "social_posts": {
    "twitter": "Rewritten with new voice, under 280 chars",
    "linkedin": "Rewritten with new voice",
    "instagram": "Rewritten with new voice"
  },
  "seo_tags": {
    "title": "Under 60 chars",
    "description": "Under 160 chars",
    "keywords": ["kw1", "kw2", "kw3", "kw4", "kw5"],
    "og_title": "Social title",
    "og_description": "Social description"
  },
  "brand_guide": "# Brand Guide (Twist Version)\\n\\n...full markdown...",
  "brand_score": 80
}

IMPORTANT: Do NOT include logo_svg. Make every element reflect the TWIST — different colors, different voice, different energy.
"""
    return prompt


def get_logo_prompt(
    business_name: str,
    industry: str,
    logo_style: str,
    colors: dict,
    brand_values: list[str],
    tagline: str = "",
) -> str:
    values_str = ", ".join(brand_values)
    primary = colors.get("primary", "#3B82F6")
    secondary = colors.get("secondary", "#1E40AF")
    accent = colors.get("accent", "#60A5FA")

    return f"""Design a professional SVG logo for "{business_name}".

CONTEXT:
- Industry: {industry}
- Tagline: {tagline}
- Brand Values: {values_str}
- Style Direction: {logo_style}
- Brand Colors: Primary={primary}, Secondary={secondary}, Accent={accent}

LOGO DESIGN REQUIREMENTS:
1. Create a CLEAN, SCALABLE SVG that works at 32px favicon size up to 400px hero size
2. Use viewBox="0 0 400 400" with proper xmlns="http://www.w3.org/2000/svg"
3. Include the business name "{business_name}" as a <text> element with proper font styling
4. Include a distinctive ICON/MARK (geometric shape, lettermark, or abstract symbol) that:
   - Reflects the {industry} industry
   - Matches the "{logo_style}" style
   - Uses the brand colors creatively
5. Layout options: icon above text, icon left of text, or integrated lettermark
6. Use <g> groups for logical organization
7. Apply colors from the palette: primary for main elements, secondary for accents
8. Ensure the logo works on both light and dark backgrounds

STYLE GUIDE for "{logo_style}":
- Minimalist: Clean lines, lots of whitespace, simple geometric shapes, thin strokes
- Modern: Bold shapes, gradient-like color blocks, contemporary feel
- Playful: Rounded shapes, bright colors, fun character, slightly irregular
- Professional: Symmetrical, balanced, serif or strong sans-serif, trustworthy
- Bold: Thick strokes, strong contrast, impactful, geometric
- Elegant: Thin lines, refined shapes, sophisticated spacing, graceful

SVG TECHNICAL RULES:
- Return ONLY raw SVG code — no markdown, no code blocks, no explanations
- Start with <svg and end with </svg>
- Use proper SVG attributes (xmlns, viewBox, width, height)
- Use <text> with font-family, font-size, font-weight attributes
- Use <path>, <circle>, <rect>, <polygon>, <line> for shapes
- Group related elements with <g>
- Keep the SVG under 200 lines of code

Return the SVG code now:"""
