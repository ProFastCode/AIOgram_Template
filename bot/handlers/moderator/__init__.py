from aiogram import Router, F
from aiogram.filters import Command

from bot.db import Role
from bot.filters import RoleCheckFilter
from bot.utils.moderator.callback_data_factories import (
    ModeratorCallback,
    ModeratorAction,
)
from bot.utils.moderator.finite_state_machine import ModeratorStates
from .mailing_list import mailing_list, send_mailing
from .moderator_panel import moderator_panel

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.MODERATOR))

# Регистрация обработчиков
router.message.register(moderator_panel, Command("moderator_panel"))
router.callback_query.register(mailing_list, ModeratorCallback.filter(F.action == ModeratorAction.MAILING_LIST))
router.message.register(send_mailing, ModeratorStates.waiting_mailing_content)

# Псевдоним
moderator_router = router
