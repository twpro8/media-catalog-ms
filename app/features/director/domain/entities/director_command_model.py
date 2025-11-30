"""
Director command model module.
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, model_validator, Field

from app.core.error.validation_error import FieldRequiredError
from app.features.director.domain.entities.director_common_model import (
    DirectorBaseModel,
)


class DirectorCreateModel(DirectorBaseModel):
    """
    DirectorCreateModel represents a write model to create a director.
    """

    model_config = ConfigDict(extra="forbid")


class DirectorUpdateModel(BaseModel):
    """
    DirectorUpdateModel represents a write model to update a director.
    """

    first_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=48,
        examples=["Tim"],
    )
    last_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=48,
        examples=["Cook"],
    )
    birth_date: date | None = Field(
        default=None,
        ge=date(1925, 1, 1),
        le=date.today(),
        examples=[date(1988, 2, 7)],
    )
    bio: str | None = Field(
        default=None, min_length=2, max_length=1024, examples=["A famous man."]
    )

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def check_some_field(self):
        if not self.model_fields_set:
            raise FieldRequiredError
        return self
