"""
Get season api route module.
"""

from typing import Annotated
from uuid import UUID
from fastapi import status, Depends

from app.features.season.presentation.routes.season_router import router
from app.features.season.domain.usecases.get_season import GetSeasonUseCase
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.dependencies import get_season_use_case


@router.get(
    path="/{season_id}",
    response_model=SeasonReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_season(
    season_id: UUID,
    get_season_use_case: Annotated[GetSeasonUseCase, Depends(get_season_use_case)],
):
    season = await get_season_use_case((season_id,))
    return season
