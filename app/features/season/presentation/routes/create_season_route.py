"""
Create season api router module.
"""

from fastapi import Response, Request, status, Depends

from app.features.season.presentation.routes.season_router import router
from app.features.season.domain.entities.season_command_model import SeasonCreateModel
from app.features.season.domain.entities.season_query_model import SeasonReadModel
from app.features.season.domain.usecases.create_season import CreateSeasonUseCase
from app.features.season.dependencies import get_create_season_use_case


@router.post(
    "/",
    response_model=SeasonReadModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_season(
    data: SeasonCreateModel,
    response: Response,
    request: Request,
    create_season_use_case: CreateSeasonUseCase = Depends(get_create_season_use_case),
):
    season = await create_season_use_case((data,))
    response.headers["location"] = f"{request.url.path}{season.id_}"
    return season
