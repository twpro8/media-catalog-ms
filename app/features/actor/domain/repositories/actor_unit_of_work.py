"""
Actor unit of work module.
"""

from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.actor.domain.repositories.actor_repository import (
    ActorRepository,
)


class ActorUnitOfWork(AbstractUnitOfWork):
    """
    ActorUnitOfWork defines an interface based on Unit of Work.
    """

    actors: ActorRepository
