import os
import json
import re
import requests

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "Inshorts LLM"
}

QUERY_PROMPT = """
You are a query parser for a news engine.

Extract and return JSON with:
{
  "intent": one of ["search", "source", "category", "score", "nearby"],
  "keywords": string or null,
  "source": string or null,
  "category": string or null,
  "min_score": number or null
}

User query:
"""

def openrouter_call(prompt):
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }

    r = requests.post(OPENROUTER_URL, headers=HEADERS, json=payload, timeout=15)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def parse_query(q):
    try:
        txt = openrouter_call(QUERY_PROMPT + q)
        print("LLM parse result:", txt)
        return json.loads(txt)
    except Exception:
        return local_parse(q)


def summarize(title, description):
    prompt = f"Summarize this article in 2 sentences:\n{title}\n{description}"
    try:
        return openrouter_call(prompt)
    except Exception:
        return local_summarize(title, description)


# ---------------- Fallback ----------------

def local_parse(q):
    ql = q.lower()

    intent = "search"
    if "near" in ql or "around" in ql:
        intent = "nearby"
    elif "from" in ql:
        intent = "source"
    elif "technology" in ql or "sports" in ql or "business" in ql:
        intent = "category"
    elif "top" in ql or "high" in ql:
        intent = "score"

    source = None
    if "reuters" in ql:
        source = "Reuters"
    elif "dw" in ql:
        source = "DW"
    elif "new york times" in ql:
        source = "New York Times"

    category = None
    if "technology" in ql:
        category = "Technology"
    elif "sports" in ql:
        category = "Sports"
    elif "business" in ql:
        category = "Business"
    elif "general" in ql:
        category = "General"

    min_score = 0.7 if intent == "score" else None

    keywords = re.sub(r"(near|around|from|top|high).*", "", q, flags=re.IGNORECASE).strip()

    return {
        "intent": intent,
        "keywords": keywords or None,
        "source": source,
        "category": category,
        "min_score": min_score
    }


def local_summarize(title, description):
    return description[:120] + "..."
