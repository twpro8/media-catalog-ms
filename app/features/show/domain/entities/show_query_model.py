"""
Show query model module.
"""

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import ConfigDict, Field

from app.features.show.domain.entities.show_entity import ShowEntity
from app.features.show.domain.entities.show_common_model import ShowBaseModel


class ShowReadModel(ShowBaseModel):
    """
    ShowReadModel represents data structure as a read model
    """

    id_: UUID
    rating: Decimal = Field(examples=["7.5"])
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @staticmethod
    def from_entity(entity: ShowEntity) -> "ShowReadModel":
        assert entity.id_ is not None
        assert entity.rating is not None
        assert entity.is_deleted is not None
        assert entity.created_at is not None
        assert entity.updated_at is not None

        return ShowReadModel(
            id_=entity.id_,
            title=entity.title,
            description=entity.description,
            release_date=entity.release_date,
            rating=entity.rating,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
