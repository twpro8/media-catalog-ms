"""
Director query service module.
"""

from app.core.services.base_query_service import QueryService
from app.features.director.domain.entities.director_query_model import DirectorReadModel


class DirectorQueryService(QueryService[DirectorReadModel]):
    """
    DirectorQueryService defines a query service interface..
    """

    pass
