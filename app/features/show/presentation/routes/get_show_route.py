"""
Get show api route module.
"""

from typing import Annotated
from uuid import UUID
from fastapi import status, Depends

from app.features.show.presentation.routes.show_router import router
from app.features.show.domain.usecases.get_show import GetShowUseCase
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.dependencies import get_show_use_case


@router.get(
    path="/{show_id}",
    response_model=ShowReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_show(
    show_id: UUID,
    get_show_use_case: Annotated[GetShowUseCase, Depends(get_show_use_case)],
):
    show = await get_show_use_case((show_id,))
    return show
