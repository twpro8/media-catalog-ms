"""
Get language api route module.
"""

from typing import Annotated
from fastapi import status, Depends

from app.features.reference.presentation.routes.language.language_router import router
from app.features.reference.domain.usecases.language.get_languages import (
    GetLanguagesUseCase,
)
from app.features.reference.domain.entities.language.language_query_model import (
    LanguageReadModel,
)
from app.features.reference.dependencies import get_languages_use_case


@router.get(
    path="",
    response_model=list[LanguageReadModel],
    status_code=status.HTTP_200_OK,
)
async def get_languages(
    get_languages_use_case: Annotated[
        GetLanguagesUseCase, Depends(get_languages_use_case)
    ],
):
    languages = await get_languages_use_case(None)
    return languages
