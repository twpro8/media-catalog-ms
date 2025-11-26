"""
Season api router module.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/seasons",
    tags=["Seasons"],
)
