"""
Test delete season route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from app.features.season.domain.entities.season_query_model import SeasonReadModel


class TestDeleteSeason:
    """
    API tests for deleting season.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_seasons: list[SeasonReadModel],
    ) -> None:
        self.path = "/v1/seasons/"
        self.ac = ac
        self.created_seasons = created_seasons

    @pytest.mark.parametrize("run", range(2))
    async def test_delete_season_success(self, run: int) -> None:
        """
        Delete season successfully.
        """

        season = self.created_seasons[run % 2]

        response = await self.ac.delete(f"{self.path}{season.id_}/")
        assert response.status_code == 200

        response_json = response.json()
        response_season = SeasonReadModel.model_validate(response_json)

        assert response_season.is_deleted

        response = await self.ac.get(f"{self.path}{season.id_}/")
        assert response.status_code == 404

    async def test_delete_season_on_conflict(self) -> None:
        """
        Delete season on conflict.
        """

        id_ = self.created_seasons[0].id_

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 200

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 409

        assert "detail" in response.json()

    async def test_delete_season_not_found(self) -> None:
        """
        Delete season not found.
        """

        id_ = uuid7()

        response = await self.ac.delete(f"{self.path}{id_}/")
        assert response.status_code == 404

        assert "detail" in response.json()
