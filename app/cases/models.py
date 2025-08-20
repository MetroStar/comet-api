from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from app.db import Base


# SQLAlchemy Model
class DBCase(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable=False)
    assigned_to = Column(String(255), nullable=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    applicant_id = Column(
        Integer, ForeignKey("applicants.id", ondelete="CASCADE"), nullable=False
    )
    applicant = relationship("DBApplicant", back_populates="case")
