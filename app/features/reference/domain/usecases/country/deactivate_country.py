"""
Deactivate country use case module.
"""

from app.core.use_cases.use_case import BaseUseCase
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)
from app.features.reference.domain.exceptions.country_error import CountryNotFoundError
from app.features.reference.domain.repositories.reference_unit_of_work import (
    ReferenceUnitOfWork,
)


class DeactivateCountryUseCase(BaseUseCase[str, CountryReadModel]):
    """
    DeactivateCountryUseCase defines a command use case interface related to the Country Entity.
    """

    unit_of_work: ReferenceUnitOfWork

    async def __call__(self, code: str) -> CountryReadModel: ...


class DeactivateCountryUseCaseImpl(DeactivateCountryUseCase):
    """
    DeactivateCountryUseCaseImpl implements a command use case related to the Country entity.
    """

    def __init__(self, unit_of_work: ReferenceUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, code: str) -> CountryReadModel:
        country = await self.unit_of_work.countries.find_by_code(code)
        if not country:
            raise CountryNotFoundError

        inactive_country = country.mark_entity_as_inactive()
        updated_country = await self.unit_of_work.countries.update(inactive_country)
        await self.unit_of_work.commit()

        return CountryReadModel.from_entity(updated_country)
