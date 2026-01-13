import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db import get_conn

def run_sql(file):
    conn = get_conn()
    cur = conn.cursor()
    with open(file) as f:
        cur.execute(f.read())
    conn.commit()
    cur.close()
    conn.close()

run_sql("scripts/db_init.sql")
run_sql("scripts/db_indexes.sql")

print("DB initialized.")
