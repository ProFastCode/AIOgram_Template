from aiogram.utils.keyboard import (InlineKeyboardBuilder,
                                    InlineKeyboardButton, InlineKeyboardMarkup)

from bot.db import Role
from bot.utils import ControlAction, ControlCallback


def ikb_control(role: Role) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="📨 Рассылка",
            callback_data=ControlCallback(action=ControlAction.SEND_MAILING).pack(),
        )
    )
    if role >= Role.ADMINISTRATOR:
        builder.add(
            InlineKeyboardButton(
                text="👥 Модераторы",
                callback_data=ControlCallback(action=ControlAction.MODERATORS).pack(),
            )
        )
        builder.add(
            InlineKeyboardButton(
                text="📊 Статистика",
                callback_data=ControlCallback(action=ControlAction.STATISTICS).pack(),
            )
        )
    builder.adjust(2)
    return builder.as_markup()
