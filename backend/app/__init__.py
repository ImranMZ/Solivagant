from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import generate, health


def create_app() -> FastAPI:
    app = FastAPI(
        title="Solivagant - AI Brand Designer",
        description="Generate complete brand identities using AI",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(generate.router, prefix="/api/generate", tags=["Generation"])
    app.include_router(health.router, prefix="/api/health", tags=["Health"])

    @app.get("/")
    async def root():
        return {
            "message": "Solivagant - AI Brand Designer",
            "version": "1.0.0",
            "docs": "/docs",
        }

    return app


app = create_app()
