CREATE INDEX idx_news_text
ON news_articles
USING GIN (to_tsvector('english', title || ' ' || description));

CREATE INDEX idx_source_pubdate
ON news_articles (source_name, publication_date DESC);

CREATE INDEX idx_category
ON news_articles
USING GIN (category);

CREATE INDEX idx_relevance
ON news_articles (relevance_score DESC);

CREATE INDEX idx_location
ON news_articles
USING GIST (location);

CREATE INDEX idx_pubdate
ON news_articles (publication_date DESC);
