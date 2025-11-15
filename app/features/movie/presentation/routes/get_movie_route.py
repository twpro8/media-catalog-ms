"""
Get movie api router module.
"""

from uuid import UUID
from fastapi import status, Depends

from app.features.movie.presentation.routes.movie_router import router
from app.features.movie.domain.usecases.get_movie import GetMovieUseCase
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.dependencies import get_movie_use_case


@router.get(
    "/{id_}/",
    response_model=MovieReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_movie(
    id_: UUID,
    get_movie_use_case: GetMovieUseCase = Depends(get_movie_use_case),
):
    movie = await get_movie_use_case((id_,))
    return movie
