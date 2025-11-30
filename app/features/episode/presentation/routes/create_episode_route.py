"""
Create episode api route module.
"""

from typing import Annotated
from fastapi import Response, Request, status, Depends

from app.features.episode.presentation.routes.episode_router import router
from app.features.episode.domain.entities.episode_command_model import (
    EpisodeCreateModel,
)
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.episode.domain.usecases.create_episode import CreateEpisodeUseCase
from app.features.episode.dependencies import get_create_episode_use_case


@router.post(
    path="",
    response_model=EpisodeReadModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_episode(
    data: EpisodeCreateModel,
    response: Response,
    request: Request,
    create_episode_use_case: Annotated[
        CreateEpisodeUseCase, Depends(get_create_episode_use_case)
    ],
):
    episode = await create_episode_use_case((data,))
    response.headers["location"] = f"{request.url.path}/{episode.id_}"
    return episode
