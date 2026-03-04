## 2026-03-03

### Achieved
- Project structure initialized (`app/`, README, PROGRESS)
- Virtual environment created
- FastAPI and Uvicorn installed
- Minimal FastAPI application implemented
- `/health` endpoint created
- Server successfully started via `uvicorn app.main:app --reload`
- Swagger documentation verified at `/docs`

### Learned
- How to properly import and instantiate FastAPI
- How ASGI apps are structured
- How uvicorn references modules (`module:app_instance`)
- Basic understanding of automatic OpenAPI/Swagger documentation

### Next Step
- Add configuration handling (environment variables)
- Introduce PostgreSQL via Docker

## 2026-03-04

### Achieved
- Refactored API structure to use FastAPI routers
- Introduced modular routing architecture
- Added API prefix `/api`
- Swagger documentation grouping via tags
- Added requirements.txt for reproducible installs

### Learned
- How FastAPI routers work
- Difference between app instance and router
- How to structure endpoints in larger projects

### Next Steps
- Introduce PostgreSQL database
- Set up Docker container for database
- Add SQLAlchemy for ORM layer

## 2026-03-04

### Achieved
- Added PostgreSQL database via Docker Compose
- Created persistent database volume
- Introduced SQLAlchemy engine and session factory
- Implemented database router
- Added `/api/database/health` endpoint
- Verified database connectivity via SQL query

### Learned
- Docker Compose basics
- Container naming conventions
- Difference between SQLAlchemy engine and session
- How to test database connectivity from FastAPI

### Next Steps
- Define first database models
- Introduce SQLAlchemy declarative base
- Create tables for job tracking domain (companies, applications)