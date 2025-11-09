"""
Movie common model module.
"""

from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


class MovieBaseModel(BaseModel):
    """
    MovieBaseModel common fields.
    """

    title: str = Field(examples=["Title Example"])
    description: str = Field(examples=["Description example"])
    release_date: date = Field(examples=[date(1988, 2, 7)])
    rating: Decimal | None = Field(examples=["7.5"])
    duration: int | None = Field(examples=[70])
