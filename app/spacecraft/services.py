from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.spacecraft.models import DBSpacecraft
from app.spacecraft.schemas import Spacecraft
from app.utils import get_next_page, get_page_count, get_prev_page


def get_items(db: Session, page_number: int, page_size: int):
    item_count = db.query(DBSpacecraft).count()
    items = (
        db.query(DBSpacecraft).limit(page_size).offset(page_number * page_size).all()
    )

    return {
        "items": items,
        "item_count": item_count,
        "page_count": get_page_count(item_count, page_size),
        "prev_page": get_prev_page(page_number),
        "next_page": get_next_page(item_count, page_number, page_size),
    }


def get_item(db: Session, spacecraft_id: int):
    return db.query(DBSpacecraft).where(DBSpacecraft.id == spacecraft_id).first()


def update_item(db: Session, id: int, spacecraft: Spacecraft):
    db_spacecraft = db.query(DBSpacecraft).filter(DBSpacecraft.id == id).first()
    if db_spacecraft is None:
        raise HTTPException(status_code=404, detail="Spacecraft not founds")

    db_spacecraft.name = spacecraft.name
    db_spacecraft.description = spacecraft.description
    db_spacecraft.affiliation = spacecraft.affiliation
    db_spacecraft.dimensions = spacecraft.dimensions
    db_spacecraft.appearances = spacecraft.appearances
    db.add(db_spacecraft)
    db.commit()
    db.refresh(db_spacecraft)

    return db_spacecraft


def create_item(db: Session, spacecraft: Spacecraft):
    db_spacecraft = DBSpacecraft(**spacecraft.model_dump())
    db.add(db_spacecraft)
    db.commit()
    db.refresh(db_spacecraft)

    return db_spacecraft


def delete_item(db: Session, id: int):
    db_spacecraft = db.query(DBSpacecraft).filter(DBSpacecraft.id == id).first()
    if db_spacecraft is None:
        raise HTTPException(status_code=404, detail="Spacecraft not founds")

    db.query(DBSpacecraft).filter(DBSpacecraft.id == id).delete()
    db.commit()
