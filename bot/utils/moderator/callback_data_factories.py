from enum import IntEnum

from aiogram.filters.callback_data import CallbackData


class ModeratorAction(IntEnum):
    """
    Действия модератора
    """

    FUTURE = 0


class ModeratorCallback(CallbackData, prefix="moderator"):
    """
    Обработка действий модератора
    """

    action: ModeratorAction
