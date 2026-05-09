from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from app.models.request import (
    BrandGenerationRequest,
    BrandGenerationResponse,
    LogoResult,
    ColorScheme,
    WebsiteContent,
    SocialPosts,
    SEOtags,
)
from app.services.logo_gen import LogoGenerator
from app.services.website_gen import WebsiteGenerator
from app.services.brand_kit import generate_brand_kit_zip

router = APIRouter()


@router.post("/brand", response_model=BrandGenerationResponse)
async def generate_brand(request: BrandGenerationRequest):
    try:
        logo_service = LogoGenerator()
        content_service = WebsiteGenerator()

        brand_data = content_service.generate_brand(
            request.business_name,
            request.tagline,
            request.industry,
            request.target_audience,
            request.brand_values,
            request.primary_goal,
            request.tone,
            request.brand_vibe,
            request.logo_style,
            request.color_mood,
            request.font_personality,
            request.inspiration,
        )

        colors = brand_data.get("colors", {})
        logo_svg = logo_service.generate_svg_logo(
            request.business_name,
            request.industry,
            request.logo_style,
            colors,
            request.brand_values,
        )

        return BrandGenerationResponse(
            business_name=request.business_name,
            logo=LogoResult(svg=logo_svg, prompt=f"Logo for {request.business_name}"),
            colors=ColorScheme(
                primary=colors.get("primary", "#3B82F6"),
                secondary=colors.get("secondary", "#1E40AF"),
                accent=colors.get("accent", "#60A5FA"),
                background=colors.get("background", "#FFFFFF"),
                text=colors.get("text", "#1F2937"),
            ),
            website_content=WebsiteContent(
                html=brand_data.get("website_html", "")
            ),
            social_posts=SocialPosts(
                twitter=brand_data.get("social_posts", {}).get("twitter", ""),
                linkedin=brand_data.get("social_posts", {}).get("linkedin", ""),
                instagram=brand_data.get("social_posts", {}).get("instagram", ""),
            ),
            seo_tags=SEOtags(
                title=brand_data.get("seo_tags", {}).get("title", ""),
                description=brand_data.get("seo_tags", {}).get("description", ""),
                keywords=brand_data.get("seo_tags", {}).get("keywords", []),
                og_title=brand_data.get("seo_tags", {}).get("og_title", ""),
                og_description=brand_data.get("seo_tags", {}).get("og_description", ""),
            ),
            brand_guide=brand_data.get("brand_guide", ""),
            brand_score=brand_data.get("brand_score", 75),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Brand generation failed: {str(e)}")


@router.post("/twist", response_model=BrandGenerationResponse)
async def twist_brand(request: BrandGenerationRequest):
    try:
        logo_service = LogoGenerator()
        content_service = WebsiteGenerator()

        brand_data = content_service.twist_brand(
            request.business_name,
            request.tagline,
            request.industry,
            request.target_audience,
            request.brand_values,
            request.primary_goal,
            request.tone,
            request.brand_vibe,
            request.logo_style,
            request.font_personality,
            request.inspiration,
        )

        colors = brand_data.get("colors", {})
        logo_svg = logo_service.generate_svg_logo(
            request.business_name,
            request.industry,
            request.logo_style,
            colors,
            request.brand_values,
        )

        return BrandGenerationResponse(
            business_name=request.business_name,
            logo=LogoResult(svg=logo_svg, prompt=f"Twist logo for {request.business_name}"),
            colors=ColorScheme(
                primary=colors.get("primary", "#3B82F6"),
                secondary=colors.get("secondary", "#1E40AF"),
                accent=colors.get("accent", "#60A5FA"),
                background=colors.get("background", "#FFFFFF"),
                text=colors.get("text", "#1F2937"),
            ),
            website_content=WebsiteContent(
                html=brand_data.get("website_html", "")
            ),
            social_posts=SocialPosts(
                twitter=brand_data.get("social_posts", {}).get("twitter", ""),
                linkedin=brand_data.get("social_posts", {}).get("linkedin", ""),
                instagram=brand_data.get("social_posts", {}).get("instagram", ""),
            ),
            seo_tags=SEOtags(
                title=brand_data.get("seo_tags", {}).get("title", ""),
                description=brand_data.get("seo_tags", {}).get("description", ""),
                keywords=brand_data.get("seo_tags", {}).get("keywords", []),
                og_title=brand_data.get("seo_tags", {}).get("og_title", ""),
                og_description=brand_data.get("seo_tags", {}).get("og_description", ""),
            ),
            brand_guide=brand_data.get("brand_guide", ""),
            brand_score=brand_data.get("brand_score", 75),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Twist generation failed: {str(e)}")


@router.post("/export")
async def export_brand_kit(request: BrandGenerationRequest):
    try:
        logo_service = LogoGenerator()
        content_service = WebsiteGenerator()

        data = content_service.generate_brand(
            request.business_name,
            request.tagline,
            request.industry,
            request.target_audience,
            request.brand_values,
            request.primary_goal,
            request.tone,
            request.brand_vibe,
            request.logo_style,
            request.color_mood,
            request.font_personality,
            request.inspiration,
        )

        colors = data.get("colors", {})
        logo_svg = logo_service.generate_svg_logo(
            request.business_name,
            request.industry,
            request.logo_style,
            colors,
            request.brand_values,
        )

        zip_bytes = generate_brand_kit_zip(
            request.business_name,
            logo_svg,
            data.get("website_html", ""),
            data.get("brand_guide", ""),
            data.get("social_posts", {}),
            data.get("seo_tags", {}),
            colors,
        )

        return Response(
            content=zip_bytes,
            media_type="application/zip",
            headers={
                "Content-Disposition": f'attachment; filename="{request.business_name}-brand-kit.zip"'
            },
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Export failed: {str(e)}")
