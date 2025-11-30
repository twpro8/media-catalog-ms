"""
Update movie api route module.
"""

from typing import Annotated
from uuid import UUID

from fastapi import Depends, status

from app.features.movie.presentation.routes.movie_router import router
from app.features.movie.dependencies import get_update_movie_use_case
from app.features.movie.domain.entities.movie_command_model import MovieUpdateModel
from app.features.movie.domain.usecases.update_movie import UpdateMovieUseCase
from app.features.movie.domain.entities.movie_query_model import MovieReadModel


@router.patch(
    path="/{movie_id}",
    response_model=MovieReadModel,
    status_code=status.HTTP_200_OK,
)
async def update_movie(
    movie_id: UUID,
    data: MovieUpdateModel,
    update_movie_use_case: Annotated[
        UpdateMovieUseCase, Depends(get_update_movie_use_case)
    ],
):
    movie = await update_movie_use_case((movie_id, data))
    return movie
