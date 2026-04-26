"""
Response models for Solivagant API endpoints.
All models are Pydantic v2 compatible.
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class HealthResponse(BaseModel):
    status: str = Field(..., description="Health status of the service")
    service: str = Field(..., description="Service name")


class LogoResponse(BaseModel):
    logo_svg: str = Field(..., description="SVG markup for the generated logo")
    logo_url: Optional[str] = Field(
        None, description="Data URL (base64) for the SVG logo – optional"
    )


class GenerateResponse(BaseModel):
    success: bool = Field(..., description="Whether generation succeeded")
    data: Dict = Field(..., description="All generated assets (logo, website, social, SEO, etc.)")


class VibeResponse(BaseModel):
    multiple_vibes: bool = Field(..., description="True when multiple vibe variations are returned")
    variations: List[Dict] = Field(..., description="List of vibe variation payloads")
    html: Optional[str] = Field(None, description="HTML of the primary variation")
    palette: Optional[Dict] = Field(None, description="Color palette of the primary variation")
    vibe_name: Optional[str] = Field(None, description="Name of the primary vibe")
    vibe_description: Optional[str] = Field(None, description="Description of the primary vibe")


class PrototypeResponse(BaseModel):
    screens: Dict[str, Dict] = Field(..., description="Screen name → data for each prototype screen")
    navigation_flow: List[str] = Field(..., description="Ordered list of page keys for navigation")
    start_page: str = Field(..., description="Entry page key for the prototype")
    total_screens: int = Field(..., description="Total number of screens generated")


class SocialPostsResponse(BaseModel):
    posts: List[Dict] = Field(..., description="List of generated social media post objects")


class SEOResponse(BaseModel):
    title: str = Field(..., description="Meta title")
    description: str = Field(..., description="Meta description")
    keywords: List[str] = Field(..., description="SEO keywords")
    og_title: str = Field(..., description="Open Graph title")
    og_description: str = Field(..., description="Open Graph description")
    twitter_card: str = Field(..., description="Twitter card type")
