"""
Update season api route module.
"""

from typing import Annotated
from uuid import UUID

from fastapi import Depends, status

from app.features.season.presentation.routes.season_router import router
from app.features.season.dependencies import get_update_season_use_case
from app.features.season.domain.entities.season_command_model import SeasonUpdateModel
from app.features.season.domain.usecases.update_season import UpdateSeasonUseCase
from app.features.season.domain.entities.season_query_model import SeasonReadModel


@router.patch(
    path="/{season_id}",
    response_model=SeasonReadModel,
    status_code=status.HTTP_200_OK,
)
async def update_season(
    season_id: UUID,
    data: SeasonUpdateModel,
    update_season_use_case: Annotated[
        UpdateSeasonUseCase, Depends(get_update_season_use_case)
    ],
):
    season = await update_season_use_case((season_id, data))
    return season
