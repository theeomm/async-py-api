import uvicorn
from fastapi import Depends, FastAPI

from app.conf.db import create_db
from app.conf.settings import Settings
from app.model.todo import *
from app.routes import todos
from app.utils import get_settings

settings = get_settings()

app = FastAPI(
    debug=settings.debug,
    title=settings.app_name,
    description=settings.app_description,
)


@app.on_event("startup")
def setup():
    create_db()


@app.get("/")
async def info(settings: Settings = Depends(get_settings)):
    """
    This route the app information
    """
    return {
        "name": settings.app_name,
        "description": settings.app_description,
        "debug": settings.debug,
    }


# App Routes
app.include_router(todos.router)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
