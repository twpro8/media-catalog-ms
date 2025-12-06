"""
Country query service implementation module.
"""

from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.features.reference.domain.services.country_query_service import (
    CountryQueryService,
)
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)
from app.features.reference.data.models.country import Country


class CountryQueryServiceImpl(CountryQueryService):
    """
    CountryQueryServiceImpl implements READ operations related to Country entity using SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_by_id(self, id_: UUID) -> CountryReadModel | None:
        raise NotImplementedError

    async def find_by_code(self, code: str) -> CountryReadModel | None:
        result: Country | None = await self.session.get(Country, code)

        if result is None:
            return None

        return result.to_read_model()

    async def findall(self) -> Sequence[CountryReadModel]:
        statement = select(Country).filter_by(active=True)

        result = await self.session.execute(statement)

        return [country.to_read_model() for country in result.scalars().all()]
