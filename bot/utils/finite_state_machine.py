from aiogram.fsm.state import State, StatesGroup


class ControlStates(StatesGroup):
    """
    Состояния центра управления
    """

    waiting_id_new_moderator = State()
    waiting_mailing_content = State()
