import psycopg

# Пробуем подключиться напрямую к books_lab
try:
    conn = psycopg.connect(
        host="localhost",
        dbname="books_lab",
        user="postgres",
        password="admin"
    )
    print("OK: подключение к books_lab прошло")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM books;")
    print("Строк в books:", cur.fetchone()[0])
    cur.close()
    conn.close()
except Exception as e:
    print("FAIL:", e)