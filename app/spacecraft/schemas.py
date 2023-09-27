from pydantic import BaseModel, ConfigDict


# Pydantic Model
class Spacecraft(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str | None = None
    affiliation: str | None = None
    dimensions: str | None = None
    appearances: int
