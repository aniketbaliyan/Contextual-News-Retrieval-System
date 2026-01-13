from fastapi import APIRouter
from app.router import route
from app.schemas import NewsResponse
from app.formatter import format_article
from app.llm import summarize

router = APIRouter()

@router.get("/query", response_model=NewsResponse)
def smart_query(q: str, lat: float = None, lon: float = None):
    rows = route(q, lat, lon)

    articles = []
    for r in rows:
        summary = summarize(r[0], r[1])
        articles.append(format_article(r, summary))

    return {"articles": articles}
