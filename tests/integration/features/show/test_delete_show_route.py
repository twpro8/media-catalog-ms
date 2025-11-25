"""
Test delete show route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from app.features.show.domain.entities.show_query_model import ShowReadModel


@pytest.mark.delete_show
class TestDeleteShow:
    """
    API tests for deleting show.
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

    @pytest.mark.parametrize("run", range(2))
    async def test_delete_show_success(self, run: int) -> None:
        """
        Delete show successfully.
        """

        show = self.created_shows[run % 2]

        response = await self.ac.delete(f"{self.path}{show.id_}/")
        assert response.status_code == 200

        response_json = response.json()
        response_show = ShowReadModel.model_validate(response_json)

        assert response_show.is_deleted

        response = await self.ac.get(f"{self.path}{show.id_}/")
        assert response.status_code == 404

    async def test_delete_show_on_conflict(self) -> None:
        """
        Delete show on conflict.
        """

        id_ = self.created_shows[0].id_

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 200

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 409

        assert "detail" in response.json()

    async def test_delete_show_not_found(self) -> None:
        """
        Delete show not found.
        """

        id_ = uuid7()

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 404

        assert "detail" in response.json()
