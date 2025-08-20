from sqlalchemy import Column, Date, DateTime, Integer, String, Text, func
from sqlalchemy.orm import relationship

from app.db import Base


class DBApplicant(Base):
    __tablename__ = "applicants"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), index=True, nullable=False)
    last_name = Column(String(50), index=True, nullable=False)
    middle_name = Column(String(50), nullable=True)
    gender = Column(String(20), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    ssn = Column(String(11), nullable=False, unique=True)
    email = Column(String(254), nullable=True)
    home_phone = Column(String(20), nullable=True)
    mobile_phone = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(50), nullable=True)
    zip = Column(String(10), nullable=True)
    country = Column(String(100), nullable=False)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    case = relationship("DBCase", back_populates="applicant")
