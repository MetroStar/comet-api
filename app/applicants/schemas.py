from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


# Pydantic Models
class ApplicantBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    gender: str
    date_of_birth: date
    ssn: str
    email: str | None = None
    home_phone: str | None = None
    mobile_phone: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    zip: str | None = None
    country: str = "USA"


class Applicant(ApplicantBase):
    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    created_at: datetime
    updated_at: datetime


class ApplicantPayload(BaseModel):
    items: list[Applicant]
    item_count: int = 0
    page_count: int = 0
    prev_page: int | None = None
    next_page: int | None = None
