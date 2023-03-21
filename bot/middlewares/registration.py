from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from bot.db import Role, SQLUser


class RegistrationMiddleware(BaseMiddleware):
    """
    ПО промежуточного слоя для регистрации пользователя
    """

    def __init__(self, administrator_id: int):
        self.administrator_id = administrator_id

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id
        full_name = event.from_user.full_name
        sql_user = SQLUser(data["session"])
        if not await sql_user.is_exists(
            user_id
        ):  # Если пользователь не зарегистрирован
            await sql_user.add(
                user_id=user_id, full_name=full_name
            )  # Добавляем в базу данных
            if (
                user_id == self.administrator_id
            ):  # Если пользователь является администратором
                await sql_user.update(
                    user_id=user_id, role=Role.ADMINISTRATOR
                )  # Присваиваем роль администратора

        return await handler(event, data)
