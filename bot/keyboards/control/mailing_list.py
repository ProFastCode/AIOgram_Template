from aiogram.utils.keyboard import (InlineKeyboardBuilder,
                                    InlineKeyboardButton, InlineKeyboardMarkup)


def ikb_mailing_list(full_name: str, moderator_username: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text=f"👤 Автор - {full_name}", url=f"https://t.me/{moderator_username}"
        )
    )
    builder.adjust(1)
    return builder.as_markup()
