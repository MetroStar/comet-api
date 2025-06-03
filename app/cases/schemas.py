from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict

from app.applicants.schemas import Applicant


# Pydantic Models
class CaseBase(BaseModel):
    status: Literal["Not Started", "In Progress", "Approved", "Denied"]
    assigned_to: str | None = None
    applicant_id: int | None = None


class Case(CaseBase):
    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    created_at: datetime
    updated_at: datetime


class CaseWithApplicant(Case):
    applicant: Applicant | None = None


class CasePayload(BaseModel):
    items: list[CaseWithApplicant]
    item_count: int = 0
    page_count: int = 0
    prev_page: int | None = None
    next_page: int | None = None
