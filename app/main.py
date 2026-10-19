from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import chat, health
from app.config import get_settings
from app.db.engine import close_db, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    if settings.database_url:
        await init_db()
    yield
    await close_db()


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, lifespan=lifespan)
    app.include_router(health.router)
    app.include_router(chat.router)
    return app


app = create_app()

