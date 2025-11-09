"""
Create movie use case module.
"""

from abc import abstractmethod
from typing import cast

from app.core.error.movie_exception import MovieAlreadyExistsError
from app.core.use_cases.use_case import BaseUseCase
from app.features.movie.domain.entities.movie_entity import MovieEntity
from app.features.movie.domain.entities.movie_command_model import MovieCreateModel
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.domain.repositories.movie_unit_of_work import MovieUnitOfWork


class CreateMovieUseCase(BaseUseCase[tuple[MovieCreateModel], MovieReadModel]):
    """
    CreateMovieUseCase defines a command use case interface related to the Movie entity.
    """

    unit_of_work: MovieUnitOfWork

    @abstractmethod
    async def __call__(self, args: tuple[MovieCreateModel]) -> MovieReadModel:
        raise NotImplementedError()


class CreateMovieUseCaseImpl(CreateMovieUseCase):
    """
    CreateMovieUseCaseImpl implements a command use case related to the Movie entity.
    """

    def __init__(self, unit_of_work: MovieUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, args: tuple[MovieCreateModel]) -> MovieReadModel:
        (data,) = args

        movie = MovieEntity(None, **data.model_dump())
        existing_movie = await self.unit_of_work.repository.find_by_title(data.title)

        if existing_movie:
            if existing_movie.is_deleted:
                unmarked_movie = existing_movie.unmark_as_deleted()
                await self.unit_of_work.repository.update(unmarked_movie)
            else:
                raise MovieAlreadyExistsError
        else:
            try:
                await self.unit_of_work.repository.create(movie)
            except Exception:
                await self.unit_of_work.rollback()
                raise

        await self.unit_of_work.commit()
        created_movie = await self.unit_of_work.repository.find_by_title(data.title)

        return MovieReadModel.from_entity(cast(MovieEntity, created_movie))
