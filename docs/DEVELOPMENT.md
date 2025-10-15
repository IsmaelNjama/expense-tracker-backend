# Development Guide

## Setup

### Local Development

1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

### Running the Application

```bash
# Development server with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or using the main module
python -m app.main

# Or using the start script
./start.sh
```

## Code Structure

### Adding New Endpoints

1. Create route in `app/api/routes/`
2. Add business logic in `app/services/`
3. Define models in `app/models/schemas.py`
4. Update tests

### Example: Adding a new endpoint

```python
# app/api/routes/new_feature.py
from fastapi import APIRouter
from ...models.schemas import NewModel
from ...services.new_service import new_service

router = APIRouter(prefix="/new", tags=["new"])

@router.post("")
async def create_new(data: NewModel):
    return new_service.create(data)
```

## Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=app

# Run specific test file
python -m pytest tests/test_expenses.py
```

### Writing Tests

```python
# tests/test_new_feature.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_new():
    response = client.post("/new", json={"field": "value"})
    assert response.status_code == 200
```

## Code Style

### Formatting

- Use Black for code formatting
- Use isort for import sorting
- Follow PEP 8 guidelines

### Type Hints

- Use type hints for all function parameters and return values
- Use Pydantic models for data validation

### Documentation

- Add docstrings to all functions and classes
- Keep docstrings concise but descriptive
- Update API documentation when adding endpoints

## Docker Development

### Building

```bash
docker build -t cost-tracker-api .
```

### Running

```bash
docker run -p 8000:8000 -v $(pwd)/data:/app/data cost-tracker-api
```

## Debugging

### Common Issues

1. **Port already in use**: Change port in `main.py` or kill existing process
2. **Module not found**: Ensure you're running from project root
3. **CORS errors**: Update `CORS_ORIGINS` in `config.py`

### Logging

Add logging for debugging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

## Performance Considerations

### Future Improvements

- Database integration (PostgreSQL/SQLite)
- Redis caching
- Async database operations
- Connection pooling
