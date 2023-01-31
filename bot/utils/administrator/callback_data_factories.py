from enum import IntEnum

from aiogram.filters.callback_data import CallbackData


class AdministratorAction(IntEnum):
    """
    Действия администратора
    """

    FUTURE = 0


class AdministratorCallback(CallbackData, prefix="administrator"):
    """
    Обработка действий администратора
    """

    action: AdministratorAction
