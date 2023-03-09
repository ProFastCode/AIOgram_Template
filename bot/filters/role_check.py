from aiogram.filters import BaseFilter
from aiogram.types import Message
from sqlalchemy.orm import sessionmaker

from bot.db import Role, SQLUser


class RoleCheckFilter(BaseFilter):
    """
    Фильтр проверки роли пользователя
    :param role: Роли
    :return: bool
    """

    def __init__(self, role: Role) -> None:
        self.role = role

    async def __call__(self, m: Message, session: sessionmaker) -> bool:
        sql_user = SQLUser(session)
        user = await sql_user.get(m.from_user.id)
        return user.role >= self.role
