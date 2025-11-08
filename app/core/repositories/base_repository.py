"""
Base repository module.
"""

from abc import ABC, abstractmethod
from typing import Sequence
from uuid import UUID


class BaseRepository[_T](ABC):
    """
    Abstract generic Repository.
    """

    @abstractmethod
    async def create(self, entity: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    async def findall(self) -> Sequence[_T]:
        raise NotImplementedError()

    @abstractmethod
    async def find_by_id(self, id_: UUID) -> _T | None:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, entity: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    async def delete_by_id(self, id_: UUID) -> _T:
        raise NotImplementedError()
