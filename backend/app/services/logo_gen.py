"""
Logo Generation Service using Pollinations.ai (Free, No API Key Required)
Generates logos based on text prompts using Pollinations.ai image generation API.
"""

import httpx
from typing import Optional
from urllib.parse import quote


class LogoGenerator:
    """Service for generating logos using Pollinations.ai"""
    
    BASE_URL = "https://image.pollinations.ai/prompt/"
    
    def __init__(self):
        self.timeout = 30  # seconds
    
    def _build_prompt(
        self,
        business_name: str,
        industry: str,
        style: str = "minimalist",
        color_scheme: Optional[str] = None
    ) -> str:
        prompt = f"Minimalist logo for {business_name} in {industry}, {style} style, vector art, clean design, professional"
        if color_scheme:
            prompt += f", {color_scheme} colors"
        return prompt

    def get_logo_url(
        self,
        business_name: str,
        industry: str,
        style: str = "minimalist",
        color_scheme: Optional[str] = None
    ) -> str:
        """
        Get the direct URL to the generated logo without downloading it
        """
        prompt = self._build_prompt(business_name, industry, style, color_scheme)
        encoded_prompt = quote(prompt)
        return f"{self.BASE_URL}{encoded_prompt}"

    def fetch_logo_bytes(
        self,
        business_name: str,
        industry: str,
        style: str = "minimalist",
        color_scheme: Optional[str] = None
    ) -> bytes:
        """
        Download the logo image bytes from Pollinations.ai
        """
        url = self.get_logo_url(business_name, industry, style, color_scheme)
        with httpx.Client(timeout=self.timeout) as client:
            response = client.get(url)
            response.raise_for_status()
            return response.content
