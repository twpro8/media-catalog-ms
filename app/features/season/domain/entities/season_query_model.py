"""
Season query model module.
"""

from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from app.features.season.domain.entities.season_entity import SeasonEntity
from app.features.season.domain.entities.season_common_model import SeasonBaseModel


class SeasonReadModel(SeasonBaseModel):
    """
    SeasonReadModel represents data structure as a read model
    """

    id_: UUID
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @staticmethod
    def from_entity(entity: SeasonEntity) -> "SeasonReadModel":
        assert entity.id_ is not None
        assert entity.is_deleted is not None
        assert entity.created_at is not None
        assert entity.updated_at is not None

        return SeasonReadModel(
            id_=entity.id_,
            show_id=entity.show_id,
            title=entity.title,
            season_number=entity.season_number,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
