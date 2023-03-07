from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from bot.db import Role, SQLUser


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
        sql_user = SQLUser(data["db_pool"])
        if not await sql_user.is_user_exists(user_id):
            await sql_user.add_user(user_id)
            if str(user_id) == self.administrator_id:
                await sql_user.update_user(user_id, role=Role.ADMINISTRATOR)
            else:
                if str(user_id) == self.moderator_id:
                    await sql_user.update_user(user_id, role=Role.MODERATOR)

        return await handler(event, data)
