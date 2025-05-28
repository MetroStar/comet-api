from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class DBApplicant(Base):
    __tablename__ = "applicants"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    gender = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    ssn = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    home_phone = Column(String, nullable=True)
    mobile_phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    zip = Column(String, nullable=True)
    country = Column(String, nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    case = relationship("DBCase", back_populates="applicant")
