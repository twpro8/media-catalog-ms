"""
Test manage country routes' module.
"""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.features.reference.data.models.country import Country
from sqlalchemy import update


class TestManageCountryRoutes:
    """
    API tests for managing countries (Get, Activate, Deactivate).
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        session: AsyncSession,
    ) -> None:
        self.path = "/v1/countries"
        self.ac = ac
        self.session = session

    async def test_get_country_by_code(self) -> None:
        response = await self.ac.get(f"{self.path}/US")
        assert response.status_code == 200
        data = response.json()
        assert data["code"] == "US"
        assert data["name"] == "United States"
        assert "active" in data

    async def test_deactivate_country(self) -> None:
        # Ensure US is active
        await self.session.execute(
            update(Country).where(Country.code == "US").values(active=True)
        )
        await self.session.commit()

        response = await self.ac.patch(f"{self.path}/US/deactivate")
        assert response.status_code == 200
        data = response.json()
        assert data["active"] is False

        response = await self.ac.get(f"{self.path}/US")
        assert response.status_code == 200
        assert response.json()["active"] is False

    async def test_activate_country(self) -> None:
        # Ensure CA is inactive
        await self.session.execute(
            update(Country).where(Country.code == "CA").values(active=False)
        )
        await self.session.commit()

        # Activate
        response = await self.ac.patch(f"{self.path}/CA/activate")
        assert response.status_code == 200
        data = response.json()
        assert data["active"] is True

        response = await self.ac.get(f"{self.path}/CA")
        assert response.status_code == 200
        assert response.json()["active"] is True

    async def test_activate_already_active_country(self) -> None:
        # Ensure US is active
        await self.session.execute(
            update(Country).where(Country.code == "US").values(active=True)
        )
        await self.session.commit()

        response = await self.ac.patch(f"{self.path}/US/activate")
        assert response.status_code == 409
        assert response.json()["detail"] == "Country already active"

    async def test_deactivate_already_inactive_country(self) -> None:
        # Ensure US is inactive
        await self.session.execute(
            update(Country).where(Country.code == "US").values(active=False)
        )
        await self.session.commit()

        response = await self.ac.patch(f"{self.path}/US/deactivate")
        assert response.status_code == 409
        assert response.json()["detail"] == "Country already inactive"
