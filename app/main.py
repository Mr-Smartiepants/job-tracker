from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.database import router as database_router
from app.database.connection import engine
from app.models.base import Base

from app.models.company import Company
from app.routers.companies import router as companies_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(health_router, prefix="/api", tags=["health"])
app.include_router(database_router, prefix="/api/database", tags=["database"])
app.include_router(companies_router, prefix="/api/companies", tags=["companies"])
