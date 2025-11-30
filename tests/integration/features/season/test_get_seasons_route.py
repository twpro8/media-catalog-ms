"""
Test get seasons route module.
"""

import pytest
from httpx import AsyncClient

from app.features.season.domain.entities.season_query_model import SeasonReadModel


class TestGetSeasons:
    """
    API tests for getting seasons.
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

    @pytest.mark.parametrize("run", range(2))
    async def test_get_seasons_success(self, run: int) -> None:
        """
        Get seasons successfully.
        """

        response = await self.ac.get(self.path)
        assert response.status_code == 200

        response_json = response.json()
        assert len(response_json) > 1
        [SeasonReadModel.model_validate(season) for season in response_json]
