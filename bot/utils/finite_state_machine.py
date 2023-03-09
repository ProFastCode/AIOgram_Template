from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    """
    Состояния пользователя
    """

    waiting_future = State()


class ModeratorStates(StatesGroup):
    """
    Состояния модератора
    """

    waiting_future = State()


class ControlStates(StatesGroup):
    """
    Состояния центра управления
    """

    waiting_id_new_moderator = State()
