from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from bot.utils.moderator.callback_data_factories import (
    ModeratorCallback,
    ModeratorAction,
)

MODERATOR_PANEL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Рассылка",
                callback_data=ModeratorCallback(action=ModeratorAction.MAILING_LIST).pack(),
            )
        ],
    ],
)
