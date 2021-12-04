from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.dispatcher.filters.command import Command


async def cmd_start(message: types.Message):
    """
    /start command handler for private chats
    :param message: Telegram message with "/start" command
    """
    await message.answer(f"Your Telegram ID is <code>{message.chat.id}</code>\nHelp and source code: /help")


async def cmd_id(message: types.Message):
    """
    /id command handler for all chats
    :param message: Telegram message with "/id" command
    """
    if message.chat.id == message.from_user.id:
        await message.answer(f"Your Telegram ID is <code>{message.from_user.id}</code>")
    else:
        await message.reply(f"This {message.chat.type} chat ID is <code>{message.chat.id}</code>\n"
                            f"Your Telegram ID is <code>{message.from_user.id}</code>")


async def cmd_help(message: types.Message):
    """
    /help command handler for all chats
    :param message: Telegram message with "/help" command
    """
    await message.answer(
        'Use this bot to get ID for different entities across Telegram:\n'
        '• Forward message from channel to get channel ID;\n'
        '• Forward message from user to get their ID (unless they restrict from doing so);\n'
        '• Send a sticker to get its file_id (currently you can use the sticker\'s file_id with any bot);\n'
        '• Add bot to group to get its ID (it will even tell you when you migrate from group to supergroup);\n'
        '• Use inline mode to send your Telegram ID to any chat.\n\n'
        'Source code: https://github.com/MasterGroosha/my-id-bot.'
    )


def register_commands(router: Router):
    router.message.register(cmd_start, Command(commands="start"), chat_type="private")
    router.message.register(cmd_id, Command(commands="id"))
    router.message.register(cmd_help, Command(commands="help"))
