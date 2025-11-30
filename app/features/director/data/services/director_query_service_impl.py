"""
Directors query service implementation module.
"""

from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.features.director.domain.services.director_query_service import (
    DirectorQueryService,
)
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from app.features.director.data.models.director import Director


class DirectorQueryServiceImpl(DirectorQueryService):
    """
    DirectorQueryServiceImpl implements READ operations related to Director entity using SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def find_by_id(self, id_: UUID) -> DirectorReadModel | None:
        result = await self.session.get(Director, id_)

        if result is None:
            return None

        return result.to_read_model()

    async def findall(self) -> Sequence[DirectorReadModel]:
        # TODO: add offset and limit
        statement = select(Director).filter_by(is_deleted=False)

        result = await self.session.execute(statement)

        return [director.to_read_model() for director in result.scalars().all()]
