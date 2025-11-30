"""
Get episodes api route module.
"""

from typing import Annotated
from fastapi import status, Depends

from app.features.episode.presentation.routes.episode_router import router
from app.features.episode.domain.usecases.get_episodes import GetEpisodesUseCase
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.episode.dependencies import get_episodes_use_case


@router.get(
    path="",
    response_model=list[EpisodeReadModel],
    status_code=status.HTTP_200_OK,
)
async def get_episodes(
    get_episodes_use_case: Annotated[
        GetEpisodesUseCase, Depends(get_episodes_use_case)
    ],
):
    episodes = await get_episodes_use_case(None)
    return episodes
