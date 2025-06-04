from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

import app.cases.services as service
from app.cases.schemas import Case, CaseBase, CasePayload, CaseWithApplicant
from app.db import get_db

router = APIRouter(
    prefix="/api",
    tags=["Cases"],
    responses={404: {"description": "Endpoint not found"}},
)

# Database dependency injection session
db_session = Annotated[Session, Depends(get_db)]


@router.get("/cases", status_code=status.HTTP_200_OK, response_model=CasePayload)
async def get_cases(db: db_session, page_number: int = 0, page_size: int = 100):
    return service.get_items(db, page_number, page_size)


@router.get(
    "/cases/{id}", status_code=status.HTTP_200_OK, response_model=CaseWithApplicant
)
async def get_case(id: int, db: db_session):
    return service.get_item(db, id)


@router.put("/cases/{id}", status_code=status.HTTP_200_OK, response_model=Case)
async def update_case(id: int, case: CaseBase, db: db_session):
    db_case = service.update_item(db, id, case)
    return db_case


@router.post("/cases", status_code=status.HTTP_201_CREATED, response_model=Case)
async def create_case(case: CaseBase, db: db_session):
    db_case = service.create_item(db, case)
    return db_case


@router.delete("/cases/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_case(id: int, db: db_session):
    service.delete_item(db, id)
