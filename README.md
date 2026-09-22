# books_lab_project

Учебный проект: связка Python + PostgreSQL + Tkinter. Тема — книги.

## Структура

- `queries.sql` — все SQL-запросы
- `app.py` … `app5.py` — чтение из базы с разными SELECT
- `app6.py` — INSERT через input()
- `app_tk.py` — окно Tkinter для добавления книги
- `app_auth.py` — авторизация + форма добавления книги

## Базы данных

- `books_lab` — таблица `books` (Название, Автор, Год, Страниц)
- `user_ui_db` — таблица `users` (Логин, Пароль)

## Как запустить

1. Установить psycopg:
   ```bash
   pip install psycopg[binary]