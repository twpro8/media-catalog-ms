"""
Test get episodes route module.
"""

import pytest
from httpx import AsyncClient

from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel


class TestGetEpisodes:
    """
    API tests for getting episodes.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_episodes: list[EpisodeReadModel],
    ) -> None:
        self.path = "/v1/episodes"
        self.ac = ac
        self.created_episodes = created_episodes

    @pytest.mark.parametrize("run", range(2))
    async def test_get_episodes_success(self, run: int) -> None:
        """
        Get episodes successfully.
        """

        response = await self.ac.get(self.path)
        assert response.status_code == 200

        response_json = response.json()
        assert len(response_json) > 1
        [EpisodeReadModel.model_validate(episode) for episode in response_json]
