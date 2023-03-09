from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from bot.utils import StateCallback, StateAction

IKB_RESET_STATE = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Отменить",
                callback_data=StateCallback(action=StateAction.RESET).pack(),
            )
        ],
    ],
)
