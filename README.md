# Шаблон для телеграм бота с aiogram

## Важно - Шаблон находится в процессе доработки

## Содержание шаблона
1. **Db** - *Содержит начальную модель пользоватля и заросы для работы с данными модели, а так-же миграции*
2. **Utils** - *Распределены по ролям(Administrator, Moderator, User) позваляет удобно создавать состояния пользователя и обрабатывать данные обратной связи*
3. **Filters** - *Проверка типа чата и роли пользователя*
4. **Handlers** - *Распределены по ролям(Administrator, Moderator, User) имеют начальную реализацию, что бы сразу приступить к разработке, а так-же выставлен анти-флуд на 5сек.*
5. **Keyboards** - *Распределены по ролям(Administrator, Moderator, User) имеют начальную реализацию, в виде инлайн кнопок, если ваше меню динамическое, используйте функции и билдер меню.*
6. **Middlewares** - *Анти-флуд(Исполнен при помощи Redis), Регистрация нового пользователя*


## Используемые библиотеки
1. redis **4.4.2** - *Python client for Redis database and key-value store*
2. alembic **1.9.1** - *A database migration tool for SQLAlchemy.*
3. aiogram **3.0.0b6** - *Modern and fully asynchronous framework for Telegram Bot API*
4. asyncpg **0.27.0** - *An asyncio PostgreSQL driver*
5. sqlalchemy **1.4.46** - *Database Abstraction Library*

## Установка, настройка и запуск
1. Установите: Redis, PostgreSQL, Poetry
2. Установите все зависимости: poetry install
3. Настройте файл конфигурации: bot.ini
4. Проведите миграции: make migrate
5. Запустите бота: poetry run bot
