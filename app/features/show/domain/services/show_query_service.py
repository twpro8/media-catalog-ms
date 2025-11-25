"""
Show query service module.
"""

from app.core.services.base_query_service import QueryService
from app.features.show.domain.entities.show_query_model import ShowReadModel


class ShowQueryService(QueryService[ShowReadModel]):
    """
    ShowQueryService defines a query service interface.
    """

    pass
