"""
Movie query service module.
"""

from app.core.services.base_query_service import QueryService
from app.features.movie.domain.entities.movie_query_model import MovieReadModel


class MovieQueryService(QueryService[MovieReadModel]):
    """
    MovieQueryService defines a query service interface..
    """

    pass
