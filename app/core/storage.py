"""Data persistence layer"""
import json
import os
from typing import List, Dict, Any
from .config import DATA_DIR, EXPENSES_FILE


class Storage:
    def __init__(self):
        self.expenses: List[Dict[str, Any]] = []
        self.counter: int = 1
        self.file_path = os.path.join(DATA_DIR, EXPENSES_FILE)
        self._ensure_data_dir()

    def _ensure_data_dir(self):
        """Ensure data directory exists"""
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

    def load(self) -> None:
        """Load data from JSON file if it exists"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    self.expenses = data.get("expenses", [])
                    self.counter = data.get("counter", 1)
            except Exception as e:
                print(f"Error loading data: {e}")

    def save(self) -> None:
        """Save data to JSON file"""
        try:
            with open(self.file_path, "w") as f:
                json.dump({
                    "expenses": self.expenses,
                    "counter": self.counter
                }, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def get_all_expenses(self) -> List[Dict[str, Any]]:
        """Get all expenses"""
        return self.expenses

    def add_expense(self, expense: Dict[str, Any]) -> Dict[str, Any]:
        """Add a new expense"""
        expense["id"] = self.counter
        self.expenses.append(expense)
        self.counter += 1
        self.save()
        return expense

    def delete_expense(self, expense_id: int) -> None:
        """Delete an expense by ID"""
        self.expenses = [
            exp for exp in self.expenses if exp["id"] != expense_id]
        self.save()


# Global storage instance
storage = Storage()
