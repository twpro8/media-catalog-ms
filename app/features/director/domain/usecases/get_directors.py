"""
Get directors use case module.
"""

from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from app.features.director.domain.services.director_query_service import (
    DirectorQueryService,
)


class GetDirectorsUseCase(BaseUseCase[None, Sequence[DirectorReadModel]]):
    """
    GetDirectorsUseCase defines a query use case interface related to the Director Entity.
    """

    service = DirectorQueryService

    async def __call__(self, args: None) -> Sequence[DirectorReadModel]: ...


class GetDirectorsUseCaseImpl(GetDirectorsUseCase):
    """
    GetDirectorsUseCaseImpl implements a query use case related to the Director entity.
    """

    def __init__(self, service: DirectorQueryService):
        self.service: DirectorQueryService = service

    async def __call__(self, args: None) -> Sequence[DirectorReadModel]:
        directors = await self.service.findall()
        return directors
