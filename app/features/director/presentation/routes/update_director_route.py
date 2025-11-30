"""
Update director api route module.
"""

from typing import Annotated
from uuid import UUID

from fastapi import Depends, status

from app.features.director.presentation.routes.director_router import router
from app.features.director.dependencies import get_update_director_use_case
from app.features.director.domain.entities.director_command_model import (
    DirectorUpdateModel,
)
from app.features.director.domain.usecases.update_director import UpdateDirectorUseCase
from app.features.director.domain.entities.director_query_model import DirectorReadModel


@router.patch(
    path="/{director_id}",
    response_model=DirectorReadModel,
    status_code=status.HTTP_200_OK,
)
async def update_director(
    director_id: UUID,
    data: DirectorUpdateModel,
    update_director_use_case: Annotated[
        UpdateDirectorUseCase, Depends(get_update_director_use_case)
    ],
):
    director = await update_director_use_case((director_id, data))
    return director
