"""
Director api router module.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/directors",
    tags=["Directors"],
)
