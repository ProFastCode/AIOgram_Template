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


class ControlAction(IntEnum):
    """
    Действия панели управления для администратора
    """

    MODERATORS = 0
    ADD_MODERATOR = 1


class ControlCallback(CallbackData, prefix="control"):
    """
    Обработка действий панели управления для администратора
    """

    action: ControlAction
