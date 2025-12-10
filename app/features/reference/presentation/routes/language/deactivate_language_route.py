"""
Deactivate language api route module.
"""

from typing import Annotated
from fastapi import status, Depends, Path
from pydantic_extra_types.language_code import LanguageAlpha2

from app.features.reference.presentation.routes.language.language_router import router
from app.features.reference.domain.usecases.language.deactivate_language import (
    DeactivateLanguageUseCase,
)
from app.features.reference.domain.entities.language.language_query_model import (
    LanguageReadModel,
)
from app.features.reference.dependencies import get_deactivate_language_use_case


@router.patch(
    path="/{code}/deactivate",
    response_model=LanguageReadModel,
    status_code=status.HTTP_200_OK,
)
async def deactivate_language(
    code: Annotated[LanguageAlpha2, Path(example="en")],
    deactivate_language_use_case: Annotated[
        DeactivateLanguageUseCase, Depends(get_deactivate_language_use_case)
    ],
):
    language = await deactivate_language_use_case(code)
    return language
