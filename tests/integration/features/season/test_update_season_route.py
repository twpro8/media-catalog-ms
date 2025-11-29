"""
Test update season route module.
"""

from typing import Iterator
from uuid import uuid7

import faker
import pytest
from httpx import AsyncClient

from app.features.season.domain.entities.season_command_model import SeasonUpdateModel
from app.features.season.domain.entities.season_query_model import SeasonReadModel


fake = faker.Faker()


class TestUpdateSeason:
    """
    API tests for updating seasons.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_seasons: list[SeasonReadModel],
        season_numbers: Iterator[int],
    ) -> None:
        self.path = "/v1/seasons/"
        self.ac = ac
        self.created_seasons = created_seasons
        self.season_numbers = season_numbers

    @pytest.mark.parametrize("run", range(10))
    async def test_update_success(self, run: int):
        """
        Update season successfully.
        """

        id_ = self.created_seasons[run % 2].id_
        request_season = {
            "title": fake.word(),
            "season_number": next(self.season_numbers),
        }

        response = await self.ac.patch(f"{self.path}{id_}/", json=request_season)
        assert response.status_code == 200

        response_json = response.json()
        SeasonReadModel.model_validate(response_json)

    @pytest.mark.parametrize(
        "field, value",
        [
            ("title", ""),
            ("title", "t" * 257),
            ("title", None),
            ("season_number", 0),
            ("season_number", 10000),
            ("season_number", None),
            ("extra", "Unknow"),
        ],
    )
    async def test_update_fail(self, field: str, value: str) -> None:
        """
        Update season fails.
        """

        id_ = self.created_seasons[0].id_
        request_season = {
            "title": fake.word(),
            "season_number": next(self.season_numbers),
            field: value,
        }

        response = await self.ac.patch(f"{self.path}{id_}/", json=request_season)
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value

    async def test_update_not_found(self):
        """
        Update season not found.
        """

        id_ = uuid7()
        request_season = {
            "title": fake.word(),
            "season_number": next(self.season_numbers),
        }

        response = await self.ac.patch(f"{self.path}{id_}/", json=request_season)
        assert response.status_code == 404

        assert "detail" in response.json()

    async def test_update_conflict(self):
        """
        Update season on conflict.
        """

        season_1 = self.created_seasons[0].model_dump(mode="json")
        season_2 = self.created_seasons[1]

        model = SeasonUpdateModel.model_validate(season_1, extra="ignore")
        request_season = model.model_dump(mode="json")

        response = await self.ac.patch(
            f"{self.path}{season_2.id_}/", json=request_season
        )
        assert response.status_code == 409

        assert "detail" in response.json()
