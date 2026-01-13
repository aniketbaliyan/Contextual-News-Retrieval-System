from fastapi import APIRouter
from app.repository.news import fetch_articles
from app.schemas import NewsResponse
from app.formatter import format_article
from app.validation import ensure_results

router = APIRouter()

@router.get("/score", response_model=NewsResponse)
def by_score(min_score: float = 0.7):
    if min_score < 0 or min_score > 1:
        raise ValueError("min_score must be between 0 and 1")

    rows = fetch_articles(min_score=min_score, mode="score")

    ensure_results(rows)

    return {"articles": [format_article(r) for r in rows]}
