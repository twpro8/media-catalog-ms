"""
Episode unit of work implementation module.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.unit_of_work.sqlalchemy.unit_of_work import SQLAlchemyUnitOfWork
from app.features.episode.domain.repositories.episode_repository import (
    EpisodeRepository,
)
from app.features.episode.domain.repositories.episode_unit_of_work import (
    EpisodeUnitOfWork,
)
from app.features.season.domain.repositories.season_repository import SeasonRepository


class EpisodeUnitOfWorkImpl(SQLAlchemyUnitOfWork, EpisodeUnitOfWork):
    """
    EpisodeUnitOfWorkImpl implements a unit of work related to the Episode entity.
    """

    def __init__(
        self,
        session: AsyncSession,
        episode_repository: EpisodeRepository,
        season_repository: SeasonRepository,
    ):
        super().__init__(session)
        self.episodes = episode_repository
        self.seasons = season_repository
