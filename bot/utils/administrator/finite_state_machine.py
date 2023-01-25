from aiogram.fsm.state import StatesGroup, State


class AdministratorStates(StatesGroup):
    """
    Состояния администратора
    """

    waiting_future = State()
