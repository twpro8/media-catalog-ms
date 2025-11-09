"""
Delete movie api router module.
"""

from uuid import UUID

from fastapi import status, Depends

from app.features.movie.presentation.routes.movie_router import router
from app.features.movie.dependencies import get_delete_movie_use_case
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.domain.usecases.delete_movie import DeleteMovieUseCase


@router.delete(
    "/{id_}/",
    response_model=MovieReadModel,
    status_code=status.HTTP_200_OK,
)
async def delete_movie(
    id_: UUID,
    delete_movie_use_case: DeleteMovieUseCase = Depends(get_delete_movie_use_case),
):
    movie = await delete_movie_use_case((id_,))
    return movie
