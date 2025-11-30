"""
Director repository implementation module.
"""

from sqlalchemy.exc import NoResultFound, IntegrityError

from app.core.error.base_exception import BaseError
from app.core.error.director_exception import (
    DirectorAlreadyExistsError,
    DirectorNotFoundError,
)
from app.core.repositories.sqlalchemy.repository import SQLAlchemyRepository
from app.features.director.data.mappers.director_data_mapper import DirectorDataMapper
from app.features.director.domain.repositories.director_repository import (
    DirectorRepository,
)
from app.features.director.domain.entities.director_entity import DirectorEntity
from app.features.director.data.models.director import Director


class DirectorRepositoryImpl(
    SQLAlchemyRepository[Director, DirectorEntity], DirectorRepository
):
    """
    DirectorRepositoryImpl implements CRUD operations related Director entity using SQLAlchemy.
    """

    model = Director
    mapper = DirectorDataMapper

    async def update(self, entity: DirectorEntity) -> DirectorEntity:
        try:
            return await super().update(entity)
        except NoResultFound as e:
            raise DirectorNotFoundError from e
        except IntegrityError as e:
            raise DirectorAlreadyExistsError from e
        except Exception as e:
            raise BaseError("Internal database error") from e
