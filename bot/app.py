from asyncio import run
from contextlib import suppress
from logging import INFO, basicConfig

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis import Redis
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from bot.handlers import user_router, moderator_router, administrator_router
from bot.middlewares import RegistrationMiddleware, AntiFloodMiddleware
from bot.config import load_config


async def main() -> None:
    # Логирование
    basicConfig(level=INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    # Конфигурация
    config = load_config("bot.ini")

    # База данных
    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=config.db.user,
        password=config.db.password,
        database=config.db.database,
        host=config.db.host,
    )
    engine = create_async_engine(url=postgres_url, echo=False, pool_pre_ping=True)
    db_pool = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

    # Хранилище Redis
    redis = Redis(
        host=config.redis.host,
        username=config.redis.username,
        password=config.redis.password,
    )

    # Бот, Диспетчер
    bot = Bot(config.bot.token, parse_mode="HTML")
    dp = Dispatcher(storage=RedisStorage(redis=redis))

    # Зарегистрировать ПО промежуточного слоя
    dp.message.outer_middleware(RegistrationMiddleware(config.bot.administrator_id, config.bot.moderator_id))
    dp.message.middleware(AntiFloodMiddleware(redis))

    # Регистрация маршрутизаторов
    dp.include_router(administrator_router)
    dp.include_router(moderator_router)
    dp.include_router(user_router)

    # Запуск
    try:
        await dp.start_polling(bot, db_pool=db_pool)
    finally:
        await dp.storage.close()
        await bot.session.close()


def bot_run():
    with suppress(KeyboardInterrupt):  # Игнорирование ошибок при остановке
        run(main())  # Запуск асинхронной функции
