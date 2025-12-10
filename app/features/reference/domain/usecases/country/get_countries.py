"""
Get countries use case module.
"""

from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)
from app.features.reference.domain.services.country_query_service import (
    CountryQueryService,
)


class GetCountriesUseCase(BaseUseCase[None, Sequence[CountryReadModel]]):
    """
    GetCountriesUseCase defines a query use case interface related to the Country Entity.
    """

    service = CountryQueryService

    async def __call__(self, args: None) -> Sequence[CountryReadModel]: ...


class GetCountriesUseCaseImpl(GetCountriesUseCase):
    """
    GetCountriesUseCaseImpl implements a query use case related to the Country entity.
    """

    def __init__(self, service: CountryQueryService):
        self.service = service

    async def __call__(self, args: None) -> Sequence[CountryReadModel]:
        countries = await self.service.findall()
        return countries
