"""
Create movie api route module.
"""

from typing import Annotated
from fastapi import Response, Request, status, Depends

from app.features.movie.presentation.routes.movie_router import router
from app.features.movie.domain.entities.movie_command_model import MovieCreateModel
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.domain.usecases.create_movie import CreateMovieUseCase
from app.features.movie.dependencies import get_create_movie_use_case


@router.post(
    path="",
    response_model=MovieReadModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_movie(
    data: MovieCreateModel,
    response: Response,
    request: Request,
    create_movie_use_case: Annotated[
        CreateMovieUseCase, Depends(get_create_movie_use_case)
    ],
):
    movie = await create_movie_use_case((data,))
    response.headers["location"] = f"{request.url.path}/{movie.id_}"
    return movie
