from pydantic import BaseModel, ConfigDict


# Pydantic Models
class Spacecraft(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    name: str
    description: str | None = None
    affiliation: str | None = None
    dimensions: str | None = None
    appearances: int = 1


class SpacecraftPayload(BaseModel):
    items: list[Spacecraft]
    item_count: int = 0
    page_count: int = 0
    prev_page: int | None = None
    next_page: int | None = None
