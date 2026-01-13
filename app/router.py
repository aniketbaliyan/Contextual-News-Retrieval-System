from app.llm import parse_query
from app.repository.news import fetch_articles

def route(query, lat=None, lon=None):
    parsed = parse_query(query)
    print("Parsed query:", parsed)

    return fetch_articles(
        keywords=parsed.get("keywords"),
        source=parsed.get("source"),
        category=parsed.get("category"),
        min_score=parsed.get("min_score"),
        lat=lat,
        lon=lon,
        mode=parsed.get("intent", "search")
    )
