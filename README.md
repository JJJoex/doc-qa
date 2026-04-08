# Document Q&A

A small document Q&A project built in **Windows 11 + WSL2 Ubuntu**, with development done inside the Linux filesystem.

## Current milestone

Milestone 1: bootstrapping the backend.

Current features:
- FastAPI app scaffold
- local `.env` configuration loading
- `/` root endpoint
- `/health` endpoint

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