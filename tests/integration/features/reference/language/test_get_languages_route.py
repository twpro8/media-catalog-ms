"""
Test get languages route module.
"""

import pytest
from httpx import AsyncClient
import pycountry


class TestGetLanguages:
    """
    API tests for getting languages.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
    ) -> None:
        self.path = "/v1/languages"
        self.ac = ac
        self.languages = [
            {
                "code": language.alpha_2,  # type: ignore
                "name": language.name,  # type: ignore
            }
            for language in pycountry.languages
            if hasattr(language, "alpha_2")
        ]
        assert len(self.languages) >= 184

    async def test_get_languages_success(self) -> None:
        """
        Get languages successfully.
        """

        response = await self.ac.get(self.path)
        assert response.status_code == 200

        assert response.json() == self.languages
