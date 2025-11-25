"""
Shows query service implementation module.
"""

from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.features.show.domain.services.show_query_service import ShowQueryService
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.data.models.show import Show


class ShowQueryServiceImpl(ShowQueryService):
    """
    ShowQueryServiceImpl implements READ operations related to Show entity using SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def find_by_id(self, id_: UUID) -> ShowReadModel | None:
        result = await self.session.get(Show, id_)

        if result is None:
            return None

        return result.to_read_model()

    async def findall(self) -> Sequence[ShowReadModel]:
        # TODO: add offset and limit
        statement = select(Show).filter_by(is_deleted=False)

        result = await self.session.execute(statement)

        return [show.to_read_model() for show in result.scalars().all()]
