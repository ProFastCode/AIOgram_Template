from aiogram import Router, F
from aiogram.types import CallbackQuery
from sqlalchemy.orm import sessionmaker

from bot.db import Role, SQLUser
from bot.filters import RoleCheckFilter
from bot.keyboards.control import ikb_moderators
from bot.utils import ControlAction, ControlCallback


# Создание маршрутизатора
router = Router(name='Get moderators')

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.ADMINISTRATOR))


# Регистрация обработчиков
@router.callback_query(ControlCallback.filter(F.action == ControlAction.MODERATORS))
async def get_moderators(c: CallbackQuery, session: sessionmaker) -> None:
    """
    Обработчик, позволяет получить всех текущих модераторов
    """
    sql_user = SQLUser(session)
    moderators = await sql_user.get_by_role(Role.MODERATOR)
    await c.message.answer('Все текущие модераторы на данный момент', reply_markup=ikb_moderators(moderators))


# Псевдоним
router_get_moderators = router
