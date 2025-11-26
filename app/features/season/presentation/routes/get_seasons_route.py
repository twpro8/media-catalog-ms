"""
Get season api router module.
"""

from fastapi import status, Depends

from app.features.season.presentation.routes.season_router import router
from app.features.season.domain.usecases.get_seasons import GetSeasonsUseCase
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.dependencies import get_seasons_use_case


@router.get(
    "/",
    response_model=list[SeasonReadModel],
    status_code=status.HTTP_200_OK,
)
async def get_seasons(
    get_seasons_use_case: GetSeasonsUseCase = Depends(get_seasons_use_case),
):
    seasons = await get_seasons_use_case(None)
    return seasons
