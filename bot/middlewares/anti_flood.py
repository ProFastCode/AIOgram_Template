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
        user_id = event.from_user.id
        time_flood = get_flag(data, "anti_flood")
        if time_flood:
            is_flood = await self.redis.get(f"anti_flood:{user_id}")
            if not is_flood:
                await self.redis.set(f"anti_flood:{user_id}", 1, time_flood)
            else:
                return await event.answer(
                    f"<b>Сработала защита от спама, ожидайте {time_flood}сек.</b>"
                )

        return await handler(event, data)
