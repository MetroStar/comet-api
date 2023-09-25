from sqlalchemy import Column, String, Integer
from app.db import Base

# SQLAlchemy Model
class DBSpacecraft(Base):
    __tablename__ = 'spacecraft'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    category = Column(String, nullable=True)
