from app.schemas import AskRequest, AskResponse


DEFAULT_MODEL = "not-configured-yet"


def answer_question(payload: AskRequest) -> AskResponse:
    cleaned_question = payload.question.strip()

    # Temporary placeholder for milestone 2.
    # Later this function will call the OpenAI API.
    return AskResponse(
        answer=f"Stub response: you asked -> {cleaned_question}",
        model=DEFAULT_MODEL,
        used_retrieval=False,
        question=cleaned_question,
    )