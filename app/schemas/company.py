from pydantic import BaseModel

class CompanyCreate(BaseModel):
    name: str
    location: str 