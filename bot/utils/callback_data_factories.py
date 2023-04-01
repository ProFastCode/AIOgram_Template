from enum import IntEnum

from aiogram.filters.callback_data import CallbackData


class ControlAction(IntEnum):
    """
    Действия панели управления для администратора
    """

    MODERATORS = 0  # Получить список модераторов
    ADD_MODERATOR = 1  # Добавить нового модератора
    DEMOTE_MODERATOR = 2  # Разжаловать модератора
    SEND_MAILING = 3  # Отправить рассылку
    STATISTICS = 4  # Получить статистику


class ControlCallback(CallbackData, prefix="control"):
    """
    Обработка действий панели управления для администратора
    """

    action: ControlAction
    moderator_id: int = None


class BasicAction(IntEnum):
    """
    Действия с базовым функционалам
    """

    RESET = 0  # Сбросить состояние пользователя


class BasicCallback(CallbackData, prefix="state"):
    """
    Обработка действий базового функционала
    """

    action: BasicAction
