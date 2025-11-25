"""
Test update show route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from app.features.show.domain.entities.show_command_model import ShowUpdateModel
from app.features.show.domain.entities.show_query_model import ShowReadModel
from tests.factories.show_factories import ShowUpdateModelFactory


@pytest.mark.update_show
class TestUpdateShow:
    """
    API tests for updating shows.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        show_update_model: ShowUpdateModelFactory,
        created_shows: list[ShowReadModel],
    ) -> None:
        self.path = "/v1/shows/"
        self.ac = ac
        self.show_update_model = show_update_model
        self.created_shows = created_shows

    @pytest.mark.parametrize("run", range(10))
    async def test_update_success(self, run: int):
        """
        Update show successfully.
        """

        id_ = self.created_shows[run % 2].id_

        model: ShowUpdateModel = self.show_update_model.build()
        request_user = model.model_dump(mode="json")

        response = await self.ac.patch(f"{self.path}{id_}/", json=request_user)
        assert response.status_code == 200

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
            ("extra", "Unknow"),
        ],
    )
    async def test_update_fail(self, field: str, value: str) -> None:
        """
        Update show fails.
        """

        id_ = self.created_shows[0].id_

        model: ShowUpdateModel = self.show_update_model.build()
        request_user = model.model_dump(mode="json")
        request_user |= {field: value}

        response = await self.ac.patch(f"{self.path}{id_}/", json=request_user)
        assert response.status_code == 422

        response_detail = response.json()["detail"]
        error_field = response_detail[0]["loc"][1]
        error_input_value = response_detail[0]["input"]

        assert error_field == field
        assert error_input_value == value

    async def test_update_not_found(self):
        """
        Update show not found.
        """

        id_ = uuid7()

        model: ShowUpdateModel = self.show_update_model.build()
        request_user = model.model_dump(mode="json")

        response = await self.ac.patch(f"{self.path}{id_}/", json=request_user)
        assert response.status_code == 404

        assert "detail" in response.json()

    async def test_update_conflict(self):
        """
        Update show on conflict.
        """

        show_1 = self.created_shows[0].model_dump(mode="json")
        show_2 = self.created_shows[1]

        model = ShowUpdateModel.model_validate(show_1, extra="ignore")
        request_user = model.model_dump(mode="json")

        response = await self.ac.patch(f"{self.path}{show_2.id_}/", json=request_user)
        assert response.status_code == 409

        assert "detail" in response.json()
