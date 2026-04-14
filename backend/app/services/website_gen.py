"""
Website content generation service using Groq API (Llama 3)
"""

import json
from groq import Groq
from typing import Dict, Any
import os

from app.utils.prompts import get_system_prompt, get_brand_generation_prompt


class WebsiteGenerator:
    """Service for generating website content using Groq API"""

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    async def generate_brand_content(
        self,
        business_name: str,
        industry: str,
        style: str,
        tagline: str = None
    ) -> Dict[str, Any]:
        """
        Generate complete brand content including colors, website copy, and SEO tags

        Args:
            business_name: Name of the business
            industry: Industry/niche
            style: Brand style
            tagline: Optional tagline

        Returns:
            Dictionary containing colors, website_content, and seo_tags
        """
        system_prompt = get_system_prompt()
        user_prompt = get_brand_generation_prompt(business_name, industry, style, tagline)

        try:
            response = self.client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=2048,
                response_format={"type": "json_object"}
            )

            content = response.choices[0].message.content

            # Parse JSON response
            result = json.loads(content)

            # Validate and structure the response
            return {
                "colors": result.get("colors", {}),
                "website_content": result.get("website_content", {}),
                "seo_tags": result.get("seo_tags", {})
            }

        except Exception:
            # Fallback to default values if API fails
            return self._get_fallback_content(business_name, industry, style)

    def _get_fallback_content(self, business_name: str, industry: str, style: str) -> Dict[str, Any]:
        """Generate fallback content if AI generation fails"""
        return {
            "colors": {
                "primary": "#3B82F6",
                "secondary": "#1E40AF",
                "accent": "#60A5FA",
                "background": "#FFFFFF",
                "text": "#1F2937"
            },
            "website_content": {
                "headline": f"Welcome to {business_name}",
                "subheadline": f"Your trusted partner in {industry}",
                "about_section": f"{business_name} is a leading provider in the {industry} sector. We deliver exceptional quality and service.",
                "features": [
                    "Professional Service",
                    "Quality Guaranteed",
                    "Customer Support"
                ],
                "cta_text": "Get Started Today",
                "contact_email": f"info@{business_name.lower().replace(' ', '')}.com"
            },
            "seo_tags": {
                "title": f"{business_name} - {industry} Services",
                "description": f"{business_name} provides professional {industry} services. Contact us today!",
                "keywords": [industry.lower(), business_name.lower(), "professional services"],
                "og_title": business_name,
                "og_description": f"Discover {business_name} for all your {industry} needs",
                "json_ld": '{"@context": "https://schema.org", "@type": "LocalBusiness", "name": "' + business_name + '"}'
            }
        }
