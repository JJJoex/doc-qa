from fastapi import FastAPI, HTTPException

from app.config import settings
from app.qa import answer_question
from app.schemas import AskRequest, AskResponse, HealthResponse


app = FastAPI(
    title="Document Q&A",
    version="0.2.0",
    description="Milestone 2: structured ask endpoint without retrieval.",
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Document Q&A API is running.",
        "docs": "/docs",
        "health": "/health",
        "ask": "/ask",
    }


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        environment=settings.app_env,
        openai_configured=bool(settings.openai_api_key),
    )


@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest) -> AskResponse:
    question = payload.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Question must not be empty.")

    return answer_question(payload)