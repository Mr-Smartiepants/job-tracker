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

## 2026-03-10

### Achieved
- Introduced SQLAlchemy ORM models
- Created `Company` database model
- Implemented `CompanyCreate` API schema
- Added `POST /api/companies` endpoint
- Successfully persisted company data to PostgreSQL
- Verified DB writes via Swagger and direct SQL query

### Learned
- Difference between ORM models and API schemas
- SQLAlchemy session workflow (`add`, `commit`, `refresh`)
- FastAPI request validation with Pydantic
- Full request flow: API → Schema → Model → Database

### Next Steps
- Implement `GET /companies` endpoint
- Introduce response schemas
- Add relationship between companies and applications

## 2026-03-11

### Achieved
- Implemented full CRUD functionality for `Company`
- Added `GET /api/companies` endpoint to retrieve all companies
- Added `GET /api/companies/{company_id}` endpoint to retrieve a single company
- Added `PATCH /api/companies/{company_id}` endpoint to update company data
- Added `DELETE /api/companies/{company_id}` endpoint to remove companies
- Introduced `CompanyUpdate` schema for partial updates
- Verified update and delete operations via Swagger

### Learned
- Difference between `PUT` and `PATCH` in REST APIs
- How to perform filtered queries with SQLAlchemy (`filter`, `first`)
- How to update ORM objects and persist changes (`commit`, `refresh`)
- How to safely delete database records with SQLAlchemy sessions
- How CRUD operations map to HTTP methods in RESTful APIs

### Next Steps
- Design and implement the `Application` model
- Introduce a relationship between `Company` and `Application`
- Implement CRUD endpoints for job applications
- Add response schemas for cleaner API responses