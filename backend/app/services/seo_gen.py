"""
SEO Generation Service using Groq API
Generates SEO metadata and tags
"""

import os
from groq import Groq
import json


class SEOGenerator:
    """Service for generating SEO metadata"""
    
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile")
    
    def generate_seo(
        self,
        business_name: str,
        tagline: str,
        industry: str
    ) -> dict:
        """
        Generate SEO metadata
        
        Args:
            business_name: Name of the business
            tagline: Business tagline
            industry: Industry type
            
        Returns:
            Dictionary with SEO metadata
        """
        
        prompt = f"""Generate SEO metadata for a website for {business_name}.
        
Tagline: {tagline}
Industry: {industry}

Create SEO metadata in JSON format with the following fields:
1. title: Meta title (max 60 characters)
2. description: Meta description (max 160 characters)
3. keywords: Array of 5-8 relevant keywords
4. og_title: Open Graph title
5. og_description: Open Graph description
6. twitter_card: Twitter card type

Respond ONLY with valid JSON, no other text."""

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500,
            )
            
            # Parse response
            response_text = completion.choices[0].message.content
            
            # Extract JSON from response
            try:
                # Try direct JSON parsing first
                seo_data = json.loads(response_text)
            except json.JSONDecodeError:
                # If that fails, extract JSON from text
                import re
                json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                if json_match:
                    seo_data = json.loads(json_match.group())
                else:
                    seo_data = self._get_default_seo(business_name, tagline)
            
            return seo_data
            
        except Exception as e:
            print(f"Error generating SEO: {e}")
            return self._get_default_seo(business_name, tagline)
    
    def _get_default_seo(self, business_name: str, tagline: str) -> dict:
        """Get default SEO metadata if generation fails"""
        return {
            "title": f"{business_name} | {tagline[:40]}",
            "description": f"{tagline[:160]}",
            "keywords": [
                business_name.lower(),
                "brand",
                "professional",
                "digital presence",
                "web solution",
                "modern design"
            ],
            "og_title": business_name,
            "og_description": tagline,
            "twitter_card": "summary_large_image"
        }
