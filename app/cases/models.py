from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


# SQLAlchemy Model
class DBCase(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
    assigned_to = Column(String, nullable=True)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    applicant_id = Column(
        Integer, ForeignKey("applicants.id", ondelete="CASCADE"), nullable=False
    )
    applicant = relationship("DBApplicant", back_populates="case")
