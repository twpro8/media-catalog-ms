"""
Base unit of work module.
"""

from abc import ABC, abstractmethod


class AbstractUnitOfWork[_T](ABC):
    """
    Abstract generic UnitOfWork.
    """

    repository: _T

    @abstractmethod
    async def begin(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError()
