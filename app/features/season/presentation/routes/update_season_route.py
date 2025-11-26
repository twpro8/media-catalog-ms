"""
Update season api router module.
"""

from uuid import UUID

from fastapi import Depends, status

from app.features.season.presentation.routes.season_router import router
from app.features.season.dependencies import get_update_season_use_case
from app.features.season.domain.entities.season_command_model import SeasonUpdateModel
from app.features.season.domain.usecases.update_season import UpdateSeasonUseCase
from app.features.season.domain.entities.season_query_model import SeasonReadModel


@router.patch(
    "/{id_}/",
    response_model=SeasonReadModel,
    status_code=status.HTTP_200_OK,
)
async def update_season(
    id_: UUID,
    data: SeasonUpdateModel,
    update_season_use_case: UpdateSeasonUseCase = Depends(get_update_season_use_case),
):
    season = await update_season_use_case((id_, data))
    return season
