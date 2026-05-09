import json
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
    ) -> str:
        values_str = ", ".join(brand_values)
        prompt = f"""Generate a clean, professional SVG logo for a business.

Business: {business_name}
Industry: {industry}
Logo Style: {logo_style}
Brand Values: {values_str}
Colors: primary={colors.get('primary')}, secondary={colors.get('secondary')}, accent={colors.get('accent')}

Rules:
- Return ONLY valid SVG code wrapped in <svg> tags
- Use viewBox="0 0 400 400"
- Include the business name text in the logo
- Use the brand colors provided
- Style must be: {logo_style}
- Do NOT wrap in markdown code blocks, return raw SVG only"""

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an expert SVG logo designer. Return raw SVG code only, no markdown."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=1500,
        )

        svg = response.choices[0].message.content.strip()
        if svg.startswith("```svg"):
            svg = svg[7:]
        if svg.startswith("```"):
            svg = svg[3:]
        if svg.endswith("```"):
            svg = svg[:-3]
        return svg.strip()
