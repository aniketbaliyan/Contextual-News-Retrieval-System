import os
import json
import psycopg2
from psycopg2.extras import execute_batch
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

cur = conn.cursor()

with open("./data/raw/news_data1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []
for a in data:
    rows.append((
        a["id"],
        a["title"],
        a["description"],
        a["url"],
        a["publication_date"],
        a["source_name"],
        a["category"],
        a["relevance_score"],
        a["latitude"],
        a["longitude"],
        a["longitude"],
        a["latitude"]
    ))

sql = """
INSERT INTO news_articles
(id, title, description, url, publication_date, source_name, category, relevance_score, latitude, longitude, location)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, ST_MakePoint(%s,%s))
ON CONFLICT (id) DO NOTHING
"""

execute_batch(cur, sql, rows, page_size=1000)
conn.commit()

cur.close()
conn.close()

print("Loaded", len(rows), "articles")
