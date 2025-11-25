"""
Get shows use case module.
"""

from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.domain.services.show_query_service import ShowQueryService


class GetShowsUseCase(BaseUseCase[None, Sequence[ShowReadModel]]):
    """
    GetShowsUseCase defines a query use case interface related to the Show Entity.
    """

    service = ShowQueryService

    async def __call__(self, args: None) -> Sequence[ShowReadModel]: ...


class GetShowsUseCaseImpl(GetShowsUseCase):
    """
    GetShowsUseCaseImpl implements a query use case related to the Show entity.
    """

    def __init__(self, service: ShowQueryService):
        self.service: ShowQueryService = service

    async def __call__(self, args: None) -> Sequence[ShowReadModel]:
        shows = await self.service.findall()
        return shows
