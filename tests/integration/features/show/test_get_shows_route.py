"""
Test get shows route module.
"""

import pytest
from httpx import AsyncClient

from app.features.show.domain.entities.show_query_model import ShowReadModel


@pytest.mark.get_shows
class TestGetShows:
    """
    API tests for getting shows.
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
    async def test_get_shows_success(self, run: int) -> None:
        """
        Get shows successfully.
        """

        response = await self.ac.get(self.path)
        assert response.status_code == 200

        response_json = response.json()
        assert len(response_json) > 1
        [ShowReadModel.model_validate(show) for show in response_json]
