from aiogram import types
from aiogram.dispatcher.router import Router


async def sticker_in_pm(message: types.Message):
    """
    /start command handler for private chats
    :param message: Telegram message with "/start" command
    """
    await message.reply(
        f"This sticker ID is\n<code>{message.sticker.file_id}</code>\n"
        f"Stickers is currently the only media type which file_ids can be used by any bot."
    )


async def other_in_pm(message: types.Message):
    """
    /id command handler for private messages
    :param message: Telegram message with "/id" command
    """
    await message.answer(f"Your Telegram ID is <code>{message.from_user.id}</code>")


def register_pm(router: Router):
    router.message.register(sticker_in_pm, chat_type="private", content_types="sticker")
    router.message.register(other_in_pm, chat_type="private")
