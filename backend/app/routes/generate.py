"""Generation endpoints for brand and website creation - Enhanced with AI capabilities"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from ..models.request import BrandRequest
from ..services.logo_gen import LogoGenerator
from ..services.website_gen_ai import WebsiteGeneratorAI
from ..services.seo_gen import SEOGenerator
from ..services.social_posts_gen import SocialPostsGenerator

router = APIRouter()


class SocialPostsRequest(BaseModel):
    business_name: str
    tagline: str
    vibe: str = "professional"
    num_posts: int = 3


@router.post("/generate")
def generate_brand(request: BrandRequest):
    """
    Generate complete brand identity with AI-powered website.

    Features:
    - AI-generated unique websites (not template-based)
    - Multiple vibe variations (Stitch-like "vibe design")
    - Multi-screen prototype generation
    - Intelligent SEO metadata

    Args:
        request: BrandRequest with business details

    Returns:
        Generated brand assets including website HTML, logo, SEO, and vibes
    """
    try:
        logo_gen = LogoGenerator()
        website_gen = WebsiteGeneratorAI()
        seo_gen = SEOGenerator()

        # Generate SVG logo using Groq
        logo_svg = logo_gen.get_logo_html(
            business_name=request.business_name,
            industry=request.industry,
            style=request.logo_style,
        )

        logo_data_url = logo_gen.get_logo_data_url(
            business_name=request.business_name,
            industry=request.industry,
            style=request.logo_style,
        )

        website_result = website_gen.generate_website(
            business_name=request.business_name,
            tagline=request.tagline,
            industry=request.industry,
            vibe=request.vibe or "professional",
            num_vibes=request.num_vibes or 1,
        )

        seo_tags = seo_gen.generate_seo(
            business_name=request.business_name,
            tagline=request.tagline,
            industry=request.industry,
        )

        posts_gen = SocialPostsGenerator()
        social_posts = posts_gen.generate_posts(
            business_name=request.business_name,
            tagline=request.tagline,
            vibe=request.vibe or "professional",
            num_posts=3,
        )

        response_data = {
            "business_name": request.business_name,
            "tagline": request.tagline,
            "industry": request.industry,
            "logo_svg": logo_svg,
            "logo_url": logo_data_url,
            "logo_download_url": f"data:image/svg+xml;base64,{logo_svg}",
            "seo_tags": seo_tags,
            "social_posts": social_posts,
        }

        if website_result.get("multiple_vibes"):
            response_data.update(
                {
                    "multiple_vibes": True,
                    "variations": website_result.get("variations", []),
                    "website_html": website_result.get("html", ""),
                    "design_palette": website_result.get("palette", {}),
                    "vibe_name": website_result.get("vibe_name", ""),
                    "vibe_description": website_result.get("vibe_description", ""),
                    "theme_name": website_result.get("vibe_name", ""),
                    "font_family": "Inter, system-ui, sans-serif",
                    "features": website_result.get("variations", [{}])[0].get(
                        "features", []
                    )
                    if website_result.get("variations")
                    else [],
                    "benefits": website_result.get("variations", [{}])[0].get(
                        "benefits", []
                    )
                    if website_result.get("variations")
                    else [],
                }
            )
        else:
            response_data.update(
                {
                    "multiple_vibes": False,
                    "website_html": website_result.get("html", ""),
                    "design_palette": website_result.get("palette", {}),
                    "vibe_name": website_result.get("vibe_name", ""),
                    "vibe_description": website_result.get("vibe_description", ""),
                    "vibe_key": website_result.get("vibe_key", ""),
                    "theme_name": website_result.get("vibe_name", ""),
                    "font_family": "Inter, system-ui, sans-serif",
                    "features": website_result.get("features", []),
                    "benefits": website_result.get("benefits", []),
                    "headline": website_result.get("headline", ""),
                    "cta_text": website_result.get("cta_text", "Get Started"),
                    "layout_variant": website_result.get(
                        "layout_variant", "modern_grid"
                    ),
                }
            )

        # Prototype generation temporarily disabled - missing PrototypeGenerator module
        if False and request.generate_prototype:  # pylint: disable=condition-eval-to-constant
            # prototype_gen = PrototypeGenerator()
            # prototype_pages = request.prototype_pages or [...]
            pass

        return {"success": True, "data": response_data}

    except Exception as e:
        import traceback

        print(f"Error in generate_brand: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate/vibes")
def generate_vibes(request: BrandRequest):
    """
    Generate multiple vibe variations (Stitch-like vibe design).

    Returns multiple design directions the user can choose from.
    """
    try:
        website_gen = WebsiteGeneratorAI()

        result = website_gen.generate_website(
            business_name=request.business_name,
            tagline=request.tagline,
            industry=request.industry,
            vibe=request.vibe or "professional",
            num_vibes=request.num_vibes or 3,
        )

        return {
            "success": True,
            "data": {
                "multiple_vibes": True,
                "variations": result.get("variations", []),
                "total_vibes": len(result.get("variations", [])),
            },
        }

    except Exception as e:
        print(f"Error generating vibes: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate/prototype")
def generate_prototype(request: BrandRequest):
    """
    Generate multi-screen prototype (Stitch-like prototyping).

    Creates interconnected screens that form a complete user flow.
    """
    try:
        prototype_gen = PrototypeGenerator()
        logo_gen = LogoGenerator()

        prototype_pages = request.prototype_pages or [
            "home",
            "features",
            "about",
            "contact",
        ]

        prototype_result = prototype_gen.generate_prototype(
            business_name=request.business_name,
            tagline=request.tagline,
            industry=request.industry,
            vibe=request.vibe or "professional",
            page_types=prototype_pages,
        )

        logo_url = logo_gen.get_logo_url(
            business_name=request.business_name,
            industry=request.industry,
            style=request.logo_style,
            color_scheme=request.color_scheme,
        )

        return {
            "success": True,
            "data": {
                "business_name": request.business_name,
                "logo_url": logo_url,
                "prototype": {
                    "screens": prototype_result.get("screens", {}),
                    "navigation_flow": prototype_result.get("navigation_flow", []),
                    "start_page": prototype_result.get("start_page", "home"),
                    "total_screens": prototype_result.get("total_screens", 0),
                },
            },
        }

    except Exception as e:
        print(f"Error generating prototype: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/vibes")
def list_vibes():
    """List available design vibes."""
    return {
        "success": True,
        "data": {
            "vibes": [
                {
                    "key": "premium",
                    "name": "Premium",
                    "description": "Luxury, sophisticated, high-end aesthetic",
                },
                {
                    "key": "playful",
                    "name": "Playful",
                    "description": "Fun, energetic, approachable design",
                },
                {
                    "key": "professional",
                    "name": "Professional",
                    "description": "Trustworthy, corporate, reliable",
                },
                {
                    "key": "minimal",
                    "name": "Minimal",
                    "description": "Clean, focused, modern simplicity",
                },
                {
                    "key": "bold",
                    "name": "Bold",
                    "description": "Attention-grabbing, confident, memorable",
                },
            ]
        },
    }


@router.get("/page-types")
def list_page_types():
    """List available page types for prototype generation."""
    return {
        "success": True,
        "data": {
            "page_types": [
                {
                    "key": "home",
                    "name": "Home/Landing",
                    "description": "Hero section, value proposition, main CTA",
                },
                {
                    "key": "features",
                    "name": "Features",
                    "description": "Detailed feature showcase with benefits",
                },
                {
                    "key": "about",
                    "name": "About Us",
                    "description": "Company story, team, mission",
                },
                {
                    "key": "pricing",
                    "name": "Pricing",
                    "description": "Pricing tiers, plans, FAQ",
                },
                {
                    "key": "contact",
                    "name": "Contact",
                    "description": "Contact form, location, social links",
                },
            ]
        },
    }


@router.post("/social-posts")
def generate_social_posts(request: SocialPostsRequest):
    """
    Generate social media posts for a brand.

    Creates engaging posts for Twitter/X, LinkedIn, and Instagram.
    """
    try:
        posts_gen = SocialPostsGenerator()

        posts = posts_gen.generate_posts(
            business_name=request.business_name,
            tagline=request.tagline,
            vibe=request.vibe,
            num_posts=request.num_posts,
        )

        return {"success": True, "data": {"posts": posts}}

    except Exception as e:
        print(f"Error generating social posts: {e}")
        raise HTTPException(status_code=500, detail=str(e))
