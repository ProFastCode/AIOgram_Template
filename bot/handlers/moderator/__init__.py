from aiogram import Router
from aiogram.filters import Command

from bot.db import Role
from bot.filters import RoleCheckFilter
from .moderator_panel import moderator_panel

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.MODERATOR))

# Регистрация обработчиков
router.message.register(moderator_panel, Command("moderator_panel"))

# Псевдоним
moderator_router = router
