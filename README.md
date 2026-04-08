# Document Q&A

A small document Q&A project built in **Windows 11 + WSL2 Ubuntu**, with development done inside the Linux filesystem.

Milestone 1: bootstrapping the backend.

Current features:
- FastAPI app scaffold
- local `.env` configuration loading
- `/` root endpoint
- `/health` endpoint


Milestone 2: structured question-answer endpoint.

Current features:
- FastAPI app scaffold
- local `.env` configuration loading
- `/` root endpoint
- `/health` endpoint
- `/ask` POST endpoint
- structured request/response schemas

## Ask endpoint

### Request

POST `/ask`

Example body:

```json
{
  "question": "What is this app for?",
  "system_prompt": "Answer concisely."
}


## Current milestone

Milestone 3: live OpenAI-backed question answering without retrieval.

Current features:
- FastAPI app scaffold
- local `.env` configuration loading
- `/` root endpoint
- `/health` endpoint
- `/ask` POST endpoint
- structured request/response schemas
- live OpenAI Responses API integration

## Local environment variables

Create a local `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=deepseek-chat
APP_ENV=development


## Project structure

```text
doc-qa/
  app/
    __init__.py
    main.py
    config.py
    schemas.py
  data/
    uploads/
  .env
  .env.example
  .gitignore
  pyproject.toml
  README.md