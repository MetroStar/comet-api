from fastapi import APIRouter
from starlette import status

from app.config import settings

router = APIRouter(
    prefix=f"{settings.API_PREFIX}/health",
    tags=["Health"],
)


@router.get("/", status_code=status.HTTP_200_OK)
def get_health():
    return {"health": "healthy"}
