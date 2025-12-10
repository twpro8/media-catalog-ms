"""
Language api router module.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/languages",
    tags=["Languages"],
)
