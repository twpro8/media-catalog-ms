"""
Episodes query service implementation module.
"""

from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.features.episode.domain.services.episode_query_service import (
    EpisodeQueryService,
)
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.episode.data.models.episode import Episode


class EpisodeQueryServiceImpl(EpisodeQueryService):
    """
    EpisodeQueryServiceImpl implements READ operations related to Episode entity using SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def find_by_id(self, id_: UUID) -> EpisodeReadModel | None:
        result = await self.session.get(Episode, id_)

        if result is None:
            return None

        return result.to_read_model()

    async def findall(self) -> Sequence[EpisodeReadModel]:
        # TODO: add offset and limit
        query = select(Episode).filter_by(is_deleted=False)

        result = await self.session.execute(query)

        return [episode.to_read_model() for episode in result.scalars().all()]
