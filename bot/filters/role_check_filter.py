from aiogram.filters import BaseFilter
from aiogram.types import Message
from sqlalchemy.orm import sessionmaker

from bot.db import Role
from bot.db.requests import get_user


class RoleCheckFilter(BaseFilter):
    """
    Фильтр проверки роли пользователя

    :param role: Роли

    :return: bool
    """

    def __init__(self, role: Role) -> None:
        self.role = role

    async def __call__(self, event: Message, db_pool: sessionmaker) -> bool:
        _get_user = await get_user(db_pool, event.from_user.id)
        return _get_user.role >= self.role
