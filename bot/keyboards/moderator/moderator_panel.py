from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from bot.utils.moderator.callback_data_factories import ModeratorCallback, ModeratorAction

MODERATOR_PANEL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Панель модератора",
                callback_data=ModeratorCallback(action=ModeratorAction.FUTURE).pack(),
            )
        ],
    ],
)
