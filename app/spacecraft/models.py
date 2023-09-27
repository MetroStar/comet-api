from sqlalchemy import Column, Integer, String

from app.db import Base


# SQLAlchemy Model
class DBSpacecraft(Base):
    __tablename__ = "spacecraft"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    affiliation = Column(String, nullable=True)
    dimensions = Column(String, nullable=True)
    appearances = Column(Integer, nullable=False)
