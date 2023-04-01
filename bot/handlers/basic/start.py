from contextlib import suppress

from aiogram import Router, Bot
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message
from sqlalchemy.orm import sessionmaker
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest

from bot.db import Role, SQLUser
from bot.filters import ChatTypeFilter, RoleCheckFilter

# Создание маршрутизатора
router = Router(name="Command start")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.USER))
router.message.filter(ChatTypeFilter(["private"]))


# Регистрация обработчиков
@router.message(CommandStart(), flags={"delay": 2})
async def start(m: Message, command: CommandObject, bot: Bot, session: sessionmaker) -> None:
    """
    Обработчик, который реагирует на команду /start
    """

    referral_id = command.args
    print(referral_id)
    if referral_id:
        sql_user = SQLUser(session)
        user = await sql_user.get(m.from_user.id)
        if not user.referral_id:
            with suppress(TelegramForbiddenError, TelegramBadRequest):
                await sql_user.update(m.from_user.id, referral_id=int(referral_id))
                await bot.send_message(referral_id, f'У вас новый реферал - {m.from_user.full_name}')

    bot_info = await bot.get_me()
    referral_link = f't.me/{bot_info.username}?start={m.from_user.id}'
    await m.answer(
        "<b>Добро пожаловать\n\n"
        "Я шаблон телеграм бота.\n"
        "Разработчик: @fast_code_profile\n"
        f"Ваша реферальная ссылка: {referral_link}</b>"
    )


# Псевдоним
router_start = router
