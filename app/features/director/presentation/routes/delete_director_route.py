"""
Delete director api route module.
"""

from typing import Annotated
from uuid import UUID

from fastapi import status, Depends

from app.features.director.presentation.routes.director_router import router
from app.features.director.dependencies import get_delete_director_use_case
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from app.features.director.domain.usecases.delete_director import DeleteDirectorUseCase


@router.delete(
    path="/{director_id}",
    response_model=DirectorReadModel,
    status_code=status.HTTP_200_OK,
)
async def delete_director(
    director_id: UUID,
    delete_director_use_case: Annotated[
        DeleteDirectorUseCase, Depends(get_delete_director_use_case)
    ],
):
    director = await delete_director_use_case((director_id,))
    return director
