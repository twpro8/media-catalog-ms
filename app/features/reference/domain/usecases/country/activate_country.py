"""
Activate country use case module.
"""

from app.core.use_cases.use_case import BaseUseCase
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)
from app.features.reference.domain.exceptions.country_error import CountryNotFoundError
from app.features.reference.domain.repositories.reference_unit_of_work import (
    ReferenceUnitOfWork,
)


class ActivateCountryUseCase(BaseUseCase[str, CountryReadModel]):
    """
    ActivateCountryUseCase defines a command use case interface related to the Country Entity.
    """

    unit_of_work: ReferenceUnitOfWork

    async def __call__(self, code: str) -> CountryReadModel: ...


class ActivateCountryUseCaseImpl(ActivateCountryUseCase):
    """
    ActivateCountryUseCaseImpl implements a command use case related to the Country entity.
    """

    def __init__(self, unit_of_work: ReferenceUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, code: str) -> CountryReadModel:
        country = await self.unit_of_work.countries.find_by_code(code)
        if not country:
            raise CountryNotFoundError

        active_country = country.mark_entity_as_active()
        updated_country = await self.unit_of_work.countries.update(active_country)
        await self.unit_of_work.commit()

        return CountryReadModel.from_entity(updated_country)
