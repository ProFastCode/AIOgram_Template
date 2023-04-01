from io import BytesIO

from aiogram import F, Router
from aiogram.types import CallbackQuery, BufferedInputFile
import matplotlib.pyplot as plt
from sqlalchemy.orm import sessionmaker

from bot.db import Role, SQLUser
from bot.filters import RoleCheckFilter
from bot.utils import ControlAction, ControlCallback

# Создание маршрутизатора
router = Router(name="Get statistics")

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.ADMINISTRATOR))


def new_diagram(users: list) -> bytes:
    fig, axs = plt.subplots()
    days_week = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]
    axs.bar(days_week, users, color="blue", label=f'Новых {sum(users)}')
    axs.set_title("Пользователи за неделю")
    axs.legend()
    axs.grid(True)
    fig.tight_layout()
    bytes_io = BytesIO()
    plt.savefig(bytes_io)
    return bytes_io.getvalue()


# Регистрация обработчиков
@router.callback_query(ControlCallback.filter(F.action == ControlAction.STATISTICS))
async def get_statistics(c: CallbackQuery, session: sessionmaker) -> None:
    sql_user = SQLUser(session)
    users_in_week = await sql_user.get_users_in_week()
    users = [len([reg for reg in users_in_week if reg.weekday() == day]) for day in range(7)]
    diagram = new_diagram(users)
    await c.message.delete()
    await c.message.answer_photo(BufferedInputFile(file=diagram, filename='diagram'))


# Псевдоним
router_get_statistics = router
