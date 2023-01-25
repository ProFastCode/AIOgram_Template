from aiogram.fsm.state import StatesGroup, State


class ModeratorStates(StatesGroup):
    """
    Состояния модератора
    """

    waiting_mailing_content = State()
