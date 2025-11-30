"""
Delete show api route module.
"""

from typing import Annotated
from uuid import UUID

from fastapi import status, Depends

from app.features.show.presentation.routes.show_router import router
from app.features.show.dependencies import get_delete_show_use_case
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.domain.usecases.delete_show import DeleteShowUseCase


@router.delete(
    path="/{show_id}",
    response_model=ShowReadModel,
    status_code=status.HTTP_200_OK,
)
async def delete_show(
    show_id: UUID,
    delete_show_use_case: Annotated[
        DeleteShowUseCase, Depends(get_delete_show_use_case)
    ],
):
    show = await delete_show_use_case((show_id,))
    return show
