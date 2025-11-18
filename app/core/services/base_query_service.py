"""
Base query service module.
"""

from abc import ABC, abstractmethod
from typing import Sequence
from uuid import UUID


class QueryService[_T](ABC):
    """
    Abstract generic query QueryService.
    """

    @abstractmethod
    async def find_by_id(self, id_: UUID) -> _T | None: ...

    @abstractmethod
    async def findall(self) -> Sequence[_T]: ...
