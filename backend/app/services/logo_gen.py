"""
Logo Generation Service using Pollinations.ai (Free, No API Key Required)
Generates logos based on text prompts using Pollinations.ai image generation API.
"""

import httpx
from typing import Optional


class LogoGenerator:
    """Service for generating logos using Pollinations.ai"""
    
    BASE_URL = "https://image.pollinations.ai/prompt/"
    
    def __init__(self):
        self.timeout = 30  # seconds
    
    async def generate_logo(
        self,
        business_name: str,
        industry: str,
        style: str = "minimalist",
        color_scheme: Optional[str] = None
    ) -> bytes:
        """
        Generate a logo using Pollinations.ai
        
        Args:
            business_name: Name of the business
            industry: Industry/niche of the business
            style: Style of the logo (e.g., minimalist, modern, playful)
            color_scheme: Optional color scheme preference
            
        Returns:
            Generated logo as bytes (PNG format)
            
        Raises:
            httpx.HTTPError: If the API request fails
        """
        # Build the prompt for logo generation
        prompt = f"Minimalist logo for {business_name} in {industry}, {style} style, vector art, clean design, professional"
        
        if color_scheme:
            prompt += f", {color_scheme} colors"
        
        # URL encode the prompt
        encoded_prompt = httpx.URL.encode_component(prompt)
        logo_url = f"{self.BASE_URL}{encoded_prompt}"
        
        # Fetch the generated logo
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(logo_url)
            response.raise_for_status()
            
            return response.content
    
    def generate_logo_sync(
        self,
        business_name: str,
        industry: str,
        style: str = "minimalist",
        color_scheme: Optional[str] = None
    ) -> bytes:
        """
        Synchronous version of logo generation
        
        Args:
            business_name: Name of the business
            industry: Industry/niche of the business
            style: Style of the logo (e.g., minimalist, modern, playful)
            color_scheme: Optional color scheme preference
            
        Returns:
            Generated logo as bytes (PNG format)
        """
        # Build the prompt for logo generation
        prompt = f"Minimalist logo for {business_name} in {industry}, {style} style, vector art, clean design, professional"
        
        if color_scheme:
            prompt += f", {color_scheme} colors"
        
        # URL encode the prompt
        encoded_prompt = httpx.URL.encode_component(prompt)
        logo_url = f"{self.BASE_URL}{encoded_prompt}"
        
        # Fetch the generated logo
        with httpx.Client(timeout=self.timeout) as client:
            response = client.get(logo_url)
            response.raise_for_status()
            
            return response.content
    
    def get_logo_url(
        self,
        business_name: str,
        industry: str,
        style: str = "minimalist",
        color_scheme: Optional[str] = None
    ) -> str:
        """
        Get the direct URL to the generated logo without downloading it
        
        Args:
            business_name: Name of the business
            industry: Industry/niche of the business
            style: Style of the logo
            color_scheme: Optional color scheme preference
            
        Returns:
            Direct URL to the generated logo image
        """
        prompt = f"Minimalist logo for {business_name} in {industry}, {style} style, vector art, clean design, professional"
        
        if color_scheme:
            prompt += f", {color_scheme} colors"
        
        encoded_prompt = httpx.URL.encode_component(prompt)
        return f"{self.BASE_URL}{encoded_prompt}"
