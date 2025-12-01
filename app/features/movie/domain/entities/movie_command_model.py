"""
Movie command model module.
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, model_validator, Field

from app.core.error.validation_exception import FieldRequiredError
from app.features.movie.domain.entities.movie_common_model import MovieBaseModel


class MovieCreateModel(MovieBaseModel):
    """
    MovieCreateModel represents a write model to create a movie.
    """

    model_config = ConfigDict(extra="forbid")


class MovieUpdateModel(BaseModel):
    """
    MovieUpdateModel represents a write model to update a movie.
    """

    title: str = Field(
        ...,
        min_length=1,
        max_length=256,
        examples=["Title Example"],
    )
    description: str = Field(
        ...,
        min_length=1,
        max_length=1024,
        examples=["Description example"],
    )
    release_date: date = Field(
        ...,
        ge=date(1000, 1, 1),
        le=date.today(),
        examples=[date(1988, 2, 7)],
    )
    duration: int | None = Field(..., lt=9999, gt=0, examples=[70])

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def check_some_field(self):
        if not self.model_fields_set:
            raise FieldRequiredError
        return self
