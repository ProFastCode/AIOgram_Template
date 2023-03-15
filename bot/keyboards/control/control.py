from aiogram.utils.keyboard import (
    InlineKeyboardMarkup,
    InlineKeyboardBuilder,
    InlineKeyboardButton,
)

from bot.db import Role
from bot.utils import ControlAction, ControlCallback


def ikb_control(role: Role) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if role >= Role.ADMINISTRATOR:
        builder.add(
            InlineKeyboardButton(
                text="👥 Модераторы",
                callback_data=ControlCallback(action=ControlAction.MODERATORS).pack(),
            )
        )
    builder.adjust(2)
    return builder.as_markup()
