import configparser
from dataclasses import dataclass

from redis.asyncio.client import Redis
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import sessionmaker


@dataclass
class BotConfig:
    token: str
    administrator_id: int


@dataclass
class DBConfig:
    user: str
    password: str
    database: str
    host: str

    def create_url(self) -> URL:
        return URL.create(
            "postgresql+asyncpg",
            username=self.user,
            password=self.password,
            database=self.database,
            host=self.host,
        )

    def create_engine(self) -> AsyncEngine:
        return create_async_engine(
            url=self.create_url(), echo=False, pool_pre_ping=True
        )

    def create_session(self) -> sessionmaker:
        return sessionmaker(
            bind=self.create_engine(), class_=AsyncSession, expire_on_commit=False
        )


@dataclass
class RedisConfig:
    host: str
    username: str
    password: str

    def connect(self):
        return Redis(host=self.host, username=self.username, password=self.password)


@dataclass
class Config:
    bot: BotConfig
    db: DBConfig
    redis: RedisConfig


def load_config(path: str):
    """
    Загрузка конфигурации
    :param path: Путь к файлу конфигурации
    """
    file_config = configparser.ConfigParser()
    file_config.read(path)
    return Config(
        bot=BotConfig(**file_config["bot"]),
        db=DBConfig(**file_config["db"]),
        redis=RedisConfig(**file_config["redis"]),
    )
