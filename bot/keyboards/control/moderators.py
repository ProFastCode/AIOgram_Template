from aiogram.utils.keyboard import (
    InlineKeyboardMarkup,
    InlineKeyboardBuilder,
    InlineKeyboardButton,
)

from bot.db import UserModel
from bot.utils import ControlAction, ControlCallback


def ikb_moderators(moderators: list[UserModel]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for moderator in moderators:
        builder.add(
            InlineKeyboardButton(
                text=moderator.full_name,
                callback_data=ControlCallback(
                    action=ControlAction.DEMOTE_MODERATOR, moderator_id=moderator.id
                ).pack(),
            )
        )

    builder.add(
        InlineKeyboardButton(
            text="Добавить модератора",
            callback_data=ControlCallback(action=ControlAction.ADD_MODERATOR).pack(),
        )
    )
    builder.adjust(2)
    return builder.as_markup()
