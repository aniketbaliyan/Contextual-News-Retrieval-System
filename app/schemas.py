from pydantic import BaseModel
from typing import List

class Article(BaseModel):
    title: str
    description: str
    url: str
    publication_date: str
    source_name: str
    category: list[str]
    relevance_score: float
    llm_summary: str | None = None

class NewsResponse(BaseModel):
    articles: List[Article]
