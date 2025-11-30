"""
Test delete director route module.
"""

from uuid import uuid7

import pytest
from httpx import AsyncClient

from tests.factories.director_factories import DirectorCreateModelFactory
from app.features.director.domain.entities.director_command_model import (
    DirectorCreateModel,
)
from app.features.director.domain.entities.director_query_model import DirectorReadModel


class TestDeleteDirector:
    """
    API tests for deleting directors.
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

    async def test_delete_success(self) -> None:
        """
        Delete director successfully.
        """
        model: DirectorCreateModel = self.director_create_model.build()
        request_director = model.model_dump(mode="json")

        response = await self.ac.post(self.path, json=request_director)
        assert response.status_code == 201
        created_director = DirectorReadModel.model_validate(response.json())

        response = await self.ac.delete(f"{self.path}/{created_director.id_}")
        assert response.status_code == 200

        deleted_director = DirectorReadModel.model_validate(response.json())
        assert deleted_director.id_ == created_director.id_

        # Verify it's gone (or marked as deleted)
        response = await self.ac.get(f"{self.path}/{created_director.id_}")
        assert response.status_code == 404

    async def test_delete_not_found(self) -> None:
        """
        Delete director not found should return 404.
        """
        response = await self.ac.delete(f"{self.path}/{uuid7()}")
        assert response.status_code == 404
