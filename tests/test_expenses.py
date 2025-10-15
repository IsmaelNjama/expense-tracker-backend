"""Test cases for expense endpoints"""
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.storage import storage

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_storage():
    """Reset storage before each test"""
    storage.expenses = []
    storage.counter = 1
    yield
    storage.expenses = []
    storage.counter = 1


def test_create_expense():
    """Test creating a new expense"""
    response = client.post(
        "/expenses",
        json={
            "description": "Groceries",
            "amount": 50.0,
            "paid_by": "Ismael",
            "date": "2024-01-15"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Groceries"
    assert data["amount"] == 50.0
    assert data["paid_by"] == "Ismael"
    assert data["id"] == 1


def test_create_expense_invalid_friend():
    """Test creating expense with invalid friend name"""
    response = client.post(
        "/expenses",
        json={
            "description": "Groceries",
            "amount": 50.0,
            "paid_by": "InvalidName"
        }
    )
    assert response.status_code == 400


def test_get_expenses():
    """Test getting all expenses"""
    # Create some expenses
    client.post(
        "/expenses",
        json={"description": "Test 1", "amount": 10.0, "paid_by": "Ismael"}
    )
    client.post(
        "/expenses",
        json={"description": "Test 2", "amount": 20.0, "paid_by": "Allan"}
    )

    response = client.get("/expenses")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_delete_expense():
    """Test deleting an expense"""
    # Create an expense
    create_response = client.post(
        "/expenses",
        json={"description": "Test", "amount": 10.0, "paid_by": "Ismael"}
    )
    expense_id = create_response.json()["id"]

    # Delete it
    delete_response = client.delete(f"/expenses/{expense_id}")
    assert delete_response.status_code == 200

    # Verify it's deleted
    get_response = client.get("/expenses")
    assert len(get_response.json()) == 0


def test_get_friends():
    """Test getting friends list"""
    response = client.get("/friends")
    assert response.status_code == 200
    data = response.json()
    assert "friends" in data
    assert len(data["friends"]) == 3
    assert "Ismael" in data["friends"]
