import re
from groq import Groq
import os


class LogoGenerator:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_svg_logo(
        self,
        business_name: str,
        industry: str,
        logo_style: str,
        colors: dict,
        brand_values: list[str],
        tagline: str = "",
    ) -> str:
        from app.utils.prompts import get_logo_prompt

        prompt = get_logo_prompt(
            business_name, industry, logo_style, colors, brand_values, tagline
        )

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert SVG logo designer. You return ONLY raw SVG code — no markdown, no code blocks, no explanations. Every SVG you create is clean, scalable, and production-ready.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.6,
            max_tokens=3000,
        )

        svg = response.choices[0].message.content.strip()
        svg = self._clean_svg(svg)
        return svg

    def _clean_svg(self, raw: str) -> str:
        """Extract clean SVG from potentially messy LLM output."""
        # Remove markdown code blocks
        raw = re.sub(r"```(?:svg|xml|html)?\s*", "", raw)
        raw = raw.strip()
        if raw.endswith("```"):
            raw = raw[:-3].strip()

        # Extract just the SVG element if there's extra text
        svg_match = re.search(r"<svg[\s\S]*?</svg>", raw, re.IGNORECASE)
        if svg_match:
            raw = svg_match.group(0)

        # Ensure xmlns is present
        if "xmlns=" not in raw and "<svg" in raw:
            raw = raw.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1)

        return raw.strip()
