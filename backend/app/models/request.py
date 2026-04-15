"""Pydantic request and response models"""
from pydantic import BaseModel, Field
from typing import Optional


class BrandRequest(BaseModel):
    """Request model for brand generation"""
    business_name: str = Field(..., min_length=1, max_length=100, description="Name of the business")
    tagline: str = Field(..., min_length=1, max_length=200, description="Business tagline/description")
    industry: str = Field(..., min_length=1, max_length=100, description="Industry or niche")
    logo_style: str = Field(default="minimalist", description="Logo style (minimalist, modern, playful)")
    color_scheme: Optional[str] = Field(default="modern", description="Color scheme preference")
    website_template: Optional[str] = Field(default="modern", description="Website template style (modern, classic, creative, minimal)")


class BrandResponse(BaseModel):
    """Response model for generated brand"""
    success: bool
    data: dict
