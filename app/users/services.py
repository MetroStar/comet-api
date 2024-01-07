from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.users.models import DBUser
from app.users.schemas import User
from app.utils import get_next_page, get_page_count, get_prev_page


def get_items(db: Session, page_number: int, page_size: int):
    item_count = db.query(DBUser).count()
    items = db.query(DBUser).limit(page_size).offset(page_number * page_size).all()

    return {
        "items": items,
        "item_count": item_count,
        "page_count": get_page_count(item_count, page_size),
        "prev_page": get_prev_page(page_number),
        "next_page": get_next_page(item_count, page_number, page_size),
    }


def get_item(db: Session, item_id: int):
    return db.query(DBUser).where(DBUser.id == item_id).first()


def update_item(db: Session, id: int, item: User):
    db_item = db.query(DBUser).filter(DBUser.id == id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.first_name = item.first_name
    db_item.last_name = item.last_name
    db_item.display_name = item.display_name
    db_item.email = item.email
    db_item.is_active = item.is_active
    db_item.modified = datetime.now()
    db_item.modified_by = item.modified_by
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def create_item(db: Session, item: User):
    db_item = DBUser(**item.model_dump())
    db_item.created = datetime.now()
    db_item.modified = datetime.now()
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def delete_item(db: Session, id: int):
    db_item = db.query(DBUser).filter(DBUser.id == id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.query(DBUser).filter(DBUser.id == id).delete()
    db.commit()
