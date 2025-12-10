"""
Get country api route module.
"""

from typing import Annotated
from fastapi import status, Depends, Path
from pydantic_extra_types.country import CountryAlpha2

from app.features.reference.presentation.routes.country.country_router import router
from app.features.reference.domain.usecases.country.get_country import (
    GetCountryUseCase,
)
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)
from app.features.reference.dependencies import get_country_use_case


@router.get(
    path="/{code}",
    response_model=CountryReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_country(
    code: Annotated[CountryAlpha2, Path(example="US")],
    get_country_use_case: Annotated[GetCountryUseCase, Depends(get_country_use_case)],
):
    country = await get_country_use_case(code)
    return country
