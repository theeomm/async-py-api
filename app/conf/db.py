from sqlmodel import Session, SQLModel, create_engine

from app.utils import get_settings

settings = get_settings()

engine = create_engine(settings.database_url, echo=settings.debug)


def create_db():
    SQLModel.metadata.create_all(engine)
