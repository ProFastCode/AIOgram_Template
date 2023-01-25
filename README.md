# **Шаблон для телеграм бота**

## **Что есть в шаблоне бота ?**
     1. Анти-флуд(Redis, Middleware)
     2. База данных(Postgresql, SQLAlchemy)
     3. Регистрациия(Middleware)
     4. Система ролей(USER, MODERATOR, ADMINISTRATOR)
     5. Проверка типа чата(Filter)
     6. Панель администратора(Просмотр статистики в виде графиков) и модератора(Рассылка)

## **Используемые библиотеки**
 1. aiogram **3.0.0b6** *Modern and fully asynchronous framework for Telegram Bot API*
 2. redis **4.4.2** *Python client for Redis database and key-value store*
 3. aioredis **2.0.1**  *asyncio (PEP 3156) Redis support*
 4. sqlalchemy **1.4.46** *Database Abstraction Library*
 5. alembic **1.9.1**  *A database migration tool for SQLAlchemy.*
 6. flake8 **6.0.0** *the modular source code checker: pep8 pyflakes and co*
 7. asyncpg **0.27.0** *An asyncio PostgreSQL driver*
 8. matplotlib **3.6.3** *Python plotting package*


## **Установка, настройка и запуск**
    1. Установите базу данных(БД) PostgreSQL и создайте БД "bot_db"
    2. Установите Redis, если у вам Windows используйте WSL
    3. Установите Poetry - Альтернатива pip
    4. Что бы установить все зависимости используйте комманду "poetry install"
    5. Настройте файл конфигурации bot.ini
    6. Проведите миграции используя комманду "make migrate" если у вам Windows, установите make
    7. Для запуска используйте комманду "poetry run bot"

