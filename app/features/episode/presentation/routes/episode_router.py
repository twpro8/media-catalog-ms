"""
Episode router module.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/v1/episodes", tags=["Episodes"])
