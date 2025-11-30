"""
Test create actor route module.
"""

import pytest
from httpx import AsyncClient
import faker

from tests.factories.actor_factories import ActorCreateModelFactory
from app.features.actor.domain.entities.actor_command_model import (
    ActorCreateModel,
)
from app.features.actor.domain.entities.actor_query_model import ActorReadModel


fake = faker.Faker()


class TestCreateActor:
    """
    API tests for creating actors.
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

    @pytest.mark.parametrize("run", range(5))
    async def test_create_success(self, run) -> None:
        """
        Create actor successfully.
        """

        model: ActorCreateModel = self.actor_create_model.build()
        request_actor = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_actor)
        assert response.status_code == 201

        response_json = response.json()
        ActorReadModel.model_validate(response_json)

    @pytest.mark.parametrize(
        "field, value",
        [
            ("first_name", ""),
            ("first_name", "t" * 49),
            ("last_name", ""),
            ("last_name", "t" * 49),
            ("birth_date", "1900-01-01"),
            ("birth_date", "2200-01-01"),
            ("bio", "t"),
            ("bio", "t" * 1025),
            ("extra", "Unknown"),
        ],
    )
    async def test_create_fail(self, field: str, value: str) -> None:
        """
        Invalid actor creation should return 422.
        """
        model: ActorCreateModel = self.actor_create_model.build()
        request_actor = model.model_dump(mode="json")
        request_actor[field] = value

        response = await self.ac.post(self.path, json=request_actor)
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value

    async def test_create_conflict(self):
        """
        Creating duplicate actor should return 409.
        """
        model: ActorCreateModel = self.actor_create_model.build()
        request_actor = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_actor)
        assert response.status_code == 201

        response = await self.ac.post(self.path, json=request_actor)
        assert response.status_code == 409
