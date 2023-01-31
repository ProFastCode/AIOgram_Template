from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker

from bot.db import Role
from bot.db.requests import add_user, is_user_exists, update_user


class RegistrationMiddleware(BaseMiddleware):
    """
    ПО промежуточного слоя для регистрации пользователя
    """

    def __init__(self, administrator_id, moderator_id):
        self.administrator_id = administrator_id
        self.moderator_id = moderator_id

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id
        db_pool: sessionmaker = data["db_pool"]
        if not await is_user_exists(db_pool, user_id):
            await add_user(db_pool, user_id)
            if str(user_id) == self.administrator_id:
                await update_user(db_pool, user_id, role=Role.ADMINISTRATOR)
            else:
                if str(user_id) == self.moderator_id:
                    await update_user(db_pool, user_id, role=Role.MODERATOR)

        return await handler(event, data)
