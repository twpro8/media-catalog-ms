"""
Test delete movie route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from app.features.movie.domain.entities.movie_query_model import MovieReadModel


class TestDeleteMovie:
    """
    API tests for deleting movie.
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

    @pytest.mark.parametrize("run", range(2))
    async def test_delete_movie_success(self, run: int) -> None:
        """
        Delete movie successfully.
        """

        movie = self.created_movies[run % 2]

        response = await self.ac.delete(f"{self.path}{movie.id_}/")
        assert response.status_code == 200

        response_json = response.json()
        response_movie = MovieReadModel.model_validate(response_json)

        assert response_movie.is_deleted

        response = await self.ac.get(f"{self.path}{movie.id_}/")
        assert response.status_code == 404

    async def test_delete_movie_on_conflict(self) -> None:
        """
        Delete movie on conflict.
        """

        id_ = self.created_movies[0].id_

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 200

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 409

        assert "detail" in response.json()

    async def test_delete_movie_not_found(self) -> None:
        """
        Delete movie not found.
        """

        id_ = uuid7()

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 404

        assert "detail" in response.json()
