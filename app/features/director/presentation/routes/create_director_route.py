"""
Create director api route module.
"""

from typing import Annotated
from fastapi import Response, Request, status, Depends

from app.features.director.presentation.routes.director_router import router
from app.features.director.domain.entities.director_command_model import (
    DirectorCreateModel,
)
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from app.features.director.domain.usecases.create_director import CreateDirectorUseCase
from app.features.director.dependencies import get_create_director_use_case


@router.post(
    path="",
    response_model=DirectorReadModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_director(
    data: DirectorCreateModel,
    response: Response,
    request: Request,
    create_director_use_case: Annotated[
        CreateDirectorUseCase, Depends(get_create_director_use_case)
    ],
):
    director = await create_director_use_case((data,))
    response.headers["location"] = f"{request.url.path}/{director.id_}"
    return director
