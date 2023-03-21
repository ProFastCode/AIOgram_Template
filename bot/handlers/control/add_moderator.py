from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker

from bot.db import Role, SQLUser
from bot.filters import RoleCheckFilter
from bot.keyboards.basic import IKB_RESET_STATE
from bot.utils import ControlStates
from bot.utils.callback_data_factories import ControlAction, ControlCallback

from .administrator import administrator

# Создание маршрутизатора
router = Router(name="Add moderator")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.ADMINISTRATOR))


# Регистрация обработчиков
@router.callback_query(ControlCallback.filter(F.action == ControlAction.ADD_MODERATOR))
async def add_moderator(c: CallbackQuery, state: FSMContext) -> None:
    """
    Обработчик, позволяет выдать права модератора обычному пользователю
    """
    await c.message.edit_text(
        "<b>🆔 Отправьте цифровой id, нового модератора</b>",
        reply_markup=IKB_RESET_STATE,
    )
    await state.set_state(ControlStates.waiting_id_new_moderator)


@router.message(ControlStates.waiting_id_new_moderator, flags={"delay": 2})
async def waited_id_new_moderator(
    m: Message, state: FSMContext, session: sessionmaker
) -> Message | None:
    """
    Обработчик, который реагирует на отправку id нового модератора.
    Выдаёт права новому пользователю, если он является пользователем бота и id действителен
    """
    sql_user = SQLUser(session)
    if m.text.isdigit():
        id_new_moderator = int(m.text)
        if await sql_user.is_exists(id_new_moderator):
            await sql_user.update(id_new_moderator, role=Role.MODERATOR)
        else:
            return await m.answer(
                "<b>✖️ Этот пользователь не использует бота,\n"
                "ℹ️ Отправьте id-пользователя, который использует бота.</b>",
                reply_markup=IKB_RESET_STATE,
            )
    else:
        return await m.answer(
            "<b>Неверно указан id-пользователя. ℹ️</b>", reply_markup=IKB_RESET_STATE
        )

    await state.clear()
    return await administrator(m, "✅ Новый модератор добавлен успешно")


# Псевдоним
router_add_moderator = router
