"""
Activate language api route module.
"""

from typing import Annotated
from fastapi import status, Depends, Path
from pydantic_extra_types.language_code import LanguageAlpha2

from app.features.reference.presentation.routes.language.language_router import router
from app.features.reference.domain.usecases.language.activate_language import (
    ActivateLanguageUseCase,
)
from app.features.reference.domain.entities.language.language_query_model import (
    LanguageReadModel,
)
from app.features.reference.dependencies import get_activate_language_use_case


@router.patch(
    path="/{code}/activate",
    response_model=LanguageReadModel,
    status_code=status.HTTP_200_OK,
)
async def activate_language(
    code: Annotated[LanguageAlpha2, Path(example="en")],
    activate_language_use_case: Annotated[
        ActivateLanguageUseCase, Depends(get_activate_language_use_case)
    ],
):
    language = await activate_language_use_case(code)
    return language
