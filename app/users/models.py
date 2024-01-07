from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.db import Base


# SQLAlchemy Model
class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    display_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime, nullable=False)
    created_by = Column(String, nullable=False)
    modified = Column(DateTime, nullable=False)
    modified_by = Column(String, nullable=False)
