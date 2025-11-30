"""
Test get movies route module.
"""

import pytest
from httpx import AsyncClient

from app.features.movie.domain.entities.movie_query_model import MovieReadModel


class TestGetMovies:
    """
    API tests for getting movies.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_movies: list[MovieReadModel],
    ) -> None:
        self.path = "/v1/movies"
        self.ac = ac
        self.created_movies = created_movies

    @pytest.mark.parametrize("run", range(2))
    async def test_get_movies_success(self, run: int) -> None:
        """
        Get movies successfully.
        """

        response = await self.ac.get(self.path)
        assert response.status_code == 200

        response_json = response.json()
        assert len(response_json) > 1
        [MovieReadModel.model_validate(movie) for movie in response_json]
