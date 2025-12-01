"""
Actor repository implementation module.
"""

from sqlalchemy.exc import NoResultFound, IntegrityError

from app.core.error.base_exception import BaseError
from app.features.actor.domain.exceptions import (
    ActorNotFoundError,
    ActorAlreadyExistsError,
)
from app.core.repositories.sqlalchemy.repository import SQLAlchemyRepository
from app.features.actor.data.mappers.actor_data_mapper import ActorDataMapper
from app.features.actor.domain.repositories.actor_repository import (
    ActorRepository,
)
from app.features.actor.domain.entities.actor_entity import ActorEntity
from app.features.actor.data.models.actor import Actor


class ActorRepositoryImpl(SQLAlchemyRepository[Actor, ActorEntity], ActorRepository):
    """
    ActorRepositoryImpl implements CRUD operations related Actor entity using SQLAlchemy.
    """

    model = Actor
    mapper = ActorDataMapper

    async def update(self, entity: ActorEntity) -> ActorEntity:
        try:
            return await super().update(entity)
        except NoResultFound as e:
            raise ActorNotFoundError from e
        except IntegrityError as e:
            raise ActorAlreadyExistsError from e
        except Exception as e:
            raise BaseError("Internal database error") from e
