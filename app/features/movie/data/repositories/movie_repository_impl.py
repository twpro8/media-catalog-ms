"""
Movie repository implementation module.
"""

from datetime import date
from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from sqlalchemy import select, update, delete

from app.features.movie.domain.repositories.movie_repository import MovieRepository
from app.features.movie.domain.entities.movie_entity import MovieEntity
from app.features.movie.data.models.movie import Movie


class MovieRepositoryImpl(MovieRepository):
    """
    MovieRepositoryImpl implements CRUD operations related Movie entity using SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def create(self, entity: MovieEntity) -> MovieEntity:
        movie = Movie.from_entity(entity)

        self.session.add(movie)
        await self.session.flush()

        return movie.to_entity()

    async def findall(self) -> Sequence[MovieEntity]:
        # TODO: add offset and limit
        statement = select(Movie)

        try:
            result: Sequence[Movie] = (
                (await self.session.execute(statement)).scalars().all()
            )
        except NoResultFound:
            return []

        return [movie.to_entity() for movie in result]

    async def find_by_id(self, id_: UUID) -> MovieEntity | None:
        result: Movie | None = await self.session.get(Movie, id_)

        if result is None:
            return None

        return result.to_entity()

    async def find_by_title_and_date(
        self, title: str, release_date: date
    ) -> MovieEntity | None:
        query = select(Movie).where(
            Movie.title == title,
            Movie.release_date == release_date,
        )

        result: Movie | None = await self.session.scalar(query)

        return result.to_entity() if result else None

    async def update(self, entity: MovieEntity) -> MovieEntity:
        movie = Movie.from_entity(entity)
        update_data = movie.to_dict()

        for key in [Movie.updated_at.key, Movie.created_at.key, Movie.id_.key]:
            update_data.pop(key)

        statement = (
            update(Movie).filter_by(id_=movie.id_).values(update_data).returning(Movie)
        )

        result = (await self.session.execute(statement)).scalar_one()

        return result.to_entity()

    async def delete_by_id(self, id_: UUID) -> MovieEntity:
        statement = delete(Movie).filter_by(id_=id_).returning(Movie)

        result = (await self.session.execute(statement)).scalar_one()

        return result.to_entity()
