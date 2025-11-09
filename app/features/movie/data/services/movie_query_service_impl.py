"""
Movies query service implementation module.
"""

from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.features.movie.domain.services.movie_query_service import MovieQueryService
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from app.features.movie.data.models.movie import Movie


class MovieQueryServiceImpl(MovieQueryService):
    """
    MovieQueryServiceImpl implements READ operations related to Movie entity using SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def find_by_id(self, id_: UUID) -> MovieReadModel | None:
        result = await self.session.get(Movie, id_)

        if result is None:
            return None

        return result.to_read_model()

    async def findall(self) -> Sequence[MovieReadModel]:
        # TODO: add offset and limit
        statement = select(Movie).filter_by(is_deleted=False)

        result = await self.session.execute(statement)

        return [movie.to_read_model() for movie in result.scalars().all()]
