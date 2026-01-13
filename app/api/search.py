from fastapi import APIRouter
from app.repository.news import fetch_articles
from app.schemas import NewsResponse
from app.formatter import format_article
from app.validation import ensure_results
from app.llm import summarize

router = APIRouter()

@router.get("/search", response_model=NewsResponse)
def search(q: str):
    if not q.strip():
        raise ValueError("Query cannot be empty")


    rows = fetch_articles(keywords=q, mode="search")

    ensure_results(rows)

    articles = []
    for r in rows:
        summary = summarize(r[0], r[1])
        articles.append(format_article(r, summary))

    return {"articles": articles}
