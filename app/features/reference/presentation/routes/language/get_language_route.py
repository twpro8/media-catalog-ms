"""
Get language api route module.
"""

from typing import Annotated
from fastapi import Path, status, Depends
from pydantic_extra_types.language_code import LanguageAlpha2

from app.features.reference.presentation.routes.language.language_router import router
from app.features.reference.domain.usecases.language.get_language import (
    GetLanguageUseCase,
)
from app.features.reference.domain.entities.language.language_query_model import (
    LanguageReadModel,
)
from app.features.reference.dependencies import get_language_use_case


@router.get(
    path="/{code}",
    response_model=LanguageReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_language(
    code: Annotated[LanguageAlpha2, Path(example="en")],
    get_language_use_case: Annotated[
        GetLanguageUseCase, Depends(get_language_use_case)
    ],
):
    language = await get_language_use_case(code)
    return language
