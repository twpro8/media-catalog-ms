"""
Test create season route module.
"""

from typing import Iterator
from uuid import uuid7

import pytest
from httpx import AsyncClient
import faker

from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.season.domain.entities.season_query_model import SeasonReadModel


fake = faker.Faker()


class TestCreateSeason:
    """
    API tests for creating seasons.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_shows: list[ShowReadModel],
        season_numbers: Iterator[int],
    ) -> None:
        self.path = "/v1/seasons"
        self.ac = ac
        self.season_numbers = season_numbers
        self.created_shows = created_shows

    @pytest.mark.parametrize("run", range(10))
    async def test_create_success(self, run: int) -> None:
        """
        Create season successfully.
        """
        show_id = str(self.created_shows[run % 2].id_)
        request_season = {
            "show_id": show_id,
            "title": fake.word(),
            "season_number": next(self.season_numbers),
        }

        response = await self.ac.post(self.path, json=request_season)
        assert response.status_code == 201

        response_json = response.json()
        SeasonReadModel.model_validate(response_json)

    @pytest.mark.parametrize(
        "field, value",
        [
            ("title", ""),
            ("title", "t" * 257),
            ("season_number", 0),
            ("season_number", 9999),
        ],
    )
    async def test_create_fail(self, field: str, value: str) -> None:
        """
        Invalid season creation should return 422.
        """

        show_id = str(self.created_shows[0].id_)
        request_season = {
            "show_id": show_id,
            "title": fake.word(),
            "season_number": next(self.season_numbers),
            field: value,
        }

        response = await self.ac.post(self.path, json=request_season)
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value

    async def test_create_show_not_found(self):
        """
        Show not found should return 404.
        """

        response = await self.ac.post(
            self.path,
            json={
                "show_id": str(uuid7()),
                "title": fake.word(),
                "season_number": next(self.season_numbers),
            },
        )
        assert response.status_code == 404
        assert "detail" in response.json()

    async def test_create_conflict(self):
        """
        Creating duplicate season should return 409.
        """

        show_id = str(self.created_shows[0].id_)
        request_season = {
            "show_id": show_id,
            "title": fake.word(),
            "season_number": next(self.season_numbers),
        }

        response = await self.ac.post(self.path, json=request_season)
        assert response.status_code == 201

        response = await self.ac.post(self.path, json=request_season)
        assert response.status_code == 409
        assert "detail" in response.json()
