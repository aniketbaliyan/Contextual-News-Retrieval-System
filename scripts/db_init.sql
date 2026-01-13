CREATE EXTENSION IF NOT EXISTS postgis;

DROP TABLE IF EXISTS news_articles;

CREATE TABLE news_articles (
    id UUID PRIMARY KEY,
    title TEXT,
    description TEXT,
    url TEXT,
    publication_date TIMESTAMP,
    source_name TEXT,
    category TEXT[],
    relevance_score FLOAT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    location GEOGRAPHY(Point, 4326)
);
