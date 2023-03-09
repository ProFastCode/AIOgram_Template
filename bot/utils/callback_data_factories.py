from enum import IntEnum

from aiogram.filters.callback_data import CallbackData


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


class StateAction(IntEnum):
    """
    Действия с состоянием
    """

    RESET = 0


class StateCallback(CallbackData, prefix="state"):
    """
    Обработка действий состояния
    """

    action: StateAction
