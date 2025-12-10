"""
Deactivate country api route module.
"""

from typing import Annotated
from fastapi import status, Depends, Path
from pydantic_extra_types.country import CountryAlpha2

from app.features.reference.presentation.routes.country.country_router import router
from app.features.reference.domain.usecases.country.deactivate_country import (
    DeactivateCountryUseCase,
)
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)
from app.features.reference.dependencies import get_deactivate_country_use_case


@router.patch(
    path="/{code}/deactivate",
    response_model=CountryReadModel,
    status_code=status.HTTP_200_OK,
)
async def deactivate_country(
    code: Annotated[CountryAlpha2, Path(example="US")],
    deactivate_country_use_case: Annotated[
        DeactivateCountryUseCase, Depends(get_deactivate_country_use_case)
    ],
):
    country = await deactivate_country_use_case(code)
    return country
