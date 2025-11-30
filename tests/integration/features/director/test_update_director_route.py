"""
Test update director route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient
import faker

from tests.factories.director_factories import DirectorCreateModelFactory
from app.features.director.domain.entities.director_command_model import (
    DirectorCreateModel,
)
from app.features.director.domain.entities.director_query_model import DirectorReadModel


fake = faker.Faker()


class TestUpdateDirector:
    """
    API tests for updating directors.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        director_create_model: DirectorCreateModelFactory,
    ) -> None:
        self.path = "/v1/directors"
        self.ac = ac
        self.director_create_model = director_create_model

    async def test_update_success(self) -> None:
        """
        Update director successfully (partial update).
        """
        model: DirectorCreateModel = self.director_create_model.build()
        request_director = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_director)
        assert response.status_code == 201
        created_director = DirectorReadModel.model_validate(response.json())

        new_name = fake.first_name()
        update_data = {"first_name": new_name}

        response = await self.ac.patch(
            f"{self.path}/{created_director.id_}", json=update_data
        )
        assert response.status_code == 200

        updated_director = DirectorReadModel.model_validate(response.json())
        assert updated_director.first_name == new_name
        assert updated_director.last_name == created_director.last_name
        assert updated_director.id_ == created_director.id_

    async def test_update_not_found(self) -> None:
        """
        Update director not found should return 404.
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
        Invalid director update should return 422.
        """
        model: DirectorCreateModel = self.director_create_model.build()
        request_director = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_director)
        assert response.status_code == 201
        created_director = DirectorReadModel.model_validate(response.json())

        update_data = {field: value}

        response = await self.ac.patch(
            f"{self.path}/{created_director.id_}", json=update_data
        )
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value
