"""
Show common model module.
"""

from datetime import date

from pydantic import BaseModel, Field


class ShowBaseModel(BaseModel):
    """
    ShowBaseModel common fields.
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
        ge=date(1000, 1, 1), le=date.today(), examples=[date(1988, 2, 7)]
    )
