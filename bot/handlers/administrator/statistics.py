from io import BytesIO

import matplotlib.pyplot as plt
from aiogram.types import CallbackQuery, BufferedInputFile
from sqlalchemy.orm import sessionmaker

from bot.db.requests import get_transactions_in_week, get_users_in_week


def new_diagram(users: list, transactions: list) -> bytes:
    fig, axs = plt.subplots(2, 1)
    days_week = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]
    axs[0].bar(days_week, users, color="blue", label=f'Новых {sum(users)}')
    axs[0].set_title("Пользователи за неделю")
    axs[0].legend()
    axs[0].grid(True)
    axs[1].plot(days_week, transactions, 'o-g', label=f'Общая прибыль {sum(transactions)}руб.')
    axs[1].set_title("Пополнения за неделю")
    axs[1].legend()
    axs[1].grid(True)
    fig.tight_layout()
    bytes_io = BytesIO()
    plt.savefig(bytes_io)
    return bytes_io.getvalue()


async def statistics(c: CallbackQuery, db_pool: sessionmaker) -> None:
    users_in_week = await get_users_in_week(db_pool)
    transactions_in_week = await get_transactions_in_week(db_pool)
    users = [len([reg for reg in users_in_week if reg.weekday() == day]) for day in range(7)]
    transactions = [sum(tr.amount for tr in transactions_in_week if tr.date.weekday() == day) for day in range(7)]
    diagram = new_diagram(users, transactions)
    await c.message.delete()
    await c.message.answer_photo(BufferedInputFile(file=diagram, filename='diagram'))
