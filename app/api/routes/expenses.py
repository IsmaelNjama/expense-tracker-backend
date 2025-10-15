"""Expense-related API endpoints"""
from fastapi import APIRouter
from typing import List

from ...models.schemas import ExpenseCreate, Expense
from ...services.expense_service import expense_service

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post("", response_model=Expense)
async def create_expense(expense: ExpenseCreate):
    """Create a new expense"""
    return expense_service.create_expense(expense)


@router.get("", response_model=List[Expense])
async def get_expenses():
    """Get all expenses"""
    return expense_service.get_all_expenses()


@router.delete("/{expense_id}")
async def delete_expense(expense_id: int):
    """Delete an expense by ID"""
    expense_service.delete_expense(expense_id)
    return {"message": "Expense deleted"}
