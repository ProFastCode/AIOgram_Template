from datetime import datetime as dt
from enum import IntEnum

from sqlalchemy import BigInteger, Column, Enum, DateTime, Float

from .base import Base


class Role(IntEnum):
    USER = 0
    MODERATOR = 1
    ADMINISTRATOR = 2


class User(Base):
    """
    Основная модель пользователей
    """
    __tablename__ = "users"  # Имя таблицы
    id = Column(BigInteger, nullable=False, primary_key=True)  # telegram id пользователя
    role = Column(Enum(Role), default=Role.USER)  # Роль пользователя в проекте
    balance = Column(Float, default=0.00)  # Баланс пользователя
    topped_up = Column(Float, default=0.00)  # Общая сумма пополнений пользователя
    update_date = Column(DateTime, default=dt.today(), onupdate=dt.today())  # Дата обновления пользователя
    registration_date = Column(DateTime, default=dt.today())  # Дата регистрации пользователя

    def __str__(self) -> str:
        """
        Возвращает ID пользователя

        :param self: User

        :return: str
        """
        return f"User ID: {self.id}"


class Transaction(Base):
    """
    Модель транзакций пользователей
    """
    __tablename__ = "transactions"  # Имя таблицы
    id = Column(BigInteger, nullable=False, primary_key=True)  # id транзакции
    date = Column(DateTime, default=dt.today())  # Дата транзакции
    amount = Column(Float, nullable=False)  # Сумма транзакции

    def __str__(self) -> str:
        """
        Возвращает id транзакции

        :param self: Transaction

        :return: str
        """
        return f"Transaction ID: {self.id}"
