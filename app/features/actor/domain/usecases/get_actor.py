"""
Get actor use case module.
"""

from abc import abstractmethod
from uuid import UUID

from app.features.actor.domain.exceptions import ActorNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from app.features.actor.domain.services.actor_query_service import (
    ActorQueryService,
)


class GetActorUseCase(BaseUseCase[tuple[UUID], ActorReadModel]):
    """
    GetActorUseCase defines a query use case interface related to the Actor Entity.
    """

    service: ActorQueryService

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> ActorReadModel: ...


class GetActorUseCaseImpl(GetActorUseCase):
    """
    GetActorUseCaseImpl implements a query use case related to the Actor entity.
    """

    def __init__(self, service: ActorQueryService):
        self.service: ActorQueryService = service

    async def __call__(self, args: tuple[UUID]) -> ActorReadModel:
        (id_,) = args

        actor = await self.service.find_by_id(id_)
        if actor is None or actor.is_deleted:
            raise ActorNotFoundError

        return actor
