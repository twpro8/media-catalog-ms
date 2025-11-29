"""
Get episodes use case module.
"""

from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.episode.domain.services.episode_query_service import (
    EpisodeQueryService,
)


class GetEpisodesUseCase(BaseUseCase[None, Sequence[EpisodeReadModel]]):
    """
    GetEpisodesUseCase defines a query use case interface related to the Episode Entity.
    """

    service = EpisodeQueryService

    async def __call__(self, args: None) -> Sequence[EpisodeReadModel]: ...


class GetEpisodesUseCaseImpl(GetEpisodesUseCase):
    """
    GetEpisodesUseCaseImpl implements a query use case related to the Episode entity.
    """

    def __init__(self, service: EpisodeQueryService):
        self.service: EpisodeQueryService = service

    async def __call__(self, args: None) -> Sequence[EpisodeReadModel]:
        episodes = await self.service.findall()
        return episodes
