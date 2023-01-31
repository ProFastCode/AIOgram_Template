from aiogram import Router
from aiogram.filters import Command

from bot.db import Role
from bot.filters import RoleCheckFilter
from .administrator_panel import administrator_panel

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.ADMINISTRATOR))

# Регистрация обработчиков
router.message.register(administrator_panel, Command('administrator_panel'))

# Псевдоним
administrator_router = router
