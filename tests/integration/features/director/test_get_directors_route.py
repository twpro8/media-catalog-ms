"""
Test get directors route module.
"""

import pytest
from httpx import AsyncClient

from tests.factories.director_factories import DirectorCreateModelFactory
from app.features.director.domain.entities.director_command_model import (
    DirectorCreateModel,
)
from app.features.director.domain.entities.director_query_model import DirectorReadModel


class TestGetDirectors:
    """
    API tests for getting directors.
    """

    @pytest.fixture(autouse=True)
    async def setup(
        self,
        ac: AsyncClient,
        director_create_model: DirectorCreateModelFactory,
    ) -> None:
        self.path = "/v1/directors"
        self.ac = ac
        self.director_create_model = director_create_model

    async def test_get_all_success(self) -> None:
        """
        Get all directors successfully.
        """
        # Create a director first
        model: DirectorCreateModel = self.director_create_model.build()
        request_director = model.model_dump(mode="json")
        await self.ac.post(self.path, json=request_director)

        response = await self.ac.get(self.path)
        assert response.status_code == 200

        response_json = response.json()
        assert len(response_json) > 0
        for director in response_json:
            DirectorReadModel.model_validate(director)
