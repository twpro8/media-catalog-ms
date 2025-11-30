"""
Create actor api route module.
"""

from typing import Annotated
from fastapi import Response, Request, status, Depends

from app.features.actor.presentation.routes.actor_router import router
from app.features.actor.domain.entities.actor_command_model import (
    ActorCreateModel,
)
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from app.features.actor.domain.usecases.create_actor import CreateActorUseCase
from app.features.actor.dependencies import get_create_actor_use_case


@router.post(
    path="",
    response_model=ActorReadModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_actor(
    data: ActorCreateModel,
    response: Response,
    request: Request,
    create_actor_use_case: Annotated[
        CreateActorUseCase, Depends(get_create_actor_use_case)
    ],
):
    actor = await create_actor_use_case((data,))
    response.headers["location"] = f"{request.url.path}/{actor.id_}"
    return actor
