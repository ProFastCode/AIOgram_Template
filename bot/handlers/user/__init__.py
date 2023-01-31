from aiogram import Router, F
from aiogram.filters import CommandStart

from bot.db import Role
from bot.filters import RoleCheckFilter
from bot.utils.user.callback_data_factories import UserCallback, UserAction
from .user_panel import user_panel, button_user_panel

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.USER))

# Регистрация обработчиков
router.message.register(user_panel, CommandStart())
router.callback_query.register(button_user_panel,
                               UserCallback.filter(F.action == UserAction.FUTURE))

# Псевдоним
user_router = router
