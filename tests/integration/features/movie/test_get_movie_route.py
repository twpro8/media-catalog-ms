"""
Test get movie route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from app.features.movie.domain.entities.movie_query_model import MovieReadModel


class TestGetMovie:
    """
    API tests for getting a movie by ID.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_movies: list[MovieReadModel],
    ) -> None:
        self.path = "/v1/movies/"
        self.ac = ac
        self.created_movies = created_movies

    @pytest.mark.parametrize("run", range(5))
    async def test_get_movie_success(self, run: int) -> None:
        """
        Get movie successfully.
        """

        movie = self.created_movies[0]

        response = await self.ac.get(f"{self.path}{movie.id_}/")
        assert response.status_code == 200

        response_json = response.json()
        response_movie = MovieReadModel.model_validate(response_json)

        assert response_movie.id_ == movie.id_
        assert response_movie.title == movie.title
        assert response_movie.description == movie.description
        assert response_movie.release_date == movie.release_date

    async def test_get_movie_not_found(self):
        """
        Get movie not found.
        """

        id_ = uuid7()

        response = await self.ac.get(f"{self.path}{id_}/")
        assert response.status_code == 404

        assert "detail" in response.json()
