"""
Get movie api router module.
"""

from fastapi import status, Depends

from app.features.movie.presentation.routes.movie_router import router
from app.features.movie.domain.usecases.get_movies import GetMoviesUseCase
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.dependencies import get_movies_use_case


@router.get(
    "/",
    response_model=list[MovieReadModel],
    status_code=status.HTTP_200_OK,
)
async def get_movies(
    get_movies_use_case: GetMoviesUseCase = Depends(get_movies_use_case),
):
    movies = await get_movies_use_case(None)
    return movies
