"""
Get show api router module.
"""

from fastapi import status, Depends

from app.features.show.presentation.routes.show_router import router
from app.features.show.domain.usecases.get_shows import GetShowsUseCase
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.dependencies import get_shows_use_case


@router.get(
    "/",
    response_model=list[ShowReadModel],
    status_code=status.HTTP_200_OK,
)
async def get_shows(
    get_shows_use_case: GetShowsUseCase = Depends(get_shows_use_case),
):
    shows = await get_shows_use_case(None)
    return shows
