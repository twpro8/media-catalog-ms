"""
Main module.
"""

from fastapi import FastAPI

from app.config import Settings
from app.dependencies import get_settings


__SETTINGS: Settings = get_settings()


app = FastAPI(title=__SETTINGS.APP_NAME)


@app.get("/hello")
async def get_hello(name: str):
    return {"status": "OK", "message": f"Hello, {name}!"}
