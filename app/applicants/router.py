from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

import app.applicants.services as service
from app.applicants.schemas import Applicant, ApplicantPayload
from app.db import get_db

router = APIRouter(
    prefix="/api",
    tags=["Applicants"],
    responses={404: {"description": "Endpoint not found"}},
)

# Database dependency injection session
db_session = Annotated[Session, Depends(get_db)]


@router.get(
    "/applicants", status_code=status.HTTP_200_OK, response_model=ApplicantPayload
)
async def get_applicants(db: db_session, page_number: int = 0, page_size: int = 100):
    return service.get_items(db, page_number, page_size)


@router.get(
    "/applicants/{id}", status_code=status.HTTP_200_OK, response_model=Applicant
)
async def get_applicant(id: int, db: db_session):
    return service.get_item(db, id)


@router.put(
    "/applicants/{id}", status_code=status.HTTP_200_OK, response_model=Applicant
)
async def update_applicant(id: int, applicant: Applicant, db: db_session):
    db_applicant = service.update_item(db, id, applicant)
    return db_applicant


@router.post(
    "/applicants", status_code=status.HTTP_201_CREATED, response_model=Applicant
)
async def create_applicant(applicant: Applicant, db: db_session):
    db_applicant = service.create_item(db, applicant)
    return db_applicant


@router.delete("/applicants/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_applicant(id: int, db: db_session):
    service.delete_item(db, id)
