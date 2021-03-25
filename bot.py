#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked, TelegramAPIError
from os import getenv
from sys import exit
import logs


logs.setup_errors_log()
if logs.enabled:
    logs.setup_stats_log()

errors_logger = logging.getLogger("errors")

if not getenv("BOT_TOKEN"):
    exit("Error: no token provided. Terminated.")

# Initialize bot and dispatcher
bot = Bot(token=getenv("BOT_TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(lambda message: message.chat.type == "private", commands="start")
async def cmd_start(message: types.Message):
    """
    /start command handler for private chats
    :param message: Telegram message with "/start" command
    """
    await message.answer(f"Your Telegram ID is <code>{message.chat.id}</code>\nHelp and source code: /help")
    logs.track("/start")


@dp.message_handler(commands="id")
async def cmd_id(message: types.Message):
    """
    /id command handler for all chats
    :param message: Telegram message with "/id" command
    """
    if message.chat.id == message.from_user.id:
        await message.answer(f"Your Telegram ID is <code>{message.from_user.id}</code>")
    else:
        await message.answer(f"This {message.chat.type} chat ID is <code>{message.chat.id}</code>")
    logs.track("/id")


@dp.message_handler(commands="help")
async def show_help(message: types.Message):
    """
    /help command handler for all chats
    :param message: Telegram message with "/help" command
    """
    await message.answer('Use this bot to get ID for different entities across Telegram:\n'
                         '• Forward message from channel to get channel ID;\n'
                         '• Forward message from user to get their ID (unless they restrict from doing so);\n'
                         '• Send a sticker to get its file_id (currently you can use the sticker\'s file_id with any bot);\n'
                         '• Add bot to group to get its ID (it will even tell you when you migrate from group to supergroup);\n'
                         '• Use inline mode to send your Telegram ID to any chat.\n\n'
                         'Source code: https://github.com/MasterGroosha/my-id-bot.')
    logs.track("/help")


@dp.message_handler(lambda message: message.forward_from_chat, content_types=types.ContentTypes.ANY)
async def get_channel_id(message: types.Message):
    """
    Handler for message forwarded from channel to some other chat
    :param message: Telegram message with "forward_from_chat" field not empty
    """
    msg = f"This channel's ID is <code>{message.forward_from_chat.id}</code>"
    if message.sticker:
        msg += f"\nAlso this sticker's ID is <code>{message.sticker.file_id}</code>"
    await message.reply(msg)
    logs.track("Get channel ID")


@dp.message_handler(lambda message: message.forward_from, content_types=types.ContentTypes.ANY)
async def get_user_id_no_privacy(message: types.Message):
    """
    Handler for message forwarded from other user who doesn't hide their ID
    :param message: Telegram message with "forward_from" field not empty
    """
    if message.forward_from.is_bot:
        msg = f"This bot's ID is <code>{message.forward_from.id}</code>"
    else:
        msg = f"This user's ID is <code>{message.forward_from.id}</code>"
    if message.sticker:
        msg += f"\nAlso this sticker's ID is <code>{message.sticker.file_id}</code>"
    await message.reply(msg)
    logs.track("Check user or bot")


@dp.message_handler(lambda message: message.forward_sender_name, content_types=types.ContentTypes.ANY)
async def get_user_id_with_privacy(message: types.Message):
    """
    Handler for message forwarded from other user who hides their ID
    :param message: Telegram message with "forward_sender_name" field not empty
    """
    msg = f"This user decided to <b>hide</b> their ID.\n\nLearn more about this feature " \
        f"<a href=\"https://telegram.org/blog/unsend-privacy-emoji#anonymous-forwarding\">here</a>."
    if message.sticker:
        msg += f"\n\nAlso this sticker's ID is <code>{message.sticker.file_id}</code>"
    await message.reply(msg)
    logs.track("Check user or bot")


@dp.message_handler(content_types=["new_chat_members"])
async def new_chat(message: types.Message):
    """
    Handler for "new_chat_members" action when bot is added to chat.
    A special check is performed so that this handler will only be fired once per chat, when
    bot itself is added to group (bot's ID is the first part of token before ":" symbol)
    :param message: Telegram message with "new_chat_members" field not empty
    """
    for user in message.new_chat_members:
        if user.id == bot.id:
            await message.answer(f"This {message.chat.type} chat ID is <code>{message.chat.id}</code>")
            logs.track("Added to group")
            return


@dp.message_handler(content_types=["migrate_to_chat_id"])
async def group_upgrade_to(message: types.Message):
    """
    When group is migrated to supergroup, sends new chat ID.
    Notice that the first argument of send_message is message.migrate_to_chat_id, not message.chat.id!
    Otherwise, MigrateChat exception will raise
    :param message: Telegram message with "migrate_to_chat_id" field not empty
    """
    await bot.send_message(message.migrate_to_chat_id, f"Group upgraded to supergroup.\n"
                                                       f"Old ID: <code>{message.chat.id}</code>\n"
                                                       f"New ID: <code>{message.migrate_to_chat_id}</code>")
    logs.track("Group migrate")


@dp.message_handler(chat_type=types.ChatType.PRIVATE, content_types=types.ContentTypes.ANY)
async def private_chat(message: types.Message):
    """
    Handler for messages in private chat (one-to-one dialogue)
    :param message: Telegram message sent to private chat (one-to-one dialogue)
    """
    msg = f"Your Telegram ID is <code>{message.chat.id}</code>"
    if message.sticker:
        msg += f"\n\nAlso this sticker's ID is <code>{message.sticker.file_id}</code>"
    await message.reply(msg)
    logs.track("Any message in PM")


@dp.inline_handler()
async def inline_message(query: types.InlineQuery):
    """
    Handler for inline queries
    :param query: Inline query with any text
    """
    result = types.InlineQueryResultArticle(
        id=".",
        title=f"Your ID is {query.from_user.id}",
        description="Tap to send your ID to current chat",
        input_message_content=types.InputTextMessageContent(
            message_text=f"My Telegram ID is <code>{query.from_user.id}</code>"
        )
    )
    # Do not forget about is_personal parameter! Otherwise all people will see the same ID
    await bot.answer_inline_query(query.id, [result], cache_time=3600, is_personal=True)
    logs.track("Inline mode")


@dp.errors_handler(exception=TelegramAPIError)
async def errors_handler(update, error):
    # Here we collect all available exceptions from Telegram and write them to file
    # First, we don't want to log BotBlocked exception, so we skip it
    if isinstance(error, BotBlocked):
        return True
    # We collect some info about an exception and write to file
    error_msg = f"Exception of type {type(error)}. Chat ID: {update.message.chat.id}. " \
                f"User ID: {update.message.from_user.id}. Error: {error}"
    errors_logger.error(error_msg)
    return True


async def setup_bot_commands(dispatcher: Dispatcher):
    """
    Here we setup bot commands to make them visible in Telegram UI
    """
    bot_commands = [
        types.BotCommand(command="/id", description="Tell your ID or group's ID"),
        types.BotCommand(command="/help", description="Help and source code")
    ]
    await bot.set_my_commands(bot_commands)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=setup_bot_commands)
