from app.db import get_conn

def fetch_articles(
    keywords=None,
    source=None,
    category=None,
    min_score=None,
    lat=None,
    lon=None,
    limit=5,
    mode="search"
):
    conn = get_conn()
    cur = conn.cursor()

    conditions = []
    params = []

    text_vector = "to_tsvector('english', title || ' ' || description)"

    if keywords:
        conditions.append(f"{text_vector} @@ plainto_tsquery(%s)")
        params.append(keywords)

    if source:
        conditions.append("source_name ILIKE %s")
        params.append(f"%{source}%")

    if category:
        conditions.append("%s = ANY(category)")
        params.append(category)

    if min_score:
        conditions.append("relevance_score >= %s")
        params.append(min_score)

    where = " AND ".join(conditions) if conditions else "TRUE"

    # Ranking logic
    if mode == "nearby":
        order = "location <-> ST_MakePoint(%s, %s)"
        params += [lon, lat]

    elif mode == "score":
        order = "relevance_score DESC"

    elif mode in ("source", "category"):
        order = "publication_date DESC"

    else:  # search
        order = f"""
            (0.7 * relevance_score +
             0.3 * ts_rank({text_vector}, plainto_tsquery(%s))) DESC
        """
        params.append(keywords)

    sql = f"""
        SELECT title, description, url, publication_date, source_name, category,
               relevance_score, latitude, longitude
        FROM news_articles
        WHERE {where}
        ORDER BY {order}
        LIMIT %s
    """

    params.append(limit)

    cur.execute(sql, params)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows
