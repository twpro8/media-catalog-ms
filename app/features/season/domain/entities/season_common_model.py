"""
Season common model module.
"""

from uuid import UUID

from pydantic import BaseModel, Field


class SeasonBaseModel(BaseModel):
    """
    SeasonBaseModel common fields.
    """

    show_id: UUID
    title: str = Field(
        min_length=1,
        max_length=256,
        examples=["Title Example"],
    )
    season_number: int = Field(
        gt=0,
        lt=9999,
        examples=[1],
    )
