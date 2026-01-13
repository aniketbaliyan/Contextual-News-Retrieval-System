from fastapi import FastAPI

from app.api import (
    search,
    source,
    category,
    score,
    nearby,
    query,
)
from app.exception_handlers import register_exception_handlers


def create_app() -> FastAPI:
    app = FastAPI(
        title="Inshorts – Contextual News API",
        version="1.0.0",
        description="LLM-powered geo-aware news retrieval backend"
    )

    # ---- Core News APIs ----
    app.include_router(search.router, prefix="/api/v1/news", tags=["news"])
    app.include_router(source.router, prefix="/api/v1/news", tags=["news"])
    app.include_router(category.router, prefix="/api/v1/news", tags=["news"])
    app.include_router(score.router, prefix="/api/v1/news", tags=["news"])
    app.include_router(nearby.router, prefix="/api/v1/news", tags=["news"])

    # ---- Intelligent LLM Router ----
    app.include_router(query.router, prefix="/api/v1", tags=["intelligent"])

    # ---- Global Error Handling ----
    register_exception_handlers(app)

    return app


app = create_app()
