from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

from bot.db import User


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
