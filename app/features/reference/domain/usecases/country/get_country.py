"""
Get country use case module.
"""

from app.core.use_cases.use_case import BaseUseCase
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)
from app.features.reference.domain.exceptions.country_error import CountryNotFoundError
from app.features.reference.domain.services.country_query_service import (
    CountryQueryService,
)


class GetCountryUseCase(BaseUseCase[str, CountryReadModel | None]):
    """
    GetCountryUseCase defines a query use case interface related to the Country Entity.
    """

    service = CountryQueryService

    async def __call__(self, code: str) -> CountryReadModel | None: ...


class GetCountryUseCaseImpl(GetCountryUseCase):
    """
    GetCountryUseCaseImpl implements a query use case related to the Country entity.
    """

    def __init__(self, service: CountryQueryService):
        self.service = service

    async def __call__(self, code: str) -> CountryReadModel | None:
        country = await self.service.find_by_code(code)
        if not country:
            raise CountryNotFoundError

        return country
