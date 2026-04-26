"""
Logo Generation Service using Groq API
Generates detailed SVG logos with brand colors - 100% AI
"""

import json
import base64
import re
from ..core.ai_client import get_ai_client


class LogoGenerator:
    """Service for generating detailed SVG logos using Groq LLM"""

    def __init__(self):
        self.ai_client = get_ai_client()
        self._cache: dict[str, str] = {}

    def _build_prompt(
        self,
        business_name: str,
        industry: str,
        style: str,
        colors: dict,
    ) -> str:
        primary = colors.get("primary", "#3B82F6")
        secondary = colors.get("secondary", "#8B5CF6")
        accent = colors.get("accent", "#10B981")
        return f"""Create a detailed, professional SVG logo for {business_name}.

COMPANY: {business_name}
INDUSTRY: {industry}
STYLE: {style}

BRAND COLORS:
- Primary: {primary}
- Secondary: {secondary}
- Accent: {accent}

REQUIREMENTS:
1. Create a COMPLETE SVG with viewBox="0 0 400 400"
2. Include a visually interesting icon/symbol (NOT just text)
3. Include the business name styled beautifully
4. Use the exact brand colors provided
5. Professional, memorable, scalable design
6. Modern and unique - not generic

Return ONLY valid SVG code wrapped in ```svg``` tags. No explanations."""

    def generate_logo_svg(
        self,
        business_name: str,
        industry: str,
        style: str = "minimalist",
        brand_colors: dict = None,
    ) -> str:
        """Generate detailed SVG logo using Groq LLM with brand colors."""
        colors = brand_colors or {
            "primary": "#3B82F6",
            "secondary": "#8B5CF6",
            "accent": "#10B981",
        }

        cache_key = f"{business_name}:{industry}:{style}:{json.dumps(colors, sort_keys=True)}"
        if cache_key in self._cache:
            return self._cache[cache_key]

        prompt = self._build_prompt(business_name, industry, style, colors)
        primary = colors.get("primary", "#3B82F6")
        secondary = colors.get("secondary", "#8B5CF6")
        accent = colors.get("accent", "#10B981")

        try:
            response_text = self.ai_client.generate(
                system_prompt="You are an expert logo designer. Create stunning, professional SVG logos. Only output SVG code.",
                user_prompt=prompt,
                max_tokens=2500,
                temperature=0.8,
            )
            svg = self._extract_svg(response_text, business_name, primary, secondary, accent)
            self._cache[cache_key] = svg
            return svg
        except Exception as e:
            print(f"Error generating logo: {e}")
            return self._get_detailed_fallback(business_name, primary, secondary, accent)

    def generate_all(
        self,
        business_name: str,
        industry: str,
        style: str = "minimalist",
        brand_colors: dict = None,
    ) -> dict:
        """
        Generate SVG and data URL in a single call (uses cache to avoid double API calls).
        Returns dict with 'svg' and 'data_url'.
        """
        svg = self.generate_logo_svg(business_name, industry, style, brand_colors)
        encoded = base64.b64encode(svg.encode()).decode()
        data_url = f"data:image/svg+xml;base64,{encoded}"
        return {"svg": svg, "data_url": data_url}

    def get_logo_html(
        self,
        business_name: str,
        industry: str,
        style: str = "minimalist",
        brand_colors: dict = None,
    ) -> str:
        """Get logo as inline HTML/SVG (alias for generate_logo_svg)."""
        return self.generate_logo_svg(business_name, industry, style, brand_colors)

    def get_logo_data_url(
        self,
        business_name: str,
        industry: str,
        style: str = "minimalist",
        brand_colors: dict = None,
    ) -> str:
        """Get logo as data URL (uses cache to avoid extra API call)."""
        result = self.generate_all(business_name, industry, style, brand_colors)
        return result["data_url"]

    def _extract_svg(
        self,
        response_text: str,
        business_name: str,
        primary: str,
        secondary: str,
        accent: str,
    ) -> str:
        """Extract SVG code from response."""
        svg_match = re.search(r"```svg\s*(.*?)\s*```", response_text, re.DOTALL)
        if svg_match:
            svg = svg_match.group(1).strip()
            if "viewBox" not in svg:
                svg = svg.replace("<svg", '<svg viewBox="0 0 400 400"')
            return svg

        svg_match = re.search(r"<svg.*?</svg>", response_text, re.DOTALL)
        if svg_match:
            svg = svg_match.group(0)
            if "viewBox" not in svg:
                svg = svg.replace("<svg", '<svg viewBox="0 0 400 400"')
            return svg

        return self._get_detailed_fallback(business_name, primary, secondary, accent)

    def _get_detailed_fallback(
        self, business_name: str, primary: str, secondary: str, accent: str
    ) -> str:
        """Generate a detailed fallback logo with brand colors."""
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{primary};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{secondary};stop-opacity:1" />
        </linearGradient>
        <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{primary};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{accent};stop-opacity:1" />
        </linearGradient>
    </defs>

    <!-- Background Circle -->
    <circle cx="200" cy="150" r="100" fill="url(#bgGrad)"/>

    <!-- Icon Elements -->
    <path d="M160 130 L200 100 L240 130 L240 170 L200 200 L160 170 Z" fill="white" opacity="0.9"/>
    <circle cx="200" cy="145" r="30" fill="white"/>

    <!-- Brand Initial -->
    <text x="200" y="160" font-family="Arial, sans-serif" font-size="35" font-weight="bold" fill="{primary}" text-anchor="middle">{business_name[:1].upper()}</text>

    <!-- Decorative Elements -->
    <circle cx="145" cy="120" r="8" fill="{accent}" opacity="0.8"/>
    <circle cx="255" cy="120" r="6" fill="{accent}" opacity="0.6"/>
    <circle cx="130" cy="180" r="5" fill="{secondary}" opacity="0.5"/>

    <!-- Business Name -->
    <text x="200" y="310" font-family="Arial, sans-serif" font-size="42" font-weight="bold" fill="url(#textGrad)" text-anchor="middle" letter-spacing="2">{business_name}</text>

    <!-- Subtitle Line -->
    <rect x="100" y="335" width="200" height="3" rx="1.5" fill="url(#bgGrad)" opacity="0.6"/>
</svg>'''
