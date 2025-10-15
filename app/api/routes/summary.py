"""Summary-related API endpoints"""
from fastapi import APIRouter

from ...models.schemas import MonthlySummary
from ...services.summary_service import summary_service

router = APIRouter(tags=["summary"])


@router.get("/summary/{year}/{month}", response_model=MonthlySummary)
async def get_monthly_summary(year: int, month: int):
    """Get summary for a specific month and year"""
    return summary_service.get_monthly_summary(year, month)


@router.get("/current-summary", response_model=MonthlySummary)
async def get_current_month_summary():
    """Get summary for the current month"""
    return summary_service.get_current_month_summary()
