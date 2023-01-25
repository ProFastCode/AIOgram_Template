from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeChat

from bot.loader import config


async def set_commands(bot: Bot):
    data = [
        (
            [
                BotCommand(command="start", description="Запустить бота"),
            ],
            BotCommandScopeAllPrivateChats(),
        ),
        (
            [
                BotCommand(command="start", description="Запустить бота"),
                BotCommand(command="moderator_panel", description="Панель модератора"),
            ],
            BotCommandScopeChat(chat_id=config.bot.moderator_id),
        ),
        (
            [
                BotCommand(command="start", description="Запустить бота"),
                BotCommand(command="moderator_panel", description="Панель модератора"),
                BotCommand(command="administrator_panel", description="Панель администратора"),
            ],
            BotCommandScopeChat(chat_id=config.bot.administrator_id),
        ),
    ]
    for commands_list, commands_scope in data:
        await bot.set_my_commands(commands=commands_list, scope=commands_scope)
