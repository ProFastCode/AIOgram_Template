from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from bot.utils import BasicCallback, BasicAction

IKB_RESET_STATE = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Отменить",
                callback_data=BasicCallback(action=BasicAction.RESET).pack(),
            )
        ],
    ],
)
