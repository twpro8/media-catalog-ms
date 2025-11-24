"""
Movie unit of work implementation module.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.unit_of_work.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from app.features.movie.domain.repositories.movie_unit_of_work import MovieUnitOfWork
from app.features.movie.domain.repositories.movie_repository import MovieRepository


class MovieUnitOfWorkImpl(SQLAlchemyUnitOfWork, MovieUnitOfWork):
    """
    Movie unit of work implementation.
    """

    def __init__(
        self,
        session: AsyncSession,
        movie_repository: MovieRepository,
    ):
        super().__init__(session)
        self.movies: MovieRepository = movie_repository
