from pydantic import BaseModel
from typing import Optional

class CompanyCreate(BaseModel):
    name: str
    location: Optional[str] = None 

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None

class CompanyRead(BaseModel):
    id: int
    name: str
    location: str | None = None

    class Config:
        from_attributes = True
