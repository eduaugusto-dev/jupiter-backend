

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações centralizadas do backend Júpiter."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # Aplicação
    APP_NAME: str = Field(default="Júpiter - Agente de RH")
    APP_VERSION: str = Field(default="1.0.0")
    DEBUG: bool = Field(default=False)
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    # Supabase
    SUPABASE_URL: str = Field(default="")
    SUPABASE_ANON_KEY: str = Field(default="")
    SUPABASE_SERVICE_ROLE_KEY: str = Field(default="")

    # LLM
    GROQ_API_KEY: str = Field(default="")
    GROQ_MODEL_PROVIDER: str = Field(default="groq")
    MODEL_NAME: str = Field(default="openai/gpt-oss-120b")

    # RAG
    KNOWLEDGE_BASE_PATH: str = Field(default="knowledge_base/")
    VECTOR_DB_PATH: str = Field(default="vector_store/")
    EMBEDDING_MODEL: str = Field(
        default="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Logs
    LOG_LEVEL: str = Field(default="INFO")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
