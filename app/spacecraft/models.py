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

def get_spacecraft(db: Session, spacecraft_id: int):
    return db.query(DBSpacecraft).where(DBSpacecraft.id == spacecraft_id).first()

def get_all_spacecraft(db: Session):
    return db.query(DBSpacecraft).all()

def create_spacecraft(db: Session, spacecraft: Spacecraft):
    db_spacecraft = DBSpacecraft(**spacecraft.dict())
    db.add(db_spacecraft)
    db.commit()
    db.refresh(db_spacecraft)

    return db_spacecraft
