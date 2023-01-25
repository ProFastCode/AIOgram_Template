from random import randint

from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from sqlalchemy.orm import sessionmaker

# from bot.db.requests import create_transaction
from bot.utils.user.finite_state_machine import UserStates


async def top_up(c: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(UserStates.waiting_for_top_up_amount)
    await c.message.edit_text('<b>Отправьте сумму пополнения</b>')
    await c.answer("Платёжная система не подключена")


async def invoicing(m: Message, state: FSMContext, db_pool: sessionmaker):
    amount = m.text
    if amount.isdigit():
        order_id = randint(1111111, 99999999)
        # await create_transaction(db_pool, order_id, float(amount))  # Эту функцию нужно вызывать после оплаты
        await m.answer(f"<b>Номер транзакции №{order_id}\n"
                       f"Сумма пополнения: {amount}\n"
                       f"<a href='https://None.payment'>Ссылка на оплату</a></b>")
    else:
        return await m.answer('<b>Отправьте сумму в виде числа.</b>')

    await state.clear()
