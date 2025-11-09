"""
Movie api router module.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/movies",
    tags=["Movies"],
)
