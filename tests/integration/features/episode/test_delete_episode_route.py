"""
Test delete episode route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel


class TestDeleteEpisode:
    """
    API tests for deleting episode.
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

    @pytest.mark.parametrize("run", range(2))
    async def test_delete_episode_success(self, run: int) -> None:
        """
        Delete episode successfully.
        """

        episode = self.created_episodes[run % 2]

        response = await self.ac.delete(f"{self.path}{episode.id_}/")
        assert response.status_code == 200

        response_json = response.json()
        response_episode = EpisodeReadModel.model_validate(response_json)

        assert response_episode.is_deleted

        response = await self.ac.get(f"{self.path}{episode.id_}/")
        assert response.status_code == 404

    async def test_delete_episode_on_conflict(self) -> None:
        """
        Delete episode on conflict.
        """

        id_ = self.created_episodes[0].id_

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 200

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 409

        assert "detail" in response.json()

    async def test_delete_episode_not_found(self) -> None:
        """
        Delete episode not found.
        """

        id_ = uuid7()

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 404

        assert "detail" in response.json()
