from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.db import Role
from bot.filters import RoleCheckFilter
from bot.keyboards.control import ikb_control

# Создание маршрутизатора
router = Router(name="Control center for administrator")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.ADMINISTRATOR))


# Регистрация обработчиков
@router.message(Command("admin"))
async def administrator(m: Message) -> None:
    """
    Центр управления для администратора
    """
    await m.answer(
        "<b>Центр управления ⚙️</b>",
        reply_markup=ikb_control(Role.ADMINISTRATOR),
    )


# Псевдоним
router_administrator = router
