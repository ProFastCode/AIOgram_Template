from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from bot.utils import ControlAction, ControlCallback

IKB_PANEL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Модераторы",
                callback_data=ControlCallback(action=ControlAction.MODERATORS).pack(),
            )
        ],
    ],
)