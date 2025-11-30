"""
Get actor api route module.
"""

from typing import Annotated
from uuid import UUID
from fastapi import status, Depends

from app.features.actor.presentation.routes.actor_router import router
from app.features.actor.domain.usecases.get_actor import GetActorUseCase
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from app.features.actor.dependencies import get_actor_use_case


@router.get(
    path="/{actor_id}",
    response_model=ActorReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_actor(
    actor_id: UUID,
    get_actor_use_case: Annotated[GetActorUseCase, Depends(get_actor_use_case)],
):
    actor = await get_actor_use_case((actor_id,))
    return actor
