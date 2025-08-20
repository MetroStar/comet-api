from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


# Pydantic Models
class ApplicantBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    middle_name: str | None = Field(None, min_length=1, max_length=50)
    gender: str = Field(..., min_length=1, max_length=20)
    date_of_birth: date
    ssn: str = Field(..., min_length=9, max_length=11)
    email: str | None = Field(None, max_length=254)
    home_phone: str | None = Field(None, max_length=20)
    mobile_phone: str | None = Field(None, max_length=20)
    address: str | None = Field(None, max_length=200)
    city: str | None = Field(None, max_length=100)
    state: str | None = Field(None, max_length=50)
    zip: str | None = Field(None, max_length=10)
    country: str = Field("USA", max_length=100)


class ApplicantCreate(ApplicantBase):
    pass


class ApplicantUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    gender: str | None = None
    date_of_birth: date | None = None
    ssn: str | None = None
    email: str | None = None
    home_phone: str | None = None
    mobile_phone: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    zip: str | None = None
    country: str | None = None


class ApplicantResponse(ApplicantBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    updated_at: datetime


class ApplicantListResponse(BaseModel):
    items: list[ApplicantResponse]
    item_count: int = 0
    page_count: int = 0
    prev_page: int | None = None
    next_page: int | None = None
