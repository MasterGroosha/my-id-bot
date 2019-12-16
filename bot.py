#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from os import getenv
from sys import exit

if not getenv("BOT_TOKEN"):
    exit("Error: no token provided. Terminated.")

# Initialize bot and dispatcher
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(lambda message: message.forward_from_chat)
async def get_channel_id(message: types.Message):
    """
    Handler for message forwarded from channel to some other chat
    :param message: Telegram message with "forward_from_chat" field not empty
    """
    await message.reply(f"This channel's ID is <code>{message.forward_from_chat.id}</code>", parse_mode="HTML")


@dp.message_handler(lambda message: message.forward_from)
async def get_user_id_no_privacy(message: types.Message):
    """
    Handler for message forwarded from other user who doesn't hide their ID
    :param message: Telegram message with "forward_from" field not empty
    """
    if message.forward_from.is_bot:
        await message.reply(f"This bot's ID is <code>{message.forward_from.id}</code>", parse_mode="HTML")
    else:
        await message.reply(f"This user's ID is <code>{message.forward_from.id}</code>", parse_mode="HTML")


@dp.message_handler(lambda message: message.forward_sender_name)
async def get_user_id_with_privacy(message: types.Message):
    """
    Handler for message forwarded from other user who hides their ID
    :param message: Telegram message with "forward_sender_name" field not empty
    """
    await message.reply(f'This user decided to <b>hide</b> their ID.\n\n'
                        f'Learn more about this feature '
                        f'<a href="https://telegram.org/blog/unsend-privacy-emoji#anonymous-forwarding">here</a>.',
                        parse_mode="HTML")


@dp.message_handler(content_types=["new_chat_members"])
async def new_chat(message: types.Message):
    """
    Handler for "new_chat_members" action when bot is added to chat.
    A special check is performed so that this handler will only be fired once per chat, when
    bot itself is added to group (bot's ID is the first part of token before ":" symbol)
    :param message: Telegram message with "new_chat_members" field not empty
    """
    bot_id = int(getenv("BOT_TOKEN").split(":")[0])
    for user in message.new_chat_members:
        if user.id == bot_id:
            await bot.send_message(message.chat.id,
                                   f"This {message.chat.type} chat ID is <code>{message.chat.id}</code>",
                                   parse_mode="HTML")


@dp.message_handler(content_types=["migrate_to_chat_id"])
async def group_upgrade_to(message: types.Message):
    """
    When group is migrated to supergroup, sends new chat ID.
    Notice that the first argument of send_message is message.migrate_to_chat_id, not message.chat.id!
    Otherwise, MigrateChat exception will raise
    :param message: Telegram message with "migrate_to_chat_id" field not empty
    """
    await bot.send_message(message.migrate_to_chat_id, f"Group upgraded to supergroup.\n"
                                                       f"New ID: <code>{message.migrate_to_chat_id}</code>",
                           parse_mode="HTML")


@dp.message_handler(content_types=["migrate_from_chat_id"])
async def group_upgrade_from(message: types.Message):
    """
    When group is upgraded to supergroup, sends previous ID (why not?)
    :param message: Telegram message with "migrate_from_chat_id" field not empty
    """
    await bot.send_message(message.chat.id, f"Group upgraded to supergroup.\n"
                                            f"Previous ID: <code>{message.migrate_from_chat_id}</code>",
                           parse_mode="HTML")


@dp.message_handler(commands=["id"])
async def just_tell_id(message: types.Message):
    """
    /id command handler for all chats
    :param message: Telegram message with "/id" command in text
    """
    await bot.send_message(message.chat.id, f"This {message.chat.type} chat ID is <code>{message.chat.id}</code>",
                           parse_mode="HTML")


@dp.message_handler(lambda message: message.chat.type == "private")
async def private_chat(message: types.Message):
    """
    Handler for messages in private chat (one-to-one dialogue)
    :param message: Telegram message sent to private chat (one-to-one dialogue)
    """
    try:
        await message.reply(f"Your Telegram ID is <code>{message.chat.id}</code>", parse_mode="HTML")
    except BotBlocked:
        pass  # Simply do nothing in this case


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
            message_text=f"My Telegram ID is <code>{query.from_user.id}</code>",
            parse_mode="HTML"
        )
    )
    # Do not forget about is_personal parameter! Otherwise all people will see the same ID
    await bot.answer_inline_query(query.id, [result], cache_time=3600, is_personal=True)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
