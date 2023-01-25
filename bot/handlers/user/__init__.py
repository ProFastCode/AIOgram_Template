from aiogram import Router, F
from aiogram.filters import CommandStart

from bot.db import Role
from bot.filters import RoleCheckFilter
from bot.utils.user.callback_data_factories import UserCallback, UserAction
from bot.utils.user.finite_state_machine import UserStates
from .top_up import top_up, invoicing
from .user_panel import user_panel

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.USER))

# Регистрация обработчиков
router.message.register(user_panel, CommandStart())
router.callback_query.register(top_up, UserCallback.filter(F.action == UserAction.TOP_UP))
router.message.register(invoicing, UserStates.waiting_for_top_up_amount)

# Псевдоним
user_router = router
