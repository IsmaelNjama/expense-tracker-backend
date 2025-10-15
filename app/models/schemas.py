"""Pydantic models for request/response validation"""
from pydantic import BaseModel
from typing import Optional, Dict, List


class ExpenseCreate(BaseModel):
    """Model for creating a new expense"""
    description: str
    amount: float
    paid_by: str
    date: Optional[str] = None


class Expense(BaseModel):
    """Model representing an expense"""
    id: int
    description: str
    amount: float
    paid_by: str


class PersonBalance(BaseModel):
    """Model representing a person's balance"""
    paid: float
    balance: float
    should_pay: float


class MonthlySummary(BaseModel):
    """Model for monthly summary of expenses"""
    month: str
    year: int
    total_expenses: float
    expenses_by_person: Dict[str, float]
    settlement: Dict[str, PersonBalance]
