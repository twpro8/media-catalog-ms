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
    async def find_one_or_none(self, **filter_by) -> MovieEntity | None:
        raise NotImplementedError()
