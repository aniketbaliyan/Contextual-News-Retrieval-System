from fastapi import APIRouter
from app.repository.news import fetch_articles
from app.schemas import NewsResponse
from app.formatter import format_article
from app.validation import ensure_results

router = APIRouter()

@router.get("/source", response_model=NewsResponse)
def by_source(source: str):
    if not source.strip():
        raise ValueError("Source cannot be empty")

    rows = fetch_articles(source=source, mode="source")

    ensure_results(rows)

    return {"articles": [format_article(r) for r in rows]}
