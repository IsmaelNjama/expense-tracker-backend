# API Documentation

## Base URL

`http://localhost:8000`

## Authentication

No authentication required for this version.

## Endpoints

### Health Check

#### GET /

Check if the API is running.

**Response:**

```json
{
  "message": "Cost Tracker API",
  "status": "running"
}
```

### Expenses

#### POST /expenses

Create a new expense.

**Request Body:**

```json
{
  "description": "Dinner at restaurant",
  "amount": 45.5,
  "paid_by": "James",
  "date": "2024-01-15" // Optional, defaults to current date
}
```

**Response:**

```json
{
  "id": 1,
  "description": "Dinner at restaurant",
  "amount": 45.5,
  "paid_by": "James"
}
```

#### GET /expenses

Get all expenses.

**Response:**

```json
[
  {
    "id": 1,
    "description": "Dinner at restaurant",
    "amount": 45.5,
    "paid_by": "James"
  }
]
```

#### DELETE /expenses/{expense_id}

Delete an expense by ID.

**Response:**

```json
{
  "message": "Expense deleted"
}
```

### Friends

#### GET /friends

Get the list of friends.

**Response:**

```json
{
  "friends": ["Ismael", "Allan", "James"]
}
```

### Summary

#### GET /summary/{year}/{month}

Get monthly expense summary with settlement calculations.

**Parameters:**

- `year`: Year (e.g., 2024)
- `month`: Month (1-12)

**Response:**

```json
{
  "month": "January",
  "year": 2024,
  "total_expenses": 150.0,
  "expenses_by_person": {
    "James": 75.0,
    "Allan": 50.0,
    "Ismael": 25.0
  },
  "settlement": {
    "James": {
      "paid": 75.0,
      "should_pay": 50.0,
      "balance": 25.0
    },
    "Allan": {
      "paid": 50.0,
      "should_pay": 50.0,
      "balance": 0.0
    },
    "Ismael": {
      "paid": 25.0,
      "should_pay": 50.0,
      "balance": -25.0
    }
  }
}
```

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request

```json
{
  "detail": "Validation error message"
}
```

### 404 Not Found

```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error

```json
{
  "detail": "Internal server error"
}
```
