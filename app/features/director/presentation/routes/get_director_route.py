"""
Get director api route module.
"""

from typing import Annotated
from uuid import UUID
from fastapi import status, Depends

from app.features.director.presentation.routes.director_router import router
from app.features.director.domain.usecases.get_director import GetDirectorUseCase
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from app.features.director.dependencies import get_director_use_case


@router.get(
    path="/{director_id}",
    response_model=DirectorReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_director(
    director_id: UUID,
    get_director_use_case: Annotated[
        GetDirectorUseCase, Depends(get_director_use_case)
    ],
):
    director = await get_director_use_case((director_id,))
    return director
