"""
API route definitions.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["health"])
async def health_check():
    """Return service health status."""
    return {"status": "healthy"}
