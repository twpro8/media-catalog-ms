"""
Test get actor route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from tests.factories.actor_factories import ActorCreateModelFactory
from app.features.actor.domain.entities.actor_command_model import (
    ActorCreateModel,
)
from app.features.actor.domain.entities.actor_query_model import ActorReadModel


class TestGetActor:
    """
    API tests for getting a actor.
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

    async def test_get_success(self) -> None:
        """
        Get actor successfully.
        """
        model: ActorCreateModel = self.actor_create_model.build()
        request_actor = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_actor)
        assert response.status_code == 201
        created_actor = ActorReadModel.model_validate(response.json())

        response = await self.ac.get(f"{self.path}/{created_actor.id_}")
        assert response.status_code == 200

        response_json = response.json()
        fetched_actor = ActorReadModel.model_validate(response_json)

        assert created_actor == fetched_actor

    async def test_get_not_found(self) -> None:
        """
        Get actor not found should return 404.
        """
        response = await self.ac.get(f"{self.path}/{uuid7()}")
        assert response.status_code == 404
