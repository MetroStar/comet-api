from pydantic import BaseModel
from typing import Optional

# Pydantic Model
class Spacecraft(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    affiliation: Optional[str] = None
    dimensions: Optional[str] = None
    appearances: int

    class Config:
        from_attributes = True
