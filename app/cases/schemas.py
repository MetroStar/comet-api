from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.applicants.schemas import Applicant


# Pydantic Models
class Case(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    status: str
    assigned_to: str | None = None
    created_at: datetime
    updated_at: datetime
    applicant_id: int | None = None


class CaseWithApplicant(BaseModel):
    id: int
    status: str
    assigned_to: str | None = None
    created_at: datetime
    updated_at: datetime
    applicant: Applicant | None = None


class CasePayload(BaseModel):
    items: list[CaseWithApplicant]
    item_count: int = 0
    page_count: int = 0
    prev_page: int | None = None
    next_page: int | None = None
