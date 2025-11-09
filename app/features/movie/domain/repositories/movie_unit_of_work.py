"""
Movie unit of work module.
"""

from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.movie.domain.repositories.movie_repository import MovieRepository


class MovieUnitOfWork(AbstractUnitOfWork[MovieRepository]):
    """
    MovieUnitOfWork defines an interface based on Unit of Work.
    """

    pass
