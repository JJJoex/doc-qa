from fastapi import FastAPI

from app.config import settings
from app.schemas import HealthResponse


app = FastAPI(
    title="Document Q&A",
    version="0.1.0",
    description="First milestone: health endpoint and local configuration loading.",
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Document Q&A API is running.",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        environment=settings.app_env,
        openai_configured=bool(settings.openai_api_key),
    )