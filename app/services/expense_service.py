"""Business logic for expense operations"""
from typing import List, Dict, Any
from datetime import datetime
from fastapi import HTTPException

from ..core.config import FRIENDS
from ..core.storage import storage
from ..models.schemas import ExpenseCreate, Expense


class ExpenseService:

    @staticmethod
    def create_expense(expense_data: ExpenseCreate) -> Dict[str, Any]:
        """Create a new expense"""
        if expense_data.paid_by not in FRIENDS:
            raise HTTPException(status_code=400, detail="Invalid friend name")

        new_expense = {
            "description": expense_data.description,
            "amount": expense_data.amount,
            "paid_by": expense_data.paid_by,
            "date": expense_data.date or datetime.now().strftime("%Y-%m-%d")
        }

        return storage.add_expense(new_expense)

    @staticmethod
    def get_all_expenses() -> List[Dict[str, Any]]:
        """Get all expenses"""
        return storage.get_all_expenses()

    @staticmethod
    def delete_expense(expense_id: int) -> None:
        """Delete an expense"""
        storage.delete_expense(expense_id)

    @staticmethod
    def get_friends() -> List[str]:
        """Get list of friends"""
        return FRIENDS


expense_service = ExpenseService()  # Global service instance
