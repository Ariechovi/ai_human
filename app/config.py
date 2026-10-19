from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ai_human"
    app_env: str = "dev"

    database_url: str = ""
    redis_url: str = "redis://127.0.0.1:16379/0"

    model_name: str = "deepseek-chat"
    model_base_url: str | None = "https://api.deepseek.com"
    model_api_key: str = ""

    embedding_model: str = "qwen3.7-text-embedding"
    embedding_base_url: str | None = "https://dashscope.aliyuncs.com/compatible-mode/v1"
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

