"""
Director fixtures module.
"""

from typing import Sequence

import pytest
from httpx import AsyncClient

from app.features.director.domain.entities.director_command_model import (
    DirectorCreateModel,
)
from app.features.director.domain.entities.director_query_model import DirectorReadModel
from tests.factories.director_factories import DirectorCreateModelFactory


@pytest.fixture
async def created_directors(
    ac: AsyncClient,
    director_create_model: DirectorCreateModelFactory,
) -> Sequence[DirectorReadModel]:
    directors = []
    for _ in range(2):
        model: DirectorCreateModel = director_create_model.build()
        request_user = model.model_dump(mode="json")

        response = await ac.post(url="/v1/directors", json=request_user)
        assert response.status_code == 201

        directors.append(
            DirectorReadModel.model_validate(response.json(), from_attributes=True)
        )

    print(directors)
    return directors
