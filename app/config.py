from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ai_human"
    app_env: str = "dev"

    database_url: str = ""
    redis_url: str = "redis://127.0.0.1:6379/0"

    model_name: str = "gpt-4o-mini"
    model_base_url: str | None = None
    model_api_key: str = ""

    embedding_model: str = "text-embedding-3-small"
    embedding_base_url: str | None = None
    embedding_api_key: str = ""

    vector_dim: int = 1536
    short_term_window: int = 10
    summary_token_cutoff: int = 3000
    rag_top_k: int = 4

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

