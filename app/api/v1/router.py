from fastapi import APIRouter
from app.api.v1.squarespace.controllers import router as squarespace_router

router = APIRouter(prefix="/v1")

router.include_router(squarespace_router, prefix="/squarespace", tags=["squarespace"])