"""
Country fixtures module.
"""

import pycountry
import pytest
from sqlalchemy import insert

from app.core.database.postgres.database import null_pool_session_maker
from app.features.reference.data.models.country import Country


@pytest.fixture(
    scope="session",
    autouse=True,
)
async def init_countries(setup_database) -> None:
    countries = [
        {
            "code": country.alpha_2,  # type: ignore
            "name": country.name,  # type: ignore
            "active": True,
        }
        for country in pycountry.countries
    ]

    assert len(countries) >= 249

    async with null_pool_session_maker() as session:
        await session.execute(
            insert(Country),
            countries,
        )
        await session.commit()
