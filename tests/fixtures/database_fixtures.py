import pytest

from app.core.database.postgres.database import null_pool_session_maker


@pytest.fixture
async def session():
    async with null_pool_session_maker() as session:
        yield session
