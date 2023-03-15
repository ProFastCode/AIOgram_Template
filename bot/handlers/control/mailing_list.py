from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker

from bot.db import Role, SQLUser
from bot.filters import RoleCheckFilter
from bot.keyboards.control import ikb_mailing_list
from bot.utils import ControlAction, ControlCallback, ControlStates
from .administrator import administrator
from .moderator import moderator

# Создание маршрутизатора
router = Router(name="Mailing list")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.MODERATOR))


# Регистрация обработчиков
@router.callback_query(ControlCallback.filter(F.action == ControlAction.SEND_MAILING))
async def mailing_list(c: CallbackQuery, state: FSMContext) -> None:
    """
    Обработчик, позволяет разослать сообщения пользователям бота
    """
    await c.message.edit_text('<b>💬 Отправьте контент для рассылки</b>')
    await state.set_state(ControlStates.waiting_mailing_content)


@router.message(ControlStates.waiting_mailing_content, flags={"anti_flood": 2})
async def waited_mailing_content(
        m: Message, state: FSMContext, session: sessionmaker
) -> Message | None:
    """
    Обработчик, который реагирует на отправку контента для рассылки.
    Отправляет рассылку пользователям бота.
    """
    sql_user = SQLUser(session)
    users = await sql_user.get_by_role(Role.USER)
    for user in users:
        await m.copy_to(user.id)

    administrators = await sql_user.get_by_role(Role.ADMINISTRATOR)
    for data_administrator in administrators:
        await m.copy_to(data_administrator.id, reply_markup=ikb_mailing_list(m.from_user.full_name,
                                                                             m.from_user.username))

    await state.clear()
    user = await sql_user.get(m.from_user.id)
    if user.role == Role.ADMINISTRATOR:
        return await administrator(m, 'Рассылка окончена ✅')
    else:
        return await moderator(m, 'Рассылка окончена ✅')

# Псевдоним
router_mailing_list = router
