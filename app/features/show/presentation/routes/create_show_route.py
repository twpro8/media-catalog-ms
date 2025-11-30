"""
Create show api route module.
"""

from typing import Annotated
from fastapi import Response, Request, status, Depends

from app.features.show.presentation.routes.show_router import router
from app.features.show.domain.entities.show_command_model import ShowCreateModel
from app.features.show.domain.entities.show_query_model import ShowReadModel
from app.features.show.domain.usecases.create_show import CreateShowUseCase
from app.features.show.dependencies import get_create_show_use_case


@router.post(
    path="",
    response_model=ShowReadModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_show(
    data: ShowCreateModel,
    response: Response,
    request: Request,
    create_show_use_case: Annotated[
        CreateShowUseCase, Depends(get_create_show_use_case)
    ],
):
    show = await create_show_use_case((data,))
    response.headers["location"] = f"{request.url.path}/{show.id_}"
    return show
