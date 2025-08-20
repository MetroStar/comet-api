from sqlalchemy import Boolean, Column, DateTime, Integer, String, func

from app.db import Base


# SQLAlchemy Model
class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    display_name = Column(String(200), nullable=False)
    email = Column(String(254), unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(100), nullable=False)
    modified = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    modified_by = Column(String(100), nullable=False)
