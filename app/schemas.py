from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    app_name: str
    environment: str
    openai_configured: bool


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=4000, description="User question")
    system_prompt: str | None = Field(
        default=None,
        max_length=4000,
        description="Optional system instruction override for experiments",
    )


class AskResponse(BaseModel):
    answer: str
    model: str
    used_retrieval: bool
    question: str