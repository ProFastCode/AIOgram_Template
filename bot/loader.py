import configparser
from dataclasses import dataclass


@dataclass
class Bot:
    token: str
    administrator_id: str
    moderator_id: str


@dataclass
class DB:
    user: str
    password: str
    database: str
    host: str


@dataclass
class Redis:
    host: str
    username: str
    password: str


@dataclass
class Config:
    bot: Bot
    db: DB
    redis: Redis


def load_config(path: str):
    file_config = configparser.ConfigParser()
    file_config.read(path)
    return Config(
        bot=Bot(**file_config["bot"]),
        db=DB(**file_config["db"]),
        redis=Redis(**file_config["redis"]),
    )


config = load_config("bot.ini")
