from enum import IntEnum

from aiogram.filters.callback_data import CallbackData


class UserAction(IntEnum):
    """
    Действия пользователя
    """

    TOP_UP = 0


class UserCallback(CallbackData, prefix="user"):
    """
    Обработка действий пользователя
    """

    action: UserAction
