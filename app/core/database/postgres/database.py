"""
Sql alchemy database module.
"""

from typing import AsyncGenerator

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.config import Settings
from app.dependencies import get_settings


__SETTINGS: Settings = get_settings()


engine = create_async_engine(url=__SETTINGS.DB_URL)
session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

null_pool_engine = create_async_engine(url=__SETTINGS.DB_URL, poolclass=NullPool)
null_pool_session_maker = async_sessionmaker(
    bind=null_pool_engine, expire_on_commit=False
)


async def get_session() -> AsyncGenerator[AsyncSession]:
    async with session_maker() as session:
        yield session
