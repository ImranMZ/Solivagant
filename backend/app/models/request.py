from pydantic import BaseModel, Field
from typing import Optional, List


class BrandGenerationRequest(BaseModel):
    business_name: str = Field(..., min_length=1, max_length=100)
    tagline: str = Field(..., min_length=1, max_length=200)
    industry: str = Field(..., min_length=1, max_length=200)
    target_audience: str = Field(..., min_length=1)
    brand_values: List[str] = Field(..., min_length=2, max_length=4)
    primary_goal: str = Field(..., min_length=1)
    tone: str = Field(default="friendly")
    brand_vibe: str = Field(...)
    logo_style: str = Field(...)
    color_mood: str = Field(...)
    font_personality: str = Field(...)
    inspiration: Optional[str] = None


class LogoResult(BaseModel):
    svg: str
    prompt: str


class ColorScheme(BaseModel):
    primary: str
    secondary: str
    accent: str
    background: str
    text: str


class WebsiteContent(BaseModel):
    html: str


class SocialPosts(BaseModel):
    twitter: str
    linkedin: str
    instagram: str


class SEOtags(BaseModel):
    title: str
    description: str
    keywords: List[str]
    og_title: str
    og_description: str


class BrandGenerationResponse(BaseModel):
    business_name: str
    logo: LogoResult
    colors: ColorScheme
    website_content: WebsiteContent
    social_posts: SocialPosts
    seo_tags: SEOtags
    brand_guide: str
    brand_score: int
