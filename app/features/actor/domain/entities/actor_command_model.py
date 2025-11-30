"""
Actor command model module.
"""

from datetime import date

from pydantic import BaseModel, ConfigDict, model_validator, Field

from app.core.error.validation_error import FieldRequiredError
from app.features.actor.domain.entities.actor_common_model import (
    ActorBaseModel,
)


class ActorCreateModel(ActorBaseModel):
    """
    ActorCreateModel represents a write model to create a actor.
    """

    model_config = ConfigDict(extra="forbid")


class ActorUpdateModel(BaseModel):
    """
    ActorUpdateModel represents a write model to update a actor.
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
