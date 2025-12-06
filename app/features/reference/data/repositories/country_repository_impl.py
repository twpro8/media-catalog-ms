"""
Country repository implementation module.
"""

from sqlalchemy import update

from app.core.repositories.sqlalchemy.repository import SQLAlchemyRepository
from app.features.reference.data.mappers.country_data_mapper import CountryDataMapper
from app.features.reference.data.models.country import Country
from app.features.reference.domain.entities.country.country_entity import (
    CountryEntity,
)
from app.features.reference.domain.repositories.country_repository import (
    CountryRepository,
)


class CountryRepositoryImpl(
    SQLAlchemyRepository[Country, CountryEntity], CountryRepository
):
    """
    CountryRepositoryImpl implements CRUD operations related Country entity using SQLAlchemy.
    """

    model = Country
    mapper = CountryDataMapper

    async def find_by_code(self, code: str) -> CountryEntity | None:
        result: Country | None = await self.session.get(self.model, code)
        return self.mapper.to_entity(result) if result else None

    async def update(self, entity: CountryEntity) -> CountryEntity:
        obj = self.mapper.from_entity(entity)
        stmt = (
            update(self.model)
            .filter_by(code=obj.code)
            .values(obj.to_dict())
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        return self.mapper.to_entity(result.scalar_one())
