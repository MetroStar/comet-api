from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/api",
    tags=["Health"],
)


@router.get("/health", status_code=status.HTTP_200_OK)
def get_health():
    return {"health": "healthy"}
