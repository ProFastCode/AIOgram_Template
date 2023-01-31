from aiogram import Router, F
from aiogram.filters import Command

from bot.db import Role
from bot.filters import RoleCheckFilter
from bot.utils.moderator.callback_data_factories import ModeratorCallback, ModeratorAction
from .moderator_panel import moderator_panel, button_moderator_panel

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.MODERATOR))

# Регистрация обработчиков
router.message.register(moderator_panel, Command("moderator_panel"), flags={'anti_flood': 5})
router.callback_query.register(button_moderator_panel,
                               ModeratorCallback.filter(F.action == ModeratorAction.FUTURE))

# Псевдоним
moderator_router = router
