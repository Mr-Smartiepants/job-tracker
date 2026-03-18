from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.database import router as database_router
from app.database.connection import engine
from app.models.base import Base
from app.models.application import Application
from app.models.company import Company
from app.routers.companies import router as companies_router
from app.routers.applications import router as applications_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(health_router, prefix="/api", tags=["health"])
app.include_router(database_router, prefix="/api/database", tags=["database"])
app.include_router(companies_router, prefix="/api/companies", tags=["companies"])
app.include_router(applications_router, prefix="/api/applications", tags=["applications"])

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")