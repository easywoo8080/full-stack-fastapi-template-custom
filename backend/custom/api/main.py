from fastapi import APIRouter

from ..core.config import settings
from .example.routers import routers as example_router
api_router = APIRouter()


# # 2025-05-23 : create a new router
api_router.include_router(example_router.router)

# local환경에서만 라우터를 포함
if settings.ENVIRONMENT == "local":
    pass
