"""
Health check endpoints
"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    message: str
    version: str


@router.get("/", response_model=HealthResponse)
async def health_check():
    """Check if the API is running"""
    return {
        "status": "healthy",
        "message": "AI Brand Generator API is running",
        "version": "1.0.0"
    }


@router.get("/ready", response_model=HealthResponse)
async def readiness_check():
    """Check if the API is ready to handle requests"""
    return {
        "status": "ready",
        "message": "API is ready to generate brands",
        "version": "1.0.0"
    }
