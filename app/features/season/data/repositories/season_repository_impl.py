"""
Season repository implementation module.
"""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, IntegrityError

from app.core.error.base_exception import BaseError
from app.features.season.domain.exceptions import (
    SeasonNotFoundError,
    SeasonAlreadyExistsError,
)
from app.core.repositories.sqlalchemy.repository import SQLAlchemyRepository
from app.features.season.data.mappers.season_data_mapper import SeasonDataMapper
from app.features.season.domain.repositories.season_repository import SeasonRepository
from app.features.season.domain.entities.season_entity import SeasonEntity
from app.features.season.data.models.season import Season


class SeasonRepositoryImpl(
    SQLAlchemyRepository[Season, SeasonEntity], SeasonRepository
):
    """
    SeasonRepositoryImpl implements CRUD operations related Season entity using SQLAlchemy.
    """

    model = Season
    mapper = SeasonDataMapper

    async def update(self, entity: SeasonEntity) -> SeasonEntity:
        try:
            return await super().update(entity)
        except NoResultFound as e:
            raise SeasonNotFoundError from e
        except IntegrityError as e:
            raise SeasonAlreadyExistsError from e
        except Exception as e:
            raise BaseError("Internal database error") from e

    async def find_by_show_and_number(
        self, show_id: UUID, season_number: int
    ) -> SeasonEntity | None:
        query = select(self.model).where(
            self.model.show_id == show_id,
            self.model.season_number == season_number,
        )
        result = await self.session.scalar(query)
        return self.mapper.to_entity(result) if result else None
