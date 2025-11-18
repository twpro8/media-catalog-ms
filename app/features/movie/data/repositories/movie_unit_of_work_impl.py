"""
Movie unit of work implementation module.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.features.movie.domain.repositories.movie_unit_of_work import MovieUnitOfWork
from app.features.movie.domain.repositories.movie_repository import MovieRepository


class MovieUnitOfWorkImpl(MovieUnitOfWork):
    """
    Movie unit of work implementation.
    """

    def __init__(
        self,
        session: AsyncSession,
        movie_repository: MovieRepository,
    ):
        self.session: AsyncSession = session
        self.movies: MovieRepository = movie_repository

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
