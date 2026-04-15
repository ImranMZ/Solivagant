"""Logo proxy route for downloading generated logo images."""
from fastapi import APIRouter, HTTPException, Response
from urllib.parse import unquote_plus
from ..services.logo_gen import LogoGenerator

router = APIRouter()


@router.get("/logo")
def download_logo(
    business_name: str,
    industry: str,
    style: str = "minimalist",
    color_scheme: str = "modern"
):
    """Download the generated logo image as PNG bytes."""
    try:
        generator = LogoGenerator()
        image_bytes = generator.fetch_logo_bytes(
            business_name=business_name,
            industry=industry,
            style=style,
            color_scheme=color_scheme or None
        )
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
