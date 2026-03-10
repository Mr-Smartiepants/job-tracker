from fastapi import APIRouter
from app.database.connection import SessionLocal
from app.models.company import Company
from app.schemas.company import CompanyCreate

router = APIRouter()

@router.post("/")
def create_company(company: CompanyCreate):
    db = SessionLocal()

    try:
        db_company = Company(
            name=company.name,
            location=company.location
        )

        db.add(db_company)
        db.commit()
        db.refresh(db_company)

        return db_company

    finally:
        db.close()