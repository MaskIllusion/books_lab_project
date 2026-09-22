import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="admin"
)
print("Python подключился к серверу:")
print("  host:", conn.info.host)
print("  port:", conn.info.port)
print("  user:", conn.info.user)

cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database ORDER BY datname;")
print("\nСписок баз, которые видит Python:")
for row in cur.fetchall():
    print(" -", row[0])

cur.close()
conn.close()