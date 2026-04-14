"""
Pydantic models for request/response validation
"""

from pydantic import BaseModel, Field
from typing import Optional, List


class BrandGenerationRequest(BaseModel):
    """Request model for brand generation"""
    business_name: str = Field(..., min_length=1, max_length=100, description="Name of the business")
    industry: str = Field(..., min_length=1, max_length=200, description="Industry or niche")
    style: str = Field(default="minimalist", description="Brand style (e.g., minimalist, modern, playful)")
    color_scheme: Optional[str] = Field(None, max_length=100, description="Preferred color scheme")
    tagline: Optional[str] = Field(None, max_length=200, description="Optional tagline")


class LogoResult(BaseModel):
    """Logo generation result"""
    url: str
    prompt: str


class SEOtags(BaseModel):
    """SEO meta tags"""
    title: str
    description: str
    keywords: List[str]
    og_title: str
    og_description: str
    json_ld: str


class WebsiteContent(BaseModel):
    """Generated website content"""
    headline: str
    subheadline: str
    about_section: str
    features: List[str]
    cta_text: str
    contact_email: str


class ColorScheme(BaseModel):
    """Brand color scheme"""
    primary: str
    secondary: str
    accent: str
    background: str
    text: str


class BrandGenerationResponse(BaseModel):
    """Complete brand generation response"""
    business_name: str
    logo: LogoResult
    colors: ColorScheme
    website_content: WebsiteContent
    seo_tags: SEOtags
    html_preview_url: Optional[str] = None
