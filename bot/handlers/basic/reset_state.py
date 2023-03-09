from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.db import Role
from bot.filters import RoleCheckFilter
from bot.utils import StateAction, StateCallback

# Создание маршрутизатора
router = Router(name="Reset state")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.USER))


# Регистрация обработчиков
@router.callback_query(StateCallback.filter(F.action == StateAction.RESET))
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
