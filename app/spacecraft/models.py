from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import Column, String, Integer

from app.db import Base
from app.spacecraft.schemas import Spacecraft

# SQLAlchemy Model
class DBSpacecraft(Base):
    __tablename__ = 'spacecraft'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    category = Column(String, nullable=True)

def get_items(db: Session):
    return db.query(DBSpacecraft).all()

def get_item(db: Session, spacecraft_id: int):
    return db.query(DBSpacecraft).where(DBSpacecraft.id == spacecraft_id).first()

def create_item(db: Session, spacecraft: Spacecraft):
    db_spacecraft = DBSpacecraft(**spacecraft.model_dump())
    db.add(db_spacecraft)
    db.commit()
    db.refresh(db_spacecraft)

    return db_spacecraft

def update_item(db: Session, id: int, spacecraft: Spacecraft):
    db_spacecraft = db.query(DBSpacecraft).filter(DBSpacecraft.id == id).first()
    if db_spacecraft is None:
        raise HTTPException(status_code=404, detail='Spacecraft not founds')

    db_spacecraft.name = spacecraft.name
    db_spacecraft.description = spacecraft.description
    db_spacecraft.category = spacecraft.category
    db.add(db_spacecraft)
    db.commit()
    db.refresh(db_spacecraft)

    return db_spacecraft

def delete_item(db: Session, id: int):
    db_spacecraft = db.query(DBSpacecraft).filter(DBSpacecraft.id == id).first()
    if db_spacecraft is None:
        raise HTTPException(status_code=404, detail='Spacecraft not founds')

    db.query(DBSpacecraft).filter(DBSpacecraft.id == id).delete()
    db.commit()
