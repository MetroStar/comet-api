from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# Pydantic Models
class UserBase(BaseModel):
    user_id: str = Field(..., min_length=1, max_length=100)
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    display_name: str = Field(..., min_length=1, max_length=200)
    email: str = Field(..., min_length=1, max_length=254)
    is_active: bool = True
    created_by: str = Field(..., min_length=1, max_length=100)
    modified_by: str = Field(..., min_length=1, max_length=100)


class UserCreate(UserBase):
    hashed_password: str | None = None


class UserUpdate(BaseModel):
    user_id: str | None = Field(None, min_length=1, max_length=100)
    first_name: str | None = Field(None, min_length=1, max_length=100)
    last_name: str | None = Field(None, min_length=1, max_length=100)
    display_name: str | None = Field(None, min_length=1, max_length=200)
    email: str | None = Field(None, min_length=1, max_length=254)
    is_active: bool | None = None
    modified_by: str | None = Field(None, min_length=1, max_length=100)


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created: datetime
    modified: datetime


class UserListResponse(BaseModel):
    items: list[UserResponse]
    item_count: int = 0
    page_count: int = 0
    prev_page: int | None = None
    next_page: int | None = None
