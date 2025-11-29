"""
Episode repository implementation module.
"""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, IntegrityError

from app.core.error.base_exception import BaseError
from app.core.error.episode_exception import (
    EpisodeNotFoundError,
    EpisodeAlreadyExistsError,
)
from app.core.repositories.sqlalchemy.repository import SQLAlchemyRepository
from app.features.episode.data.mappers.episode_data_mapper import EpisodeDataMapper
from app.features.episode.domain.repositories.episode_repository import (
    EpisodeRepository,
)
from app.features.episode.domain.entities.episode_entity import EpisodeEntity
from app.features.episode.data.models.episode import Episode


class EpisodeRepositoryImpl(
    SQLAlchemyRepository[Episode, EpisodeEntity], EpisodeRepository
):
    """
    EpisodeRepositoryImpl implements CRUD operations related Episode entity using SQLAlchemy.
    """

    model = Episode
    mapper = EpisodeDataMapper

    def __init__(self, session):
        super().__init__(session)

    async def update(self, entity: EpisodeEntity) -> EpisodeEntity:
        try:
            return await super().update(entity)
        except NoResultFound as e:
            raise EpisodeNotFoundError from e
        except IntegrityError as e:
            raise EpisodeAlreadyExistsError from e
        except Exception as e:
            raise BaseError("Internal database error") from e

    async def find_by_season_and_number(
        self, season_id: UUID, episode_number: int
    ) -> EpisodeEntity | None:
        query = select(self.model).where(
            self.model.season_id == season_id,
            self.model.episode_number == episode_number,
        )
        result = await self.session.scalar(query)
        return self.mapper.to_entity(result) if result else None
