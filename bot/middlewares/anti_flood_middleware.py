from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message
from aioredis import Redis


class AntiFloodMiddleware(BaseMiddleware):
    """
    ПО промежуточного слоя для защиты от флуда
    """

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        redis: Redis = data["redis"]
        anti_flood = get_flag(data, "anti_flood")
        redis_get = await redis.get(f"anti_flood:{event.from_user.id}")
        if anti_flood:
            if not redis_get:
                await redis.set(f"anti_flood:{event.from_user.id}", 1, anti_flood)
            else:
                return await event.answer(f"Сработала защита от спама, ожидай {anti_flood}.")

        return await handler(event, data)
