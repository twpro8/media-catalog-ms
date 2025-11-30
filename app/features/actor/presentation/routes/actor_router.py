"""
Actor api router module.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/actors",
    tags=["Actors"],
)
