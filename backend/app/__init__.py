"""
AI Brand Generator Backend Application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import generate, health


def create_app() -> FastAPI:
    """Create and configure the FastAPI application"""

    app = FastAPI(
        title="AI Brand Generator API",
        description="Generate complete brand identities and landing pages using AI",
        version="1.0.0"
    )

    # Configure CORS for frontend communication
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure appropriately for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(generate.router, prefix="/api/generate", tags=["Generation"])
    app.include_router(health.router, prefix="/api/health", tags=["Health"])

    @app.get("/")
    async def root():
        return {
            "message": "AI Brand Generator API",
            "version": "1.0.0",
            "docs": "/docs"
        }

    return app


app = create_app()
