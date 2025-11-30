"""
Actor query service module.
"""

from app.core.services.base_query_service import QueryService
from app.features.actor.domain.entities.actor_query_model import ActorReadModel


class ActorQueryService(QueryService[ActorReadModel]):
    """
    ActorQueryService defines a query service interface..
    """

    pass
