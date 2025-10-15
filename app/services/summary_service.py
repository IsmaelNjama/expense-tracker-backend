"""Business logic for summary calculations"""
from typing import Dict, Any
from datetime import datetime

from ..core.config import FRIENDS
from ..core.storage import storage
from ..models.schemas import MonthlySummary, PersonBalance


class SummaryService:

    @staticmethod
    def get_monthly_summary(year: int, month: int) -> Dict[str, Any]:
        """Calculate monthly summary for a given year/month"""
        # Filter expenses for the given month/year
        all_expenses = storage.get_all_expenses()
        month_expenses = [
            exp for exp in all_expenses
            if datetime.strptime(exp["date"], "%Y-%m-%d").year == year and
            datetime.strptime(exp["date"], "%Y-%m-%d").month == month
        ]

        total_expenses = sum(exp["amount"] for exp in month_expenses)

        # Calculate expenses by person
        expenses_by_person = {friend: 0 for friend in FRIENDS}
        for exp in month_expenses:
            expenses_by_person[exp["paid_by"]] += exp["amount"]

        # Calculate settlement (how much each person owes/is owed)
        per_person_share = total_expenses / len(FRIENDS)
        settlement = {}

        for friend in FRIENDS:
            paid = expenses_by_person[friend]
            owes = per_person_share - paid
            settlement[friend] = {
                "paid": paid,
                "should_pay": per_person_share,
                "balance": -owes  # negative means they owe money, positive means they're owed money
            }

        return {
            "month": f"{year}-{month:02d}",
            "year": year,
            "total_expenses": total_expenses,
            "expenses_by_person": expenses_by_person,
            "settlement": settlement
        }

    @staticmethod
    def get_current_month_summary() -> Dict[str, Any]:
        """Get summary for the current month"""
        now = datetime.now()
        return SummaryService.get_monthly_summary(now.year, now.month)


summary_service = SummaryService()  # Global service instance
