from pydantic import BaseModel
from typing import Optional

# Pydantic Model
class Spacecraft(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None

    class Config:
        from_attributes = True
