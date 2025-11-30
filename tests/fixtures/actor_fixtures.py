"""
Actor fixtures module.
"""

from typing import Sequence

import pytest
from httpx import AsyncClient

from app.features.actor.domain.entities.actor_command_model import (
    ActorCreateModel,
)
from app.features.actor.domain.entities.actor_query_model import ActorReadModel
from tests.factories.actor_factories import ActorCreateModelFactory


@pytest.fixture
async def created_actors(
    ac: AsyncClient,
    actor_create_model: ActorCreateModelFactory,
) -> Sequence[ActorReadModel]:
    actors = []
    for _ in range(2):
        model: ActorCreateModel = actor_create_model.build()
        request_user = model.model_dump(mode="json")

        response = await ac.post(url="/v1/actors", json=request_user)
        assert response.status_code == 201

        actors.append(
            ActorReadModel.model_validate(response.json(), from_attributes=True)
        )

    print(actors)
    return actors
