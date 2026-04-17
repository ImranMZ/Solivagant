"""
Social Media Posts Generation Service using Groq LLM
100% AI-generated shareable poster designs with brand colors
"""

import os
import json
from typing import List, Dict
from groq import Groq


class SocialPostsGenerator:
    """Service for generating social media posts with detailed poster designs - 100% Groq AI"""

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    def generate_posts(
        self,
        business_name: str,
        tagline: str,
        vibe: str = "professional",
        num_posts: int = 3,
        brand_colors: dict = None,
    ) -> List[Dict]:
        """Generate social media posts with detailed shareable poster designs."""
        colors = brand_colors or {
            "primary": "#3B82F6",
            "secondary": "#8B5CF6",
            "accent": "#10B981",
        }

        prompt = self._build_prompt(business_name, tagline, vibe, colors, num_posts)

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert social media designer. Create stunning HTML/CSS poster designs.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.85,
                max_tokens=4500,
            )

            response_text = completion.choices[0].message.content
            return self._parse_posts(
                response_text, business_name, tagline, vibe, colors, num_posts
            )

        except Exception as e:
            print(f"Error generating posts: {e}")
            return self._get_detailed_posts(business_name, tagline, vibe, colors)

    def _build_prompt(
        self, business_name: str, tagline: str, vibe: str, colors: dict, num_posts: int
    ) -> str:
        """Build prompt for unique AI-generated poster designs."""

        primary = colors.get("primary", "#3B82F6")
        secondary = colors.get("secondary", "#8B5CF6")
        accent = colors.get("accent", "#10B981")

        return f"""Create {num_posts} UNIQUE and CREATIVE social media poster designs for {business_name} using AI.

BUSINESS: {business_name}
TAGLINE: {tagline}
VIBE STYLE: {vibe}

BRAND COLORS:
- Primary: {primary}
- Secondary: {secondary}  
- Accent: {accent}

REQUIREMENTS for each UNIQUE poster:

POSTER 1 - Twitter/Launch (800x800):
- Creative gradient background using {primary} and {secondary}
- Large typography for brand name "{business_name}"
- Include tagline: "{tagline}"
- Add animated elements or geometric shapes
- Professional, eye-catching design

POSTER 2 - LinkedIn/Story (800x800):
- Different color scheme - use {secondary} and {accent}
- Quote format with inspiring message about brand
- Include decorative border or card design
- Warm, corporate feel

POSTER 3 - Instagram/Product (800x800):
- Bold design with {primary} as dominant
- Feature-focused with call-to-action
- Modern, trendy aesthetic
- Include platform icon

CRITICAL: Each poster_html must be DIFFERENT from the others. Use varied layouts, colors, and styles.

Return ONLY valid JSON array:
[
    {{
        "platform": "twitter",
        "caption": "Your unique caption text...",
        "hashtags": ["#Unique1", "#Tag2", "#Tag3"],
        "brand_message": "Punchy headline",
        "poster_html": "Full HTML div with inline styles"
    }}
]

Make each poster UNIQUE and completely different from others!"""

    def _parse_posts(
        self,
        response_text: str,
        business_name: str,
        tagline: str,
        vibe: str,
        colors: dict,
        num_posts: int,
    ) -> List[Dict]:
        """Parse AI response."""
        try:
            posts = json.loads(response_text)
        except json.JSONDecodeError:
            import re

            json_match = re.search(r"\[.*\]", response_text, re.DOTALL)
            if json_match:
                try:
                    posts = json.loads(json_match.group())
                except json.JSONDecodeError:
                    return self._get_detailed_posts(
                        business_name, tagline, vibe, colors
                    )
            else:
                return self._get_detailed_posts(business_name, tagline, vibe, colors)

        # Ensure all posts have poster_html
        for post in posts:
            if "poster_html" not in post or not post["poster_html"]:
                post["poster_html"] = self._generate_detailed_poster(
                    post, business_name, tagline, vibe, colors
                )

        return posts

    def _generate_detailed_poster(
        self, post: Dict, business_name: str, tagline: str, vibe: str, colors: dict
    ) -> str:
        """Generate detailed poster HTML with brand colors."""
        primary = colors.get("primary", "#3B82F6")
        secondary = colors.get("secondary", "#8B5CF6")
        accent = colors.get("accent", "#10B981")
        brand_msg = post.get("brand_message", business_name)
        platform = post.get("platform", "twitter")
        tagline_text = tagline or ""

        return f"""<div style="width:800px;height:800px;background:linear-gradient(135deg,{primary} 0%,{secondary} 100%);font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;color:white;text-align:center;padding:60px;box-sizing:border-box;position:relative;overflow:hidden;">
    <!-- Decorative circles -->
    <div style="position:absolute;top:-100px;right:-100px;width:300px;height:300px;background:rgba(255,255,255,0.1);border-radius:50%;"></div>
    <div style="position:absolute;bottom:-50px;left:-50px;width:200px;height:200px;background:rgba(255,255,255,0.08);border-radius:50%;"></div>

    <!-- Logo Icon -->
    <div style="width:120px;height:120px;background:white;border-radius:30px;display:flex;align-items:center;justify-content:center;margin-bottom:40px;box-shadow:0 20px 60px rgba(0,0,0,0.3);">
        <span style="color:{primary};font-size:60px;font-weight:bold;">{business_name[:1].upper()}</span>
    </div>

    <!-- Brand Message -->
    <h1 style="font-size:64px;font-weight:800;margin:0 0 20px;letter-spacing:-2px;text-shadow:0 4px 20px rgba(0,0,0,0.3);max-width:700px;">{brand_msg}</h1>

    <!-- Tagline -->
    <p style="font-size:28px;margin:0 0 50px;opacity:0.95;max-width:600px;line-height:1.4;">{tagline_text}</p>

    <!-- Decorative Line -->
    <div style="width:100px;height:4px;background:white;border-radius:2px;margin-bottom:40px;"></div>

    <!-- Business Name -->
    <p style="font-size:36px;font-weight:700;margin:0;letter-spacing:4px;">{business_name.upper()}</p>

    <!-- Platform Badge -->
    <div style="position:absolute;bottom:30px;right:30px;background:rgba(255,255,255,0.2);padding:10px 20px;border-radius:20px;font-size:16px;font-weight:600;">
        {platform.upper()}
    </div>
</div>"""

    def _get_detailed_posts(
        self, business_name: str, tagline: str, vibe: str, colors: dict
    ) -> List[Dict]:
        """Get detailed default posts."""
        posts = [
            {
                "platform": "twitter",
                "caption": f"🚀 {business_name} is here! {tagline} The future of innovation starts now. Join us! #{business_name.replace(' ', '')}",
                "hashtags": [
                    f"#{business_name.replace(' ', '')}",
                    "#Innovation",
                    "#Launch",
                    "#Tech",
                ],
                "brand_message": "The Future Is Here",
            },
            {
                "platform": "linkedin",
                "caption": f"Proud to introduce {business_name} - {tagline}. Our mission: deliver exceptional value and drive meaningful change. Join our journey!",
                "hashtags": [
                    f"#{business_name.replace(' ', '')}",
                    "#Leadership",
                    "#Growth",
                    "#Innovation",
                ],
                "brand_message": "Building Tomorrow Together",
            },
            {
                "platform": "instagram",
                "caption": f"Something extraordinary is coming. {business_name}. {tagline}. Are you ready for what's next? ✨",
                "hashtags": [
                    f"#{business_name.replace(' ', '')}",
                    "#ComingSoon",
                    "#Reveal",
                    "#Launch",
                ],
                "brand_message": "Something Great Is Coming",
            },
        ]

        for post in posts:
            post["poster_html"] = self._generate_detailed_poster(
                post, business_name, tagline, vibe, colors
            )

        return posts
