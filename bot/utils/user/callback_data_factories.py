from enum import IntEnum

from aiogram.filters.callback_data import CallbackData


class UserAction(IntEnum):
    """
    Действия пользователя
    """

    FUTURE = 0


class UserCallback(CallbackData, prefix="user"):
    """
    Обработка действий пользователя
    """

    action: UserAction
