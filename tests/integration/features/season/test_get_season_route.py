"""
Test get season route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from app.features.season.domain.entities.season_query_model import SeasonReadModel


class TestGetSeason:
    """
    API tests for getting a season by ID.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        created_seasons: list[SeasonReadModel],
    ) -> None:
        self.path = "/v1/seasons"
        self.ac = ac
        self.created_seasons = created_seasons

    @pytest.mark.parametrize("run", range(5))
    async def test_get_season_success(self, run: int) -> None:
        """
        Get season successfully.
        """

        season = self.created_seasons[0]

        response = await self.ac.get(f"{self.path}/{season.id_}")
        assert response.status_code == 200

        response_json = response.json()
        response_season = SeasonReadModel.model_validate(response_json)

        assert response_season.id_ == season.id_
        assert response_season.show_id == season.show_id
        assert response_season.title == season.title
        assert response_season.season_number == season.season_number

    async def test_get_season_not_found(self):
        """
        Get season not found.
        """

        id_ = uuid7()

        response = await self.ac.get(f"{self.path}/{id_}")
        assert response.status_code == 404

        assert "detail" in response.json()
