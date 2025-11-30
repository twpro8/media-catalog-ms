"""
Get actor api route module.
"""

from typing import Annotated
from fastapi import status, Depends

from app.features.actor.presentation.routes.actor_router import router
from app.features.actor.domain.usecases.get_actors import GetActorsUseCase
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from app.features.actor.dependencies import get_actors_use_case


@router.get(
    path="",
    response_model=list[ActorReadModel],
    status_code=status.HTTP_200_OK,
)
async def get_actors(
    get_actors_use_case: Annotated[GetActorsUseCase, Depends(get_actors_use_case)],
):
    actors = await get_actors_use_case(None)
    return actors
