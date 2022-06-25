from functools import lru_cache

from sqlmodel import Session

from app.conf.settings import Settings


@lru_cache
def get_settings():
    return Settings()


def get_session():
    from app.conf.db import engine

    with Session(engine) as session:
        yield session
