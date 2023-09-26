from pydantic import BaseModel


# Pydantic Model
class Spacecraft(BaseModel):
    id: int
    name: str
    description: str | None = None
    affiliation: str | None = None
    dimensions: str | None = None
    appearances: int

    class Config:
        from_attributes = True
