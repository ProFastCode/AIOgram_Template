from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy.orm import sessionmaker

from bot.db import Role, SQLUser
from bot.filters import RoleCheckFilter
from bot.keyboards.basic import IKB_RESET_STATE
from bot.utils import ControlStates
from bot.utils.callback_data_factories import ControlCallback, ControlAction

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
    await c.message.answer(
        "Отправьте id-Пользователя, котору хотите выдать права модератора",
        reply_markup=IKB_RESET_STATE,
    )
    await state.set_state(ControlStates.waiting_id_new_moderator)


@router.message(ControlStates.waiting_id_new_moderator, flags={"anti_flood": 2})
async def waited_id_new_moderator(
    m: Message, state: FSMContext, session: sessionmaker
) -> Message:
    """
    Обработчик, который реагирует на отправку id нового модератора
    Выдаёт права новому пользователю, если он является пользователем бота и id действителен
    """
    sql_user = SQLUser(session)
    if m.text.isdigit():
        id_new_moderator = int(m.text)
        if await sql_user.is_exists(id_new_moderator):
            await sql_user.update(id_new_moderator, role=Role.MODERATOR)
            await m.answer("Успешно выдал права новому модератору")
        else:
            return await m.answer(
                "Этот id-пользователя не найден в базе данных,\n"
                "Отправьте id-пользователя, который использует бота.",
                reply_markup=IKB_RESET_STATE,
            )
    else:
        return await m.answer(
            "Отправьте цифровой id-пользователя", reply_markup=IKB_RESET_STATE
        )

    await state.clear()


# Псевдоним
router_add_moderator = router
