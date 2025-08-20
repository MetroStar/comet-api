from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from app.applicants.schemas import ApplicantResponse

# Constants
CASE_STATUS = Literal["Not Started", "In Progress", "Approved", "Denied"]


# Pydantic Models
class CaseBase(BaseModel):
    status: CASE_STATUS
    assigned_to: str | None = Field(None, min_length=1, max_length=255)


class CaseCreate(CaseBase):
    applicant_id: int


class CaseUpdate(BaseModel):
    status: CASE_STATUS | None = None
    assigned_to: str | None = None


class CaseResponse(CaseBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    applicant_id: int
    created_at: datetime
    updated_at: datetime


class CaseWithApplicant(CaseResponse):
    applicant: ApplicantResponse | None = None


class CaseListResponse(BaseModel):
    items: list[CaseWithApplicant]
    item_count: int
    page_count: int
    prev_page: int | None = None
    next_page: int | None = None
