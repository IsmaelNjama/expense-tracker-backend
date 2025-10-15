"""Friends-related API endpoints"""
from fastapi import APIRouter

from ...services.expense_service import expense_service

router = APIRouter(tags=["friends"])


@router.get("/friends")
async def get_friends():
    """Get list of friends"""
    return {"friends": expense_service.get_friends()}
