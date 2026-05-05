from fastapi import FastAPI

from app.api.routes import router as api_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        debug=settings.DEBUG,
    )
    app.include_router(api_router, prefix=settings.API_PREFIX)
    return app


app = create_app()
