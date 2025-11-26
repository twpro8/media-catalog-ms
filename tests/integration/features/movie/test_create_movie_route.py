"""
Test create movie route module.
"""

from datetime import date

import pytest
from httpx import AsyncClient
import faker

from tests.factories.movie_factories import MovieCreateModelFactory
from app.features.movie.domain.entities.movie_command_model import MovieCreateModel
from app.features.movie.domain.entities.movie_query_model import MovieReadModel


fake = faker.Faker()


class TestCreateMovie:
    """
    API tests for creating movies.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        movie_create_model: MovieCreateModelFactory,
    ) -> None:
        self.path = "/v1/movies/"
        self.ac = ac
        self.movie_create_model = movie_create_model

    @pytest.mark.parametrize("run", range(10))
    async def test_create_success(self, run) -> None:
        """
        Create movie successfully.
        """

        model: MovieCreateModel = self.movie_create_model.build()
        request_movie = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_movie)
        assert response.status_code == 201

        response_json = response.json()
        MovieReadModel.model_validate(response_json)

    @pytest.mark.parametrize(
        "field, value",
        [
            ("title", ""),
            ("title", "t" * 257),
            ("description", ""),
            ("description", "d" * 1025),
            ("release_date", "999-01-01"),
            ("release_date", "2100-01-01"),
            ("duration", 0),
            ("duration", 10000),
        ],
    )
    async def test_create_fail(self, field: str, value: str) -> None:
        """
        Invalid movie creation should return 422.
        """

        request_movie = {
            "title": fake.word(),
            "description": fake.word(),
            "release_date": date.today().isoformat(),
            "duration": 70,
            field: value,
        }

        response = await self.ac.post(self.path, json=request_movie)
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value

    async def test_create_conflict(self):
        """
        Creating duplicate movie should return 409.
        """

        model: MovieCreateModel = self.movie_create_model.build()
        request_movie = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_movie)
        assert response.status_code == 201

        response = await self.ac.post(self.path, json=request_movie)
        assert response.status_code == 409
        assert "detail" in response.json()
