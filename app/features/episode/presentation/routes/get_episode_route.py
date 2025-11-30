"""
Get episode api route module.
"""

from typing import Annotated
from uuid import UUID
from fastapi import status, Depends

from app.features.episode.presentation.routes.episode_router import router
from app.features.episode.domain.usecases.get_episode import GetEpisodeUseCase
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.episode.dependencies import get_episode_use_case


@router.get(
    path="/{episode_id}",
    response_model=EpisodeReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_episode(
    episode_id: UUID,
    get_episode_use_case: Annotated[GetEpisodeUseCase, Depends(get_episode_use_case)],
):
    episode = await get_episode_use_case((episode_id,))
    return episode
