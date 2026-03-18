from fastapi import APIRouter
from app.database.connection import SessionLocal
from app.models.application import Application
from app.schemas.application import ApplicationCreate
from app.schemas.application import ApplicationUpdate
from app.schemas.application import ApplicationRead
from sqlalchemy.orm import joinedload

router = APIRouter()

@router.post("/")
def create_application(application: ApplicationCreate):
    db = SessionLocal()

    try:
        db_application = Application(
            company_id=application.company_id,
            position=application.position,
            source=application.source,
            notes=application.notes,
            status="applied"
        )
        db.add(db_application)
        db.commit()
        db.refresh(db_application)
        return db_application
    
    finally:
        db.close()

@router.get("/", response_model=list[ApplicationRead])
def get_applications():
    db = SessionLocal()

    try:
        applications = db.query(Application).options(joinedload(Application.company)).all()
        return applications
    
    finally:
        db.close()

@router.get("/{application_id}", response_model=ApplicationRead)
def get_application(application_id: int):
    db = SessionLocal()

    try:
        application = db.query(Application).options(joinedload(Application.company)).filter(Application.id == application_id).first()

        if application is None:
            return {"error": "Application not found"}
        
        return application
    
    finally:
        db.close()

@router.patch("/{application_id}")
def update_application(application_id: int, application_update: ApplicationUpdate):
    db = SessionLocal()

    try:
        application = db.query(Application).filter(Application.id == application_id).first()

        if application is None:
            return {"error": "Application not found"}

        if application_update.position is not None:
            application.position = application_update.position

        if application_update.source is not None:
            application.source = application_update.source

        if application_update.notes is not None:
            application.notes = application_update.notes

        if application_update.status is not None:
            application.status = application_update.status

        db.commit()
        db.refresh(application)

        return application

    finally:
        db.close()    