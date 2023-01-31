from aiogram import Router
from aiogram.filters import CommandStart

from bot.db import Role
from bot.filters import RoleCheckFilter
from .user_panel import user_panel

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.USER))

# Регистрация обработчиков
router.message.register(user_panel, CommandStart())

# Псевдоним
user_router = router
