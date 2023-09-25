from fastapi import APIRouter, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from app.db import get_db
from app.spacecraft.models import Spacecraft
import app.spacecraft.models as model

router = APIRouter(
    prefix="/api",
    tags=["Spacecraft"],
    responses={404: {"description": "Endpoint not found"}},
)

# Database dependency injection context
db_context = Annotated[Session, Depends(get_db)]

@router.get('/spacecraft', response_model=List[Spacecraft])
def get_all_spacecraft(db: db_context):
    return model.get_all_spacecraft(db)

@router.get('/spacecraft/{id}')
def get_spacecraft(id: int, db: db_context):
    return model.get_spacecraft(db, id)

@router.post('/spacecraft/', response_model=Spacecraft)
def create_spacecraft(spacecraft: Spacecraft, db: db_context):
    db_spacecraft = model.create_spacecraft(db, spacecraft)
    return db_spacecraft
