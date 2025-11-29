"""
Delete episode api router module.
"""

from typing import Annotated
from uuid import UUID

from fastapi import status, Depends

from app.features.episode.presentation.routes.episode_router import router
from app.features.episode.dependencies import get_delete_episode_use_case
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.episode.domain.usecases.delete_episode import DeleteEpisodeUseCase


@router.delete(
    "/{id_}/",
    response_model=EpisodeReadModel,
    status_code=status.HTTP_200_OK,
)
async def delete_episode(
    id_: UUID,
    delete_episode_use_case: Annotated[
        DeleteEpisodeUseCase, Depends(get_delete_episode_use_case)
    ],
):
    episode = await delete_episode_use_case((id_,))
    return episode
