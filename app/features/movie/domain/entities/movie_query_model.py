"""
Movie query model module.
"""

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import ConfigDict, Field

from app.features.movie.domain.entities.movie_entity import MovieEntity
from app.features.movie.domain.entities.movie_common_model import MovieBaseModel


class MovieReadModel(MovieBaseModel):
    """
    MovieReadModel represents data structure as a read model
    """

    id_: UUID
    rating: Decimal = Field(examples=["7.5"])
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @staticmethod
    def from_entity(entity: MovieEntity) -> "MovieReadModel":
        return MovieReadModel(
            id_=entity.id_,
            title=entity.title,
            description=entity.description,
            release_date=entity.release_date,
            rating=entity.rating,
            duration=entity.duration,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
