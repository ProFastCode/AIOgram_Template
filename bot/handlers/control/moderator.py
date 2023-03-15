from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.db import Role
from bot.filters import RoleCheckFilter
from bot.keyboards.control import ikb_control

# Создание маршрутизатора
router = Router(name="Control center for moderator")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.MODERATOR))


# Регистрация обработчиков
@router.message(Command("moder"))
async def moderator(m: Message, add_text: str = "") -> None:
    """
    Центр управления для администратора
    """
    await m.answer(
        "<b>Центр управления ⚙️\n" f"{add_text}</b>",
        reply_markup=ikb_control(Role.MODERATOR),
    )


# Псевдоним
router_moderator = router
