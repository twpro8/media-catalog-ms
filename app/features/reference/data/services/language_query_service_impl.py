"""
Languages query service implementation module.
"""

from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.features.reference.domain.services.language.language_query_service import (
    LanguageQueryService,
)
from app.features.reference.domain.entities.language.language_query_model import (
    LanguageReadModel,
)
from app.features.reference.data.models.language import Language


class LanguageQueryServiceImpl(LanguageQueryService):
    """
    LanguageQueryServiceImpl implements READ operations related to Language entity using SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_by_id(self, id_: UUID) -> LanguageReadModel | None:
        raise NotImplementedError

    async def find_by_code(self, code: str) -> LanguageReadModel | None:
        result = await self.session.get(Language, code)

        if result is None:
            return None

        return result.to_read_model()

    async def findall(self) -> Sequence[LanguageReadModel]:
        statement = select(Language).filter_by(active=True)

        result = await self.session.execute(statement)

        return [language.to_read_model() for language in result.scalars().all()]
