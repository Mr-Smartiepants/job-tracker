# Job Application Tracker API

A production-oriented REST API for tracking job applications.

The goal of this project is to build a structured backend application using modern Python backend practices.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- PostgreSQL (planned)
- Docker (planned)

## Current Features

- FastAPI application structure
- Router architecture
- Health endpoint
- Swagger/OpenAPI documentation

## API

Example endpoint:

GET /api/health

Returns:

{
  "status": "online"
}

## Project Goals

- User authentication (JWT)
- Application tracking
- Company management
- PostgreSQL integration
- Docker containerization

## Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload