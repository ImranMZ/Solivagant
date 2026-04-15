"""
FastAPI Application for AI-Powered Brand & Website Generator
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from backend/.env
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=str(env_path))

app = FastAPI(
    title="AI Brand & Website Generator",
    description="Generate complete brand identities and landing pages using AI",
    version="1.0.0"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routes after app initialization
from .routes import health, generate, logo

# Include routers
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(generate.router, prefix="/api", tags=["Generation"])
app.include_router(logo.router, prefix="/api", tags=["Logo"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to AI Brand & Website Generator",
        "version": "1.0.0",
        "endpoints": {
            "health": "/api/health",
            "generate": "/api/generate"
        }
    }
