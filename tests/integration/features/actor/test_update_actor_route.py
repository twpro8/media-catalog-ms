"""
Test update actor route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient
import faker

from tests.factories.actor_factories import ActorCreateModelFactory
from app.features.actor.domain.entities.actor_command_model import (
    ActorCreateModel,
)
from app.features.actor.domain.entities.actor_query_model import ActorReadModel


fake = faker.Faker()


class TestUpdateActor:
    """
    API tests for updating actors.
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

    async def test_update_success(self) -> None:
        """
        Update actor successfully (partial update).
        """
        model: ActorCreateModel = self.actor_create_model.build()
        request_actor = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_actor)
        assert response.status_code == 201
        created_actor = ActorReadModel.model_validate(response.json())

        new_name = fake.first_name()
        update_data = {"first_name": new_name}

        response = await self.ac.patch(
            f"{self.path}/{created_actor.id_}", json=update_data
        )
        assert response.status_code == 200

        updated_actor = ActorReadModel.model_validate(response.json())
        assert updated_actor.first_name == new_name
        assert updated_actor.last_name == created_actor.last_name
        assert updated_actor.id_ == created_actor.id_

    async def test_update_not_found(self) -> None:
        """
        Update actor not found should return 404.
        """
        response = await self.ac.patch(
            f"{self.path}/{uuid7()}", json={"first_name": "New"}
        )
        assert response.status_code == 404

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
    async def test_update_fail(self, field: str, value: str) -> None:
        """
        Invalid actor update should return 422.
        """
        model: ActorCreateModel = self.actor_create_model.build()
        request_actor = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_actor)
        assert response.status_code == 201
        created_actor = ActorReadModel.model_validate(response.json())

        update_data = {field: value}

        response = await self.ac.patch(
            f"{self.path}/{created_actor.id_}", json=update_data
        )
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value
