from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

import app.users.services as service
from app.db import get_db
from app.users.schemas import User, UserPayload

router = APIRouter(
    prefix="/api",
    tags=["Users"],
    responses={404: {"description": "Endpoint not found"}},
)

# Database dependency injection session
db_session = Annotated[Session, Depends(get_db)]


@router.get(
    "/users",
    status_code=status.HTTP_200_OK,
    response_model=UserPayload,
)
async def get_items(db: db_session, page_number: int = 0, page_size: int = 100):
    return service.get_items(db, page_number, page_size)


@router.get("/users/{id}", status_code=status.HTTP_200_OK, response_model=User)
async def get_item(id: int, db: db_session):
    return service.get_item(db, id)


@router.put("/users/{id}", status_code=status.HTTP_200_OK, response_model=User)
async def update_item(id: int, item: User, db: db_session):
    db_item = service.update_item(db, id, item)
    return db_item


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_item(item: User, db: db_session):
    db_item = service.create_item(db, item)
    return db_item


@router.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(id: int, db: db_session):
    service.delete_item(db, id)
