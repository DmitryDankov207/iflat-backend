from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api_v1.api import api_router
from config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Set all CORS enabled origins
allowed_origins = [str(origin) for origin in settings.BACKEND_CORS_ORIGINS]
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
