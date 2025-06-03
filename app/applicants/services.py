from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.applicants.models import DBApplicant
from app.applicants.schemas import ApplicantBase
from app.utils import get_next_page, get_page_count, get_prev_page


def get_items(db: Session, page_number: int, page_size: int):
    item_count = db.query(DBApplicant).count()
    items = db.query(DBApplicant).limit(page_size).offset(page_number * page_size).all()

    return {
        "items": items,
        "item_count": item_count,
        "page_count": get_page_count(item_count, page_size),
        "prev_page": get_prev_page(page_number),
        "next_page": get_next_page(item_count, page_number, page_size),
    }


def get_item(db: Session, applicant_id: int):
    return db.query(DBApplicant).where(DBApplicant.id == applicant_id).first()


def update_item(db: Session, id: int, applicant: ApplicantBase):
    db_applicant = db.query(DBApplicant).filter(DBApplicant.id == id).first()
    if db_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not founds")

    db_applicant.first_name = applicant.first_name
    db_applicant.last_name = applicant.last_name
    db_applicant.middle_name = applicant.middle_name
    db_applicant.gender = applicant.gender
    db_applicant.date_of_birth = applicant.date_of_birth
    db_applicant.ssn = applicant.ssn
    db_applicant.email = applicant.email
    db_applicant.home_phone = applicant.home_phone
    db_applicant.mobile_phone = applicant.mobile_phone
    db_applicant.address = applicant.address
    db_applicant.city = applicant.city
    db_applicant.state = applicant.state
    db_applicant.zip = applicant.zip
    db_applicant.country = applicant.country
    db_applicant.date_of_birth = applicant.date_of_birth
    db_applicant.updated_at = datetime.now()
    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)

    return db_applicant


def create_item(db: Session, applicant: ApplicantBase):
    db_applicant = DBApplicant(**applicant.model_dump())
    db_applicant.created_at = datetime.now()
    db_applicant.updated_at = datetime.now()
    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)

    return db_applicant


def delete_item(db: Session, id: int):
    db_applicant = db.query(DBApplicant).filter(DBApplicant.id == id).first()
    if db_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not founds")

    db.query(DBApplicant).filter(DBApplicant.id == id).delete()
    db.commit()
