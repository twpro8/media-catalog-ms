"""
Update movie use case module.
"""

from abc import abstractmethod
from typing import cast
from uuid import UUID

from sqlalchemy.exc import IntegrityError

from app.core.error.movie_exception import MovieAlreadyExistsError, MovieNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.movie.domain.entities.movie_command_model import MovieUpdateModel
from app.features.movie.domain.entities.movie_entity import MovieEntity
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.domain.repositories.movie_unit_of_work import MovieUnitOfWork


class UpdateMovieUseCase(BaseUseCase[tuple[UUID, MovieUpdateModel], MovieReadModel]):
    """
    UpdateMovieUseCase defines a query use case interface related to the Movie Entity.
    """

    unit_of_work: MovieUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[UUID, MovieUpdateModel]) -> MovieReadModel: ...


class UpdateMovieUseCaseImpl(UpdateMovieUseCase):
    """
    UpdateMovieUseCaseImpl implements a query use case related to the Movie entity.
    """

    def __init__(self, unit_of_work: MovieUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[UUID, MovieUpdateModel]) -> MovieReadModel:
        id_, update_data = args

        existing_movie = await self.unit_of_work.movies.find_by_id(id_)
        if existing_movie is None:
            raise MovieNotFoundError

        update_entity = existing_movie.update_entity(
            update_data, lambda movie_data: update_data.model_dump(exclude_unset=True)
        )

        try:
            updated_movie = await self.unit_of_work.movies.update(update_entity)
        except IntegrityError:
            raise MovieAlreadyExistsError

        await self.unit_of_work.commit()

        return MovieReadModel.from_entity(cast(MovieEntity, updated_movie))
