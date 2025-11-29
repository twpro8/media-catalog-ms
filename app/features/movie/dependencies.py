"""
Movie dependencies module.
"""

from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.postgres.database import get_session
from app.features.movie.data.repositories.movie_repository_impl import (
    MovieRepositoryImpl,
)
from app.features.movie.data.repositories.movie_unit_of_work_impl import (
    MovieUnitOfWorkImpl,
)
from app.features.movie.data.services.movie_query_service_impl import (
    MovieQueryServiceImpl,
)
from app.features.movie.domain.repositories.movie_repository import MovieRepository
from app.features.movie.domain.repositories.movie_unit_of_work import MovieUnitOfWork
from app.features.movie.domain.services.movie_query_service import MovieQueryService
from app.features.movie.domain.usecases.create_movie import (
    CreateMovieUseCase,
    CreateMovieUseCaseImpl,
)
from app.features.movie.domain.usecases.delete_movie import (
    DeleteMovieUseCase,
    DeleteMovieUseCaseImpl,
)
from app.features.movie.domain.usecases.get_movie import (
    GetMovieUseCase,
    GetMovieUseCaseImpl,
)
from app.features.movie.domain.usecases.get_movies import (
    GetMoviesUseCase,
    GetMoviesUseCaseImpl,
)
from app.features.movie.domain.usecases.update_movie import (
    UpdateMovieUseCase,
    UpdateMovieUseCaseImpl,
)


def get_movie_query_service(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> MovieQueryService:
    return MovieQueryServiceImpl(session)


def get_movie_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> MovieRepository:
    return MovieRepositoryImpl(session)


async def get_movie_unit_of_work(
    session: Annotated[AsyncSession, Depends(get_session)],
    movie_repository: Annotated[MovieRepository, Depends(get_movie_repository)],
) -> AsyncGenerator[MovieUnitOfWork]:
    async with MovieUnitOfWorkImpl(session, movie_repository) as uow:
        yield uow


def get_create_movie_use_case(
    unit_of_work: Annotated[MovieUnitOfWork, Depends(get_movie_unit_of_work)],
) -> CreateMovieUseCase:
    return CreateMovieUseCaseImpl(unit_of_work)


def get_movie_use_case(
    movie_query_service: Annotated[MovieQueryService, Depends(get_movie_query_service)],
) -> GetMovieUseCase:
    return GetMovieUseCaseImpl(movie_query_service)


def get_movies_use_case(
    movie_query_service: Annotated[MovieQueryService, Depends(get_movie_query_service)],
) -> GetMoviesUseCase:
    return GetMoviesUseCaseImpl(movie_query_service)


def get_update_movie_use_case(
    unit_of_work: Annotated[MovieUnitOfWork, Depends(get_movie_unit_of_work)],
) -> UpdateMovieUseCase:
    return UpdateMovieUseCaseImpl(unit_of_work)


def get_delete_movie_use_case(
    unit_of_work: Annotated[MovieUnitOfWork, Depends(get_movie_unit_of_work)],
) -> DeleteMovieUseCase:
    return DeleteMovieUseCaseImpl(unit_of_work)
