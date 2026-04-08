import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_name: str = "Document Q&A"
    app_env: str = os.getenv("APP_ENV", "development")
    openai_api_key: str | None = os.getenv("DEEPSEEK_API_KEY")
    openai_model: str = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")


settings = Settings()