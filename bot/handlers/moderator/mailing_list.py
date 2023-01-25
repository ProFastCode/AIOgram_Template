from aiogram import Bot
from aiogram import html
from aiogram.exceptions import TelegramForbiddenError
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy.orm import sessionmaker

from bot.db.requests import get_user_ids
from bot.utils.moderator.finite_state_machine import ModeratorStates


async def mailing_list(c: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(ModeratorStates.waiting_mailing_content)
    await c.message.edit_text(
        "<b>Отправьте содержание рассылки,\n"
        "Форматирование текста:\n</b>"
        f'<s>Перечеркнутый</s> - {html.quote("<s>Перечеркнутый</s>")}\n'
        f'<u>Подчеркнутый</u> - {html.quote("<u>Подчеркнутый</u>")}\n'
        f'<a href=t.me>Сайт</a> - {html.quote("<a href=t.me>Сайт</a>")}\n'
        f'<b>Жирный</b> - {html.quote("<b>Жирный</b>")}\n'
        f'<code>Код</code> - {html.quote("<code>Код</code>")}\n'
        f'<i>Курсив</i> - {html.quote("<i>Курсив</i>")}'
    )


async def send_mailing(m: Message, bot: Bot, db_pool: sessionmaker, state: FSMContext) -> None:
    await state.clear()
    user_ids = await get_user_ids(db_pool)
    mailing_count = 0
    successful_mailings_count = 0
    unsuccessful_mailings_count = 0
    for user_id in user_ids:
        try:
            await bot.send_message(user_id, m.text)
            successful_mailings_count += 1

        except TelegramForbiddenError:
            unsuccessful_mailings_count += 1

        mailing_count += 1

    await m.answer(
        "<b>Рассылка окончена\n\n"
        f"Попыток: {mailing_count}\n"
        f"Успешных: {successful_mailings_count}\n"
        f"Не успешных: {unsuccessful_mailings_count}</b>"
    )
