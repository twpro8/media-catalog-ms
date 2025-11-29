"""
Test get episode route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel


class TestGetEpisode:
    """
    API tests for getting an episode by ID.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_episodes: list[EpisodeReadModel],
    ) -> None:
        self.path = "/v1/episodes/"
        self.ac = ac
        self.created_episodes = created_episodes

    @pytest.mark.parametrize("run", range(5))
    async def test_get_episode_success(self, run: int) -> None:
        """
        Get episode successfully.
        """

        episode = self.created_episodes[0]

        response = await self.ac.get(f"{self.path}{episode.id_}/")
        assert response.status_code == 200

        response_json = response.json()
        response_episode = EpisodeReadModel.model_validate(response_json)

        assert response_episode.id_ == episode.id_
        assert response_episode.season_id == episode.season_id
        assert response_episode.title == episode.title
        assert response_episode.episode_number == episode.episode_number

    async def test_get_episode_not_found(self):
        """
        Get episode not found.
        """

        id_ = uuid7()

        response = await self.ac.get(f"{self.path}{id_}/")
        assert response.status_code == 404

        assert "detail" in response.json()
