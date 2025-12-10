"""
Language fixtures module.
"""

import pycountry
import pytest
from sqlalchemy import insert

from app.core.database.postgres.database import null_pool_session_maker
from app.features.reference.data.models.language import Language


@pytest.fixture(
    scope="session",
    autouse=True,
)
async def init_languages(setup_database) -> None:
    languages = [
        {
            "code": language.alpha_2,  # type: ignore
            "name": language.name,  # type: ignore
            "active": True,
        }
        for language in pycountry.languages
        if hasattr(language, "alpha_2")
    ]

    assert len(languages) >= 184

    async with null_pool_session_maker() as session:
        await session.execute(
            insert(Language),
            languages,
        )
        await session.commit()
