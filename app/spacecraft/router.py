from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from app.db import get_db
from app.spacecraft.models import Spacecraft, get_spacecraft, create_spacecraft

router = APIRouter(
    prefix="/api",
    tags=["Spacecraft"],
    responses={404: {"description": "Not found"}},
)

@router.get('/spacecraft', response_model=List[Spacecraft])
def get_characters_view(db: Session = Depends(get_db)):
    return get_spacecraft(db)

@router.get('/spacecraft/{spacecraft_id}')
def get_characters_view(spacecraft_id: int, db: Session = Depends(get_db)):
    return get_spacecraft(db, spacecraft_id)

@router.post('/spacecraft/', response_model=Spacecraft)
def create_characters_view(spacecraft: Spacecraft, db: Session = Depends(get_db)):
    db_spacecraft = create_spacecraft(db, spacecraft)
    return db_spacecraft
