"""
Actor repository module.
"""

from app.core.repositories.base_repository import BaseRepository
from app.features.actor.domain.entities.actor_entity import ActorEntity


class ActorRepository(BaseRepository[ActorEntity]):
    """
    ActorRepository defines a repositories interface for Actor entity.
    """

    pass
