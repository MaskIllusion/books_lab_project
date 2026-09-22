# books_lab_project

Учебный проект: связка Python + PostgreSQL + Tkinter.

## Описание
Проект демонстрирует работу с базой данных PostgreSQL из Python. Включает в себя:
- Выполнение SQL-запросов (SELECT) с различными условиями.
- Добавление данных в базу через консольный ввод (INSERT).
- Создание графического интерфейса (GUI) для добавления книг на Tkinter.
- Авторизацию пользователя с разделением прав и записью в отдельную базу данных.

## Структура проекта
- `queries.sql` — все SQL-запросы (Блок 2)
- `app.py` — SELECT * FROM books
- `app2.py` — SELECT двух столбцов
- `app3.py` — SELECT трёх столбцов
- `app4.py` — SELECT с WHERE
- `app5.py` — SELECT двух столбцов с WHERE
- `app6.py` — INSERT через input()
- `app_tk.py` — GUI на Tkinter для добавления книги
- `app_auth.py` — окно авторизации и регистрации + форма добавления книги

## Базы данных
- `books_lab` — база с книгами (таблица `books`)
- `user_ui_db` — база с пользователями (таблица `users`)

## Скриншоты работы

### База данных (pgAdmin)
![Дерево базы](screenshot_tree.png)

### Запросы (Query Tool)
![Скрин 2.1](screenshot_2_1.png)
![Скрин 2.4](screenshot_2_4.png)
![Скрин 2.8](screenshot_2_8.png)
![Скрин 2.11](screenshot_2_11.png)

### Работа Python-скриптов
![Консоль app](screenshot_app.png)
![Консоль app2](screenshot_app2.png)
![Консоль app3](screenshot_app3.png)
![Консоль app4](screenshot_app4.png)
![Консоль app5](screenshot_app5.png)
![Консоль app6](screenshot_app6.png)

### Графический интерфейс (Tkinter)
![Окно app_tk](screenshot_tk.png)

### Авторизация
![Окно app_auth](screenshot_auth.png)

## Как запустить
1. Установить библиотеку для работы с PostgreSQL:
   ```bash
   pip install psycopg[binary]
