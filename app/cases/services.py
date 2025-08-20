from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.cases.models import DBCase
from app.cases.schemas import CaseCreate, CaseUpdate
from app.utils import get_next_page, get_page_count, get_prev_page


def get_items(db: Session, page_number: int, page_size: int):
    item_count = db.query(DBCase).count()
    items = db.query(DBCase).limit(page_size).offset(page_number * page_size).all()

    return {
        "items": items,
        "item_count": item_count,
        "page_count": get_page_count(item_count, page_size),
        "prev_page": get_prev_page(page_number),
        "next_page": get_next_page(item_count, page_number, page_size),
    }


def create_item(db: Session, case: CaseCreate):
    db_case = DBCase(**case.model_dump())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)

    return db_case


def get_item(db: Session, case_id: int):
    case = (
        db.query(DBCase)
        .options(joinedload(DBCase.applicant))
        .where(DBCase.id == case_id)
        .first()
    )

    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")

    # Handle case where applicant might be None
    applicant_data = None
    if case.applicant:
        applicant_data = {
            "id": case.applicant.id,
            "first_name": case.applicant.first_name,
            "last_name": case.applicant.last_name,
            "middle_name": case.applicant.middle_name,
            "email": case.applicant.email,
            "gender": case.applicant.gender,
            "date_of_birth": case.applicant.date_of_birth,
            "ssn": case.applicant.ssn,
            "home_phone": case.applicant.home_phone,
            "mobile_phone": case.applicant.mobile_phone,
            "address": case.applicant.address,
            "city": case.applicant.city,
            "state": case.applicant.state,
            "zip": case.applicant.zip,
            "country": case.applicant.country,
            "created_at": case.applicant.created_at,
            "updated_at": case.applicant.updated_at,
        }

    return {
        "id": case.id,
        "status": case.status,
        "applicant_id": case.applicant_id,
        "applicant": applicant_data,
        "assigned_to": case.assigned_to,
        "created_at": case.created_at,
        "updated_at": case.updated_at,
    }


def update_item(db: Session, id: int, case: CaseUpdate):
    db_case = db.query(DBCase).filter(DBCase.id == id).first()
    if db_case is None:
        raise HTTPException(status_code=404, detail="Case not found")

    if case.status is not None:
        db_case.status = case.status
    if case.assigned_to is not None:
        db_case.assigned_to = case.assigned_to

    db.add(db_case)
    db.commit()
    db.refresh(db_case)

    return db_case


def delete_item(db: Session, id: int):
    db_case = db.query(DBCase).filter(DBCase.id == id).first()
    if db_case is None:
        raise HTTPException(status_code=404, detail="Case not found")

    db.query(DBCase).filter(DBCase.id == id).delete()
    db.commit()

    return None
