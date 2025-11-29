"""
Update episode api router module.
"""

from typing import Annotated
from uuid import UUID

from fastapi import Depends, status

from app.features.episode.presentation.routes.episode_router import router
from app.features.episode.dependencies import get_update_episode_use_case
from app.features.episode.domain.entities.episode_command_model import (
    EpisodeUpdateModel,
)
from app.features.episode.domain.usecases.update_episode import UpdateEpisodeUseCase
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel


@router.patch(
    "/{id_}/",
    response_model=EpisodeReadModel,
    status_code=status.HTTP_200_OK,
)
async def update_episode(
    id_: UUID,
    data: EpisodeUpdateModel,
    update_episode_use_case: Annotated[
        UpdateEpisodeUseCase, Depends(get_update_episode_use_case)
    ],
):
    episode = await update_episode_use_case((id_, data))
    return episode
