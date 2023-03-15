from aiogram import F, Router
from aiogram.types import CallbackQuery
from sqlalchemy.orm import sessionmaker

from bot.db import Role, SQLUser
from bot.filters import RoleCheckFilter
from bot.utils.callback_data_factories import ControlAction, ControlCallback

from .get_moderators import get_moderators

# Создание маршрутизатора
router = Router(name="Demote moderator")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.ADMINISTRATOR))


# Регистрация обработчиков
@router.callback_query(
    ControlCallback.filter(F.action == ControlAction.DEMOTE_MODERATOR)
)
async def demote_moderator(
    c: CallbackQuery, callback_data: ControlCallback, session: sessionmaker
) -> None:
    """
    Обработчик, позволяет разжаловать модератора
    """
    moderator_id = callback_data.moderator_id
    sql_user = SQLUser(session)
    await sql_user.update(moderator_id, role=Role.USER)
    await c.answer("👇🏻 Модератор разжалован")
    return await get_moderators(c, session)


# Псевдоним
router_demote_moderator = router
