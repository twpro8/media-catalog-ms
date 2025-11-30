"""
Actor unit of work implementation module.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.unit_of_work.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from app.features.actor.domain.repositories.actor_unit_of_work import (
    ActorUnitOfWork,
)
from app.features.actor.domain.repositories.actor_repository import (
    ActorRepository,
)


class ActorUnitOfWorkImpl(SQLAlchemyUnitOfWork, ActorUnitOfWork):
    """
    Actor unit of work implementation.
    """

    def __init__(
        self,
        session: AsyncSession,
        actor_repository: ActorRepository,
    ):
        super().__init__(session)
        self.actors: ActorRepository = actor_repository
