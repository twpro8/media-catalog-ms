"""
Get episode use case module.
"""

from abc import abstractmethod
from uuid import UUID

from app.core.error.episode_exception import EpisodeNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.episode.domain.services.episode_query_service import (
    EpisodeQueryService,
)


class GetEpisodeUseCase(BaseUseCase[tuple[UUID], EpisodeReadModel]):
    """
    GetEpisodeUseCase defines a query use case interface related to the Episode Entity.
    """

    service: EpisodeQueryService

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> EpisodeReadModel: ...


class GetEpisodeUseCaseImpl(GetEpisodeUseCase):
    """
    GetEpisodeUseCaseImpl implements a query use case related to the Episode entity.
    """

    def __init__(self, service: EpisodeQueryService):
        self.service: EpisodeQueryService = service

    async def __call__(self, args: tuple[UUID]) -> EpisodeReadModel:
        (id_,) = args

        episode = await self.service.find_by_id(id_)
        if episode is None or episode.is_deleted:
            raise EpisodeNotFoundError

        return episode
