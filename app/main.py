from fastapi import FastAPI, HTTPException

from app.config import settings
from app.qa import answer_question
from app.schemas import AskRequest, AskResponse, HealthResponse


app = FastAPI(
    title="Document Q&A",
    version="0.3.0",
    description="Milestone 3: live OpenAI-backed ask endpoint without retrieval.",
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
    print()
    if not question:
        raise HTTPException(status_code=400, detail="Question must not be empty.")

    try:
        return answer_question(payload)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Model call failed: {exc}") from exc