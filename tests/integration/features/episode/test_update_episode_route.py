"""
Test update episode route module.
"""

from typing import Iterator
from uuid import uuid7

import faker
import pytest
from httpx import AsyncClient

from app.features.episode.domain.entities.episode_command_model import (
    EpisodeUpdateModel,
)
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from datetime import date


fake = faker.Faker()


class TestUpdateEpisode:
    """
    API tests for updating episodes.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_episodes: list[EpisodeReadModel],
        episode_numbers: Iterator[int],
    ) -> None:
        self.path = "/v1/episodes"
        self.ac = ac
        self.created_episodes = created_episodes
        self.episode_numbers = episode_numbers

    @pytest.mark.parametrize("run", range(10))
    async def test_update_success(self, run: int):
        """
        Update episode successfully.
        """

        id_ = self.created_episodes[run % 2].id_
        request_episode = {
            "title": fake.word(),
            "episode_number": next(self.episode_numbers),
            "release_date": date.today().isoformat(),
            "duration": 45,
        }

        response = await self.ac.patch(f"{self.path}/{id_}", json=request_episode)
        assert response.status_code == 200

        response_json = response.json()
        EpisodeReadModel.model_validate(response_json)

    @pytest.mark.parametrize(
        "field, value",
        [
            ("title", ""),
            ("title", "t" * 257),
            ("title", None),
            ("episode_number", 0),
            ("episode_number", 10000),
            ("episode_number", None),
            ("release_date", "999-01-01"),
            ("release_date", "2200-01-01"),
            ("release_date", None),
            ("duration", 0),
            ("duration", 10000),
            ("extra", "Unknown"),
        ],
    )
    async def test_update_fail(self, field: str, value: str) -> None:
        """
        Update episode fails.
        """

        id_ = self.created_episodes[0].id_
        request_episode = {
            "title": fake.word(),
            "episode_number": next(self.episode_numbers),
            "release_date": date.today().isoformat(),
            "duration": 45,
            field: value,
        }

        response = await self.ac.patch(f"{self.path}/{id_}", json=request_episode)
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value

    async def test_update_not_found(self):
        """
        Update episode not found.
        """

        id_ = uuid7()
        request_episode = {
            "title": fake.word(),
            "episode_number": next(self.episode_numbers),
            "release_date": date.today().isoformat(),
            "duration": 45,
        }

        response = await self.ac.patch(f"{self.path}/{id_}", json=request_episode)
        assert response.status_code == 404

        assert "detail" in response.json()

    async def test_update_conflict(self):
        """
        Update episode on conflict.
        """

        episode_1 = self.created_episodes[0].model_dump(mode="json")
        episode_2 = self.created_episodes[1]

        model = EpisodeUpdateModel.model_validate(episode_1, extra="ignore")
        request_episode = model.model_dump(mode="json")

        response = await self.ac.patch(
            f"{self.path}/{episode_2.id_}", json=request_episode
        )
        assert response.status_code == 409

        assert "detail" in response.json()
