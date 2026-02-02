from fastapi import APIRouter
from api.v1.routers.ebay import router as ebay_router

router = APIRouter(prefix="/api/v1")

router.include_router(ebay_router)
