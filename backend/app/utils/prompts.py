"""
AI prompt templates for content generation
"""

def get_system_prompt() -> str:
    """Get the system prompt for the AI"""
    return """You are an expert brand strategist and web developer. 
Your task is to create complete brand identities and landing page content.
Always respond with valid JSON that matches the expected schema.
Be creative, professional, and ensure consistency across all brand elements."""


def get_brand_generation_prompt(business_name: str, industry: str, style: str, tagline: str = None) -> str:
    """Generate the prompt for brand creation"""
    
    prompt = f"""Create a complete brand identity for a business with these details:
- Business Name: {business_name}
- Industry: {industry}
- Style: {style}
"""
    
    if tagline:
        prompt += f"- Tagline: {tagline}\n"
    
    prompt += """
Provide the following in valid JSON format:
{
  "colors": {
    "primary": "#HEXCODE",
    "secondary": "#HEXCODE",
    "accent": "#HEXCODE",
    "background": "#HEXCODE",
    "text": "#HEXCODE"
  },
  "website_content": {
    "headline": "Compelling headline (max 60 chars)",
    "subheadline": "Supporting subheadline (max 120 chars)",
    "about_section": "Brief about section (2-3 sentences)",
    "features": ["Feature 1", "Feature 2", "Feature 3"],
    "cta_text": "Call-to-action button text",
    "contact_email": "contact@business.com"
  },
  "seo_tags": {
    "title": "SEO title (max 60 chars)",
    "description": "Meta description (max 160 chars)",
    "keywords": ["keyword1", "keyword2", "keyword3"],
    "og_title": "Open Graph title",
    "og_description": "Open Graph description",
    "json_ld": "JSON-LD structured data string"
  }
}

Ensure:
1. Colors work well together and match the {style} style
2. Content is engaging and professional
3. SEO tags are optimized for search engines
4. All text is original and compelling
"""
    
    return prompt


def get_logo_prompt(business_name: str, industry: str, style: str) -> str:
    """Generate prompt for logo creation"""
    return f"Minimalist logo for {business_name} in {industry}, {style} style, vector art, clean design, professional"
