"""
Get country api route module.
"""

from typing import Annotated
from fastapi import status, Depends

from app.features.reference.presentation.routes.country.country_router import router
from app.features.reference.domain.usecases.country.get_countries import (
    GetCountriesUseCase,
)
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)
from app.features.reference.dependencies import get_countries_use_case


@router.get(
    path="",
    response_model=list[CountryReadModel],
    status_code=status.HTTP_200_OK,
)
async def get_countries(
    get_countries_use_case: Annotated[
        GetCountriesUseCase, Depends(get_countries_use_case)
    ],
):
    countries = await get_countries_use_case(None)
    return countries
