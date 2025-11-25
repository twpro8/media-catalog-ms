"""
Main module.
"""

from fastapi import FastAPI

from app.config import Settings
from app.dependencies import get_settings
from app.core.error.base_exception import BaseError
from app.core.error.exception_handler import app_exception_handler
from app.features.movie.presentation.routes import movie_router
from app.features.show.presentation.routes import show_router


__SETTINGS: Settings = get_settings()


app = FastAPI(title=__SETTINGS.APP_NAME)
app.add_exception_handler(BaseError, app_exception_handler)
app.include_router(movie_router)
app.include_router(show_router)


@app.get("/hello")
async def get_hello(name: str):
    return {"status": "OK", "message": f"Hello, {name}!"}
