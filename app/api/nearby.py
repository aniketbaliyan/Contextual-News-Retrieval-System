from fastapi import APIRouter
from app.repository.news import fetch_articles
from app.schemas import NewsResponse
from app.formatter import format_article
from app.validation import validate_lat_lon, ensure_results
from app.llm import summarize

router = APIRouter()

@router.get("/nearby", response_model=NewsResponse)
def nearby(lat: float, lon: float):
    validate_lat_lon(lat, lon)

    rows = fetch_articles(lat=lat, lon=lon, mode="nearby")

    ensure_results(rows)
    
    articles = []
    for r in rows:
        summary = summarize(r[0], r[1])
        articles.append(format_article(r, summary))

    return {"articles": articles}