"""
Main generation endpoint for brand creation
"""

from fastapi import APIRouter, HTTPException
from typing import Optional

from app.models.request import (
    BrandGenerationRequest,
    BrandGenerationResponse,
    LogoResult,
    ColorScheme,
    WebsiteContent,
    SEOtags
)
from app.services.logo_gen import LogoGenerator
from app.services.website_gen import WebsiteGenerator
from app.utils.prompts import get_logo_prompt

router = APIRouter()


@router.post("/brand", response_model=BrandGenerationResponse)
async def generate_brand(request: BrandGenerationRequest):
    """
    Generate a complete brand identity including logo, colors, website content, and SEO tags

    Args:
        request: BrandGenerationRequest with business details

    Returns:
        BrandGenerationResponse with all generated assets
    """
    try:
        # Initialize services
        logo_service = LogoGenerator()
        content_service = WebsiteGenerator()

        # Generate logo URL
        logo_prompt = get_logo_prompt(
            request.business_name,
            request.industry,
            request.style
        )
        logo_url = logo_service.get_logo_url(
            request.business_name,
            request.industry,
            request.style,
            request.color_scheme
        )

        # Generate brand content (colors, website copy, SEO)
        brand_content = await content_service.generate_brand_content(
            request.business_name,
            request.industry,
            request.style,
            request.tagline
        )

        # Extract and structure the response
        colors_data = brand_content.get("colors", {})
        website_data = brand_content.get("website_content", {})
        seo_data = brand_content.get("seo_tags", {})

        # Build response object
        response = BrandGenerationResponse(
            business_name=request.business_name,
            logo=LogoResult(
                url=logo_url,
                prompt=logo_prompt
            ),
            colors=ColorScheme(
                primary=colors_data.get("primary", "#3B82F6"),
                secondary=colors_data.get("secondary", "#1E40AF"),
                accent=colors_data.get("accent", "#60A5FA"),
                background=colors_data.get("background", "#FFFFFF"),
                text=colors_data.get("text", "#1F2937")
            ),
            website_content=WebsiteContent(
                headline=website_data.get("headline", f"Welcome to {request.business_name}"),
                subheadline=website_data.get("subheadline", ""),
                about_section=website_data.get("about_section", ""),
                features=website_data.get("features", []),
                cta_text=website_data.get("cta_text", "Get Started"),
                contact_email=website_data.get("contact_email", "info@business.com")
            ),
            seo_tags=SEOtags(
                title=seo_data.get("title", f"{request.business_name} - {request.industry}"),
                description=seo_data.get("description", ""),
                keywords=seo_data.get("keywords", []),
                og_title=seo_data.get("og_title", request.business_name),
                og_description=seo_data.get("og_description", ""),
                json_ld=seo_data.get("json_ld", "")
            )
        )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating brand: {str(e)}"
        )


@router.post("/logo")
async def generate_logo_only(
    business_name: str,
    industry: str,
    style: str = "minimalist",
    color_scheme: Optional[str] = None
):
    """
    Generate only a logo without other brand assets

    Args:
        business_name: Name of the business
        industry: Industry/niche
        style: Logo style
        color_scheme: Optional color scheme

    Returns:
        Logo URL and prompt
    """
    try:
        logo_service = LogoGenerator()

        logo_url = logo_service.get_logo_url(
            business_name,
            industry,
            style,
            color_scheme
        )

        prompt = get_logo_prompt(business_name, industry, style)

        return {
            "url": logo_url,
            "prompt": prompt,
            "business_name": business_name
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Error generating logo"
        )
