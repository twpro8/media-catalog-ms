"""
Episode repository module.
"""

from abc import abstractmethod
from uuid import UUID

from app.core.repositories.base_repository import BaseRepository
from app.features.episode.domain.entities.episode_entity import EpisodeEntity


class EpisodeRepository(BaseRepository[EpisodeEntity]):
    """
    EpisodeRepository defines a repository interface for Episode entity.
    """

    @abstractmethod
    async def find_by_season_and_number(
        self, season_id: UUID, episode_number: int
    ) -> EpisodeEntity | None: ...
