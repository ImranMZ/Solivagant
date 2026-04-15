"""Generation endpoints for brand and website creation"""
from fastapi import APIRouter, HTTPException
from ..models.request import BrandRequest
from ..services.logo_gen import LogoGenerator
from ..services.website_gen import WebsiteGenerator
from ..services.seo_gen import SEOGenerator
from urllib.parse import quote_plus
import json

router = APIRouter()


@router.post("/generate")
def generate_brand(request: BrandRequest):
    """
    Generate complete brand identity and website
    
    Args:
        request: BrandRequest with business details
        
    Returns:
        Generated brand assets and website HTML
    """
    try:
        # Initialize services
        logo_gen = LogoGenerator()
        website_gen = WebsiteGenerator()
        seo_gen = SEOGenerator()
        
        # Generate logo URL (Pollinations.ai is free, returns direct URL)
        logo_url = logo_gen.get_logo_url(
            business_name=request.business_name,
            industry=request.industry,
            style=request.logo_style,
            color_scheme=request.color_scheme
        )
        
        # Generate website HTML/CSS and design palette
        website_payload = website_gen.generate_website(
            business_name=request.business_name,
            tagline=request.tagline,
            color_scheme=request.color_scheme,
            industry=request.industry,
            website_template=request.website_template
        )
        
        # Generate SEO metadata
        seo_tags = seo_gen.generate_seo(
            business_name=request.business_name,
            tagline=request.tagline,
            industry=request.industry
        )

        logo_download_url = (
            f"/api/logo?business_name={quote_plus(request.business_name)}"
            f"&industry={quote_plus(request.industry)}"
            f"&style={quote_plus(request.logo_style)}"
            f"&color_scheme={quote_plus(request.color_scheme or '')}"
        )
        
        return {
            "success": True,
            "data": {
                "business_name": request.business_name,
                "logo_url": logo_url,
                "logo_download_url": logo_download_url,
                "website_html": website_payload["html"],
                "seo_tags": seo_tags,
                "design_palette": website_payload["palette"],
                "theme_name": website_payload["theme_name"],
                "font_family": website_payload["font_family"],
                "palette_suggestions": website_payload["palette_suggestions"],
                "features": website_payload["features"],
                "sections": website_payload["sections"],
                "website_template": request.website_template,
                "template_name": website_payload.get("template_name"),
                "template_description": website_payload.get("template_description")
            }
        }
        
    except Exception as e:
        import traceback
        print(f"Error in generate_brand: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
