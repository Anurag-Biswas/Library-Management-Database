import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host = os.getenv("DB_HOST", "Localhost"),
    port = os.getenv("DB_PORT", 5432),
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASS"),
)

cur = conn.cursor()

author = "George Orwell"

cur.execute(
    """
    SELECT b.title
    FROM books b
    JOIN book_authors ba
    ON b.book_id = ba.book_id
    JOIN authors a
    ON
    ba.author_id = a.author_id
    WHERE a.author_name = %s
    """,
    (author,)
)

for row in cur.fetchall():
    print(row)

cur.close()
conn.close()


Output:-
PS C:\Users\hp\Documents\pythonProgram> python Inheritance\connect_database1.py
PS C:\Users\hp\Documents\pythonProgram>

