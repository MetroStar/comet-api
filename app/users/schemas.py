from datetime import datetime

from pydantic import BaseModel, ConfigDict


# Pydantic Models
class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    user_id: str
    first_name: str
    last_name: str
    display_name: str
    email: str
    is_active: bool = True
    created: datetime | None = None
    created_by: str
    modified: datetime | None = None
    modified_by: str


class UserPayload(BaseModel):
    items: list[User]
    item_count: int = 0
    page_count: int = 0
    prev_page: int | None = None
    next_page: int | None = None
