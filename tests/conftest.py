"""
Conftest module.
"""

from typing import AsyncGenerator, Any

import pytest
from httpx import AsyncClient, ASGITransport
from polyfactory.pytest_plugin import register_fixture

from app.config import Settings
from app.dependencies import get_settings
from app.main import app

from app.core.database.postgres.database import get_session
from tests.dependency_overrides.session import get_session_null_pool
from app.core.database.postgres.database import null_pool_engine
from app.core.models.postgres.models import Base
from tests.factories.actor_factories import (
    ActorCreateModelFactory,
    ActorUpdateModelFactory,
)
from tests.factories.director_factories import (
    DirectorCreateModelFactory,
    DirectorUpdateModelFactory,
)
from tests.factories.movie_factories import (
    MovieCreateModelFactory,
    MovieUpdateModelFactory,
)
from tests.factories.show_factories import (
    ShowCreateModelFactory,
    ShowUpdateModelFactory,
)

# Initializing models
from app.core.models import *


__SETTINGS: Settings = get_settings()


@pytest.fixture(scope="session", autouse=True)
def check_test_mode():
    assert __SETTINGS.MODE == "TEST"


@pytest.fixture(scope="session", autouse=True)
async def setup_database(check_test_mode):
    """
    Setup database fixture.
    Fixture creates all tables.
    """
    async with null_pool_engine.begin() as session:
        await session.run_sync(Base.metadata.drop_all)
        await session.run_sync(Base.metadata.create_all)


@pytest.fixture(name="ac")
async def async_client() -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient(
        transport=ASGITransport(app),
        base_url="http://test",
    ) as client:
        yield client


# Dependency overrides
app.dependency_overrides[get_session] = get_session_null_pool

# Register fixtures
register_fixture(MovieCreateModelFactory, name="movie_create_model")
register_fixture(MovieUpdateModelFactory, name="movie_update_model")
register_fixture(ShowCreateModelFactory, name="show_create_model")
register_fixture(ShowUpdateModelFactory, name="show_update_model")
register_fixture(DirectorCreateModelFactory, name="director_create_model")
register_fixture(DirectorUpdateModelFactory, name="director_update_model")
register_fixture(ActorCreateModelFactory, name="actor_create_model")
register_fixture(ActorUpdateModelFactory, name="actor_update_model")
pytest_plugins = [
    "tests.fixtures.movie_fixtures",
    "tests.fixtures.show_fixtures",
    "tests.fixtures.season_fixtures",
    "tests.fixtures.episode_fixtures",
    "tests.fixtures.director_fixtures",
    "tests.fixtures.actor_fixtures",
    "tests.fixtures.country_fixtures",
    "tests.fixtures.language_fixtures",
]
