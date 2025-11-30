"""
Test create director route module.
"""

import pytest
from httpx import AsyncClient
import faker

from tests.factories.director_factories import DirectorCreateModelFactory
from app.features.director.domain.entities.director_command_model import (
    DirectorCreateModel,
)
from app.features.director.domain.entities.director_query_model import DirectorReadModel


fake = faker.Faker()


class TestCreateDirector:
    """
    API tests for creating directors.
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

    @pytest.mark.parametrize("run", range(5))
    async def test_create_success(self, run) -> None:
        """
        Create director successfully.
        """

        model: DirectorCreateModel = self.director_create_model.build()
        request_director = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_director)
        assert response.status_code == 201

        response_json = response.json()
        DirectorReadModel.model_validate(response_json)

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
        Invalid director creation should return 422.
        """
        model: DirectorCreateModel = self.director_create_model.build()
        request_director = model.model_dump(mode="json")
        request_director[field] = value

        response = await self.ac.post(self.path, json=request_director)
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value

    async def test_create_conflict(self):
        """
        Creating duplicate director should return 409.
        """
        model: DirectorCreateModel = self.director_create_model.build()
        request_director = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_director)
        assert response.status_code == 201

        response = await self.ac.post(self.path, json=request_director)
        assert response.status_code == 409
