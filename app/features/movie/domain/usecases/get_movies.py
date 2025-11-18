"""
Get movies use case module.
"""

from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.domain.services.movie_query_service import MovieQueryService


class GetMoviesUseCase(BaseUseCase[None, Sequence[MovieReadModel]]):
    """
    GetMoviesUseCase defines a query use case interface related to the Movie Entity.
    """

    service = MovieQueryService

    async def __call__(self, args: None) -> Sequence[MovieReadModel]: ...


class GetMoviesUseCaseImpl(GetMoviesUseCase):
    """
    GetMoviesUseCaseImpl implements a query use case related to the Movie entity.
    """

    def __init__(self, service: MovieQueryService):
        self.service: MovieQueryService = service

    async def __call__(self, args: None) -> Sequence[MovieReadModel]:
        movies = await self.service.findall()
        return movies
