"""Health check endpoint"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "AI Brand & Website Generator API"
    }
