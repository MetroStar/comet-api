from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from starlette import status

from app.auth import validate_jwt

router = APIRouter(
    prefix="/api",
    tags=["Admin"],
)


@router.get(
    "/current-user",
    dependencies=[Depends(HTTPBearer())],
    status_code=status.HTTP_200_OK,
)
async def get_current_user(current_user: Annotated[dict, Depends(validate_jwt)]):
    return {"user": current_user}
