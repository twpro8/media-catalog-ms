"""
Get director api route module.
"""

from typing import Annotated
from fastapi import status, Depends

from app.features.director.presentation.routes.director_router import router
from app.features.director.domain.usecases.get_directors import GetDirectorsUseCase
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from app.features.director.dependencies import get_directors_use_case


@router.get(
    path="",
    response_model=list[DirectorReadModel],
    status_code=status.HTTP_200_OK,
)
async def get_directors(
    get_directors_use_case: Annotated[
        GetDirectorsUseCase, Depends(get_directors_use_case)
    ],
):
    directors = await get_directors_use_case(None)
    return directors
