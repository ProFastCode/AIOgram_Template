from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.db import Role
from bot.filters import RoleCheckFilter
from bot.keyboards.control import IKB_PANEL

# Создание маршрутизатора
router = Router(name='Center control')

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.ADMINISTRATOR))


# Регистрация обработчиков
@router.message(Command('panel'))
async def panel(m: Message) -> None:
    """
    Обработчик, который реагирует на команду /panel
    Панель управления для администратора
    """
    await m.answer('Хай, это панель управления', reply_markup=IKB_PANEL)


# Псевдоним
router_panel = router
