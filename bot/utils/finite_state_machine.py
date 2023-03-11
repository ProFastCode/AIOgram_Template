from aiogram.fsm.state import StatesGroup, State


class ControlStates(StatesGroup):
    """
    Состояния центра управления
    """

    waiting_id_new_moderator = State()
