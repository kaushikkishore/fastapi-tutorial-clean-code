from fastapi import APIRouter
from interfaces.api.user.user_router import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/user", tags=["user"])
