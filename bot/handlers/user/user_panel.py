from aiogram.types import Message, CallbackQuery

from bot.keyboards.user.user_panel import USER_PANEL


async def user_panel(m: Message) -> None:
    await m.answer("<b>Добро пожаловать в панель пользователя</b>", reply_markup=USER_PANEL)


async def button_user_panel(c: CallbackQuery) -> None:
    await c.answer('Думаю, что тебе придётся делать это самому')
