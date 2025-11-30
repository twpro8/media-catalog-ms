"""
Actors query service implementation module.
"""

from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.features.actor.domain.services.actor_query_service import (
    ActorQueryService,
)
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from app.features.actor.data.models.actor import Actor


class ActorQueryServiceImpl(ActorQueryService):
    """
    ActorQueryServiceImpl implements READ operations related to Actor entity using SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def find_by_id(self, id_: UUID) -> ActorReadModel | None:
        result = await self.session.get(Actor, id_)

        if result is None:
            return None

        return result.to_read_model()

    async def findall(self) -> Sequence[ActorReadModel]:
        # TODO: add offset and limit
        statement = select(Actor).filter_by(is_deleted=False)

        result = await self.session.execute(statement)

        return [actor.to_read_model() for actor in result.scalars().all()]
