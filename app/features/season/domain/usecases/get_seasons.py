"""
Get seasons use case module.
"""

from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.domain.services.season_query_service import SeasonQueryService


class GetSeasonsUseCase(BaseUseCase[None, Sequence[SeasonReadModel]]):
    """
    GetSeasonsUseCase defines a query use case interface related to the Season Entity.
    """

    service = SeasonQueryService

    async def __call__(self, args: None) -> Sequence[SeasonReadModel]: ...


class GetSeasonsUseCaseImpl(GetSeasonsUseCase):
    """
    GetSeasonsUseCaseImpl implements a query use case related to the Season entity.
    """

    def __init__(self, service: SeasonQueryService):
        self.service: SeasonQueryService = service

    async def __call__(self, args: None) -> Sequence[SeasonReadModel]:
        seasons = await self.service.findall()
        return seasons
