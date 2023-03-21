from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import CallbackQuery, Message


class AntiFloodMiddleware(BaseMiddleware):
    """
    ПО промежуточного слоя для защиты от флуда
    """

    def __init__(self, redis):
        self.redis = redis

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id
        delay = get_flag(data, "delay")  # Время задержки в секундах
        if delay:  # Если передан флаг задержки
            is_spam = await self.redis.get(
                f"anti_flood:{user_id}"
            )  # Находится ли в ожидании
            if not is_spam:  # Если не находится в ожидании
                await self.redis.set(
                    f"anti_flood:{user_id}", 1, delay
                )  # Добавляем в ожидание
            else:  # Если находится в ожидании
                return await event.answer(
                    f"<b>Сработала защита от спама, ожидайте {delay}сек.</b>"
                )

        return await handler(event, data)
