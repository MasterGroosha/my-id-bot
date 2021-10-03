from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats


async def set_bot_commands(bot: Bot):
    data = [
        # Commands in private chats (English and Russian)
        (
            [
                BotCommand(command="id", description="Print your Telegram ID"),
                BotCommand(command="help", description="Help and source code"),
            ],
            BotCommandScopeAllPrivateChats(),
            "en"
        ),
        (
            [
                BotCommand(command="id", description="Узнать свой ID"),
                BotCommand(command="help", description="Справка и исходники"),
            ],
            BotCommandScopeAllPrivateChats(),
            "ru"
        ),
        # Commands in (super)groups (English and Russian)
        (
            [BotCommand(command="id", description="Print Telegram ID of this group chat")],
            BotCommandScopeAllGroupChats(),
            "en"
        ),
        (
            [BotCommand(command="id", description="Узнать ID этой группы")],
            BotCommandScopeAllGroupChats(),
            "ru"
        ),
    ]

    for commands_list, commands_scope, language in data:
        await bot.set_my_commands(commands=commands_list, scope=commands_scope, language_code=language)
