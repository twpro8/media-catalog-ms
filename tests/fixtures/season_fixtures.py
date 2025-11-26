"""
Season fixtures module.
"""

from typing import Sequence, Iterator

import pytest
from httpx import AsyncClient

from app.features.season.domain.entities.season_command_model import SeasonCreateModel
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.show.domain.entities.show_query_model import ShowReadModel


@pytest.fixture(scope="session")
def season_numbers() -> Iterator[int]:
    """Season numbers pool fixture."""
    return iter(range(1, 1000))


@pytest.fixture
async def created_seasons(
    ac: AsyncClient,
    created_shows: Sequence[ShowReadModel],
    season_numbers: Iterator[int],
) -> Sequence[SeasonReadModel]:
    show_id = created_shows[0].id_
    seasons = []
    for _ in range(2):
        model = SeasonCreateModel(
            show_id=show_id, title="Test Season", season_number=next(season_numbers)
        )
        request_user = model.model_dump(mode="json")

        response = await ac.post(url="/v1/seasons/", json=request_user)
        assert response.status_code == 201

        seasons.append(
            SeasonReadModel.model_validate(response.json(), from_attributes=True)
        )

    return seasons
