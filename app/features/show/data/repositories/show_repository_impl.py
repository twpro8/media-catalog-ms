"""
Show repository implementation module.
"""

from datetime import date
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, IntegrityError

from app.core.error.base_exception import BaseError
from app.core.error.show_exception import ShowNotFoundError, ShowAlreadyExistsError
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

    async def update(self, entity: ShowEntity) -> ShowEntity:
        try:
            return await super().update(entity)
        except NoResultFound as e:
            raise ShowNotFoundError from e
        except IntegrityError as e:
            raise ShowAlreadyExistsError from e
        except Exception as e:
            raise BaseError("Internal database error") from e

    async def find_by_title_and_date(
        self, title: str, release_date: date
    ) -> ShowEntity | None:
        query = select(self.model).where(
            self.model.title == title,
            self.model.release_date == release_date,
        )
        result = await self.session.scalar(query)
        return self.mapper.to_entity(result) if result else None
