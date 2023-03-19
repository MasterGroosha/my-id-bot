from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats
from fluent.runtime import FluentLocalization

from bot.fluent_helper import FluentDispenser


async def set_bot_commands(bot: Bot, dispenser: FluentDispenser) -> None:
    """
    Set bot commands in UI (using Menu or "/" buttons)
    :param bot: Bot object
    :param dispenser: FluentDispenser object
    """
    data = list()

    for lang_key in dispenser.available_languages:
        locale_object: FluentLocalization = dispenser.get_language(lang_key)

        data.extend(
            [
                (
                    [
                        BotCommand(command="id", description=locale_object.format_value("cmd-hint-id-pm")),
                        BotCommand(command="help", description=locale_object.format_value("cmd-hint-help")),
                    ],
                    BotCommandScopeAllPrivateChats(),
                    lang_key
                ),
                (
                    [BotCommand(command="id", description=locale_object.format_value("cmd-hint-id-group"))],
                    BotCommandScopeAllGroupChats(),
                    lang_key
                ),
            ]

        )
    for commands_list, commands_scope, language in data:
        await bot.set_my_commands(commands=commands_list, scope=commands_scope, language_code=language)
