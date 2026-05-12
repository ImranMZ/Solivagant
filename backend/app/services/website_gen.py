import json
import os
from groq import Groq

from app.utils.prompts import get_system_prompt, get_brand_generation_prompt, get_twist_prompt


class WebsiteGenerator:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_brand(
        self,
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
    ) -> dict:
        system_prompt = get_system_prompt()
        user_prompt = get_brand_generation_prompt(
            business_name, tagline, industry, target_audience,
            brand_values, primary_goal, tone, brand_vibe,
            logo_style, color_mood, font_personality, inspiration,
        )

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
            max_tokens=6000,
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content
        result = json.loads(content)
        return self._validate_and_fill(result, business_name)

    def twist_brand(
        self,
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
    ) -> dict:
        system_prompt = get_system_prompt()
        user_prompt = get_twist_prompt(
            business_name, tagline, industry, target_audience,
            brand_values, primary_goal, tone, brand_vibe,
            logo_style, font_personality, inspiration,
        )

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.85,
            max_tokens=6000,
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content
        result = json.loads(content)
        return self._validate_and_fill(result, business_name)

    def _validate_and_fill(self, data: dict, business_name: str) -> dict:
        """Ensure all required fields exist with sensible defaults."""
        # Colors
        if "colors" not in data or not isinstance(data["colors"], dict):
            data["colors"] = {}
        colors = data["colors"]
        default_colors = {
            "primary": "#8B5CF6",
            "secondary": "#A78BFA",
            "accent": "#F472B6",
            "background": "#FFFFFF",
            "text": "#1E293B",
        }
        for key, default in default_colors.items():
            if not colors.get(key):
                colors[key] = default

        # Website HTML
        if not data.get("website_html"):
            data["website_html"] = self._fallback_html(business_name, colors)

        # Social posts
        if "social_posts" not in data or not isinstance(data["social_posts"], dict):
            data["social_posts"] = {}
        social = data["social_posts"]
        if not social.get("twitter"):
            social["twitter"] = f"Introducing {business_name} — where innovation meets purpose. 🚀"
        if not social.get("linkedin"):
            social["linkedin"] = f"Excited to share {business_name} with the world. Our mission is simple: deliver excellence in everything we do. Follow our journey."
        if not social.get("instagram"):
            social["instagram"] = f"✨ {business_name} is here! Follow us for updates, behind-the-scenes, and more. #{business_name.replace(' ', '')}"

        # SEO tags
        if "seo_tags" not in data or not isinstance(data["seo_tags"], dict):
            data["seo_tags"] = {}
        seo = data["seo_tags"]
        if not seo.get("title"):
            seo["title"] = f"{business_name} — Welcome"
        if not seo.get("description"):
            seo["description"] = f"Discover {business_name}. We deliver exceptional value and quality."
        if not seo.get("keywords") or not isinstance(seo["keywords"], list):
            seo["keywords"] = [business_name.lower(), "quality", "innovation", "services"]
        if not seo.get("og_title"):
            seo["og_title"] = business_name
        if not seo.get("og_description"):
            seo["og_description"] = seo["description"]

        # Brand guide
        if not data.get("brand_guide"):
            data["brand_guide"] = f"# {business_name} Brand Guide\n\n## Colors\n- Primary: {colors['primary']}\n- Secondary: {colors['secondary']}\n- Accent: {colors['accent']}\n\n## Typography\n- Headings: Bold, modern sans-serif\n- Body: Clean, readable sans-serif"

        # Brand score
        if not data.get("brand_score") or not isinstance(data["brand_score"], int):
            data["brand_score"] = 75
        data["brand_score"] = max(0, min(100, data["brand_score"]))

        return data

    def _fallback_html(self, business_name: str, colors: dict) -> str:
        """Generate a minimal landing page if AI fails."""
        primary = colors.get("primary", "#8B5CF6")
        secondary = colors.get("secondary", "#A78BFA")
        text = colors.get("text", "#1E293B")
        bg = colors.get("background", "#FFFFFF")
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{business_name}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: system-ui, sans-serif; color: {text}; background: {bg}; }}
  .hero {{ background: linear-gradient(135deg, {primary}, {secondary}); color: white; padding: 80px 20px; text-align: center; }}
  .hero h1 {{ font-size: 3rem; margin-bottom: 16px; }}
  .hero p {{ font-size: 1.25rem; opacity: 0.9; }}
  .cta {{ display: inline-block; margin-top: 24px; padding: 14px 32px; background: white; color: {primary}; border-radius: 9999px; text-decoration: none; font-weight: 700; }}
  .features {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; padding: 60px 20px; max-width: 1100px; margin: 0 auto; }}
  .feature {{ padding: 32px; border-radius: 16px; background: #f8fafc; text-align: center; }}
  .feature h3 {{ margin: 16px 0 8px; }}
  .footer {{ text-align: center; padding: 40px 20px; color: #64748b; border-top: 1px solid #e2e8f0; }}
</style>
</head>
<body>
<section class="hero">
  <h1>{business_name}</h1>
  <p>Welcome to the future of excellence.</p>
  <a href="#" class="cta">Get Started</a>
</section>
<section class="features">
  <div class="feature">
    <h3>🚀 Innovation</h3>
    <p>Cutting-edge solutions tailored to your needs.</p>
  </div>
  <div class="feature">
    <h3>💎 Quality</h3>
    <p>Uncompromising standards in everything we do.</p>
  </div>
  <div class="feature">
    <h3>🤝 Trust</h3>
    <p>Building lasting relationships with our clients.</p>
  </div>
</section>
<footer class="footer">
  <p>&copy; 2025 {business_name}. All rights reserved.</p>
</footer>
</body>
</html>'''
