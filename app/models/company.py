from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Company(Base):
    __tablename__="companies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String)