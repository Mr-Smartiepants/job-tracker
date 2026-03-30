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


## 🚀 Getting Started

Follow these steps to run the Job Tracker locally.

### 1. Navigate to the project directory

```bash
cd job-tracker
````

### 2. Activate virtual environment

```bash
source venv/bin/activate
```

### 3. Start the database (Docker)

```bash
docker compose up -d
```

Optional: Check if the container is running

```bash
docker compose ps
```

### 4. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

### 5. Open in browser

Frontend:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

API docs (Swagger):
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🛑 Stopping the application

Stop FastAPI server:

```bash
CTRL + C
```

Stop Docker containers:

```bash
docker compose down
```

## 🧠 Notes

* Make sure Docker is running before starting the database
* The database data is persisted via Docker volumes
* The `--reload` flag automatically restarts the server on code changes

```

---

Jetzt hast du **ein einziges, sauberes Markdown-Stück**, das direkt in deine README passt.

Wenn du willst, machen wir als nächstes den oberen Teil deiner README richtig stark (Projektbeschreibung + Features), damit das Ding auch für Bewerbungen richtig knallt.
```
