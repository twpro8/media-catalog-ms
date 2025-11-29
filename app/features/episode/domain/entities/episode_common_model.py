"""
Episode common model module.
"""

from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field


class EpisodeBaseModel(BaseModel):
    """
    EpisodeBaseModel common fields.
    """

    season_id: UUID
    title: str = Field(
        min_length=1,
        max_length=256,
        examples=["Title Example"],
    )
    episode_number: int = Field(
        gt=0,
        lt=9999,
        examples=[1],
    )
    release_date: date = Field(
        ge=date(1000, 1, 1),
        le=date.today(),
        examples=[date(1988, 2, 7)],
    )
    duration: int | None = Field(None, lt=9999, gt=0, examples=[70])
