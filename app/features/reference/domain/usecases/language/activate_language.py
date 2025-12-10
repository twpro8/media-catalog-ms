"""
Activate language use case module.
"""

from app.core.use_cases.use_case import BaseUseCase
from app.features.reference.domain.entities.language.language_query_model import (
    LanguageReadModel,
)
from app.features.reference.domain.exceptions.language_error import (
    LanguageNotFoundError,
)
from app.features.reference.domain.repositories.reference_unit_of_work import (
    ReferenceUnitOfWork,
)


class ActivateLanguageUseCase(BaseUseCase[str, LanguageReadModel]):
    """
    ActivateLanguageUseCase defines a command use case interface related to the Language Entity.
    """

    unit_of_work: ReferenceUnitOfWork

    async def __call__(self, code: str) -> LanguageReadModel: ...


class ActivateLanguageUseCaseImpl(ActivateLanguageUseCase):
    """
    ActivateLanguageUseCaseImpl implements a command use case related to the Language entity.
    """

    def __init__(self, unit_of_work: ReferenceUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, code: str) -> LanguageReadModel:
        language = await self.unit_of_work.languages.find_by_code(code)
        if language is None:
            raise LanguageNotFoundError

        active_language = language.mark_entity_as_active()
        updated_language = await self.unit_of_work.languages.update(active_language)
        await self.unit_of_work.commit()

        return LanguageReadModel.from_entity(updated_language)
