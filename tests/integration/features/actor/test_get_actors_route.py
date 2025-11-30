"""
Test get actors route module.
"""

import pytest
from httpx import AsyncClient

from tests.factories.actor_factories import ActorCreateModelFactory
from app.features.actor.domain.entities.actor_command_model import (
    ActorCreateModel,
)
from app.features.actor.domain.entities.actor_query_model import ActorReadModel


class TestGetActors:
    """
    API tests for getting actors.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        actor_create_model: ActorCreateModelFactory,
    ) -> None:
        self.path = "/v1/actors"
        self.ac = ac
        self.actor_create_model = actor_create_model

    async def test_get_all_success(self) -> None:
        """
        Get all actors successfully.
        """
        # Create a actor first
        model: ActorCreateModel = self.actor_create_model.build()
        request_actor = model.model_dump(mode="json")
        await self.ac.post(self.path, json=request_actor)

        response = await self.ac.get(self.path)
        assert response.status_code == 200

        response_json = response.json()
        assert len(response_json) > 0
        for actor in response_json:
            ActorReadModel.model_validate(actor)
