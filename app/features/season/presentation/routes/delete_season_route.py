"""
Delete season api router module.
"""

from uuid import UUID

from fastapi import status, Depends

from app.features.season.presentation.routes.season_router import router
from app.features.season.dependencies import get_delete_season_use_case
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.domain.usecases.delete_season import DeleteSeasonUseCase


@router.delete(
    "/{id_}/",
    response_model=SeasonReadModel,
    status_code=status.HTTP_200_OK,
)
async def delete_season(
    id_: UUID,
    delete_season_use_case: DeleteSeasonUseCase = Depends(get_delete_season_use_case),
):
    season = await delete_season_use_case((id_,))
    return season
