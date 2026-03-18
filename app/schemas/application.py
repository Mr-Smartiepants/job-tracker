from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.company import CompanyRead

class ApplicationCreate(BaseModel):
    company_id: int
    position: str
    source: Optional[str] = None
    notes: Optional[str] = None

class ApplicationUpdate(BaseModel):
    position: Optional[str] = None
    source: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = None

class ApplicationRead(BaseModel):
    id: int 
    company_id: int
    position: str
    source: Optional[str] = None
    applied_at: datetime
    notes: Optional[str] = None
    status: str
    company: CompanyRead

    class Config:
        from_attributes = True