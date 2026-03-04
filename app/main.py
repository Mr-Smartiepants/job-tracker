from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.database import router as database_router

app = FastAPI()

app.include_router(health_router, prefix="/api", tags=["health"])
app.include_router(database_router, prefix="/api/database", tags=["database"])
