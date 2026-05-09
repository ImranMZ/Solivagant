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
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
            max_tokens=4096,
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content
        return json.loads(content)

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
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.9,
            max_tokens=4096,
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content
        return json.loads(content)
