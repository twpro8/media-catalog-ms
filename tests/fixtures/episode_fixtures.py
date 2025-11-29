"""
Episode fixtures module.
"""

from typing import Iterator, Sequence

import pytest
from httpx import AsyncClient

from app.features.episode.domain.entities.episode_command_model import (
    EpisodeCreateModel,
)
from app.features.episode.domain.entities.episode_query_model import EpisodeReadModel
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from datetime import date


@pytest.fixture(scope="function")
def episode_numbers() -> Iterator[int]:
    """Episode numbers pool fixture."""
    return iter(range(1, 1000))


@pytest.fixture
async def created_episodes(
    ac: AsyncClient,
    created_seasons: Sequence[SeasonReadModel],
    episode_numbers: Iterator[int],
) -> Sequence[EpisodeReadModel]:
    season_id = created_seasons[0].id_
    episodes = []
    for _ in range(2):
        model = EpisodeCreateModel(
            season_id=season_id,
            title="Test Episode",
            episode_number=next(episode_numbers),
            release_date=date.today(),
            duration=60,
        )
        request_episode = model.model_dump(mode="json")

        response = await ac.post(url="/v1/episodes/", json=request_episode)
        assert response.status_code == 201

        episodes.append(
            EpisodeReadModel.model_validate(response.json(), from_attributes=True)
        )

    return episodes
