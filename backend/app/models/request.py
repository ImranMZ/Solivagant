"""Pydantic request and response models - Enhanced for Stitch-like features"""

from pydantic import BaseModel, Field
from typing import Optional, List


class BrandRequest(BaseModel):
    """Request model for brand generation"""

    business_name: str = Field(
        ..., min_length=1, max_length=100, description="Name of the business"
    )
    tagline: str = Field(
        ..., min_length=1, max_length=200, description="Business tagline/description"
    )
    industry: str = Field(
        ..., min_length=1, max_length=100, description="Industry or niche"
    )
    logo_style: str = Field(
        default="minimalist", description="Logo style (minimalist, modern, playful)"
    )
    color_scheme: Optional[str] = Field(
        default="modern", description="Color scheme preference"
    )
    website_template: Optional[str] = Field(
        default="modern",
        description="Website template style (modern, classic, creative, minimal)",
    )
    vibe: Optional[str] = Field(
        default="professional",
        description="Design vibe (premium, playful, professional, minimal, bold)",
    )
    num_vibes: Optional[int] = Field(
        default=1, ge=1, le=5, description="Number of vibe variations to generate (1-5)"
    )
    generate_prototype: Optional[bool] = Field(
        default=False, description="Generate multi-screen prototype"
    )
    prototype_pages: Optional[List[str]] = Field(
        default=None, description="Pages to include in prototype"
    )


class BrandResponse(BaseModel):
    """Response model for generated brand"""

    success: bool
    data: dict


class VibeVariation(BaseModel):
    """Single vibe variation"""

    vibe_name: str
    vibe_description: str
    vibe_key: str
    html: str
    palette: dict
    headline: str
    features: List[dict]
    benefits: List[str]


class PrototypeScreen(BaseModel):
    """Single screen in prototype"""

    page_name: str
    html: str
    title: str
    meta_description: str


class GenerationMode(str):
    """Generation mode options"""

    SINGLE = "single"
    MULTI_VIBE = "multi_vibe"
    PROTOTYPE = "prototype"
