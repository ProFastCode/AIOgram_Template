from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    """
    Состояния пользователя
    """

    waiting_for_top_up_amount = State()
