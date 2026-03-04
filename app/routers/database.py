from fastapi import APIRouter
from app.database.connection import SessionLocal
from sqlalchemy import text


router = APIRouter()


@router.get("/health")
def database_health():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))
        return {"database": "ok"}
    finally: 
        db.close()



