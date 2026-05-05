# FastAPIProject

Skeleton for a FastAPI web app.

## Project layout

```text
app/
  api/          API route definitions
  core/         Settings and shared configuration
  models/       Database models
  schemas/      Pydantic request/response schemas
  services/     Business logic
tests/          Test suite
```

## Local setup

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Create local environment settings:

```bash
cp .env.example .env
```

Run the app:

```bash
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs`.

## Run with Docker

Build and start the app:

```bash
docker compose up --build
```

Then open `http://127.0.0.1:8000/docs`.

Stop the container with `Ctrl+C`.

## Tests

```bash
pytest
```
