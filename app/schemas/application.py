from pydantic import BaseModel
from typing import Optional

class ApplicationCreate(BaseModel):
    company_id: int
    position: str
    source: Optional[str] = None
    notes: Optional[str] = None
    status: str

class ApplicationUpdate(BaseModel):
    position: Optional[str] = None
    source: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = None