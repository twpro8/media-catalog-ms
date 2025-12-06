"""
Test get countries route module.
"""

import pytest
from httpx import AsyncClient
import pycountry


class TestGetCountries:
    """
    API tests for getting countries.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
    ) -> None:
        self.path = "/v1/countries"
        self.ac = ac
        self.countries = [
            {
                "code": country.alpha_2,  # type: ignore
                "name": country.name,  # type: ignore
            }
            for country in pycountry.countries
        ]
        assert len(self.countries) >= 249

    async def test_get_countries_success(self) -> None:
        """
        Get countries successfully.
        """

        response = await self.ac.get(self.path)
        assert response.status_code == 200

        assert response.json() == self.countries
