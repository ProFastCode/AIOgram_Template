from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    """
    Состояния пользователя
    """

    waiting_future = State()
