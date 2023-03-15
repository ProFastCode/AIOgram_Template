from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from bot.utils import BasicAction, BasicCallback

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
