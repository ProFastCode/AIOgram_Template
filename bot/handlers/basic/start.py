from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.db import Role
from bot.filters import RoleCheckFilter

# Создание маршрутизатора
router = Router(name="Command start")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.USER))


# Регистрация обработчиков
@router.message(CommandStart(), flags={"anti_flood": 2})
async def start(m: Message) -> None:
    """
    Обработчик, который реагирует на команду /start
    """
    await m.answer(
        "Добро пожаловать\n\n"
        "Я шаблон телеграм бота.\n"
        f"Разработчик: @fast_code_profile"
    )


# Псевдоним
router_start = router
