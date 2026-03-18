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

## 2026-03-18

### Achieved
- Implemented `Application` database model with foreign key to `Company`
- Introduced relational structure (Company 1 → n Applications)
- Added `ApplicationCreate` and `ApplicationUpdate` schemas
- Implemented `POST /api/applications` endpoint
- Implemented `GET /api/applications` endpoint
- Implemented `GET /api/applications/{id}` endpoint
- Implemented `PATCH /api/applications/{id}` endpoint
- Implemented `GET /api/companies/{company_id}/applications` endpoint
- Verified relational integrity via foreign key constraints

### Learned
- How to design and implement relational database models
- How foreign keys enforce data integrity
- How to structure APIs beyond basic CRUD (resource relationships)
- Early return pattern for cleaner control flow
- Difference between querying by primary key vs foreign key

### Next Steps
- Implement `DELETE /api/applications/{id}`
- Introduce proper error handling (HTTP status codes)
- Add response schemas for cleaner API output
- Improve data validation (e.g. status as Enum)

## 2026-03-18

### Achieved
- Implemented basic frontend (`index.html`) served via FastAPI
- Displayed applications dynamically using `fetch` and DOM manipulation
- Integrated `GET /api/companies` into frontend (dropdown population)
- Built application form for creating new entries
- Implemented logic to:
  - select existing company via dropdown
  - create new company via `POST /api/companies`
  - dynamically resolve `company_id` in frontend
- Removed status from create flow and set default `"applied"` in backend
- Fixed validation issue by making `location` optional in Company schema

### Learned
- How frontend and backend interact in a full request cycle
- How Pydantic validation errors can break frontend logic
- Difference between browser validation (`required`) and custom JS validation
- Handling conditional workflows (existing vs new entity creation)
- Importance of debugging full data flow (form → JS → API → DB)

### Next Steps
- Complete `POST /api/applications` integration in frontend
- Reset form after successful submission
- Reload application list after creating a new entry
- Add status update via `PATCH` (UI dropdown per application)