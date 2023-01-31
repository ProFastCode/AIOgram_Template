from aiogram.types import Message, CallbackQuery

from bot.keyboards.moderator.moderator_panel import MODERATOR_PANEL


async def moderator_panel(m: Message) -> None:
    await m.answer("<b>Добро пожаловать в панель модератора</b>", reply_markup=MODERATOR_PANEL)


async def button_moderator_panel(c: CallbackQuery) -> None:
    await c.answer('Думаю, что тебе придётся делать это самому')
