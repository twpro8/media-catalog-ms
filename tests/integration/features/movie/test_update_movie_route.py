"""
Test update movie route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from app.features.movie.domain.entities.movie_command_model import MovieUpdateModel
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from tests.factories.movie_factories import MovieUpdateModelFactory


class TestUpdateMovie:
    """
    API tests for updating movies.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        movie_update_model: MovieUpdateModelFactory,
        created_movies: list[MovieReadModel],
    ) -> None:
        self.path = "/v1/movies/"
        self.ac = ac
        self.movie_update_model = movie_update_model
        self.created_movies = created_movies

    @pytest.mark.parametrize("run", range(10))
    async def test_update_success(self, run: int):
        """
        Update movie successfully.
        """

        id_ = self.created_movies[run % 2].id_

        model: MovieUpdateModel = self.movie_update_model.build()
        request_movie = model.model_dump(mode="json")

        response = await self.ac.patch(f"{self.path}{id_}/", json=request_movie)
        assert response.status_code == 200

        response_json = response.json()
        MovieReadModel.model_validate(response_json)

    @pytest.mark.parametrize(
        "field, value",
        [
            ("title", ""),
            ("title", "t" * 257),
            ("title", None),
            ("description", ""),
            ("description", "d" * 1025),
            ("description", None),
            ("release_date", "999-01-01"),
            ("release_date", "2100-01-01"),
            ("release_date", None),
            ("duration", 0),
            ("duration", 10000),
            ("extra", "Unknow"),
        ],
    )
    async def test_update_fail(self, field: str, value: str) -> None:
        """
        Update movie fails.
        """

        id_ = self.created_movies[0].id_

        model: MovieUpdateModel = self.movie_update_model.build()
        request_movie = model.model_dump(mode="json")
        request_movie |= {field: value}

        response = await self.ac.patch(f"{self.path}{id_}/", json=request_movie)
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value

    async def test_update_not_found(self):
        """
        Update movie not found.
        """

        id_ = uuid7()

        model: MovieUpdateModel = self.movie_update_model.build()
        request_movie = model.model_dump(mode="json")

        response = await self.ac.patch(f"{self.path}{id_}/", json=request_movie)
        assert response.status_code == 404

        assert "detail" in response.json()

    async def test_update_conflict(self):
        """
        Update movie on conflict.
        """

        movie_1 = self.created_movies[0].model_dump(mode="json")
        movie_2 = self.created_movies[1]

        model = MovieUpdateModel.model_validate(movie_1, extra="ignore")
        request_movie = model.model_dump(mode="json")

        response = await self.ac.patch(f"{self.path}{movie_2.id_}/", json=request_movie)
        assert response.status_code == 409

        assert "detail" in response.json()
