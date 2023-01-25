from aiogram.types import Message

from bot.keyboards.moderator.moderator_panel import MODERATOR_PANEL


async def moderator_panel(m: Message) -> None:
    await m.answer("<b>Добро пожаловать в панель модератора</b>", reply_markup=MODERATOR_PANEL)
