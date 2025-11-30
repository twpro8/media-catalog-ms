"""
Director query model module.
"""

from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from app.features.director.domain.entities.director_entity import DirectorEntity
from app.features.director.domain.entities.director_common_model import (
    DirectorBaseModel,
)


class DirectorReadModel(DirectorBaseModel):
    """
    DirectorReadModel represents data structure as a read model
    """

    id_: UUID
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @staticmethod
    def from_entity(entity: DirectorEntity) -> "DirectorReadModel":
        assert entity.id_ is not None
        assert entity.is_deleted is not None
        assert entity.created_at is not None
        assert entity.updated_at is not None

        return DirectorReadModel(
            id_=entity.id_,
            first_name=entity.first_name,
            last_name=entity.last_name,
            birth_date=entity.birth_date,
            bio=entity.bio,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
