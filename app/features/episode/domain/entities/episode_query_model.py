"""
Episode query model module.
"""

from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict

from app.features.episode.domain.entities.episode_common_model import EpisodeBaseModel
from app.features.episode.domain.entities.episode_entity import EpisodeEntity


class EpisodeReadModel(EpisodeBaseModel):
    id_: UUID
    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    model_config = ConfigDict(from_attributes=True)

    @staticmethod
    def from_entity(entity: EpisodeEntity) -> "EpisodeReadModel":
        assert entity.id_ is not None
        assert entity.created_at is not None
        assert entity.updated_at is not None
        assert entity.is_deleted is not None

        return EpisodeReadModel(
            id_=entity.id_,
            season_id=entity.season_id,
            title=entity.title,
            episode_number=entity.episode_number,
            release_date=entity.release_date,
            duration=entity.duration,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            is_deleted=entity.is_deleted,
        )
