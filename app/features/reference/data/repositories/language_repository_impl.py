"""
Language repository implementation module.
"""

from sqlalchemy import update

from app.core.repositories.sqlalchemy.repository import SQLAlchemyRepository
from app.features.reference.data.mappers.language_data_mapper import LanguageDataMapper
from app.features.reference.data.models.language import Language
from app.features.reference.domain.entities.language.language_entity import (
    LanguageEntity,
)
from app.features.reference.domain.repositories.language_repository import (
    LanguageRepository,
)


class LanguageRepositoryImpl(
    SQLAlchemyRepository[Language, LanguageEntity], LanguageRepository
):
    """
    LanguageRepositoryImpl implements CRUD operations related Language entity using SQLAlchemy.
    """

    model = Language
    mapper = LanguageDataMapper

    async def find_by_code(self, code: str) -> LanguageEntity | None:
        result: Language | None = await self.session.get(self.model, code)
        return self.mapper.to_entity(result) if result else None

    async def update(self, entity: LanguageEntity) -> LanguageEntity:
        obj = self.mapper.from_entity(entity)
        stmt = (
            update(self.model)
            .filter_by(code=obj.code)
            .values(obj.to_dict())
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        return self.mapper.to_entity(result.scalar_one())
