"""
SQLAlchemy unit of work implementation module.
"""

from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyUnitOfWork:
    """
    SQLAlchemyUnitOfWork unit of work implementation.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self.session.rollback()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
