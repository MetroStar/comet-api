from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

import app.applicants.services as service
from app.applicants.schemas import (
    ApplicantCreate,
    ApplicantListResponse,
    ApplicantResponse,
    ApplicantUpdate,
)
from app.db import get_db

router = APIRouter(
    prefix="/applicants",
    tags=["Applicants"],
    responses={404: {"description": "Endpoint not found"}},
)

# Database dependency injection session
db_session = Annotated[Session, Depends(get_db)]


@router.get("/", status_code=status.HTTP_200_OK, response_model=ApplicantListResponse)
async def get_applicants(db: db_session, page_number: int = 0, page_size: int = 100):
    return service.get_items(db, page_number, page_size)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ApplicantResponse)
async def create_applicant(applicant: ApplicantCreate, db: db_session):
    db_applicant = service.create_item(db, applicant)
    return db_applicant


@router.get(
    "/{applicant_id}", status_code=status.HTTP_200_OK, response_model=ApplicantResponse
)
async def get_applicant(applicant_id: int, db: db_session):
    return service.get_item(db, applicant_id)


@router.put(
    "/{applicant_id}", status_code=status.HTTP_200_OK, response_model=ApplicantResponse
)
async def update_applicant(
    applicant_id: int, applicant: ApplicantUpdate, db: db_session
):
    db_applicant = service.update_item(db, applicant_id, applicant)
    return db_applicant


@router.delete("/{applicant_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_applicant(applicant_id: int, db: db_session):
    service.delete_item(db, applicant_id)
