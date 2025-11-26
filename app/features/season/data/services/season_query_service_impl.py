"""
Seasons query service implementation module.
"""

from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.features.season.domain.services.season_query_service import SeasonQueryService
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.data.models.season import Season


class SeasonQueryServiceImpl(SeasonQueryService):
    """
    SeasonQueryServiceImpl implements READ operations related to Season entity using SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def find_by_id(self, id_: UUID) -> SeasonReadModel | None:
        result = await self.session.get(Season, id_)

        if result is None:
            return None

        return result.to_read_model()

    async def findall(self) -> Sequence[SeasonReadModel]:
        # TODO: add offset and limit
        statement = select(Season).filter_by(is_deleted=False)

        result = await self.session.execute(statement)

        return [season.to_read_model() for season in result.scalars().all()]
