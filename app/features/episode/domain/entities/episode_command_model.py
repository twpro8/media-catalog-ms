"""
Episode command model module.
"""

from datetime import date

from pydantic import BaseModel, Field, ConfigDict, model_validator

from app.core.error.validation_exception import FieldRequiredError
from app.features.episode.domain.entities.episode_common_model import EpisodeBaseModel


class EpisodeCreateModel(EpisodeBaseModel):
    """
    EpisodeCreateModel represents a write model to create an episode.
    """

    model_config = ConfigDict(extra="forbid")


class EpisodeUpdateModel(BaseModel):
    """
    EpisodeUpdateModel represents a write model to update an episode.
    """

    title: str = Field(
        ...,
        min_length=1,
        max_length=256,
        examples=["Title Example"],
    )
    episode_number: int = Field(
        ...,
        gt=0,
        lt=9999,
        examples=[1],
    )
    release_date: date = Field(
        ...,
        ge=date(1000, 1, 1),
        le=date.today(),
        examples=[date(1988, 2, 7)],
    )
    duration: int | None = Field(
        ...,
        lt=9999,
        gt=0,
        examples=[70],
    )

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def check_some_field(self):
        if not self.model_fields_set:
            raise FieldRequiredError
        return self
