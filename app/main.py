"""
Main module.
"""

from fastapi import FastAPI

from app.config import Settings
from app.dependencies import get_settings
from app.core.error.base_exception import BaseError
from app.core.error.exception_handler import app_exception_handler


__SETTINGS: Settings = get_settings()


app = FastAPI(title=__SETTINGS.APP_NAME)
app.add_exception_handler(BaseError, app_exception_handler)


@app.get("/hello")
async def get_hello(name: str):
    return {"status": "OK", "message": f"Hello, {name}!"}
