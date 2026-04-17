"""Logo routes for generated logo assets."""

from fastapi import APIRouter, HTTPException
from ..services.logo_gen import LogoGenerator

router = APIRouter()


@router.get("/logo")
def get_logo_svg(
    business_name: str,
    industry: str,
    style: str = "minimalist",
    color_scheme: str = "modern",
):
    """Get the generated logo as SVG."""
    try:
        generator = LogoGenerator()
        svg = generator.get_logo_html(
            business_name=business_name, industry=industry, style=style
        )
        return {"logo_svg": svg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
