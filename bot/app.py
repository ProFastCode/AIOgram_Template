from asyncio import run
from contextlib import suppress
from logging import INFO, basicConfig

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from bot.config import load_config
from bot.handlers import routers
from bot.middlewares import AntiFloodMiddleware, RegistrationMiddleware


async def main() -> None:
    # Конфигурация
    config = load_config("bot.ini")

    # База данных
    session = config.db.create_session()

    # Хранилище
    redis = config.redis.connect()
    storage = RedisStorage(redis=redis)

    # Бот, Диспетчер
    bot = Bot(config.bot.token, parse_mode="HTML")
    dp = Dispatcher(storage=storage)

    # Зарегистрировать ПО промежуточного слоя
    dp.message.outer_middleware(RegistrationMiddleware(config.bot.administrator_id))
    dp.message.middleware(AntiFloodMiddleware(redis))

    # Регистрация маршрутизаторов
    for router in routers:
        dp.include_router(router)

    # Запуск
    try:
        await dp.start_polling(bot, session=session)
    finally:
        await dp.storage.close()
        await bot.session.close()


def bot_run():
    # Логирование
    basicConfig(
        level=INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    with suppress(KeyboardInterrupt):  # Игнорирование ошибок при остановке
        run(main())  # Запуск асинхронной функции
