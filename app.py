import psycopg

conn = psycopg.connect(
    host="localhost", dbname="books_lab",
    user="postgres", password="admin"
)
cur = conn.cursor()
cur.execute("SELECT * FROM books;")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()