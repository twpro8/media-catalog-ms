"""
Movie repository implementation module.
"""

from datetime import date

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, IntegrityError

from app.core.error.base_exception import BaseError
from app.core.error.movie_exception import MovieAlreadyExistsError, MovieNotFoundError
from app.core.repositories.sqlalchemy.repository import SQLAlchemyRepository
from app.features.movie.data.mappers.movie_data_mapper import MovieDataMapper
from app.features.movie.domain.repositories.movie_repository import MovieRepository
from app.features.movie.domain.entities.movie_entity import MovieEntity
from app.features.movie.data.models.movie import Movie


class MovieRepositoryImpl(SQLAlchemyRepository[Movie, MovieEntity], MovieRepository):
    """
    MovieRepositoryImpl implements CRUD operations related Movie entity using SQLAlchemy.
    """

    model = Movie
    mapper = MovieDataMapper

    async def update(self, entity: MovieEntity) -> MovieEntity:
        try:
            return await super().update(entity)
        except NoResultFound as e:
            raise MovieNotFoundError from e
        except IntegrityError as e:
            raise MovieAlreadyExistsError from e
        except Exception as e:
            raise BaseError("Internal database error") from e

    async def find_by_title_and_date(
        self, title: str, release_date: date
    ) -> MovieEntity | None:
        query = select(self.model).where(
            self.model.title == title,
            self.model.release_date == release_date,
        )
        result = await self.session.scalar(query)
        return self.mapper.to_entity(result) if result else None
