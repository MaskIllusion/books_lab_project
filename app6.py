import psycopg

conn = psycopg.connect(
    host="localhost", dbname="books_lab",
    user="postgres", password="admin"
)
cur = conn.cursor()

nazvanie = input("Название: ")
avtor = input("Автор: ")
god = int(input("Год: "))
stranic = int(input("Страниц: "))

cur.execute(
    "INSERT INTO books (Название, Автор, Год, Страниц) VALUES (%s, %s, %s, %s);",
    (nazvanie, avtor, god, stranic)
)
conn.commit()
print("Строка добавлена.")

cur.execute("SELECT * FROM books;")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()