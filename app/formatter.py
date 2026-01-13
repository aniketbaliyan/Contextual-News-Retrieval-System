from datetime import datetime

def format_article(row, summary=None):
    pub = row[3]
    if isinstance(pub, datetime):
        pub = pub.isoformat()

    return {
        "title": row[0],
        "description": row[1],
        "url": row[2],
        "publication_date": pub,
        "source_name": row[4],
        "category": row[5],
        "relevance_score": float(row[6]),
        "latitude": float(row[7]),
        "longitude": float(row[8]),
        "llm_summary": summary
    }
