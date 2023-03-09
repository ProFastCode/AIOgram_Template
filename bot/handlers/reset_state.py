from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.db import Role
from bot.utils.callback_data_factories import UserCallback, UserAction
from bot.filters import RoleCheckFilter

# Создание маршрутизатора
router = Router(name="Reset state")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.USER))


# Регистрация обработчиков
@router.message(Command("cancel"), flags={"anti_flood": 2})
async def command_reset_state(m: Message, state: FSMContext) -> None:
    """
    Обработчик, который реагирует на команду /cancel
    Позволяет сбросить состояние пользователя
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()


@router.callback_query(UserCallback.filter(F.action == UserAction.FUTURE))
async def callback_reset_state(c: CallbackQuery, state: FSMContext) -> bool:
    """
    Обработчик, который реагирует на команду /cancel
    Позволяет сбросить состояние пользователя
    """
    current_state = await state.get_state()
    if current_state is None:
        return await c.answer("Вам нечего отменять")

    await state.clear()
    await c.answer("Отмена")


# Псевдоним
router_reset_state = router
