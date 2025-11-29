"""
Movie common model module.
"""

from datetime import date

from pydantic import BaseModel, Field


class MovieBaseModel(BaseModel):
    """
    MovieBaseModel common fields.
    """

    title: str = Field(
        min_length=1,
        max_length=256,
        examples=["Title Example"],
    )
    description: str = Field(
        min_length=1,
        max_length=1024,
        examples=["Description example"],
    )
    release_date: date = Field(
        ge=date(1000, 1, 1),
        le=date.today(),
        examples=[date(1988, 2, 7)],
    )
    duration: int | None = Field(None, lt=9999, gt=0, examples=[70])
