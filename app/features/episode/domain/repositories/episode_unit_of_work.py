"""
Episode unit of work module.
"""

from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.episode.domain.repositories.episode_repository import (
    EpisodeRepository,
)
from app.features.season.domain.repositories.season_repository import SeasonRepository


class EpisodeUnitOfWork(AbstractUnitOfWork):
    """
    EpisodeUnitOfWork defines a unit of work interface for Episode entity.
    """

    episodes: EpisodeRepository
    seasons: SeasonRepository
