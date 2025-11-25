"""
Delete show api router module.
"""

from uuid import UUID

from fastapi import status, Depends

from app.features.show.presentation.routes.show_router import router
from app.features.show.dependencies import get_delete_show_use_case
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.domain.usecases.delete_show import DeleteShowUseCase


@router.delete(
    "/{id_}/",
    response_model=ShowReadModel,
    status_code=status.HTTP_200_OK,
)
async def delete_show(
    id_: UUID,
    delete_show_use_case: DeleteShowUseCase = Depends(get_delete_show_use_case),
):
    show = await delete_show_use_case((id_,))
    return show
