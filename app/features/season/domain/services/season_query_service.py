"""
Season query service module.
"""

from app.core.services.base_query_service import QueryService
from app.features.season.domain.entities.season_query_model import SeasonReadModel


class SeasonQueryService(QueryService[SeasonReadModel]):
    """
    SeasonQueryService defines a query service interface.
    """

    pass
