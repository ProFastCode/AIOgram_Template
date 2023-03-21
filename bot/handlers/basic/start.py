from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.db import Role
from bot.filters import ChatTypeFilter, RoleCheckFilter

# Создание маршрутизатора
router = Router(name="Command start")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.USER))
router.message.filter(ChatTypeFilter(["private"]))


# Регистрация обработчиков
@router.message(CommandStart(), flags={"delay": 2})
async def start(m: Message) -> None:
    """
    Обработчик, который реагирует на команду /start
    """
    await m.answer(
        "<b>Добро пожаловать\n\n"
        "Я шаблон телеграм бота.\n"
        "Разработчик: @fast_code_profile</b>"
    )


# Псевдоним
router_start = router
