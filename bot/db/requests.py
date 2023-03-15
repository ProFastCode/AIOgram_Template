from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

from bot.db import UserModel, Role


class SQLUser:
    def __init__(self, session: sessionmaker):
        """
        Метод инициализации
        :param session: Пул соединений с БД
        :return: bool
        """
        self.session = session

    async def is_exists(self, user_id: int) -> bool:
        """
        Существует ли пользователь
        :param user_id: Телеграм id пользователя
        :return: bool
        """
        async with self.session() as session:
            async with session.begin():
                return (
                    await session.execute(
                        select(UserModel).where(UserModel.id == user_id)
                    )
                ).first()

    async def add(self, user_id: int, full_name: str) -> None:
        """
        Добавить нового пользователя
        :param user_id: Телеграм id пользователя
        :param full_name: Полное имя пользователя
        :return: None
        """
        async with self.session() as session:
            async with session.begin():
                user = UserModel(id=user_id, full_name=full_name)
                session.add(user)

    async def get(self, user_id: int) -> UserModel:
        """
        Получить данные пользователя
        :param user_id: Телеграм id пользователя
        :return: UserModel
        """
        async with self.session() as session:
            async with session.begin():
                return (
                    (
                        await session.execute(
                            select(UserModel).where(UserModel.id == user_id)
                        )
                    )
                    .scalars()
                    .first()
                )

    async def get_by_role(self, role: Role):
        """
        Получить данные всех модераторов
        :param role: Роль пользователей
        :return: UserModel
        """
        async with self.session() as session:
            async with session.begin():
                return (
                    await session.execute(
                        select(UserModel).where(UserModel.role == role)
                    )
                ).scalars()

    async def update(self, user_id: int, **kwargs) -> None:
        """
        Обновить данные пользователя
        :param user_id: Телеграм id пользователя
        :param kwargs: Параметры которые нужно обновить
        :return: None
        """
        async with self.session() as session:
            async with session.begin():
                await session.execute(
                    update(UserModel).where(UserModel.id == user_id).values(kwargs)
                )
