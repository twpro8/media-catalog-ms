"""
Activate country api route module.
"""

from typing import Annotated
from fastapi import status, Depends, Path
from pydantic_extra_types.country import CountryAlpha2

from app.features.reference.presentation.routes.country.country_router import router
from app.features.reference.domain.usecases.country.activate_country import (
    ActivateCountryUseCase,
)
from app.features.reference.domain.entities.country.country_query_model import (
    CountryReadModel,
)
from app.features.reference.dependencies import get_activate_country_use_case


@router.patch(
    path="/{code}/activate",
    response_model=CountryReadModel,
    status_code=status.HTTP_200_OK,
)
async def activate_country(
    code: Annotated[CountryAlpha2, Path(example="US")],
    activate_country_use_case: Annotated[
        ActivateCountryUseCase, Depends(get_activate_country_use_case)
    ],
):
    country = await activate_country_use_case(code)
    return country
