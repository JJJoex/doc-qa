from openai import OpenAI

from app.config import settings
from app.schemas import AskRequest, AskResponse


DEFAULT_INSTRUCTIONS = (
    "You are a helpful document Q&A assistant. "
    "Answer clearly and directly. "
    "If the user asks something ambiguous, make a best effort answer based on the question alone. "
    "Do not claim to have used retrieval or external documents in this stage."
)


def answer_question(payload: AskRequest) -> AskResponse:
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    client = OpenAI(api_key=settings.openai_api_key, base_url="https://api.deepseek.com/v1")

    instructions = payload.system_prompt.strip() if payload.system_prompt else DEFAULT_INSTRUCTIONS
    cleaned_question = payload.question.strip()

    response = client.chat.completions.create(
        model=settings.openai_model,
        messages=[{
            "role": "system",
            "content": instructions
        }, {
            "role": "user",
            "content": cleaned_question
        }],
        stream=False
    )

    answer_text = response.choices[0].message.content 
    if not answer_text:
        answer_text = "The model returned an empty response."

    return AskResponse(
        answer=answer_text,
        model=settings.openai_model,
        used_retrieval=False,
        question=cleaned_question,
    )