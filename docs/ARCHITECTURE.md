# Architecture Documentation

## Overview

The Cost Tracker API follows a layered architecture pattern with clear separation of concerns:

```
┌─────────────────┐
│   API Routes    │  ← HTTP endpoints
├─────────────────┤
│    Services     │  ← Business logic
├─────────────────┤
│     Models      │  ← Data validation
├─────────────────┤
│    Storage      │  ← Data persistence
└─────────────────┘
```

## Components

### API Layer (`app/api/routes/`)
- **Purpose**: Handle HTTP requests and responses
- **Files**: `expenses.py`, `friends.py`, `summary.py`
- **Responsibilities**:
  - Request validation
  - Response formatting
  - HTTP status codes
  - Route definitions

### Service Layer (`app/services/`)
- **Purpose**: Business logic and data processing
- **Files**: `expense_service.py`, `summary_service.py`
- **Responsibilities**:
  - Expense CRUD operations
  - Balance calculations
  - Monthly summaries
  - Data transformations

### Models Layer (`app/models/`)
- **Purpose**: Data validation and serialization
- **Files**: `schemas.py`
- **Responsibilities**:
  - Request/response validation
  - Type definitions
  - Data contracts

### Core Layer (`app/core/`)
- **Purpose**: Application configuration and storage
- **Files**: `config.py`, `storage.py`
- **Responsibilities**:
  - Configuration management
  - File-based storage
  - Data persistence

## Data Flow

1. **Request**: Client sends HTTP request to API endpoint
2. **Validation**: Pydantic models validate request data
3. **Processing**: Service layer processes business logic
4. **Storage**: Data is persisted to JSON files
5. **Response**: Validated response sent back to client

## Storage Strategy

### File-based Storage
- **Format**: JSON files in `data/` directory
- **Benefits**: Simple, no database setup required
- **Limitations**: Not suitable for high concurrency

### Data Structure
```json
{
  "expenses": [
    {
      "id": 1,
      "description": "Expense description",
      "amount": 50.0,
      "paid_by": "Friend name",
      "date": "2024-01-15"
    }
  ]
}
```

## Configuration Management

### Environment-based Config
- Friends list defined in `config.py`
- CORS origins configurable
- Storage paths configurable

### Future Enhancements
- Environment variables support
- Database integration
- Authentication/authorization
- Caching layer