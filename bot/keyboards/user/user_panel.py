from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from bot.utils.user.callback_data_factories import UserCallback, UserAction

USER_PANEL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Пополнить",
                callback_data=UserCallback(action=UserAction.TOP_UP).pack(),
            )
        ],
    ],
)
