from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from dotenv import load_dotenv
from app.routes import generate, health

load_dotenv()


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

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """Return user-friendly validation error messages."""
        errors = exc.errors()
        messages = []
        for err in errors:
            loc = err.get("loc", [])
            # Skip the first element if it's 'body' — show field path only
            field_parts = [str(p) for p in loc[1:]] if loc and loc[0] == "body" else [str(p) for p in loc]
            field = " -> ".join(field_parts) if field_parts else "request"
            msg = err.get("msg", "Invalid value")
            # Clean up common Pydantic messages
            if "field required" in msg.lower():
                messages.append(f"'{field}' is required")
            elif "ensure this value has at least" in msg.lower():
                messages.append(f"'{field}' needs more items")
            elif "ensure this value has at most" in msg.lower():
                messages.append(f"'{field}' has too many items")
            else:
                messages.append(f"{field}: {msg}")

        return JSONResponse(
            status_code=422,
            content={
                "detail": "Missing or invalid fields: " + "; ".join(messages),
                "errors": messages,
            },
        )

    @app.get("/")
    async def root():
        return {
            "message": "Solivagant - AI Brand Designer",
            "version": "1.0.0",
            "docs": "/docs",
        }

    return app


app = create_app()
