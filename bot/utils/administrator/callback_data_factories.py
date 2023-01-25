from enum import IntEnum

from aiogram.filters.callback_data import CallbackData


class AdministratorAction(IntEnum):
    """
    Действия администратора
    """

    MAILING_LIST = 0
    STATISTICS = 1
    NEW_USERS_IN_WEEK = 2
    EARNINGS = 3


class AdministratorCallback(CallbackData, prefix="administrator"):
    """
    Обработка действий администратора
    """

    action: AdministratorAction
