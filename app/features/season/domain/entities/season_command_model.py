"""
Season command model module.
"""

from pydantic import BaseModel, ConfigDict, model_validator, Field

from app.core.error.validation_error import FieldRequiredError
from app.features.season.domain.entities.season_common_model import SeasonBaseModel


class SeasonCreateModel(SeasonBaseModel):
    """
    SeasonCreateModel represents a write model to create a season.
    """

    model_config = ConfigDict(extra="forbid")


class SeasonUpdateModel(BaseModel):
    """
    SeasonUpdateModel represents a write model to update a season.
    """

    title: str | None = Field(
        None,
        min_length=1,
        max_length=256,
        examples=["Title Example"],
    )
    season_number: int | None = Field(
        None,
        gt=0,
        lt=9999,
        examples=[1],
    )

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def check_some_field(self):
        if not self.model_fields_set:
            raise FieldRequiredError
        return self
