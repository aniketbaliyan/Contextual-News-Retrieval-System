from fastapi import APIRouter
from app.repository.news import fetch_articles
from app.schemas import NewsResponse
from app.formatter import format_article
from app.validation import ensure_results

router = APIRouter()

@router.get("/category", response_model=NewsResponse)
def by_category(category: str):
    if not category.strip():
        raise ValueError("Category cannot be empty")

    rows = fetch_articles(category=category, mode="category")

    ensure_results(rows)

    return {"articles": [format_article(r) for r in rows]}
