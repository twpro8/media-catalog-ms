"""
Test manage language routes module.
"""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.features.reference.data.models.language import Language
from sqlalchemy import update


class TestManageLanguageRoutes:
    """
    API tests for managing languages (Get, Activate, Deactivate).
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        session: AsyncSession,
    ) -> None:
        self.path = "/v1/languages"
        self.ac = ac
        self.session = session

    async def test_get_language_by_code(self) -> None:
        response = await self.ac.get(f"{self.path}/en")
        assert response.status_code == 200
        data = response.json()
        assert data["code"] == "en"
        assert data["name"] == "English"
        assert "active" in data  # Verify active field is present

    async def test_deactivate_language(self) -> None:
        # Ensure en is active
        await self.session.execute(
            update(Language).where(Language.code == "en").values(active=True)
        )
        await self.session.commit()

        # Deactivate
        response = await self.ac.patch(f"{self.path}/en/deactivate")
        assert response.status_code == 200
        data = response.json()
        assert data["active"] is False

        response = await self.ac.get(f"{self.path}/en")
        assert response.status_code == 200
        assert response.json()["active"] is False

    async def test_activate_language(self) -> None:
        # Ensure fr is inactive
        await self.session.execute(
            update(Language).where(Language.code == "fr").values(active=False)
        )
        await self.session.commit()

        # Activate
        response = await self.ac.patch(f"{self.path}/fr/activate")
        assert response.status_code == 200
        data = response.json()
        assert data["active"] is True

        # Verify
        response = await self.ac.get(f"{self.path}/fr")
        assert response.status_code == 200
        assert response.status_code == 200
        assert response.json()["active"] is True

    async def test_activate_already_active_language(self) -> None:
        # Ensure 'en' is active
        await self.session.execute(
            update(Language).where(Language.code == "en").values(active=True)
        )
        await self.session.commit()
        response = await self.ac.patch(f"{self.path}/en/activate")
        assert response.status_code == 409
        assert response.json()["detail"] == "Language already active"

    async def test_deactivate_already_inactive_language(self) -> None:
        # First deactivate
        await self.ac.patch(f"{self.path}/en/deactivate")

        # Try to deactivate again
        response = await self.ac.patch(f"{self.path}/en/deactivate")
        assert response.status_code == 409
        assert response.json()["detail"] == "Language already inactive"
