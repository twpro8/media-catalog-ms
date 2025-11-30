"""
Actor common model module.
"""

from datetime import date

from pydantic import BaseModel, Field


class ActorBaseModel(BaseModel):
    """
    ActorBaseModel common fields.
    """

    first_name: str = Field(
        min_length=2,
        max_length=48,
        examples=["John"],
    )
    last_name: str = Field(
        min_length=2,
        max_length=48,
        examples=["W.Davis"],
    )
    birth_date: date = Field(
        ge=date(1925, 1, 1),
        le=date.today(),
        examples=[date(1988, 2, 7)],
    )
    bio: str | None = Field(
        None, min_length=2, max_length=1024, examples=["A famous fantasy writer."]
    )
