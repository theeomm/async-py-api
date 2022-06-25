from pydantic import BaseSettings


class Settings(BaseSettings):
    # Base configuration
    app_name = "Async API"
    app_description = "FASTAPI, SQLModel and Alembic"
    debug = False
    database_url: str

    class Config:
        env_file = ".env"
        
settings = Settings()
