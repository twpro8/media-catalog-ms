"""
Test get show route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from app.features.show.domain.entities.show_query_model import ShowReadModel


class TestGetShow:
    """
    API tests for getting a show by ID.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_shows: list[ShowReadModel],
    ) -> None:
        self.path = "/v1/shows/"
        self.ac = ac
        self.created_shows = created_shows

    @pytest.mark.parametrize("run", range(5))
    async def test_get_show_success(self, run: int) -> None:
        """
        Get show successfully.
        """

        show = self.created_shows[0]

        response = await self.ac.get(f"{self.path}{show.id_}/")
        assert response.status_code == 200

        response_json = response.json()
        response_show = ShowReadModel.model_validate(response_json)

        assert response_show.id_ == show.id_
        assert response_show.title == show.title
        assert response_show.description == show.description
        assert response_show.release_date == show.release_date

    async def test_get_show_not_found(self):
        """
        Get show not found.
        """

        id_ = uuid7()

        response = await self.ac.get(f"{self.path}{id_}/")
        assert response.status_code == 404

        assert "detail" in response.json()
