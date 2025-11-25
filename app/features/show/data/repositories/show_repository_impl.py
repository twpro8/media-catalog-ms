"""
Show repository implementation module.
"""

from datetime import date
from sqlalchemy import select

from app.core.repositories.sqlalchemy.repository import SQLAlchemyRepository
from app.features.show.data.mappers.show_data_mapper import ShowDataMapper
from app.features.show.domain.repositories.show_repository import ShowRepository
from app.features.show.domain.entities.show_entity import ShowEntity
from app.features.show.data.models.show import Show


class ShowRepositoryImpl(SQLAlchemyRepository[Show, ShowEntity], ShowRepository):
    """
    ShowRepositoryImpl implements CRUD operations related Show entity using SQLAlchemy.
    """

    model = Show
    mapper = ShowDataMapper

    async def find_by_title_and_date(
        self, title: str, release_date: date
    ) -> ShowEntity | None:
        query = select(self.model).where(
            self.model.title == title,
            self.model.release_date == release_date,
        )
        result = await self.session.scalar(query)
        return self.mapper.to_entity(result) if result else None
