from enum import IntEnum

from aiogram.filters.callback_data import CallbackData


class ModeratorAction(IntEnum):
    """
    Действия модератора
    """

    MAILING_LIST = 0


class ModeratorCallback(CallbackData, prefix="moderator"):
    """
    Обработка действий модератора
    """

    action: ModeratorAction
