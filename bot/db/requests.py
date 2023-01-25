from datetime import datetime, timedelta

from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

from bot.db import User, Transaction


async def is_user_exists(db_pool: sessionmaker, user_id: int) -> bool:
    """
    Существует ли пользователь

    :param db_pool: Пул соединений с БД
    :param user_id: Телеграм id пользователя

    :return: bool
    """
    async with db_pool() as session:
        async with session.begin():
            return (await session.execute(select(User).where(User.id == user_id))).first()


async def add_user(db_pool: sessionmaker, user_id: int) -> None:
    """
    Добавить нового пользователя

    :param db_pool: Пул соединений с БД
    :param user_id: Телеграм id пользователя

    :return: None
    """
    async with db_pool() as session:
        async with session.begin():
            new_user = User(id=user_id)
            session.add(new_user)


async def get_user(db_pool: sessionmaker, user_id: int) -> User:
    """
    Получить данные пользователя

    :param db_pool: Пул соединений с БД
    :param user_id: Телеграм id пользователя

    :return: User
    """
    async with db_pool() as session:
        async with session.begin():
            return (await session.execute(select(User)
                                          .where(User.id == user_id))).scalars().first()


async def update_user(db_pool: sessionmaker, user_id: int, **kwargs) -> None:
    """
    Обновить данные пользователя

    :param db_pool: Пул соединений с БД
    :param user_id: Телеграм id пользователя
    :param kwargs: Параметры которые нужно обновить

    :return: None
    """
    async with db_pool() as session:
        async with session.begin():
            await session.execute(update(User)
                                  .where(User.id == user_id).values(kwargs))


async def get_user_ids(db_pool: sessionmaker) -> list[User]:
    """
    Получить все id пользователей

    :param db_pool: Пул соединений с БД

    :return: list[User]
    """
    async with db_pool() as session:
        async with session.begin():
            return list((await session.execute(select(User.id))).scalars())


async def get_users_in_week(db_pool: sessionmaker) -> list[datetime]:
    """
    Получить дату регистрации новых пользователей за неделю

    :param db_pool: Пул соединений с БД

    :return: list[datetime]
    """
    async with db_pool() as session:
        async with session.begin():
            week = datetime.today() - timedelta(days=7)
            return list((await session.execute(select(User.registration_date)
                                               .where(User.registration_date >= week))).scalars())


async def create_transaction(db_pool: sessionmaker, order_id: int, amount: float) -> None:
    """
    Создать новую транзакцию

    :param db_pool: Пул соединений с БД
    :param order_id: id транзакции
    :param amount: Сумма пополнения

    :return: None
    """
    async with db_pool() as session:
        async with session.begin():
            new_transaction = Transaction(id=order_id, amount=amount)
            session.add(new_transaction)


async def get_transactions_in_week(db_pool: sessionmaker) -> list[Transaction]:
    """
    Получить сумму новых транзакций за неделю

    :param db_pool: Пул соединений с БД

    :return: list[float]
    """
    async with db_pool() as session:
        async with session.begin():
            week = datetime.today() - timedelta(days=7)
            return list((await session.execute(select(Transaction.date, Transaction.amount)
                                               .where(Transaction.date >= week))))
