"""
Delete movie use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from app.core.error.invalid_operation_exception import InvalidOperationError
from app.features.movie.domain.exceptions import (
    MovieNotFoundError,
    MovieAlreadyDeletedError,
)
from app.core.use_cases.use_case import BaseUseCase
from app.features.movie.domain.entities.movie_entity import MovieEntity
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.domain.repositories.movie_unit_of_work import MovieUnitOfWork


class DeleteMovieUseCase(BaseUseCase[tuple[UUID], MovieReadModel]):
    """
    DeleteMovieUseCase defines a command use case interface related to the Movie entity.
    """

    unit_of_work: MovieUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> MovieReadModel: ...


class DeleteMovieUseCaseImpl(DeleteMovieUseCase):
    """
    DeleteMovieUseCaseImpl implements a command use case related to the Movie entity.
    """

    def __init__(self, unit_of_work: MovieUnitOfWork):
        self.unit_of_work: MovieUnitOfWork = unit_of_work

    async def __call__(self, args: tuple[UUID]) -> MovieReadModel:
        (id_,) = args

        existing_movie = await self.unit_of_work.movies.find_by_id(id_)
        if existing_movie is None:
            raise MovieNotFoundError

        try:
            marked_movie = existing_movie.mark_entity_as_deleted()
        except InvalidOperationError:
            raise MovieAlreadyDeletedError

        deleted_movie = await self.unit_of_work.movies.update(marked_movie)

        await self.unit_of_work.commit()

        return MovieReadModel.from_entity(cast(MovieEntity, deleted_movie))
