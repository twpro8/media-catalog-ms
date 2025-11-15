from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database.postgres.database import null_pool_session_maker


async def get_session_null_pool() -> AsyncGenerator[AsyncSession]:
    async with null_pool_session_maker() as null_pool_session:
        yield null_pool_session
