"""
Base use case module.
"""

from abc import ABC, abstractmethod


class BaseUseCase[_T, _R](ABC):
    """
    Abstract generic UseCase.
    """

    @abstractmethod
    async def __call__(self, args: _T) -> _R: ...
