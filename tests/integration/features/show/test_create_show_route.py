"""
Test create show route module.
"""

from datetime import date

import pytest
from httpx import AsyncClient
import faker

from tests.factories.show_factories import ShowCreateModelFactory
from app.features.show.domain.entities.show_command_model import ShowCreateModel
from app.features.show.domain.entities.show_query_model import ShowReadModel


fake = faker.Faker()


class TestCreateShow:
    """
    API tests for creating shows.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        show_create_model: ShowCreateModelFactory,
    ) -> None:
        self.path = "/v1/shows"
        self.ac = ac
        self.show_create_model = show_create_model

    @pytest.mark.parametrize("run", range(5))
    async def test_create_success(self, run) -> None:
        """
        Create show successfully.
        """

        model: ShowCreateModel = self.show_create_model.build()
        request_show = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_show)
        assert response.status_code == 201

        response_json = response.json()
        ShowReadModel.model_validate(response_json)

    @pytest.mark.parametrize(
        "field, value",
        [
            ("title", ""),
            ("title", "t" * 257),
            ("description", ""),
            ("description", "d" * 1025),
            ("release_date", "999-01-01"),
            ("release_date", "2100-01-01"),
        ],
    )
    async def test_create_fail(self, field: str, value: str) -> None:
        """
        Invalid show creation should return 422.
        """

        request_show = {
            "title": fake.word(),
            "description": fake.word(),
            "release_date": date.today().isoformat(),
            field: value,
        }

        response = await self.ac.post(self.path, json=request_show)
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value

    async def test_create_conflict(self):
        """
        Creating duplicate show should return 409.
        """

        model: ShowCreateModel = self.show_create_model.build()
        request_show = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_show)
        assert response.status_code == 201

        response = await self.ac.post(self.path, json=request_show)
        assert response.status_code == 409
        assert "detail" in response.json()
