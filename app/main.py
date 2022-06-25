from fastapi import Depends, FastAPI

from app.conf import Settings, settings
from app.utils import get_settings

app = FastAPI(
    debug=settings.debug,
    title=settings.app_name,
    description=settings.app_description,
)


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
