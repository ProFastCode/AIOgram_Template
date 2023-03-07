from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

from bot.db import UserModel


class SQLUser:
    def __init__(self, db_pool: sessionmaker):
        """
        Метод инициализации

        :param db_pool: Пул соединений с БД
        :return: bool
        """
        self.db_pool = db_pool

    async def is_user_exists(self, user_id: int) -> bool:
        """
        Существует ли пользователь

        :param user_id: Телеграм id пользователя
        :return: bool
        """
        async with self.db_pool() as session:
            async with session.begin():
                return (await session.execute(select(UserModel).where(UserModel.id == user_id))).first()

    async def add_user(self, user_id: int) -> None:
        """
        Добавить нового пользователя
    
        :param user_id: Телеграм id пользователя
    
        :return: None
        """
        async with self.db_pool() as session:
            async with session.begin():
                new_user = UserModel(id=user_id)
                session.add(new_user)

    async def get_user(self, user_id: int) -> UserModel:
        """
        Получить данные пользователя
    
        :param user_id: Телеграм id пользователя
    
        :return: UserModel
        """
        async with self.db_pool() as session:
            async with session.begin():
                return (await session.execute(select(UserModel)
                                              .where(UserModel.id == user_id))).scalars().first()

    async def update_user(self, user_id: int, **kwargs) -> None:
        """
        Обновить данные пользователя
    
        :param user_id: Телеграм id пользователя
        :param kwargs: Параметры которые нужно обновить
    
        :return: None
        """
        async with self.db_pool() as session:
            async with session.begin():
                await session.execute(update(UserModel)
                                      .where(UserModel.id == user_id).values(kwargs))
