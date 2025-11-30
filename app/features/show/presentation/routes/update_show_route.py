"""
Update show api route module.
"""

from typing import Annotated
from uuid import UUID

from fastapi import Depends, status

from app.features.show.presentation.routes.show_router import router
from app.features.show.dependencies import get_update_show_use_case
from app.features.show.domain.entities.show_command_model import ShowUpdateModel
from app.features.show.domain.usecases.update_show import UpdateShowUseCase
from app.features.show.domain.entities.show_query_model import ShowReadModel


@router.patch(
    path="/{show_id}",
    response_model=ShowReadModel,
    status_code=status.HTTP_200_OK,
)
async def update_show(
    show_id: UUID,
    data: ShowUpdateModel,
    update_show_use_case: Annotated[
        UpdateShowUseCase, Depends(get_update_show_use_case)
    ],
):
    show = await update_show_use_case((show_id, data))
    return show
