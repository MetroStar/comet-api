from fastapi import APIRouter, Depends
from typing import Annotated, List
from starlette import status
from sqlalchemy.orm import Session
from app.db import get_db
from app.spacecraft.models import Spacecraft
import app.spacecraft.models as model

router = APIRouter(
    prefix="/api",
    tags=["Spacecraft"],
    responses={404: {"description": "Endpoint not found"}},
)

# Database dependency injection session
db_session = Annotated[Session, Depends(get_db)]

@router.get('/spacecraft', status_code=status.HTTP_200_OK, response_model=List[Spacecraft])
def get_all_spacecraft(db: db_session):
    return model.get_items(db)

@router.get('/spacecraft/{id}', status_code=status.HTTP_200_OK, response_model=Spacecraft)
def get_spacecraft(id: int, db: db_session):
    return model.get_item(db, id)

@router.put('/spacecraft/{id}', status_code=status.HTTP_200_OK, response_model=Spacecraft)
def update_spacecraft(id: int, spacecraft: Spacecraft, db: db_session):
    db_spacecraft = model.update_item(db, id, spacecraft)
    return db_spacecraft

@router.post('/spacecraft/', status_code=status.HTTP_201_CREATED, response_model=Spacecraft)
def create_spacecraft(spacecraft: Spacecraft, db: db_session):
    db_spacecraft = model.create_item(db, spacecraft)
    return db_spacecraft

@router.delete('/spacecraft/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_spacecraft(id: int, db: db_session):
    model.delete_item(db, id)
