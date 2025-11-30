"""
Update actor api route module.
"""

from typing import Annotated
from uuid import UUID

from fastapi import Depends, status

from app.features.actor.presentation.routes.actor_router import router
from app.features.actor.dependencies import get_update_actor_use_case
from app.features.actor.domain.entities.actor_command_model import (
    ActorUpdateModel,
)
from app.features.actor.domain.usecases.update_actor import UpdateActorUseCase
from app.features.actor.domain.entities.actor_query_model import ActorReadModel


@router.patch(
    path="/{actor_id}",
    response_model=ActorReadModel,
    status_code=status.HTTP_200_OK,
)
async def update_actor(
    actor_id: UUID,
    data: ActorUpdateModel,
    update_actor_use_case: Annotated[
        UpdateActorUseCase, Depends(get_update_actor_use_case)
    ],
):
    actor = await update_actor_use_case((actor_id, data))
    return actor
