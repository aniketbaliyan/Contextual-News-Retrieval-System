from fastapi import APIRouter
from app.repository.news import fetch_articles
from app.schemas import NewsResponse
from app.formatter import format_article
from app.validation import ensure_results
from app.llm import summarize

router = APIRouter()

@router.get("/source", response_model=NewsResponse)
def by_source(source: str):
    if not source.strip():
        raise ValueError("Source cannot be empty")

    rows = fetch_articles(source=source, mode="source")

    ensure_results(rows)

    articles = []
    for r in rows:
        summary = summarize(r[0], r[1])
        articles.append(format_article(r, summary))

    return {"articles": articles}
