from fastapi import APIRouter
from app.routers import wikipedia, saved_articles

api_router = APIRouter()
api_router.include_router(wikipedia.router, prefix="/wikipedia", tags=["wikipedia"])
api_router.include_router(saved_articles.router, prefix="/saved-articles", tags=["saved-articles"])
