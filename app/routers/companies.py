from fastapi import APIRouter
from app.database.connection import SessionLocal
from app.models.company import Company
from app.schemas.company import CompanyCreate
from app.schemas.company import CompanyUpdate
from app.models.application import Application
from app.schemas.application import ApplicationRead

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

@router.get("/")
def get_companies():
    db = SessionLocal()

    try:
        companies = db.query(Company).all()
        return companies
    finally:
        db.close()

@router.get("/{company_id}")
def get_company(company_id: int):
    db = SessionLocal()

    try:
        company = db.query(Company).filter(Company.id == company_id).first()

        if company is None:
            return {"error": "Company not found"}

        return company

    finally:
        db.close()

@router.delete("/{company_id}")
def delete_company(company_id: int):
    db = SessionLocal()

    try:
        company = db.query(Company).filter(Company.id == company_id).first()

        if company is None:
            return {"error": "Company not found"}

        db.delete(company)
        db.commit()

        return {"message": "Company deleted"}

    finally:
        db.close()

@router.patch("/{company_id}")
def update_company(company_id: int, company_update: CompanyUpdate):
    db = SessionLocal()

    try:
        company = db.query(Company).filter(Company.id == company_id).first()

        if company is None:
            return {"error": "Company not found"}

        if company_update.name is not None:
            company.name = company_update.name

        if company_update.location is not None:
            company.location = company_update.location

        db.commit()
        db.refresh(company)

        return company

    finally:
        db.close()

@router.get("/{company_id}/applications", response_model=list[ApplicationRead])
def get_applications_for_company(company_id: int):
    db = SessionLocal()

    try:
        company = db.query(Company).filter(Company.id == company_id).first()
        
        if company is None:
            return {"error": "Company not found"}
        
        applications = db.query(Application).options(joinedload(Application.company)).filter(Application.company_id == company_id).all()
        return applications
    
    finally:
        db.close()