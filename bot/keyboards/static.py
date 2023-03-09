from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from bot.utils.callback_data_factories import UserCallback, ModeratorCallback, UserAction, ModeratorAction


RESET_STATE = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Отменить",
                callback_data=UserCallback(action=UserAction.FUTURE).pack(),
            )
        ],
    ],
)

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
