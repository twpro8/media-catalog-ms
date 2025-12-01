"""
Get season use case module.
"""

from abc import abstractmethod
from uuid import UUID

from app.features.season.domain.exceptions import SeasonNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.domain.services.season_query_service import SeasonQueryService


class GetSeasonUseCase(BaseUseCase[tuple[UUID], SeasonReadModel]):
    """
    GetSeasonUseCase defines a query use case interface related to the Season Entity.
    """

    service: SeasonQueryService

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> SeasonReadModel: ...


class GetSeasonUseCaseImpl(GetSeasonUseCase):
    """
    GetSeasonUseCaseImpl implements a query use case related to the Season entity.
    """

    def __init__(self, service: SeasonQueryService):
        self.service: SeasonQueryService = service

    async def __call__(self, args: tuple[UUID]) -> SeasonReadModel:
        (id_,) = args

        season = await self.service.find_by_id(id_)
        if season is None or season.is_deleted:
            raise SeasonNotFoundError

        return season
