"""
Show command model module.
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, model_validator, Field

from app.core.error.validation_exception import FieldRequiredError
from app.features.show.domain.entities.show_common_model import ShowBaseModel


class ShowCreateModel(ShowBaseModel):
    """
    ShowCreateModel represents a write model to create a show.
    """

    model_config = ConfigDict(extra="forbid")


class ShowUpdateModel(BaseModel):
    """
    ShowUpdateModel represents a write model to update a show.
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

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def check_some_field(self):
        if not self.model_fields_set:
            raise FieldRequiredError
        return self
