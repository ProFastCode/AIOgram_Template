from aiogram.types import Message

from bot.keyboards.administrator.administrator_panel import ADMINISTRATOR_PANEL


async def administrator_panel(m: Message) -> None:
    await m.answer(
        "<b>Добро пожаловать в панель администратора</b>",
        reply_markup=ADMINISTRATOR_PANEL,
    )
