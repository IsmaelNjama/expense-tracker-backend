# Cost Tracker API

A FastAPI-based backend service for managing expenses and tracking costs among friends.

## Features

- **Expense Management**: Create, view, and delete expenses
- **Friend Management**: Manage a list of friends who share expenses
- **Monthly Summaries**: Generate monthly expense reports with settlement calculations
- **Balance Tracking**: Calculate who owes what to whom

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:
   ```bash
   python -m app.main
   ```
   Or use the provided script:
   ```bash
   ./start.sh
   ```

The API will be available at `http://localhost:8000`

### Docker Setup

Build and run with Docker:
```bash
docker build -t cost-tracker-api .
docker run -p 8000:8000 cost-tracker-api
```

## API Documentation

Once running, visit:
- **Interactive API docs**: `http://localhost:8000/docs`
- **ReDoc documentation**: `http://localhost:8000/redoc`

## Project Structure

```
expense-tracker-backend/
├── app/
│   ├── api/routes/          # API endpoint definitions
│   ├── core/                # Core configuration and storage
│   ├── models/              # Pydantic data models
│   ├── services/            # Business logic layer
│   └── main.py             # FastAPI application setup
├── data/                   # Data storage (JSON files)
├── tests/                  # Test files
└── requirements.txt        # Python dependencies
```

## API Endpoints

### Expenses
- `POST /expenses` - Create a new expense
- `GET /expenses` - Get all expenses
- `DELETE /expenses/{id}` - Delete an expense

### Friends
- `GET /friends` - Get list of friends

### Summary
- `GET /summary/{year}/{month}` - Get monthly expense summary

## Configuration

Edit `app/core/config.py` to configure:
- Friends list
- CORS origins
- Storage settings

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Development Dependencies
```bash
pip install -r requirements-dev.txt
```

## Data Storage

The application uses JSON file storage in the `data/` directory. Expenses are automatically saved and loaded on startup.