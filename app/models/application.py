from sqlalchemy import Column, Integer, String, ForeignKey, func, DateTime
from app.models.base import Base
from sqlalchemy.orm import relationship

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    position = Column(String, nullable=False)
    source = Column(String)
    applied_at = Column(DateTime, default=func.now())
    notes = Column(String, nullable=True)
    status = Column(String, nullable=False)
    company = relationship("Company", back_populates="applications")