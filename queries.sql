-- 2.1
SELECT * FROM books;
-- 2.2
SELECT Название, Автор FROM books;
-- 2.3
SELECT Название, Автор, Год FROM books;
-- 2.4
SELECT * FROM books WHERE Автор = 'Булгаков';
-- 2.5
SELECT * FROM books WHERE Год = 1997;
-- 2.6
SELECT * FROM books WHERE Год < 1950;
-- 2.7
SELECT * FROM books WHERE Год > 1960;
-- 2.8
SELECT * FROM books WHERE Страниц > 400;
-- 2.9
SELECT * FROM books WHERE Страниц >= 300;
-- 2.10
SELECT * FROM books WHERE Автор = 'Булгаков';
-- 2.11
SELECT * FROM books ORDER BY Название ASC;