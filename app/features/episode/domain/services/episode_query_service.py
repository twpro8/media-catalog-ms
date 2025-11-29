"""
Episode query service module.
"""

from app.core.services.base_query_service import QueryService
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel


class EpisodeQueryService(QueryService[EpisodeReadModel]):
    """
    EpisodeQueryService defines a query service interface.
    """

    pass
