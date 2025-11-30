"""
Test create episode route module.
"""

from typing import Iterator
from uuid import uuid7
from datetime import date

import pytest
from httpx import AsyncClient
import faker

from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel


fake = faker.Faker()


class TestCreateEpisode:
    """
    API tests for creating episodes.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_seasons: list[SeasonReadModel],
        episode_numbers: Iterator[int],
    ) -> None:
        self.path = "/v1/episodes"
        self.ac = ac
        self.episode_numbers = episode_numbers
        self.created_seasons = created_seasons

    @pytest.mark.parametrize("run", range(5))
    async def test_create_success(self, run: int) -> None:
        """
        Create episode successfully.
        """
        season_id = str(self.created_seasons[run % 2].id_)
        request_episode = {
            "season_id": season_id,
            "title": fake.word(),
            "episode_number": next(self.episode_numbers),
            "release_date": date.today().isoformat(),
            "duration": 60,
        }

        response = await self.ac.post(self.path, json=request_episode)
        assert response.status_code == 201

        response_json = response.json()
        EpisodeReadModel.model_validate(response_json)

    @pytest.mark.parametrize(
        "field, value",
        [
            ("title", ""),
            ("title", "t" * 257),
            ("episode_number", 0),
            ("episode_number", 9999),
            ("release_date", "999-01-01"),
            ("release_date", "2200-01-01"),
            ("duration", 0),
            ("duration", 10000),
        ],
    )
    async def test_create_fail(self, field: str, value: str) -> None:
        """
        Invalid episode creation should return 422.
        """

        season_id = str(self.created_seasons[0].id_)
        request_episode = {
            "season_id": season_id,
            "title": fake.word(),
            "episode_number": next(self.episode_numbers),
            "release_date": date.today().isoformat(),
            "duration": 60,
            field: value,
        }

        response = await self.ac.post(self.path, json=request_episode)
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value

    async def test_create_season_not_found(self):
        """
        Season not found should return 404.
        """

        response = await self.ac.post(
            self.path,
            json={
                "season_id": str(uuid7()),
                "title": fake.word(),
                "episode_number": next(self.episode_numbers),
                "release_date": date.today().isoformat(),
                "duration": 60,
            },
        )
        assert response.status_code == 404

    async def test_create_conflict(self):
        """
        Creating duplicate episode should return 409.
        """

        season_id = str(self.created_seasons[0].id_)
        request_episode = {
            "season_id": season_id,
            "title": fake.word(),
            "episode_number": next(self.episode_numbers),
            "release_date": date.today().isoformat(),
            "duration": 60,
        }

        response = await self.ac.post(self.path, json=request_episode)
        assert response.status_code == 201

        response = await self.ac.post(self.path, json=request_episode)
        assert response.status_code == 409
