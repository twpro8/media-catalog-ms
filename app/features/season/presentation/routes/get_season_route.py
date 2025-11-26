"""
Get season api router module.
"""

from uuid import UUID
from fastapi import status, Depends

from app.features.season.presentation.routes.season_router import router
from app.features.season.domain.usecases.get_season import GetSeasonUseCase
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.dependencies import get_season_use_case


@router.get(
    "/{id_}/",
    response_model=SeasonReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_season(
    id_: UUID,
    get_season_use_case: GetSeasonUseCase = Depends(get_season_use_case),
):
    season = await get_season_use_case((id_,))
    return season
