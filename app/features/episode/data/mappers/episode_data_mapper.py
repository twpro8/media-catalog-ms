"""
Episode data mapper module.
"""

from app.core.repositories.data_mapper import DataMapper
from app.features.episode.domain.entities.episode_entity import EpisodeEntity
from app.features.episode.data.models.episode import Episode


class EpisodeDataMapper(DataMapper):
    """
    EpisodeDataMapper defines a data mapper between Episode entity and Episode ORM model.
    """

    model = Episode
    entity = EpisodeEntity
