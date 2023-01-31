from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message


class AntiFloodMiddleware(BaseMiddleware):
    """
    ПО промежуточного слоя для защиты от флуда
    """

    def __init__(self, redis):
        self.redis = redis

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        anti_flood = get_flag(data, "anti_flood")
        redis_get = await self.redis.get(f"anti_flood:{event.from_user.id}")
        if anti_flood:
            if not redis_get:
                await self.redis.set(f"anti_flood:{event.from_user.id}", 1, anti_flood)
            else:
                return await event.answer(f"<b>Сработала защита от спама, ожидай {anti_flood}.</b>")

        return await handler(event, data)
