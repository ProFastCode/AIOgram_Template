from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from bot.utils.administrator.callback_data_factories import (
    AdministratorCallback,
    AdministratorAction,
)

ADMINISTRATOR_PANEL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Статистика",
                callback_data=AdministratorCallback(action=AdministratorAction.STATISTICS).pack(),
            ),
        ],
    ],
)
