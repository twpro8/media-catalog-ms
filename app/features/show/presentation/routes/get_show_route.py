"""
Get show api router module.
"""

from uuid import UUID
from fastapi import status, Depends

from app.features.show.presentation.routes.show_router import router
from app.features.show.domain.usecases.get_show import GetShowUseCase
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.dependencies import get_show_use_case


@router.get(
    "/{id_}/",
    response_model=ShowReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_show(
    id_: UUID,
    get_show_use_case: GetShowUseCase = Depends(get_show_use_case),
):
    show = await get_show_use_case((id_,))
    return show
