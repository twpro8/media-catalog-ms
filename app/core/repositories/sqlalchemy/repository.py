"""
Sqlalchemy repository implementation.
"""

from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from app.core.models.postgres.models import Base
from app.core.repositories.data_mapper import DataMapper


class SQLAlchemyRepository[TModel: Base, TEntity]:
    """
    SQLAlchemyRepository implements base sqlalchemy repository.
    """

    model: type[TModel]
    mapper: type[DataMapper[TModel, TEntity]]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, entity: TEntity) -> TEntity:
        obj = self.mapper.from_entity(entity)
        self.session.add(obj)
        await self.session.flush()
        return self.mapper.to_entity(obj)

    async def findall(self) -> Sequence[TEntity]:
        # TODO: add pagination
        query = select(self.model)
        result = await self.session.execute(query)
        return [self.mapper.to_entity(obj) for obj in result.scalars().all()]

    async def find_by_id(self, id_) -> TEntity | None:
        result = await self.session.get(self.model, id_)
        return self.mapper.to_entity(result) if result else None

    async def update(self, entity: TEntity) -> TEntity:
        obj = self.mapper.from_entity(entity)
        stmt = (
            update(self.model)
            .filter_by(id_=obj.id_)
            .values(obj.to_dict())
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        return self.mapper.to_entity(result.scalar_one())

    async def delete_by_id(self, id_: UUID) -> TEntity:
        stmt = delete(self.model).filter_by(id_=id_).returning(self.model)
        result = await self.session.execute(stmt)
        return self.mapper.to_entity(result.scalar_one())
