from sqlalchemy import Column, Integer, String
from app.models.base import Base
from sqlalchemy.orm import relationship
class Company(Base):
    __tablename__="companies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    applications = relationship("Application", back_populates="company")
    location = Column(String)