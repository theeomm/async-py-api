from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    # Base configuration
    app_name = "Async API"
    app_description = "FASTAPI, SQLModel and Alembic"

    # Server
    debug = False
    host: str = "127.0.0.1"
    port: int = 8000

    # Database
    database_url: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
