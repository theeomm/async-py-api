from sqlmodel import Session, SQLModel, create_engine

from app.conf.settings import settings

engine = create_engine(settings.database_url, echo=settings.debug,)

from sqlmodel import Session


def get_session():
    with Session(engine) as session:
        yield session


def create_db():
    SQLModel.metadata.create_all(engine)
