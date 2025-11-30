"""
Delete actor api route module.
"""

from typing import Annotated
from uuid import UUID

from fastapi import status, Depends

from app.features.actor.presentation.routes.actor_router import router
from app.features.actor.dependencies import get_delete_actor_use_case
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from app.features.actor.domain.usecases.delete_actor import DeleteActorUseCase


@router.delete(
    path="/{actor_id}",
    response_model=ActorReadModel,
    status_code=status.HTTP_200_OK,
)
async def delete_actor(
    actor_id: UUID,
    delete_actor_use_case: Annotated[
        DeleteActorUseCase, Depends(get_delete_actor_use_case)
    ],
):
    actor = await delete_actor_use_case((actor_id,))
    return actor
