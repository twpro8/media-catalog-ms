"""
Show fixtures module.
"""

from typing import Sequence

import pytest
from httpx import AsyncClient

from app.features.show.domain.entities.show_command_model import ShowCreateModel
from app.features.show.domain.entities.show_query_model import ShowReadModel
from tests.factories.show_factories import ShowCreateModelFactory


@pytest.fixture
async def created_shows(
    ac: AsyncClient,
    show_create_model: ShowCreateModelFactory,
) -> Sequence[ShowReadModel]:
    shows = []
    for _ in range(2):
        model: ShowCreateModel = show_create_model.build()
        request_user = model.model_dump(mode="json")

        response = await ac.post(url="/v1/shows", json=request_user)
        assert response.status_code == 201

        shows.append(
            ShowReadModel.model_validate(response.json(), from_attributes=True)
        )

    return shows
