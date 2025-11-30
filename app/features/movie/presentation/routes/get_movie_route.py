"""
Get movie api route module.
"""

from typing import Annotated
from uuid import UUID
from fastapi import status, Depends

from app.features.movie.presentation.routes.movie_router import router
from app.features.movie.domain.usecases.get_movie import GetMovieUseCase
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.dependencies import get_movie_use_case


@router.get(
    path="/{movie_id}",
    response_model=MovieReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_movie(
    movie_id: UUID,
    get_movie_use_case: Annotated[GetMovieUseCase, Depends(get_movie_use_case)],
):
    movie = await get_movie_use_case((movie_id,))
    return movie
