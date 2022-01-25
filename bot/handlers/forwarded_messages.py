from aiogram import types, html
from aiogram.dispatcher.router import Router
from magic_filter import F


async def get_channel_id(message: types.Message):
    """
    Handler for message forwarded from channel to some other chat
    :param message: Telegram message with "forward_from_chat" field not empty
    """
    msg = f"This channel's ID is {html.code(message.forward_from_chat.id)}"
    if message.sticker:
        msg += f"\nAlso this sticker's ID is {html.code(message.sticker.file_id)}"
    await message.reply(msg)


async def get_user_id_no_privacy(message: types.Message):
    """
    Handler for message forwarded from other user who doesn't hide their ID
    :param message: Telegram message with "forward_from" field not empty
    """
    if message.forward_from.is_bot:
        msg = f"This bot's ID is {html.code(message.forward_from.id)}"
    else:
        msg = f"This user's ID is {html.code(message.forward_from.id)}"
    if message.sticker:
        msg += f"\nAlso this sticker's ID is {html.code(message.sticker.file_id)}"
    await message.reply(msg)


async def get_user_id_with_privacy(message: types.Message):
    """
    Handler for message forwarded from other user who hides their ID
    :param message: Telegram message with "forward_sender_name" field not empty
    """
    msg = f"This user decided to <b>hide</b> their ID.\n\nLearn more about this feature " \
          f"{html.link(link='https://telegram.org/blog/unsend-privacy-emoji#anonymous-forwarding', value='here')}."
    if message.sticker:
        msg += f"\n\nAlso this sticker's ID is {html.code(message.sticker.file_id)}"
    await message.reply(msg)


def register_forwards(router: Router):
    router.message.register(get_channel_id, F.forward_from_chat)
    router.message.register(get_user_id_no_privacy, F.forward_from)
    router.message.register(get_user_id_with_privacy, F.forward_sender_name)
