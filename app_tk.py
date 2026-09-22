from tkinter import *
from tkinter import ttk
import psycopg


def save_book():
    nazvanie = entry_name.get()
    avtor = entry_author.get()
    god = int(entry_year.get())
    stranic = int(entry_pages.get())

    conn = psycopg.connect(
        host="localhost", dbname="books_lab",
        user="postgres", password="admin"
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books (Название, Автор, Год, Страниц) VALUES (%s, %s, %s, %s);",
        (nazvanie, avtor, god, stranic)
    )
    conn.commit()
    cur.close()
    conn.close()
    label["text"] = "Добавлено: " + nazvanie


root = Tk()
root.title("Добавить книгу")
root.geometry("280x280")

ttk.Label(root, text="Название").pack(anchor=NW, padx=6, pady=2)
entry_name = ttk.Entry(); entry_name.pack(anchor=NW, padx=6, pady=2)

ttk.Label(root, text="Автор").pack(anchor=NW, padx=6, pady=2)
entry_author = ttk.Entry(); entry_author.pack(anchor=NW, padx=6, pady=2)

ttk.Label(root, text="Год").pack(anchor=NW, padx=6, pady=2)
entry_year = ttk.Entry(); entry_year.pack(anchor=NW, padx=6, pady=2)

ttk.Label(root, text="Страниц").pack(anchor=NW, padx=6, pady=2)
entry_pages = ttk.Entry(); entry_pages.pack(anchor=NW, padx=6, pady=2)

btn = ttk.Button(text="Добавить", command=save_book)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label(); label.pack(anchor=NW, padx=6, pady=6)
root.mainloop()