from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    """
    Фильтр проверки типа чата
    :param chat_types: Типы чатов
    :return: bool
    """

    def __init__(self, chat_types: list) -> None:
        self.chat_types = chat_types

    async def __call__(self, m: Message) -> bool:
        return m.chat.type in self.chat_types
