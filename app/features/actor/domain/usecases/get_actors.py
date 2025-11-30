"""
Get actors use case module.
"""

from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from app.features.actor.domain.services.actor_query_service import (
    ActorQueryService,
)


class GetActorsUseCase(BaseUseCase[None, Sequence[ActorReadModel]]):
    """
    GetActorsUseCase defines a query use case interface related to the Actor Entity.
    """

    service = ActorQueryService

    async def __call__(self, args: None) -> Sequence[ActorReadModel]: ...


class GetActorsUseCaseImpl(GetActorsUseCase):
    """
    GetActorsUseCaseImpl implements a query use case related to the Actor entity.
    """

    def __init__(self, service: ActorQueryService):
        self.service: ActorQueryService = service

    async def __call__(self, args: None) -> Sequence[ActorReadModel]:
        actors = await self.service.findall()
        return actors
