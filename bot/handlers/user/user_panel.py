from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.orm import sessionmaker

from bot.db.requests import get_user
from bot.keyboards.user.user_panel import USER_PANEL


async def user_panel(m: Message, state: FSMContext, db_pool: sessionmaker) -> None:
    _get_user = await get_user(db_pool, m.from_user.id)
    await m.answer(
        "<b>Добро пожаловать в панель пользователя\n\n"
        f"Ваш баланс: {_get_user.balance}</b>",
        reply_markup=USER_PANEL)

    await state.clear()
