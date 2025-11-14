"""
Movie fixtures module.
"""

from typing import Sequence

import pytest
from httpx import AsyncClient

from app.features.movie.domain.entities.movie_command_model import MovieCreateModel
from app.features.movie.domain.entities.movie_query_model import MovieReadModel
from tests.factories.movie_factories import MovieCreateModelFactory


@pytest.fixture
async def created_movies(
    ac: AsyncClient,
    movie_create_model: MovieCreateModelFactory,
) -> Sequence[MovieReadModel]:
    movies = []
    for _ in range(2):
        model: MovieCreateModel = movie_create_model.build()
        request_user = model.model_dump(mode="json")

        response = await ac.post(url="/v1/movies/", json=request_user)
        assert response.status_code == 201

        movies.append(
            MovieReadModel.model_validate(response.json(), from_attributes=True)
        )

    return movies
