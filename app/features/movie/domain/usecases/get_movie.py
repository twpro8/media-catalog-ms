"""
Get movie use case module.
"""

from abc import abstractmethod
from uuid import UUID

from app.core.error.movie_exception import MovieNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.domain.services.movie_query_service import MovieQueryService


class GetMovieUseCase(BaseUseCase[tuple[UUID], MovieReadModel]):
    """
    GetMovieUseCase defines a query use case interface related to the Movie Entity.
    """

    service: MovieQueryService

    @abstractmethod
    async def __call__(self, args: tuple[UUID]) -> MovieReadModel:
        raise NotImplementedError()


class GetMovieUseCaseImpl(GetMovieUseCase):
    """
    GetMovieUseCaseImpl implements a query use case related to the Movie entity.
    """

    def __init__(self, service: MovieQueryService):
        self.service: MovieQueryService = service

    async def __call__(self, args: tuple[UUID]) -> MovieReadModel:
        (id_,) = args

        movie = await self.service.find_by_id(id_)
        if movie is None or movie.is_deleted:
            raise MovieNotFoundError

        return movie
