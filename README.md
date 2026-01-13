# Inshorts – Contextual News Retrieval System

A backend system that fetches, ranks, and enriches news articles using text search, geospatial queries, and an LLM.

It simulates how modern news platforms (Google News, Bloomberg, Perplexity) combine databases and AI to deliver contextual news.

------------------------------------------------------

FEATURES

• Five retrieval modes
  - Search
  - Source
  - Category
  - Relevance score
  - Nearby (geo-based)

• LLM-powered query understanding  
  The system uses an LLM to extract intent, entities, and constraints from user queries.

• Hybrid ranking  
  Combines editorial relevance_score with full-text search ranking.

• Geospatial search  
  Uses PostGIS to rank articles by physical distance.

• LLM summaries  
  Each article is enriched with an LLM-generated summary.

------------------------------------------------------

ARCHITECTURE

User Query  
    ↓  
LLM (OpenRouter or fallback)  
    ↓  
Intent + Entities  
    ↓  
Router  
    ↓  
PostgreSQL (Search + Geo + Ranking)  
    ↓  
JSON API Response

------------------------------------------------------

DATA FLOW

JSON files → PostgreSQL → Indexed Search & Geo → FastAPI → LLM-enriched responses

------------------------------------------------------

API ENDPOINTS

Data APIs:

/api/v1/news/search?q=  
/api/v1/news/source?source=  
/api/v1/news/category?category=  
/api/v1/news/score?min_score=  
/api/v1/news/nearby?lat=&lon=

Intelligent API:

/api/v1/query?q=...&lat=...&lon=...

The LLM automatically selects the best retrieval strategy.

------------------------------------------------------

RANKING RULES

search   → relevance_score + text match  
source   → most recent  
category → most recent  
score    → highest relevance_score  
nearby   → closest distance  

------------------------------------------------------

SETUP

1. Install dependencies  
pip install -r requirements.txt

2. Create .env file  

DB_HOST=localhost  
DB_NAME=inshorts  
DB_USER=postgres  
DB_PASSWORD=postgres  
OPENROUTER_API_KEY=your_key  

3. Initialize database  

python3 scripts/reset_db.py  
python3 scripts/load_data.py  

4. Run server  

uvicorn app.main:app --reload  

Open API docs at  
http://127.0.0.1:8000/docs

------------------------------------------------------

This project demonstrates how to build a real AI-powered news retrieval backend using SQL, geospatial indexing, and LLMs.
