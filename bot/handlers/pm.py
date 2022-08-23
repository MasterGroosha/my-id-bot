from aiogram import Router, types, html, F

router = Router()
router.message.filter(F.chat.type == "private")


@router.message(F.forward_from_chat.type.as_("chat_type"))
async def get_channel_or_supergroup_id(message: types.Message, chat_type: str):
    """
    Handler for message forwarded from channel
    or from anonymous admin writing on behalf
    of a supergroup

    :param message: Telegram message with "forward_from_chat" field not empty
    :param chat_type: parsed chat_type ("channel" or "supergroup")
    """
    msg = f"This {chat_type}'s ID is {html.code(message.forward_from_chat.id)}"
    if message.sticker:
        msg += f"\nAlso this sticker's ID is {html.code(message.sticker.file_id)}"
    await message.reply(msg)


@router.message(F.forward_from)
async def get_user_id_no_privacy(message: types.Message):
    """
    Handler for message forwarded from other user who doesn't hide their ID
    :param message: Telegram message with "forward_from" field not empty
    """
    account_type = "bot" if message.forward_from.is_bot else "user"
    msg = f"This {account_type}'s ID is {html.code(message.forward_from.id)}"
    if message.sticker:
        msg += f"\nAlso this sticker's ID is {html.code(message.sticker.file_id)}"
    await message.reply(msg)


@router.message(F.forward_sender_name)
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


@router.message(F.sticker)
async def sticker_in_pm(message: types.Message):
    """
    /start command handler for private chats
    :param message: Telegram message with "/start" command
    """
    await message.reply(
        f"This sticker ID is\n{html.code(message.sticker.file_id)}\n"
        f"Stickers is currently the only media type which file_ids can be used by any bot."
    )


@router.message()
async def other_in_pm(message: types.Message):
    """
    /id command handler for private messages
    :param message: Telegram message with "/id" command
    """
    await message.answer(f"Your Telegram ID is {html.code(message.from_user.id)}")
