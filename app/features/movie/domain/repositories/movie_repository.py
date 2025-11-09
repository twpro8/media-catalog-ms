"""
Movie repository module.
"""

from abc import abstractmethod

from app.core.repositories.base_repository import BaseRepository
from app.features.movie.domain.entities.movie_entity import MovieEntity


class MovieRepository(BaseRepository[MovieEntity]):
    """
    MovieRepository defines a repositories interface for Movie entity.
    """

    @abstractmethod
    async def find_by_title(self, title: str) -> MovieEntity | None:
        raise NotImplementedError()
